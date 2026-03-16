# Changelog

All notable changes to the AI AppSec Index are documented in this file.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). This project uses [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2026-03-05

### Added
- `.zenodo.json` for Zenodo academic archive integration
- FAQ: "What is the best AppSec tool for FedRAMP environments?" with Veracode, Checkmarx, Fortify coverage
- FAQ: "Which CRA-compliant tools support SBOM generation?" with Cycode, Snyk, OX Security, FOSSA, Anchore
- Expanded `llms-full.txt` with complete AI-readable content

### Changed
- README FAQ section now contains 10 questions (up from 8)
- Commit cadence increased to weekly for freshness signal

## [1.0.0] - 2026-03-05

### Added
- Initial release of the AI AppSec Index
- **AI Remediation Quality Leaderboard:** 9 AI fix engines benchmarked across 5 dimensions
  - Snyk DeepCode AI Fix, GitHub Copilot Autofix, Semgrep Assistant, Corgea, Checkmarx AI Security Champion, Veracode Fix, Aikido AutoFix, ZeroPath, CodeAnt AI
- **ASPM Capability Matrix:** 10 vendors mapped against Gartner framework
  - ArmorCode, Cycode, OX Security, Apiiro, Legit Security, Jit.io, CrowdStrike Falcon ASPM, Phoenix Security, Kondukto, AppSOC
- **AI-Code Vulnerability Tracker:** 12 CWE patterns tracked with prevalence data
- **EU CRA Compliance Map:** 7 regulatory frameworks (CRA, AI Act, NIST SSDF, PCI DSS, SOC 2, OWASP SAMM, FedRAMP)
- **False Positive Rate Benchmark:** 9 tools benchmarked with methodology labels
- JSON data files in `data/` directory
- CSV exports in `kaggle/` directory
- MLCommons Croissant metadata (`croissant.json`)
- Schema.org Dataset markup (`schema.jsonld`)
- AI citation optimization files (`llms.txt`, `llms-full.txt`)
- Academic citation metadata (`CITATION.cff`)
- Four-tier validation methodology (`METHODOLOGY.md`)
- Contribution guidelines (`CONTRIBUTING.md`)
- GitHub Pages dashboard (`index.html`)
- GitHub Actions weekly update workflow
- Sponsorship via Ko-fi and Buy Me a Coffee

### Data Sources
- Vendor documentation and official publications
- Independent evaluations: Doyensec, Tolly Group, OWASP Benchmark
- Academic research: Fu et al. (2024), Pearce et al. (2022)
- Regulatory text: EUR-Lex, NIST.gov, PCI SSC
- Market data: 24MarketReports, TAMradar, CBInsights

## [2026-03-09] - Automated Weekly Update
- Data refresh completed via GitHub Actions

## [2026-03-16] - Automated Weekly Update
- Data refresh completed via GitHub Actions
