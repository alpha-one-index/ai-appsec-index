# Contributing to the AI AppSec Index

Thank you for your interest in contributing to the AI AppSec Index. This project relies on community contributions to maintain accuracy and comprehensiveness.

## What We Need

### High Priority
- **Independent benchmark data** for AI remediation tools (fix accuracy, code quality evaluations)
- **False positive rate data** from production environments (anonymized)
- **New ASPM vendor profiles** with sourced capability data
- **CRA compliance tool mappings** with references to official regulatory text
- **AI-code vulnerability patterns** with CWE classification and research citations

### Also Welcome
- Corrections to existing data with source URLs
- New vendor additions with complete profiles
- Academic paper references for vulnerability patterns
- Translation of compliance requirements
- Kaggle notebook analyses

## How to Contribute

### Data Corrections
1. Fork the repository
2. Edit the relevant JSON file in `data/`
3. Include the source URL in the `source` or `data_source` field
4. Submit a PR with a clear description of what changed and why

### New Vendor Additions
1. Fork the repository
2. Add the vendor to the appropriate JSON file(s)
3. Fill all required fields (see `SCHEMA.md` for field definitions)
4. Include at least 2 source URLs for quantitative claims
5. Submit a PR

### Data Challenges
If you believe existing data is incorrect:
1. Open an issue with the `data-challenge` label
2. Reference the specific file, field, and current value
3. Provide your proposed correction with source URL
4. Maintainers will review within 7 days

## Contribution Requirements

### Source Citations
- Every quantitative claim must include a source URL
- Vendor self-reported data must be labeled as such
- Academic citations must include DOI or arXiv ID where available
- Funding data must cite Crunchbase, SEC filings, or official press releases

### Conflict of Interest Disclosure
- If you are employed by or affiliated with a vendor tracked in this index, disclose this in your PR description
- Vendor-affiliated contributors may submit data but it will be labeled as vendor-contributed
- This is not a barrier to contribution -- transparency is the goal

### JSON Schema Compliance
- All data must conform to the schemas defined in `SCHEMA.md`
- Run `python scripts/validate.py` before submitting (when available)
- Required fields must be filled; use `null` for unknown values, not empty strings

## PR Review Process

1. Automated checks run (schema validation, URL reachability)
2. Maintainer reviews source quality and data accuracy
3. Feedback provided within 7 days
4. Approved PRs are merged and credited in CHANGELOG.md

## Code of Conduct

- Be respectful and constructive
- Data accuracy over vendor preference
- Transparency over completeness (it is better to mark data as unknown than to guess)
- Cite sources for everything

## Questions?

Open an issue with the `question` label or start a Discussion.

---

*See [METHODOLOGY.md](METHODOLOGY.md) for details on our data collection and validation framework.*
