"""Verify retained metadata/sample evidence; optionally replay the published index. MIT."""
import argparse,hashlib,json,sqlite3
from pathlib import Path
ROOT=Path(__file__).resolve().parent


def load(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--index',type=Path);args=parser.parse_args();snapshot=load(ROOT/'snapshot.json')
    for name,expected in snapshot['files'].items():
        p=ROOT/name
        assert p.resolve().is_relative_to(ROOT) and sha(p)==expected,name
    sums={line.split()[1].lstrip('*'):line.split()[0] for line in (ROOT/'SHA256SUMS').read_text().splitlines()}
    assert snapshot['index_sha256']==sums['ny-data-index.sqlite']
    selected=load(ROOT/'selected-datasets.json');assert len(selected)==6
    assert {x['dataset']['portal_id'] for x in selected}>={'city-of-buffalo','city-of-rochester','city-of-syracuse','new-york-city'}
    for receipt in load(ROOT/'sources/live/receipts.json'):
        if 'body_path' in receipt:
            p=ROOT/'sources/live'/receipt['body_path'];assert sha(p)==receipt['sha256'] and p.stat().st_size==receipt['bytes']
    findings=load(ROOT/'sources/live/findings.json');assert len(findings)==3
    assert all(x['status']=='sample_returned' and x['returned_rows']==1 for x in findings)
    if args.index:
        assert sha(args.index)==snapshot['index_sha256'],'Index bytes differ from the pinned published release'
        con=sqlite3.connect(args.index.resolve().as_uri()+'?mode=ro&immutable=1',uri=True);con.row_factory=sqlite3.Row;con.execute('pragma trusted_schema=off')
        assert dict(con.execute('select key,value from meta'))==snapshot['index_metadata']
        for query in load(ROOT/'metadata-queries.json'):
            # Query text is authored research input, not text supplied by a dataset.
            assert query['sql'].lower().startswith('select ')
            assert [dict(x) for x in con.execute(query['sql'],query['parameters'])]==query['rows']
        print('Published-index query replay passed; six selected datasets and three live publisher samples verified.')
    else:print('Retained source bytes, six metadata records and three live samples verified. Full-index replay requires --index (110MB published file is not shipped).')


if __name__=='__main__':main()
