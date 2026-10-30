# Historical skill-layout runtime

Frozen source and skill bytes used by the original retained module manifests.
This is an archive, not the active skill distribution. housing_runtime.py checks
this snapshot and invokes the original verifier in an separate Python process
when a retained package does not match the current implementation. Unknown or
modified packages still have to pass that original verifier. Existing example
manifests and provider invocation records are not rewritten.

New builds use the current modules and skills under the repository root. The
archived verifier is read-only and supports historical verification only; it is
not a fallback collector, builder, image provider or compatibility guarantee for
arbitrary past versions. Geometry still requires the recorded dependency versions.
