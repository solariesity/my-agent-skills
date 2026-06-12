---
name: paper-analyst-zh
description: "Translate and deeply analyze English computer science and engineering papers in Chinese. Use when the user is a Chinese reader and wants an English paper, preprint, or PDF explained in Chinese with: (1) faithful translation, (2) plain-language explanation for non-specialists, (3) formal academic expression, (4) professional full-text analysis of methods, experiments, results, strengths, weaknesses, and reproduction value, and (5) a presentation outline for group meetings. Typical triggers include: 组会, 组会准备, 文献汇报, 帮我梳理这篇文献, 论文汇报, 文献阅读, 帮我读一篇论文, 论文汇报准备, 翻译这篇论文, 分析这篇论文. When the source is a PDF file, PDF attachment, or .pdf path, first invoke the pdf skill or an equivalent PDF-reading workflow automatically before analysis."
---

# Paper Analyst Zh

## Overview

Read an English CS or engineering paper, preserve technical accuracy, and explain it in layered Chinese for different audiences. Also suitable for preparing group meeting presentations and literature review reports.

Use a workflow-based structure. Keep terminology precise, avoid hallucinating missing details, and separate direct translation from interpretation.

## 触发条件

当用户说出以下关键词或类似表述时，自动应用此规范：
- "组会" / "组会准备" / "文献汇报"
- "帮我梳理/分析这篇文献/论文"
- "论文汇报" / "文献阅读" / "论文汇报准备"
- "翻译这篇论文" / "分析这篇论文" / "帮我读一篇论文"
- 上下文明显指向论文阅读、分析或汇报准备

## Workflow

### 1. Ingest the paper carefully

Read the full source before analyzing it.

Detect the source type first:
- If the user provides a `.pdf` file, PDF attachment, PDF URL, or a filesystem path ending in `.pdf`, automatically use the `pdf` skill or an equivalent PDF-reading workflow first.
- If the user pastes plain text, Markdown, HTML, or extracted sections directly, analyze that content directly without forcing a PDF workflow.

If the paper is a PDF, first use a PDF-reading workflow or skill to extract the content and inspect figures, tables, captions, and section structure instead of relying on raw text alone.

Capture at least:
- title
- abstract
- problem statement
- method or system design
- datasets
- baselines
- metrics
- implementation details
- main quantitative results
- ablation or component analysis
- limitations or failure cases

If a figure, table, or formula is important but partially unclear, say that explicitly instead of guessing.

### 1.1 PDF auto-handoff rule

When the source is a PDF, do not ask the user whether to use the `pdf` skill unless there is a concrete blocker. Treat PDF ingestion as the default first step.

Use the `pdf` skill to help with:
- extracting section text
- preserving page structure
- checking figure and table captions
- identifying experiment tables and result plots that need focused analysis

After PDF ingestion, continue with the normal Chinese translation and analysis workflow in this skill.

### 2. Use layered Chinese output

Unless the user asks for a different format, produce the answer in this order:

1. Paper snapshot
2. Full Chinese translation
3. Plain-language explanation
4. Formal academic expression
5. Professional deep analysis
6. Presentation outline (when preparing for group meetings or report prep mode)
7. Key takeaways and limitations
8. Terminology glossary

Keep translation and interpretation separate. Do not mix your opinions into the translation section.

The default deliverable is two Markdown files, not one mixed response:
- one file for the full Chinese translation only
- one file for all non-translation content, including the snapshot, plain-language explanation, formal academic expression, professional analysis, presentation outline, experiment analysis, limitations, and glossary

If the user does not explicitly opt out, write both files to disk.

### 2.1 Output file rules

When writing results, create two Markdown files by default.

Filename rules:
- If the source is a local file path such as `paper.pdf`, use the same basename and write:
  - `paper.translation.zh.md`
  - `paper.analysis.zh.md`
- If the source is an attachment with a visible filename, derive the basename from that filename.
- If the source has no stable filename, write:
  - `paper-translation.zh.md`
  - `paper-analysis.zh.md`

Location rules:
- If the source is a local file, write the Markdown files next to the source file unless the user requests another directory.
- Otherwise, write them in the current working directory.

Content rules:
- The translation file must contain translation only, plus minimal structural metadata such as the title and section headings.
- The analysis file must not repeat the full translation. It should contain the snapshot, plain-language explanation, formal academic expression, professional analysis, presentation outline (when applicable), experiment analysis, limitations, and glossary.
- In the chat response, briefly report the output paths and a short summary, rather than pasting the full translation unless the user explicitly asks for it inline.

### 3. Write the paper snapshot first

Start with a short structured summary:
- Chinese title
- original English title
- research area
- one-sentence core question
- one-sentence main contribution
- one-sentence result takeaway

If the venue, year, or author information is available in the source, include it.

### 4. Translate faithfully into Chinese

Translate the paper section by section in Chinese.

