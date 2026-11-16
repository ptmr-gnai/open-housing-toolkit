"""Front elevation of a verified massing, drawn to scale as PNG (for the image tool) and SVG (for people). MIT."""
import math
import struct
import zlib

SKY = (250, 250, 248)
GROUND = (60, 60, 60)
RETAIL = (176, 196, 210)
RETAIL_BAY = (120, 150, 170)
BODY = (172, 98, 72)
WINDOW = (55, 65, 80)
LINE = (35, 35, 35)
LOT = (200, 200, 195)


def edges(polygon):
    pts = polygon[:-1] if polygon[0] == polygon[-1] else polygon
    out = []
    for i, a in enumerate(pts):
        b = pts[(i + 1) % len(pts)]
        out.append({'index': i, 'start': a, 'end': b, 'length_ft': round(math.dist(a, b), 1)})
    return out


def frontage_frame(parcel, edge_index=None):
    """Unit vectors along and into the lot for the chosen street edge (default: longest mapped edge)."""
    es = edges(parcel)
    edge = max(es, key=lambda e: e['length_ft']) if edge_index is None else next(e for e in es if e['index'] == edge_index)
    (x0, y0), (x1, y1) = edge['start'], edge['end']
    length = math.dist((x0, y0), (x1, y1))
    u = ((x1 - x0) / length, (y1 - y0) / length)
    n = (-u[1], u[0])
    cx = sum(p[0] for p in parcel) / len(parcel)
    cy = sum(p[1] for p in parcel) / len(parcel)
    if (cx - x0) * n[0] + (cy - y0) * n[1] < 0:
        n = (-n[0], -n[1])
    return edge, (x0, y0), u, n


def project(geometry, edge_index=None):
    parcel = geometry['source_geometry']['polygon_ft']
    edge, origin, u, n = frontage_frame(parcel, edge_index)
    along = lambda p: (p[0] - origin[0]) * u[0] + (p[1] - origin[1]) * u[1]
    depth = lambda p: (p[0] - origin[0]) * n[0] + (p[1] - origin[1]) * n[1]
    lot = [along(p) for p in parcel]
    lot_min, lot_max = min(lot), max(lot)
    floors = []
    for f in geometry['floors']:
        xs = [along(p) for p in f['footprint_ft']]
        ds = [depth(p) for p in f['footprint_ft']]
        floors.append({'id': f['id'], 'left_ft': round(min(xs) - lot_min, 1), 'right_ft': round(max(xs) - lot_min, 1),
                       'width_ft': round(max(xs) - min(xs), 1), 'street_setback_ft': round(max(min(ds), 0), 1),
                       'base_ft': f['base_z_ft'], 'top_ft': f['top_z_ft'],
                       'retail': f['nonresidential_proxy_sf'] > 0.5})
    return {'frontage_edge': {'index': edge['index'], 'length_ft': edge['length_ft'],
                              'rule': 'chosen edge' if edge_index is not None else 'longest mapped parcel edge (assumed street frontage)'},
            'lot_width_ft': round(lot_max - lot_min, 1), 'height_ft': geometry['total_height_ft'], 'floors': floors,
            'available_edges': [{'index': e['index'], 'length_ft': e['length_ft']} for e in edges(parcel)]}


def _canvas(elev, scale):
    margin = 40
    width = int(elev['lot_width_ft'] * scale) + 2 * margin
    height = int((elev['height_ft'] + 12) * scale) + 2 * margin
    base_y = height - margin
    return width, height, margin, base_y


def png(elev, scale=4):
    """Flat elevation raster: retail ground floor with bays, upper floors with countable window rows."""
    width, height, margin, base_y = _canvas(elev, scale)
    px = [[SKY] * width for _ in range(height)]

    def rect(x0, y0, x1, y1, color):
        for y in range(max(0, int(y0)), min(height, int(y1))):
            row = px[y]
            for x in range(max(0, int(x0)), min(width, int(x1))):
                row[x] = color

    rect(margin, base_y, margin + elev['lot_width_ft'] * scale, base_y + 6, LOT)
    rect(0, base_y + 6, width, height, GROUND)
    for f in elev['floors']:
        x0, x1 = margin + f['left_ft'] * scale, margin + f['right_ft'] * scale
        y0, y1 = base_y - f['top_ft'] * scale, base_y - f['base_ft'] * scale
        rect(x0, y0, x1, y1, RETAIL if f['retail'] else BODY)
        if f['retail']:
            bay = 25 * scale
            x = x0 + 4 * scale
            while x + 18 * scale < x1:
                rect(x, y0 + 3 * scale, x + 18 * scale, y1 - 1 * scale, RETAIL_BAY)
                x += bay
        else:
            step = 12 * scale
            x = x0 + 4 * scale
            while x + 5 * scale < x1 - 2 * scale:
                rect(x, y0 + 3 * scale, x + 5 * scale, y0 + 8 * scale, WINDOW)
                x += step
        rect(x0, y0, x1, y0 + 2, LINE)
        rect(x0, y0, x0 + 2, y1, LINE)
        rect(x1 - 2, y0, x1, y1, LINE)
    raw = b''.join(b'\x00' + bytes(c for p in row for c in p) for row in px)

    def chunk(tag, data):
        return struct.pack('>I', len(data)) + tag + data + struct.pack('>I', zlib.crc32(tag + data) & 0xffffffff)
    return (b'\x89PNG\r\n\x1a\n' + chunk(b'IHDR', struct.pack('>IIBBBBB', width, height, 8, 2, 0, 0, 0))
            + chunk(b'IDAT', zlib.compress(raw, 9)) + chunk(b'IEND', b''))


def svg(elev, scale=4):
    width, height, margin, base_y = _canvas(elev, scale)
    color = lambda c: 'rgb(%d,%d,%d)' % c
    parts = ['<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d" font-family="sans-serif">'
             % (width, height + 30, width, height + 30),
             '<rect width="100%%" height="100%%" fill="%s"/>' % color(SKY),
             '<rect x="0" y="%d" width="%d" height="%d" fill="%s"/>' % (base_y + 6, width, height - base_y + 24, color(GROUND))]
    for f in elev['floors']:
        x0, x1 = margin + f['left_ft'] * scale, margin + f['right_ft'] * scale
        y0, y1 = base_y - f['top_ft'] * scale, base_y - f['base_ft'] * scale
        parts.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s" stroke="%s" stroke-width="1.5"/>'
                     % (x0, y0, x1 - x0, y1 - y0, color(RETAIL if f['retail'] else BODY), color(LINE)))
        parts.append('<text x="%.1f" y="%.1f" font-size="11" fill="#fff">%s</text>' % (x0 + 4, y1 - 4, f['id'].replace('floor-', 'Floor ')))
    top = base_y - elev['height_ft'] * scale
    parts.append('<text x="%d" y="%d" font-size="13">%s ft tall · lot frontage %s ft (assumed street edge)</text>'
                 % (margin, top - 8, elev['height_ft'], elev['lot_width_ft']))
    parts.append('<text x="%d" y="%d" font-size="12" fill="#fff">Front elevation drawn from the schematic massing; not a design</text>'
                 % (margin, height + 18))
    parts.append('</svg>')
    return '\n'.join(parts) + '\n'
