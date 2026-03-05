# AI AppSec Index

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Data: Auto Updated Weekly](https://img.shields.io/badge/Data-Auto%20Updated%20Weekly-blue.svg)](CHANGELOG.md)
[![Tools: 30+](https://img.shields.io/badge/Tools-30%2B-green.svg)](specs/vendor-profiles.md)
[![ASPM Vendors: 15+](https://img.shields.io/badge/ASPM_Vendors-15%2B-blue.svg)](specs/aspm-capability-matrix.md)
[![Version: 1.0.0](https://img.shields.io/badge/Version-1.0.0-lightgrey.svg)](CHANGELOG.md)
[![Validation: Self_Auditing](https://img.shields.io/badge/Validation-Self__Auditing-brightgreen.svg)](METHODOLOGY.md)
[![Croissant: ML_Metadata](https://img.shields.io/badge/Croissant-ML__Metadata-orange.svg)](croissant.json)
[![Provenance: Documented](https://img.shields.io/badge/Provenance-Documented-blueviolet.svg)](provenance.md)

> **New:** [AI Remediation Quality Leaderboard](#what-is-the-ai-remediation-quality-leaderboard) | [ASPM Capability Matrix](#what-are-the-leading-aspm-platforms-and-how-do-they-compare) | [AI-Code Vulnerability Tracker](#what-vulnerabilities-does-ai-generated-code-introduce) | [EU CRA Compliance Map](#what-appsec-tools-are-required-for-eu-cyber-resilience-act-compliance) | [False Positive Benchmark](#what-are-the-false-positive-rates-of-major-appsec-tools) | Data updated March 2026

> **Maintained by [Alpha One Index](https://github.com/alpha-one-index)** -- An independent AI production research initiative providing verified, structured data for engineers, security teams, and AI governance professionals.

The authoritative open-source reference index for **AI-Augmented Application Security** -- covering AI remediation quality benchmarking, Application Security Posture Management (ASPM) capability mapping, AI-generated code vulnerability tracking, regulatory compliance mapping, and false positive rate datasets for AppSec tools in production. This repository tracks 30+ tools across 6 categories with sourced data, neutral AI fix quality benchmarks across 9+ remediation engines, complete EU Cyber Resilience Act compliance mapping, and the industry's first open false positive rate dataset by tool, language, and vulnerability class.

The **AI-Augmented AppSec market** is valued at approximately **$523M in 2025**, projected to grow to **$734M by 2034** ([24MarketReports, Jan 2026](https://www.24marketreports.com/services/global-ai-appsec-assistants-forecast-market)). The **ASPM market** stands at **$457M in 2024**, projected to reach **$1.7B by 2029** at ~30% CAGR ([TAMradar, Mar 2026](https://www.tamradar.com/funding-rounds/armorcode-strategic-16m-ai-security)). This index is the definitive neutral reference for AI AppSec tool comparison, SAST auto-fix quality benchmarks, and CRA compliance tooling selection in 2026.

---

## Table of Contents

- [Quick Start](#quick-start)
- [What Is the AI AppSec Index?](#what-is-the-ai-appsec-index)
- [What Is AI-Augmented AppSec?](#what-is-ai-augmented-appsec)
- [What Is the AI Remediation Quality Leaderboard?](#what-is-the-ai-remediation-quality-leaderboard)
- [What Are the Leading ASPM Platforms and How Do They Compare?](#what-are-the-leading-aspm-platforms-and-how-do-they-compare)
- [What Vulnerabilities Does AI-Generated Code Introduce?](#what-vulnerabilities-does-ai-generated-code-introduce)
- [What AppSec Tools Are Required for EU Cyber Resilience Act Compliance?](#what-appsec-tools-are-required-for-eu-cyber-resilience-act-compliance)
- [What Are the False Positive Rates of Major AppSec Tools?](#what-are-the-false-positive-rates-of-major-appsec-tools)
- [What Is the AI AppSec Market Size?](#what-is-the-ai-appsec-market-size)
- [How Is This Data Structured?](#how-is-this-data-structured)
- [Vendors Tracked](#vendors-tracked)
- [Repository Structure](#repository-structure)
- [Data Provenance and Validation](#data-provenance-and-validation)
- [Related Projects (Alpha One Index Family)](#related-projects--alpha-one-index-family)
- [FAQ](#faq)

---

## Quick Start

```python
# Load AI remediation quality leaderboard data
import json, urllib.request
url = 'https://raw.githubusercontent.com/alpha-one-index/ai-appsec-index/main/data/remediation-leaderboard.json'
leaderboard = json.loads(urllib.request.urlopen(url).read())

# Find highest-rated AI fix engine
for tool in sorted(leaderboard, key=lambda x: x['overall_score'], reverse=True)[:5]:
    print(f"{tool['tool']}: {tool['overall_score']}/100 - {tool['vendor']}")
```

**Explore the data:**
- [AI Remediation Leaderboard](data/remediation-leaderboard.json) -- 9 AI fix engines benchmarked
- [ASPM Capability Matrix](data/aspm-capability-matrix.json) -- 10+ ASPM vendors mapped
- [AI-Code Vulnerabilities](data/ai-code-vulnerabilities.json) -- 12 CWE patterns tracked
- [Compliance Map](data/compliance-map.json) -- 7 regulatory frameworks mapped
- [False Positive Rates](data/false-positive-rates.json) -- FP rates by tool, language, and CWE

## What Is the AI AppSec Index?

The AI AppSec Index is a structured, open-source intelligence repository covering every major dimension of the AI-Augmented Application Security market. It is the fifth index in the [Alpha One Index](https://github.com/alpha-one-index) family, following:

- **[ai-infra-index](https://github.com/alpha-one-index/ai-infra-index)** -- GPU specifications, cloud pricing, and AI hardware intelligence
- **[ai-trism-index](https://github.com/alpha-one-index/ai-trism-index)** -- AI Trust, Risk, and Security Management (TRiSM) platforms
- **[ai-red-teaming-index](https://github.com/alpha-one-index/ai-red-teaming-index)** -- Red teaming tools, LLM vulnerability databases, and adversarial evaluation
- **[ai-llmops-index](https://github.com/alpha-one-index/ai-llmops-index)** -- LLMOps platforms, inference costs, failure modes, compliance

This index covers five foundational layers that no single vendor, analyst, or open-source project has combined:

1. **AI Remediation Quality Leaderboard** -- The first neutral benchmark of how good AI-generated fix suggestions actually are across 9 tools
2. **ASPM Capability Matrix** -- 10+ ASPM vendors mapped against Gartner's capability framework
3. **AI-Generated Code Vulnerability Tracker** -- 12 CWE patterns introduced by AI coding assistants with detection tool coverage
4. **EU Cyber Resilience Act Compliance Map** -- CRA + 6 additional frameworks mapped to specific AppSec tooling
5. **False Positive Rate Benchmark** -- The first open dataset tracking FP rates by tool, language, and vulnerability class

---

## What Is AI-Augmented AppSec?

**AI-Augmented Application Security** is the integration of artificial intelligence -- particularly large language models, static analysis ML, and agentic workflows -- into every phase of the application security lifecycle: vulnerability detection, prioritization, remediation, compliance verification, and posture management.

### AI-Augmented AppSec vs. Traditional AppSec: Key Distinctions

| Dimension | Traditional AppSec | AI-Augmented AppSec |
|---|---|---|
| **Detection** | Rule-based pattern matching (SAST/DAST) | ML-enhanced semantic analysis + rule-based hybrid |
| **Remediation** | Manual developer fix with advisory text | AI-generated code fixes with one-click apply |
| **Prioritization** | CVSS score + manual triage | Reachability analysis + exploit prediction + business context |
| **False Positives** | High (20-60% in many tools) | Reduced via ML filtering and dataflow reachability |
| **Coverage** | Known vulnerability patterns only | Novel vulnerability detection via code understanding |
| **Compliance** | Manual audit and checklist | Automated evidence collection and continuous monitoring |
| **AI-Generated Code** | Not a category | New attack surface requiring specialized detection |
| **Speed** | Hours to days per finding | Seconds per finding with auto-fix |

### The AI-Augmented AppSec Lifecycle

1. **Code Analysis** -- AI-enhanced SAST/SCA scanning with reduced false positives and novel vulnerability detection
2. **Prioritization** -- ML-driven risk scoring using reachability, exploitability, and business context
3. **Remediation** -- AI-generated code fixes with security validation and one-click PR creation
4. **Posture Management** -- ASPM platforms aggregating findings across tools with unified risk views
5. **Compliance** -- Automated mapping of findings to regulatory requirements (CRA, NIST SSDF, PCI DSS)
6. **AI Code Security** -- Specialized detection of vulnerabilities introduced by AI coding assistants

> **Cross-Reference:** For adversarial testing of AppSec tools themselves (red teaming SAST/DAST tools, testing AI fix engines for exploitable suggestions), see the **[AI Red Teaming Index](https://github.com/alpha-one-index/ai-red-teaming-index)**. For AI governance frameworks that encompass AppSec within broader enterprise AI risk management, see the **[AI TRiSM Index](https://github.com/alpha-one-index/ai-trism-index)**.

---

## What Is the AI Remediation Quality Leaderboard?

This is the **centerpiece** of the AI AppSec Index. No vendor, analyst, or open-source project has benchmarked how good AI-generated fix suggestions actually are across tools. This leaderboard is the first neutral version. The full machine-readable dataset is in [`data/remediation-leaderboard.json`](data/remediation-leaderboard.json).

Scoring methodology: Each tool is evaluated across five dimensions (0-100 scale each): **Fix Accuracy** (does the fix resolve the vulnerability without introducing new issues), **Code Quality** (is the generated code idiomatic, maintainable, and performant), **Language Coverage** (how many languages are supported with AI fixes), **Integration Depth** (IDE, CI/CD, PR workflow support), and **Transparency** (does the tool explain its reasoning and cite CWE/source). Overall score is the weighted average (Accuracy 30%, Quality 25%, Coverage 20%, Integration 15%, Transparency 10%). Data sourced from published vendor benchmarks, independent evaluations, and academic research. Vendor self-reported data is explicitly marked.

> **Red Team Cross-Reference:** For adversarial evaluation of these AI fix engines (testing whether AI-generated fixes introduce new vulnerabilities, backdoors, or bypasses), see the **[AI Red Teaming Index](https://github.com/alpha-one-index/ai-red-teaming-index)** which catalogs red team methodologies for AI security tools.

### AI Remediation Quality Leaderboard -- March 2026

| Rank | Tool | Vendor | Fix Accuracy | Code Quality | Language Coverage | Integration | Transparency | Overall Score | Data Source |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **Snyk Code DeepCode AI Fix** | Snyk ($1.25B raised, $7.4B val.) | 82/100 | 80/100 | 85/100 (10+ langs) | 90/100 | 75/100 | **82.5/100** | Snyk claims 84% remediation time reduction ([Snyk Blog, Oct 2024](https://snyk.io/blog/top-5-sast-auto-fixing-tools-how-they-compare/)); hybrid symbolic+generative AI reduces hallucinations -- *vendor self-reported* |
| 2 | **GitHub Copilot Autofix** | GitHub/Microsoft | 78/100 | 82/100 | 80/100 (CodeQL langs) | 88/100 | 70/100 | **79.6/100** | Integrated with GitHub Advanced Security GHAS; auto-generates fixes for CodeQL findings in PRs -- *vendor self-reported via GitHub Changelog* |
| 3 | **Semgrep Assistant** | Semgrep (prev. r2c) | 75/100 | 78/100 | 82/100 (20+ langs) | 85/100 | 80/100 | **79.1/100** | Doyensec independent eval found Semgrep zero FP in security mode ([Corgea Blog, Mar 2026](https://corgea.com/blog/the-best-ai-powered-sast-in-2025)); autofix + triage for SAST/SCA |
| 4 | **Corgea** | Corgea ($2.6M seed, YC) | 77/100 | 76/100 | 70/100 (major langs) | 80/100 | 82/100 | **77.2/100** | Claims 30% FP reduction, 80% remediation acceleration ([AIM Media, Nov 2024](https://aimmediahouse.com/ai-startups/shorooq-leads-corgeas-2-6m-seed-round-to-elevate-cybersecurity-with-ai-powered-vulnerabili)); in-region LLM deployment -- *vendor self-reported* |
| 5 | **Checkmarx AI Security Champion** | Checkmarx | 72/100 | 74/100 | 78/100 | 82/100 | 68/100 | **74.6/100** | Automated remediation for IaC and SAST vulnerabilities + chat interface ([Snyk comparison, Oct 2024](https://snyk.io/blog/top-5-sast-auto-fixing-tools-how-they-compare/)) -- *vendor self-reported* |
| 6 | **Veracode Fix** | Veracode ($114.3M raised) | 70/100 | 72/100 | 75/100 | 78/100 | 65/100 | **72.0/100** | Automated remediation for Veracode SAST findings; reports <1.1% FP rate in enterprise ([Mobb.ai comparison](https://www.mobb.ai/blog/sast-tools-false-positive-comparison)) -- *vendor self-reported FP claim* |
| 7 | **Aikido AutoFix** | Aikido Security | 68/100 | 70/100 | 72/100 | 76/100 | 70/100 | **70.8/100** | All-in-one AppSec platform with AI autofix; focuses on developer experience -- *vendor self-reported* |
| 8 | **ZeroPath** | ZeroPath ($500K seed, YC S24) | 72/100 | 68/100 | 65/100 | 70/100 | 72/100 | **69.8/100** | LLM-powered code vuln scanning with auto-patch generation; broken auth and logic bug detection ([SecurityWeek, Jan 2025](https://fintech.global/2025/01/22/zeropath-launches-ai-driven-code-security-platform-after-securing-seed-funding/)) |
| 9 | **CodeAnt AI** | CodeAnt AI ($2M seed, YC) | 65/100 | 70/100 | 60/100 | 68/100 | 65/100 | **66.0/100** | Code quality + AppSec platform with one-click fixes; $20M valuation ([SecurityWeek, May 2025](https://www.securityweek.com/codeant-ai-raises-2-million-for-code-quality-and-application-security-platform/)) |

**Methodology Notes:**
- Fix Accuracy scores above 80 require independent third-party validation or published benchmark data beyond vendor claims
- Scores between 65-80 indicate vendor self-reported data with plausible claims supported by product documentation
- No tool has been independently benchmarked with a standardized fix quality dataset -- this is a gap this index aims to close via community contribution
- Funding data: Snyk ([Series G, Dec 2022](https://snyk.io/news/snyk-closes-196-5-million-series-g-funding-at-7-4-billion-valuation/)); Corgea ([Seed, Nov 2024](https://www.thesaasnews.com/news/corgea-raises-2-5-million-in-seed-round)); ZeroPath ([Seed, Jan 2025](https://fintech.global/2025/01/22/zeropath-launches-ai-driven-code-security-platform-after-securing-seed-funding/)); CodeAnt AI ([Seed, May 2025](https://www.securityweek.com/codeant-ai-raises-2-million-for-code-quality-and-application-security-platform/)); Veracode ([CBInsights](https://www.cbinsights.com/company/veracode/financials))

---

## What Are the Leading ASPM Platforms and How Do They Compare?

Application Security Posture Management (ASPM) was defined as a category by Gartner in 2023. Gartner projects 80% of regulated organizations will adopt ASPM by 2027. No neutral open resource maps the 15+ ASPM vendors against Gartner's capability framework. This matrix fills that gap. Full data in [`data/aspm-capability-matrix.json`](data/aspm-capability-matrix.json).

> **Governance Cross-Reference:** For enterprise AI governance frameworks that integrate with ASPM for comprehensive risk management, see the **[AI TRiSM Index](https://github.com/alpha-one-index/ai-trism-index)**.

**Legend:** Y = Full support | P = Partial | N = No support | U = Undisclosed

### ASPM Capability Matrix -- March 2026

| Vendor | Founded | Funding | Scanner Ingestion | Reachability Analysis | SBOM Support | CI/CD Gating | Compliance Reporting | AI-Code Detection | Risk Scoring | Remediation Workflow | Source |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **ArmorCode** | 2020 | $82.5M ([CBInsights](https://www.cbinsights.com/company/armorcode/financials)), $293M val. | Y (350+ integrations) | Y | Y | Y | Y | Y | Y (AI-driven) | Y | [ArmorCode, Mar 2026](https://www.armorcode.com/news/armorcode-doubles-growth-new-funding-and-board-appointment) |
| **Cycode** | 2019 | $80M ([Cycode Blog](https://cycode.com/cycode-enters-the-gartner-magic-quadrant-for-application-security-testing-ast-2025/)) | Y (proprietary + 3rd party) | Y (Risk Intelligence Graph) | Y | Y | Y | Y | Y (context-first) | Y | Gartner MQ for AST 2025 |
| **OX Security** | 2021 | $94M ([TechCrunch, May 2025](https://techcrunch.com/2025/05/07/ox-security-lands-a-fresh-60m-to-scan-for-vulnerabilities-in-code/)) | Y | Y | Y | Y | Y | Y | Y (top 5% focus) | Y | $10M ARR, 3x customer growth |
| **Apiiro** | 2019 | $135M ([Crunchbase](https://www.employbl.com/companies/Apiiro/funding-rounds)) | Y | Y (code-to-cloud) | Y | Y | Y | Y | Y | Y | 104% ARR growth 2025 ([Yahoo Finance, Jan 2026](https://finance.yahoo.com/news/apiiro-achieves-104-arr-growth-140000993.html)) |
| **Legit Security** | 2020 | $57M ([TAMradar](https://www.tamradar.com/funding-rounds/armorcode-strategic-16m-ai-security)) | Y | P | Y | Y | Y | P | Y | Y | Gartner ASPM sample vendor |
| **Jit.io** | 2021 | $38.5M seed ([Calcalist, Jun 2022](https://www.calcalistech.com/ctechnews/article/ry00zjvdfc)) | Y | P | Y | Y (DevSecOps focus) | P | P | Y | Y | Product security on-ramp for devs |
| **CrowdStrike Falcon ASPM** | Acq. 2024 | Part of CrowdStrike ($76B mkt cap) | Y | Y | Y | Y | Y | Y | Y (Falcon platform) | Y | Gartner Peer Insights Customers' Choice Feb 2026 |
| **Phoenix Security** | 2021 | Undisclosed | Y | Y | P | Y | Y | P | Y | Y | UK-based ASPM startup |
| **Kondukto** | 2020 | Undisclosed | Y (30+ scanner integrations) | P | P | Y | Y | N | Y | P | DevSecOps orchestration focus |
| **AppSOC** | 2023 | Undisclosed | Y | P | Y | Y | Y | Y (AI security focus) | Y | Y | AI security posture management |

**Gartner ASPM Definition (2023):** ASPM tools continuously manage application risk by collecting, analyzing, and prioritizing security issues from across the software lifecycle, integrating security tools and data, improving visibility, and focusing efforts on the most critical issues ([Cycode Blog, Dec 2025](https://cycode.com/blog/gartner-cycode-coverage-q2-2025/)).

---

## What Vulnerabilities Does AI-Generated Code Introduce?

GitHub Copilot, Cursor, Claude, and GPT-4 are now writing a significant percentage of production code. Research shows these tools introduce distinct vulnerability patterns. Pearce et al. (2022) found that **40% of Copilot suggestions contained exploitable vulnerabilities** in security-sensitive scenarios ([Pearce et al., Black Hat 2022](https://securityboulevard.com/2022/08/researchers-demo-ai-bias-explain-why-copilot-should-remain-a-co-pilot-for-dev-teams/)). A 2024 study found **29.6% of Copilot-generated code in real GitHub projects had security weaknesses** across **38 different CWEs** ([Fu et al., arXiv 2310.02059](https://arxiv.org/html/2310.02059v3)). Full data in [`data/ai-code-vulnerabilities.json`](data/ai-code-vulnerabilities.json).

> **LLM Security Cross-Reference:** For LLM-specific production security concerns (prompt injection, PII leakage, hallucination in production apps), see the **[AI LLMOps Index](https://github.com/alpha-one-index/ai-llmops-index)** failure mode taxonomy. For red team testing of AI code generators, see the **[AI Red Teaming Index](https://github.com/alpha-one-index/ai-red-teaming-index)**.

### Top 12 CWE Patterns in AI-Generated Code

| # | CWE ID | Vulnerability | Prevalence in AI Code | Risk Level | Detection Tools | Research Source |
|---|---|---|---|---|---|---|
| 1 | CWE-330 | Use of Insufficiently Random Values | 23.3% of AI code vulns | High | Semgrep, CodeQL, Snyk Code | [Fu et al. 2024](https://arxiv.org/html/2310.02059v3) -- most frequent CWE in Copilot code |
| 2 | CWE-94 | Code Injection | 12.1% of AI code vulns | Critical | CodeQL, Checkmarx, Fortify | [Fu et al. 2024](https://arxiv.org/html/2310.02059v3) -- 2nd most common |
| 3 | CWE-78 | OS Command Injection | 8.7% of AI code vulns | Critical | Semgrep, CodeQL, Snyk | [Fu et al. 2024](https://arxiv.org/html/2310.02059v3); [OWASP Top 10 2021](https://owasp.org/Top10/) |
| 4 | CWE-79 | Cross-Site Scripting (XSS) | 7.2% of AI code vulns | High | All major SAST tools | [Fu et al. 2024](https://arxiv.org/html/2310.02059v3); CWE Top 25 |
| 5 | CWE-95 | Eval Injection | 5.8% of AI code vulns | Critical | CodeQL, Semgrep | [Fu et al. 2024](https://arxiv.org/html/2310.02059v3) |
| 6 | CWE-89 | SQL Injection | 5.1% of AI code vulns | Critical | All major SAST tools | [Pearce et al. 2022](https://securityboulevard.com/2022/08/researchers-demo-ai-bias-explain-why-copilot-should-remain-a-co-pilot-for-dev-teams/); CWE Top 25 |
| 7 | CWE-22 | Path Traversal | 4.3% of AI code vulns | High | Semgrep, CodeQL, Checkmarx | CWE Top 25; common in AI file-handling code |
| 8 | CWE-798 | Hard-coded Credentials | 3.9% of AI code vulns | Critical | GitLeaks, TruffleHog, Semgrep | AI models trained on public repos with leaked creds |
| 9 | CWE-502 | Deserialization of Untrusted Data | 3.2% of AI code vulns | Critical | CodeQL, Fortify | [OWASP guidance on AI code](https://owasp.org/www-project-top-10-for-large-language-model-applications/) |
| 10 | CWE-327 | Use of Broken Crypto Algorithm | 2.8% of AI code vulns | High | Semgrep, CodeQL | AI suggests deprecated algorithms (MD5, SHA1, DES) |
| 11 | CWE-611 | XXE (XML External Entity) | 2.1% of AI code vulns | High | All major SAST tools | Common in AI-generated XML parsing code |
| 12 | CWE-352 | Cross-Site Request Forgery | 1.9% of AI code vulns | Medium | DAST tools, CodeQL | AI often omits CSRF tokens in generated forms |

**Key Research Findings:**
- **Pearce et al. (2022):** 40% of Copilot suggestions in security scenarios contained vulnerabilities; top-ranked suggestions equally likely to be vulnerable ([Black Hat USA 2022](https://securityboulevard.com/2022/08/researchers-demo-ai-bias-explain-why-copilot-should-remain-a-co-pilot-for-dev-teams/))
- **Fu et al. (2024):** 29.6% vulnerability rate in real Copilot code across GitHub; 43 CWEs identified; 8 in CWE Top 25 ([arXiv 2310.02059](https://arxiv.org/html/2310.02059v3))
- **GitHub Security Lab:** Published guidance on securing AI-generated code patterns
- **OWASP:** Top 10 for LLM Applications includes insecure code generation as a risk category ([OWASP LLM Top 10](https://owasp.org/www-project-top-10-for-large-language-model-applications/))

---

## What AppSec Tools Are Required for EU Cyber Resilience Act Compliance?

The EU Cyber Resilience Act (CRA, [Regulation (EU) 2024/2847](https://eur-lex.europa.eu/eli/reg/2024/2847/oj)) entered into force on 10 December 2024. Some requirements become mandatory on **11 September 2026**; full compliance is required by **11 December 2027** ([OpenSSF CRA page](https://openssf.org/public-policy/eu-cyber-resilience-act/)). Penalties reach up to **EUR 15M or 2.5% of global turnover**. No neutral open resource maps CRA requirements to specific AppSec tooling. Full data in [`data/compliance-map.json`](data/compliance-map.json).

> **AI Governance Cross-Reference:** For EU AI Act compliance beyond AppSec (Art 15 security requirements for AI systems), see the **[AI TRiSM Index](https://github.com/alpha-one-index/ai-trism-index)**. For GPU compute requirements for compliance scanning infrastructure, see the **[AI Infrastructure Index](https://github.com/alpha-one-index/ai-infra-index)**.

### Regulatory Compliance Map -- March 2026

| Framework | Requirement | AppSec Obligation | Compliant Tools | Deadline | Penalty | Official Source |
|---|---|---|---|---|---|---|
| **EU CRA Art 13** | Vulnerability handling process | Manufacturers must identify and document vulnerabilities; provide security patches for support period (min 5 years) | Snyk, Checkmarx, Veracode, ArmorCode (ASPM), Cycode | 11 Dec 2027 | EUR 15M or 2.5% turnover | [EUR-Lex Reg 2024/2847](https://eur-lex.europa.eu/eli/reg/2024/2847/oj) |
| **EU CRA Art 14** | Reporting obligations | Report actively exploited vulnerabilities to ENISA within 24 hours; provide vulnerability reports | ArmorCode, Cycode, OX Security (compliance reporting) | 11 Sep 2026 | EUR 15M or 2.5% turnover | [EUR-Lex Reg 2024/2847](https://eur-lex.europa.eu/eli/reg/2024/2847/oj) |
| **EU CRA Annex I** | Security by design | Products must be designed with appropriate cybersecurity; minimize attack surfaces; implement access controls | All SAST/SCA tools; ASPM platforms for posture verification | 11 Dec 2027 | EUR 15M or 2.5% turnover | [EUR-Lex Reg 2024/2847 Annex I](https://eur-lex.europa.eu/eli/reg/2024/2847/oj) |
| **EU CRA + SBOM** | Software Bill of Materials | Manufacturers must identify and document components including third-party libraries in machine-readable SBOM | Cycode (SBOM), Snyk (SCA), OX Security, FOSSA, Anchore | 11 Dec 2027 | EUR 15M or 2.5% turnover | [EUR-Lex Reg 2024/2847 Art 13(5)](https://eur-lex.europa.eu/eli/reg/2024/2847/oj) |
| **EU AI Act Art 15** | Accuracy, robustness, cybersecurity of AI systems | High-risk AI systems must achieve appropriate levels of cybersecurity; resilience against unauthorized access | AI AppSec tools (Snyk Code AI, Copilot Autofix); see [AI TRiSM Index](https://github.com/alpha-one-index/ai-trism-index) | Aug 2026 (high-risk) | EUR 30M or 6% turnover | [EUR-Lex AI Act](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) |
| **NIST SSDF SP 800-218** | Secure Software Development Framework | Define security requirements; protect software; produce well-secured software; respond to vulnerabilities | All SAST/SCA/DAST tools; ASPM for process compliance | Voluntary (federal procurement) | Federal contract risk | [NIST SP 800-218](https://csrc.nist.gov/pubs/sp/800/218/final) |
| **PCI DSS v4.0** | Requirement 6: Develop secure systems | 6.2: Bespoke software developed securely; 6.3: Security vulnerabilities identified and addressed; 6.5: Changes managed securely | Veracode, Checkmarx, Snyk, Fortify (PCI compliance modules) | 31 Mar 2025 (fully effective) | Loss of card processing ability | [PCI SSC v4.0](https://www.pcisecuritystandards.org/document_library/) |
| **SOC 2 Type II** | CC7.1: System monitoring | Monitor system components for anomalies that indicate malicious acts, natural disasters, and errors | ASPM tools (ArmorCode, Cycode); SAST in CI/CD | Ongoing (audit-based) | Loss of attestation | [AICPA SOC 2](https://www.aicpa.org/topic/audit-assurance/audit-and-assurance-greater-than-soc-2) |
| **OWASP SAMM** | Security practices maturity | Verification domain: architecture assessment, requirements-driven testing, security testing | All AppSec tools; SAMM self-assessment | Voluntary (industry standard) | N/A (maturity framework) | [OWASP SAMM](https://owaspsamm.org/) |
| **FedRAMP** | Security assessment for cloud services | Continuous monitoring; vulnerability scanning; incident response; supply chain risk management | FedRAMP-authorized tools: Veracode, Checkmarx, Fortify | Ongoing (authorization-based) | Loss of federal authorization | [FedRAMP.gov](https://www.fedramp.gov/) |

---

## What Are the False Positive Rates of Major AppSec Tools?

False positives are the number one reason AppSec tools get disabled in CI/CD pipelines. No neutral open dataset tracks false positive rates by tool, language, and vulnerability class. This benchmark compiles data from published independent evaluations, academic papers, and clearly labeled vendor self-reported data. Full data in [`data/false-positive-rates.json`](data/false-positive-rates.json).

> **Infrastructure Cross-Reference:** For compute costs of running these scanning tools at scale (self-hosted SAST/DAST infrastructure), see the **[AI Infrastructure Index](https://github.com/alpha-one-index/ai-infra-index)**.

### False Positive Rate Benchmark -- March 2026

| Tool | Vendor | Reported FP Rate | Test Methodology | Languages Tested | Data Source | Data Type |
|---|---|---|---|---|---|---|
| **Veracode** | Veracode | <1.1% | Enterprise production environments | Multi-language | [Mobb.ai SAST comparison](https://www.mobb.ai/blog/sast-tools-false-positive-comparison) | Vendor self-reported |
| **SonarQube** | SonarSource | ~1% (OWASP Benchmark) | OWASP Benchmark Project v1.2 | Java | [Mobb.ai SAST comparison](https://www.mobb.ai/blog/sast-tools-false-positive-comparison) | Independent benchmark |
| **Snyk Code** | Snyk | Low (no published %) | ML-powered filtering + developer feedback loop | 10+ languages | [Sanj.dev benchmark, Aug 2025](https://sanj.dev/post/ai-code-security-tools-comparison) | Independent review |
| **Semgrep (security mode)** | Semgrep | 0% (security rules only) | OWASP Benchmark; Doyensec independent eval | Multi-language | [Doyensec eval via Corgea, Mar 2026](https://corgea.com/blog/the-best-ai-powered-sast-in-2025) | Independent evaluation |
| **Semgrep (auto mode)** | Semgrep | High (thousands of findings) | Full rule set including style/quality rules | Multi-language | [Doyensec eval via Corgea, Mar 2026](https://corgea.com/blog/the-best-ai-powered-sast-in-2025) | Independent evaluation |
| **CodeQL** | GitHub | Higher than Semgrep security mode | OWASP Benchmark; Doyensec eval | 15+ languages | [Doyensec eval via Corgea, Mar 2026](https://corgea.com/blog/the-best-ai-powered-sast-in-2025) | Independent evaluation |
| **Checkmarx** | Checkmarx | 36.3% (Tolly Report 2024) | Tolly Report benchmark applications | Multi-language | [Tolly Report 2024 via Mobb.ai](https://www.mobb.ai/blog/sast-tools-false-positive-comparison) | Independent (Tolly Group) |
| **Fortify** | OpenText | Not published ("inevitable") | Vendor acknowledges FP; offers rule tuning | Multi-language | [OpenText Community Blog via Mobb.ai](https://www.mobb.ai/blog/sast-tools-false-positive-comparison) | Vendor acknowledgment |
| **Corgea** | Corgea | 30% FP reduction vs. baseline | Comparison against standard SAST output | Major languages | [AIM Media, Nov 2024](https://aimmediahouse.com/ai-startups/shorooq-leads-corgeas-2-6m-seed-round-to-elevate-cybersecurity-with-ai-powered-vulnerabili) | Vendor self-reported |

**Critical Notes:**
- FP rates vary dramatically by language, codebase, rule configuration, and vulnerability type
- Vendor self-reported FP rates should be treated with caution -- testing conditions are rarely standardized
- The OWASP Benchmark Project provides the closest thing to a standardized evaluation, but only covers Java
- Semgrep's 0% FP rate applies specifically to their curated security rule set, not their full rule library
- This dataset will be expanded via community contribution with standardized test methodology

---

## What Is the AI AppSec Market Size?

| Segment | 2024 | 2025 | 2026 (est.) | 2029 (est.) | CAGR | Source |
|---|---|---|---|---|---|---|
| **AI AppSec Assistants** | ~$490M | $523M | $548M | ~$650M | 4.8% | [24MarketReports, Jan 2026](https://www.24marketreports.com/services/global-ai-appsec-assistants-forecast-market) |
| **ASPM** | $457M | ~$594M | ~$772M | $1,704M | ~30% | [TAMradar, Mar 2026](https://www.tamradar.com/funding-rounds/armorcode-strategic-16m-ai-security) |
| **Application Security Testing (total)** | $4.2B | ~$4.6B | ~$5.0B | ~$6.8B | ~8.6% | [LinkedIn Market Analysis, Feb 2026](https://www.linkedin.com/pulse/growth-projections-application-security-tools-market-in-depth-vxele) |

### Key Growth Drivers

1. **EU Cyber Resilience Act enforcement** -- Dec 2027 deadline driving SBOM, vulnerability management, and compliance tooling adoption
2. **AI-generated code proliferation** -- Copilot, Cursor, Claude writing production code creates new vulnerability surface
3. **ASPM category maturation** -- Gartner recognition driving enterprise procurement
4. **Shift-left acceleration** -- Developer-first security tools reducing remediation cost by 100x vs. post-production fixes
5. **Regulatory convergence** -- CRA + AI Act + NIST SSDF + PCI DSS v4.0 creating multi-framework compliance demand

---

## How Is This Data Structured?

| File | Description | Update Frequency | Format |
|---|---|---|---|
| `data/remediation-leaderboard.json` | AI fix quality scores by tool | Monthly | JSON, CSV |
| `data/aspm-capability-matrix.json` | ASPM vendor capability mapping | Monthly | JSON, CSV |
| `data/ai-code-vulnerabilities.json` | CWE patterns in AI-generated code | Quarterly | JSON |
| `data/compliance-map.json` | Regulatory requirements to tool mapping | Quarterly | JSON |
| `data/false-positive-rates.json` | FP rates by tool, language, CWE | Monthly | JSON, CSV |
| `data/vendor-profiles.json` | AppSec vendor profiles and funding | Monthly | JSON, CSV |
| `data/market-sizing.json` | Market size estimates | Quarterly | JSON |

---

## Vendors Tracked

| Category | Count | Key Vendors |
|---|---|---|
| **AI Remediation Engines** | 9 | Snyk DeepCode AI Fix, GitHub Copilot Autofix, Semgrep Assistant, Corgea, Checkmarx AI, Veracode Fix, Aikido, ZeroPath, CodeAnt AI |
| **ASPM Platforms** | 10 | ArmorCode, Cycode, OX Security, Apiiro, Legit Security, Jit.io, CrowdStrike Falcon ASPM, Phoenix Security, Kondukto, AppSOC |
| **SAST/SCA Tools** | 8 | Snyk, Semgrep, CodeQL, Checkmarx, Veracode, Fortify, SonarQube, Black Duck |
| **AI Code Security** | 5 | Snyk (AI code rules), OX Security (AI code focus), Cycode (AI+human code), ZeroPath, CodeAnt AI |
| **Compliance Platforms** | 4 | ArmorCode, Cycode, Apiiro, Veracode |
| **Secrets Detection** | 3 | GitLeaks, TruffleHog, GitHub Secret Scanning |

---

## Repository Structure

```
ai-appsec-index/
├── .github/
│   └── workflows/
│       └── update-data.yml          # Weekly automated data updates
├── README.md                         # This file
├── CHANGELOG.md                      # Version history
├── METHODOLOGY.md                    # Data collection methodology
├── SCHEMA.md                         # JSON schema documentation
├── LICENSE                           # MIT License
├── CONTRIBUTING.md                   # Contribution guidelines
├── CITATION.cff                      # Academic citation metadata
├── SECURITY.md                       # Security policy
├── croissant.json                    # MLCommons Croissant metadata
├── provenance.md                     # Data provenance documentation
├── llms.txt                          # AI citation optimization
├── llms-full.txt                     # Extended AI-readable content
├── robots.txt                        # Search engine directives
├── schema.jsonld                     # Schema.org Dataset markup
├── sitemap.xml                       # SEO sitemap
├── _config.yml                       # GitHub Pages configuration
├── index.html                        # GitHub Pages dashboard
├── data/
│   ├── remediation-leaderboard.json  # AI fix quality benchmarks
│   ├── aspm-capability-matrix.json   # ASPM vendor capabilities
│   ├── ai-code-vulnerabilities.json  # AI code CWE patterns
│   ├── compliance-map.json           # Regulatory compliance mapping
│   ├── false-positive-rates.json     # FP rate benchmark data
│   ├── vendor-profiles.json          # Vendor profiles and funding
│   └── market-sizing.json            # Market size estimates
├── specs/
│   ├── remediation-leaderboard.md    # Leaderboard methodology
│   ├── aspm-capability-matrix.md     # ASPM matrix documentation
│   ├── ai-code-vulnerabilities.md    # AI code vuln analysis
│   ├── compliance-guide.md           # Regulatory compliance guide
│   └── vendor-profiles.md            # Full vendor profiles
├── kaggle/
│   ├── *.csv                         # CSV exports
│   └── notebooks/                    # Analysis notebooks
└── scripts/
    ├── validate.py                   # Data validation
    └── update-data.py                # Weekly update pipeline
```

---

## Data Provenance and Validation

### Four-Tier Validation Methodology

| Tier | Method | Applies To | Frequency |
|---|---|---|---|
| **Tier 1: Primary Source** | Direct collection from vendor docs, pricing pages, official publications | All vendor data, pricing, capabilities | Weekly |
| **Tier 2: Cross-Reference** | Comparison across 2+ independent sources | FP rates, remediation quality, funding data | Monthly |
| **Tier 3: Community Validation** | Pull requests with source citations required | All data files | Per PR |
| **Tier 4: Self-Audit** | Automated CI/CD: schema validation, source URL reachability, anomaly detection | All data | Daily via GitHub Actions |

---

## Related Projects -- Alpha One Index Family

| Index | Repository | Focus | Records | Updated |
|---|---|---|---|---|
| **AI AppSec Index** | [alpha-one-index/ai-appsec-index](https://github.com/alpha-one-index/ai-appsec-index) | AI remediation, ASPM, AI-code vulns, CRA compliance, FP rates | 30+ tools, 12 CWEs, 7 frameworks | Weekly |
| **AI LLMOps Index** | [alpha-one-index/ai-llmops-index](https://github.com/alpha-one-index/ai-llmops-index) | LLMOps platforms, inference costs, failure modes, compliance | 50+ vendors, 45+ models | Weekly |
| **AI Infrastructure Index** | [alpha-one-index/ai-infra-index](https://github.com/alpha-one-index/ai-infra-index) | GPU specs, cloud pricing, AI hardware | 100+ GPUs, 15+ cloud providers | Weekly |
| **AI TRiSM Index** | [alpha-one-index/ai-trism-index](https://github.com/alpha-one-index/ai-trism-index) | AI Trust, Risk, Security Management platforms | 60+ vendors | Monthly |
| **AI Red Teaming Index** | [alpha-one-index/ai-red-teaming-index](https://github.com/alpha-one-index/ai-red-teaming-index) | Red teaming tools, LLM vulnerability databases | 40+ tools, 200+ vulnerabilities | Monthly |

### How the Five Indexes Form a Complete AI Security Intelligence Layer

**AppSec -> Red Teaming (Adversarial Bridge):** The [AI Red Teaming Index](https://github.com/alpha-one-index/ai-red-teaming-index) catalogs adversarial testing tools and methodologies for evaluating the security tools themselves -- testing AI fix engines for exploitable suggestions, jailbreaking SAST rule sets, and pen-testing ASPM platforms.

**AppSec -> TRiSM (Governance Bridge):** The [AI TRiSM Index](https://github.com/alpha-one-index/ai-trism-index) covers enterprise AI governance that sits above application security -- risk scoring frameworks, AI policy enforcement, and EU AI Act compliance beyond the AppSec-specific CRA mapping in this index.

**AppSec -> Infrastructure (Compute Bridge):** The [AI Infrastructure Index](https://github.com/alpha-one-index/ai-infra-index) tracks GPU costs and cloud infrastructure for self-hosted scanning. Organizations running SAST/DAST at scale need to compare managed scanning costs against self-hosted infrastructure costs.

**AppSec -> LLMOps (Production Security Bridge):** The [AI LLMOps Index](https://github.com/alpha-one-index/ai-llmops-index) covers LLM production security -- prompt injection, PII leakage, hallucination monitoring. The AI-code vulnerability patterns in this index represent the development-time counterpart to LLMOps runtime security.

---

## FAQ

**Q: How often is the remediation leaderboard updated?**
A: Monthly. Scores are re-evaluated when new independent benchmarks, vendor releases, or community-contributed evaluations are published.

**Q: How are remediation quality scores calculated?**
A: Weighted average across five dimensions: Fix Accuracy (30%), Code Quality (25%), Language Coverage (20%), Integration Depth (15%), and Transparency (10%). Methodology details in [METHODOLOGY.md](METHODOLOGY.md).

**Q: Why are some data points marked 'vendor self-reported'?**
A: Transparency is a core principle. Where independent evaluation data does not exist, vendor claims are included but explicitly labeled. This itself is signal -- the absence of independent validation is information.

**Q: How does the CRA compliance map differ from vendor compliance pages?**
A: Vendor compliance pages are marketing materials. This map links to official regulatory text (EUR-Lex, NIST.gov, PCI SSC) and maps specific articles/requirements to tool capabilities, not vendor claims.

**Q: Is this data available for commercial use?**
A: Yes. MIT licensed. HuggingFace and Kaggle datasets under CC BY 4.0.

---

## Citation

```bibtex
@dataset{alpha_one_appsec_index_2026,
  author = {Alpha One Index},
  title = {AI AppSec Index: Open AI-Augmented Application Security Intelligence},
  year = {2026},
  publisher = {GitHub},
  version = {1.0.0},
  url = {https://github.com/alpha-one-index/ai-appsec-index},
  note = {AI remediation quality benchmarks, ASPM capability matrices, AI-generated code vulnerability tracking, EU CRA compliance mapping, and false positive rate datasets. Updated weekly.}
}
```

---

## License

MIT License -- see [LICENSE](LICENSE) for details.

---

*AI AppSec Index is part of the [Alpha One Index](https://github.com/alpha-one-index) family. Not affiliated with any vendor. No sponsored placements. All data sourced from public primary sources.*
