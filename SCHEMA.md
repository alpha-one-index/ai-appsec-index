# JSON Schema Documentation

This document defines the schema for all JSON data files in the AI AppSec Index.

## remediation-leaderboard.json

Array of objects, each representing an AI remediation tool.

| Field | Type | Required | Description |
|---|---|---|---|
| `rank` | integer | Yes | Current leaderboard position |
| `tool` | string | Yes | Tool name |
| `vendor` | string | Yes | Vendor/company name |
| `fix_accuracy` | integer (0-100) | Yes | Fix accuracy score |
| `code_quality` | integer (0-100) | Yes | Code quality score |
| `language_coverage` | integer (0-100) | Yes | Language coverage score |
| `integration` | integer (0-100) | Yes | Integration depth score |
| `transparency` | integer (0-100) | Yes | Transparency score |
| `overall_score` | number (0-100) | Yes | Weighted average score |
| `data_source` | string | Yes | Source URL or citation |
| `data_type` | enum | Yes | `independent` or `vendor_self_reported` or `community` |
| `last_updated` | string (ISO 8601) | Yes | Date of last data verification |

## aspm-capability-matrix.json

Array of objects, each representing an ASPM vendor.

| Field | Type | Required | Description |
|---|---|---|---|
| `vendor` | string | Yes | Vendor name |
| `founded` | integer | Yes | Year founded |
| `funding` | string | Yes | Total funding amount |
| `scanner_ingestion` | enum | Yes | Y/P/N/U |
| `reachability_analysis` | enum | Yes | Y/P/N/U |
| `sbom_support` | enum | Yes | Y/P/N/U |
| `cicd_gating` | enum | Yes | Y/P/N/U |
| `compliance_reporting` | enum | Yes | Y/P/N/U |
| `ai_code_detection` | enum | Yes | Y/P/N/U |
| `risk_scoring` | enum | Yes | Y/P/N/U |
| `remediation_workflow` | enum | Yes | Y/P/N/U |
| `source` | string | Yes | Source URL |

## ai-code-vulnerabilities.json

Array of objects, each representing a CWE pattern.

| Field | Type | Required | Description |
|---|---|---|---|
| `cwe_id` | string | Yes | CWE identifier (e.g., CWE-330) |
| `vulnerability` | string | Yes | Vulnerability name |
| `prevalence` | number | Yes | Percentage prevalence in AI code |
| `risk_level` | enum | Yes | Critical/High/Medium/Low |
| `detection_tools` | array[string] | Yes | Tools that detect this pattern |
| `research_source` | string | Yes | Academic citation |

## compliance-map.json

Array of objects, each representing a regulatory requirement.

| Field | Type | Required | Description |
|---|---|---|---|
| `framework` | string | Yes | Regulatory framework name |
| `requirement` | string | Yes | Specific requirement identifier |
| `obligation` | string | Yes | Description of the obligation |
| `compliant_tools` | array[string] | Yes | Tools meeting this requirement |
| `deadline` | string | Yes | Compliance deadline |
| `penalty` | string | Yes | Non-compliance penalty |
| `official_source` | string | Yes | Official regulatory text URL |

## false-positive-rates.json

Array of objects, each representing a tool's FP rate data.

| Field | Type | Required | Description |
|---|---|---|---|
| `tool` | string | Yes | Tool name |
| `vendor` | string | Yes | Vendor name |
| `fp_rate` | string | Yes | Reported FP rate |
| `test_methodology` | string | Yes | How FP rate was measured |
| `languages_tested` | string | Yes | Languages in the evaluation |
| `data_source` | string | Yes | Source URL |
| `data_type` | enum | Yes | `independent` or `vendor_self_reported` |

---

*See [METHODOLOGY.md](METHODOLOGY.md) for data collection and validation details.*
