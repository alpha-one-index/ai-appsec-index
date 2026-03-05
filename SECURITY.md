# Security Policy

## Reporting a Vulnerability

This repository contains **data files only** (JSON, CSV, Markdown). It does not contain executable code that could be exploited in a traditional security vulnerability sense.

However, if you discover:
- **Malicious data injection:** Data that has been manipulated to mislead users about tool capabilities or security ratings
- **Source URL manipulation:** Links that redirect to malicious sites
- **Workflow compromise:** Issues with GitHub Actions workflows

Please report via:
1. **GitHub Security Advisories:** Use the "Security" tab to report privately
2. **Email:** Open an issue with the `security` label

## Response Timeline
- Acknowledgment: within 48 hours
- Assessment: within 7 days
- Fix: within 14 days for confirmed issues

## Scope

This policy covers:
- Data integrity of JSON/CSV files
- Source URL validity and safety
- GitHub Actions workflow security
- Repository access controls

## Data Integrity

All data in this repository is validated through our [four-tier methodology](METHODOLOGY.md). If you suspect data has been tampered with or is intentionally misleading, please report it as a data integrity issue.
