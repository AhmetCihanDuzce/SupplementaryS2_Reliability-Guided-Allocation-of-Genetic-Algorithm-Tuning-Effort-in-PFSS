# Prospective matrix replay clarification

The 24 prospective processing-time matrices are byte-exactly recoverable from the prespecified target seeds.

The prospective protocol recorded NumPy `PCG64DXSM`, iid discrete Uniform{1,...,99}, and the seed formula `2026082701 + n*1000 + m`. The archived matrix fingerprints identify a 16-bit integer draw stream as the implementation detail required to reproduce the exact matrices. For values 1..99, signed and unsigned 16-bit storage generate the same value stream and the same CSV bytes.

An earlier replay attempt using NumPy's default integer path (`int64`) generated a different stream. Replaying the matrices with the recovered 16-bit draw path yields 24/24 SHA-256 matches and 24/24 standard-NEH matches. This clarification concerns reproducibility only; it does not change any target, action, GA outcome, or reported result.
