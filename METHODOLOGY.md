# Data Collection Methodology

> How the AI AppSec Index collects, validates, and maintains data quality across all five moat components.

## Overview

The AI AppSec Index uses a four-tier validation methodology to ensure data accuracy, transparency, and reproducibility. Every data point is tagged with its source type, collection date, and confidence level.

## Four-Tier Validation Framework

### Tier 1: Primary Source Collection
- **Method:** Direct collection from vendor documentation, official pricing pages, published benchmarks, regulatory text (EUR-Lex, NIST.gov, PCI SSC)
- **Applies to:** All vendor data, capability claims, regulatory requirements
- **Frequency:** Weekly automated checks + manual review
- **Quality bar:** Data must link to a publicly accessible URL; archived via Wayback Machine if source is volatile

### Tier 2: Cross-Reference Validation
- **Method:** Every quantitative claim (FP rates, remediation scores, funding amounts) requires minimum 2 independent sources
- **Applies to:** False positive rates, remediation quality scores, market sizing, funding data
- **Frequency:** Monthly
- **Quality bar:** Discrepancies >10% between sources trigger manual review and are flagged in data with `confidence: "disputed"`

### Tier 3: Community Validation
- **Method:** Pull requests with source citations required; peer review by maintainers
- **Applies to:** All data files
- **Frequency:** Per PR
- **Quality bar:** PRs without source URLs are rejected; vendor-affiliated contributors must disclose affiliation

### Tier 4: Automated Self-Audit
- **Method:** GitHub Actions CI/CD pipeline running daily
- **Checks performed:**
  - JSON schema validation against `SCHEMA.md` definitions
  - Source URL reachability (HTTP 200 check)
  - Price/score range anomaly detection (statistical outlier flagging)
  - Completeness check (all required fields present)
  - Date freshness (records not updated within 90 days are flagged)
- **Frequency:** Daily via GitHub Actions

## Remediation Leaderboard Scoring Methodology

### Dimensions (Weighted)
| Dimension | Weight | Description | Scoring Criteria |
|---|---|---|---|
| Fix Accuracy | 30% | Does the fix resolve the vulnerability without introducing new issues? | 80+ requires independent third-party validation |
| Code Quality | 25% | Is the generated code idiomatic, maintainable, and performant? | Evaluated against language-specific style guides |
| Language Coverage | 20% | How many programming languages are supported with AI fixes? | Scaled: 5 langs = 50, 10 = 70, 15 = 80, 20+ = 90 |
| Integration Depth | 15% | IDE, CI/CD, PR workflow support | Points for each: IDE plugin, CI action, PR bot, API |
| Transparency | 10% | Does the tool explain reasoning and cite CWE/source? | Points for: explanation text, CWE mapping, confidence score, source citation |

### Score Confidence Labels
- **Independently Verified (IV):** Score backed by published third-party benchmark or academic paper
- **Vendor Self-Reported (VSR):** Score based on vendor claims supported by product documentation
- **Community Reported (CR):** Score contributed via PR with source citations
- **Estimated (EST):** Score derived from indirect evidence; explicitly flagged

## ASPM Capability Matrix Methodology

Capabilities are mapped against Gartner's 2023 ASPM definition framework. Each capability is rated:
- **Y (Yes):** Full support confirmed via vendor documentation or independent review
- **P (Partial):** Feature exists but with limitations documented in notes field
- **N (No):** Feature not available based on current documentation
- **U (Undisclosed):** Vendor has not published information; field is left for community contribution

## AI-Code Vulnerability Tracker Methodology

CWE patterns and prevalence percentages are sourced from peer-reviewed academic research:
- Fu et al. (2024) - arXiv 2310.02059: Primary source for Copilot vulnerability patterns
- Pearce et al. (2022) - Black Hat USA: Foundational research on AI code security
- OWASP LLM Top 10: Framework alignment for AI-specific risks

Prevalence percentages represent the proportion of AI-generated vulnerabilities attributable to each CWE, not the absolute probability of any given code suggestion being vulnerable.

## Compliance Map Methodology

Regulatory requirements are sourced exclusively from official legal text:
- EU CRA: EUR-Lex Regulation (EU) 2024/2847
- EU AI Act: EUR-Lex Regulation (EU) 2024/1689
- NIST SSDF: SP 800-218
- PCI DSS: PCI SSC document library

Tool-to-requirement mappings are based on published vendor compliance documentation and independent analyst reports. Mappings are conservative: a tool is only listed as compliant if its documentation explicitly addresses the specific regulatory article.

## False Positive Benchmark Methodology

### Data Source Hierarchy
1. Independent benchmarks (OWASP Benchmark Project, Tolly Reports, Doyensec evaluations)
2. Academic papers with reproducible methodology
3. Vendor self-reported data (explicitly labeled)

### Normalization
FP rates are reported as-is from their source without normalization across tools, because testing conditions vary significantly. Each entry includes:
- Test methodology description
- Languages tested
- Data source with URL
- Data type label (independent/vendor self-reported)

## Data Freshness Policy

| Data Type | Maximum Age Before Flag | Update Trigger |
|---|---|---|
| Vendor capabilities | 90 days | Product release, acquisition, funding round |
| FP rates | 180 days | New benchmark publication |
| Remediation scores | 90 days | Major tool update, new independent eval |
| Compliance mappings | 365 days | Regulatory amendment or enforcement date |
| Market sizing | 180 days | New analyst report publication |

## Conflict of Interest Policy

- No vendor pays for placement or favorable scores
- No sponsored content; all data is editorially independent
- Vendor-affiliated contributors must disclose affiliation in PR description
- Maintainers with vendor relationships recuse from scoring that vendor

## How to Challenge a Data Point

1. Open an issue with the tag `data-challenge`
2. Cite the specific data point (file, field, value)
3. Provide your proposed correction with source URL
4. Maintainers review within 7 days

---

*Last updated: March 2026 | Version 1.0.0*