This translation must be complete and strict by default. Do not replace full translation with a summary, condensation, or selected excerpts unless the user explicitly asks for a shorter mode.

Rules:
- Preserve the original structure and heading hierarchy.
- Translate technical terms into natural Chinese, but keep the original English term in parentheses the first time it appears.
- Keep variable names, metric names, dataset names, model names, and code identifiers unchanged.
- Translate important figure captions, table captions, and experiment descriptions.
- Do not fabricate omitted text for unreadable equations or figures; mark them as unreadable or unclear when needed.
- References do not need full line-by-line translation unless the user explicitly asks for it.
- Translate every main body section that is readable from the source, including abstract, introduction, related work if present, method, experiments, conclusion, appendix sections that affect understanding, and important figure or table captions.
- If some text cannot be extracted cleanly, say exactly which section or page is incomplete.

For long papers, chunk the translation by sections while preserving continuity, but still write the complete translation to the translation Markdown file.

### 5. Explain it for non-specialists

After the translation, explain the paper in simple Chinese that a non-expert can follow.

Prefer:
- the problem in real-world terms
- why earlier approaches were insufficient
- the paper's idea in intuitive language
- what the experiments are trying to prove
- what the final conclusion means in practice

Avoid dense jargon. When jargon is necessary, explain it with a short analogy or plain paraphrase.

### 6. Write the formal academic expression (规范学术表述)

After the plain-language explanation, provide a formal academic restatement of the paper's methods and conclusions in polished Chinese.

This section is neither a faithful translation (which follows the original structure) nor a professional critique (which evaluates and questions). It presents the paper's contributions in formal academic Chinese, as one would write in a Chinese journal paper abstract or a conference summary.

Rules:
- Use standard academic terminology naturally, without over-stuffing jargon.
- Sentence structure can be formal but not overly complex.
- Avoid excessively obscure expressions.
- Cover the core method and main conclusions with academic rigor.
- The overall level should be comparable to a well-written Chinese academic abstract.

### 7. Write the professional deep analysis

Use the checklist in `references/analysis-checklist.md`.

At minimum, analyze:
- research problem and motivation
- technical route and method pipeline
- novelty versus likely prior baselines or common approaches
- assumptions and prerequisites
- experiment setting: datasets, baselines, metrics, implementation details, hardware or training setup if provided
- experiment results: headline wins, tradeoffs, weak cases, variance, fairness of comparison
- ablation studies: what each module contributes and whether the evidence is convincing
- robustness, generalization, efficiency, scalability, or deployment implications when discussed
- limitations, threats to validity, and what is still unproven
- reproduction difficulty and what artifacts would be needed to reproduce the work

When evaluating experiments, distinguish:
- what the paper explicitly proves
- what the paper suggests but does not fully prove
- what remains uncertain

### 8. Focus hard on experiments

For CS and engineering papers, give extra attention to experimental evidence.

Always answer these questions when the source supports them:
- What datasets or benchmarks were used, and are they appropriate?
- What baselines were compared, and are they strong enough?
- What metrics were used, and do they match the claim?
- Is the comparison fair?
- How large is the improvement in absolute and relative terms?
- Is the gain consistent across settings or only on a subset?
- Do the ablations really isolate the contribution?
- Are there hidden costs such as computation, latency, memory, annotation effort, or deployment complexity?

If the experiments are weak, say so clearly and explain why.

### 9. Write the presentation outline (汇报大纲)

When the user's context suggests group meeting or presentation preparation (e.g., 组会, 文献汇报, report prep mode), generate a structured presentation outline based on the analysis.

Recommended structure:
```
一、研究背景与问题
二、核心方法
三、实验结果
四、结论与启示
```

The outline should include:
- Section titles and key bullet points for each section.
- Annotations indicating which parts are best delivered in plain language (通俗解释) and which in formal academic register (规范表述).
- Logical flow that tells a coherent story to an audience with mixed expertise levels.

If the user is not preparing for a presentation and is not in report prep mode, this section can be condensed to a brief optional outline or omitted.

### 10. Use disciplined wording

Use these wording rules:
- Say "the paper states" when describing claims from the source.
- Say "this suggests" for reasonable but weaker inferences.
- Say "I cannot confirm from the provided paper text" when evidence is missing.

Do not overclaim novelty or practical value beyond the evidence shown.

### 11. Adapt depth to the user's goal

If the user asks for one of these modes, adapt accordingly:
- quick reading: keep a complete translation file, but shorten only the analysis file and the chat summary
- detailed reading: keep the full translation and full analysis (including formal academic expression and presentation outline)
- report prep: emphasize contributions, experiment results, likely audience questions, formal academic expression, and a detailed presentation outline
- reproduction prep: emphasize implementation details, missing settings, and experimental risks

If the user gives no mode, default to detailed reading.

## Resource

Read `references/analysis-checklist.md` when preparing the professional analysis section or when you need a stable checklist for experiments and evidence quality.
