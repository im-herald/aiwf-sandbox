# aiwf-sandbox

Disposable sandbox repository for testing an engineering workflow end to end: pull requests,
GitHub Actions checks, signed review attestations and branch rules. The code (`slugkit`, a tiny
slug helper) is synthetic test material and is not used anywhere.

- Unit tests: `python -m unittest discover -s tests -t . -v`
- Release checks: `python -m unittest -v tests_release/test_release.py`
- Specification: `SPEC.md`; coding standards: `CODING_STANDARDS.md`

Pull requests are reviewed and verified by the `aiwf-ci` and `aiwf-review` workflows; merging into
`main` is done by the repository owner only.
