---
license: mit
task_categories:
  - text-classification
  - tabular-classification
language:
  - en
tags:
  - application-security
  - appsec
  - ai-security
  - vulnerability
  - cve
  - aspm
  - benchmark
  - false-positive
  - cra
  - eu-cyber-resilience-act
  - sast
  - devsecops
pretty_name: AI AppSec Index
size_categories:
  - n<1K
source_datasets:
  - original
---

# AI AppSec Index

The definitive open-source reference for AI-augmented application security.

## Dataset Description

6 structured datasets covering the AI AppSec landscape:

| Dataset | Records | Description |
|---------|---------|-------------|
| AI Remediation Leaderboard | 9+ | Benchmark scores for AI-powered code remediation engines |
| ASPM Capability Matrix | 15+ | Vendor comparison across 20+ capabilities |
| AI-Code Vulnerability Tracker | 48+ | Real CVEs in AI-generated code mapped to CWEs |
| EU CRA Compliance Map | 12+ | Tool-by-tool CRA regulatory readiness |
| False Positive Benchmark | 20+ | FP rates by tool, language, and CWE |
| CRA Timeline | 7 | Key compliance dates and requirements |

## Usage

```python
from datasets import load_dataset
ds = load_dataset("alpha-one-index/ai-appsec-index")
```

Or install the Python package:
```python
pip install git+https://github.com/alpha-one-index/ai-appsec-index.git
import ai_appsec_index
data = ai_appsec_index.load_dataset("remediation-leaderboard")
```

## Links

- [GitHub Repository](https://github.com/alpha-one-index/ai-appsec-index)
- [Interactive Dashboard](https://alpha-one-index.github.io/ai-appsec-index/)
- [Kaggle Dataset](https://www.kaggle.com/datasets/alpha-one-index/ai-appsec-index)
- [Methodology](https://github.com/alpha-one-index/ai-appsec-index/blob/main/METHODOLOGY.md)

## Citation

```bibtex
@dataset{ai_appsec_index_2026,
  title={AI AppSec Index},
  author={Alpha One Index},
  year={2026},
  url={https://github.com/alpha-one-index/ai-appsec-index}
}
```
