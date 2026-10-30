# Repository skills

Start with [start-here](start-here/SKILL.md). Each active skill lives directly under
`skills/<skill-name>/`, with a short SKILL.md and on-demand references. Scripts
remain canonical in their Python modules or shared scripts directory and are linked
by those references. No extra current/ layer or duplicate script wrappers are used.

The [catalogue](catalog.json) lists one coordinator and ten leaf skills. This is
checkout-based use through AGENTS.md/CLAUDE.md; native host-menu discovery and a
portable installer remain separate work.

Historical instructions and their original executable verifiers are frozen in
[archive/skill-layout-v0](../archive/skill-layout-v0/README.md). Retained examples
keep their original manifests and provider records. On an implementation mismatch,
the current verifier checks the archive and runs that original verifier in an
separate Python process. Unknown implementations or changed artifacts still fail;
we do not regenerate hashes to make historical packages pass.

New builds bind the current skill entry and its local execution references, plus
the shared runtime helper. Host skill activation itself is not automatically
recorded as an agent-execution receipt.
