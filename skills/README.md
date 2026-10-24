# Project modeling and review skills

The `anthropic/` folder contains four downloaded, project-local reference skills from [Anthropic's financial-services repository](https://github.com/anthropics/financial-services) at commit `574ed3624aebd0418c7e96cd101262f30210ab26` (retrieved October 24, 2026). They are redistributed under the included [Apache 2.0 license](anthropic/LICENSE). They are text workflows and optional scripts; no third-party script was run to produce this case model.

| Skill | Case use |
|---|---|
| [DCF model](anthropic/dcf-model/SKILL.md) | Cash-flow structure, discounting, terminal value and sensitivities |
| [Comps analysis](anthropic/comps-analysis/SKILL.md) | Peer selection and metric consistency if a comparable set is added |
| [Competitive analysis](anthropic/competitive-analysis/SKILL.md) | Candidate and channel diligence |
| [Investment banking deck check](anthropic/ib-check-deck/SKILL.md) | Appendix and slide number reconciliation |

These are **project-scoped downloads** available to teammates through the repository. The current model uses the local spreadsheet artifact workflow and its own assumptions; external skills are guidance, not a claim that a full comps analysis or a CAPM-derived WACC has been completed. Read source filings and the case prompt before relying on any template defaults. The team's explicit case instructions take precedence over these reference workflows.
