# Analysis Checklist

Use this checklist to keep the analysis rigorous and consistent.

## 1. Basic identity

- What problem does the paper solve?
- Which subfield does it belong to?
- What task setting is assumed?
- What is the claimed contribution?

## 2. Problem and motivation

- Why is the problem important?
- What pain point in prior work is emphasized?
- Is the motivation practical, scientific, or benchmark-driven?
- Are the assumptions realistic?

## 3. Method understanding

- What is the full pipeline?
- What are the key modules or stages?
- What inputs and outputs does each stage use?
- Which part appears genuinely new?
- Which parts are standard engineering combinations?

## 4. Technical novelty

- Is the novelty algorithmic, architectural, training-related, systems-related, or evaluation-related?
- Is the contribution fundamental or incremental?
- Would the method still be useful if the main novelty were removed?
- Does the paper compare against the strongest relevant baseline family?

## 5. Experiment setting

- Which datasets or benchmarks are used?
- How large are they?
- Are train/validation/test splits described?
- Which baselines are selected?
- Are metrics appropriate for the task?
- Are implementation details sufficient?
- Are hyperparameters, hardware, runtime, or training budget reported?

## 6. Result analysis

- What are the main headline numbers?
- What is the absolute improvement?
- What is the relative improvement?
- **Δ vs SOTA**：What is the innovation delta relative to the strongest baseline? Is it transformative, meaningful, or marginal? On which metrics is Δ≈0?
- Are gains consistent across datasets, metrics, or settings?
- Are any results statistically fragile or suspiciously narrow?
- Are there tradeoffs in speed, memory, cost, or complexity?

## 7. Ablation and evidence quality

- Does the ablation isolate each claimed contribution?
- Are component interactions tested?
- Is there a sensitivity study?
- Are failure cases or boundary conditions shown?
- Is qualitative evidence aligned with the quantitative claims?

## 8. Limitations and validity

- What limitations does the paper admit?
- What important limitations are not discussed?
- What confounders or threats to validity remain?
- What would make the conclusion stronger?

## 9. Reproduction value

- Could a graduate student reproduce this work from the paper alone?
- What details are missing?
- Is code or data availability mentioned?
- What parts are likely to be implementation-sensitive?

## 10. Output framing

In the final answer, keep three layers distinct:
- faithful translation
- plain-language explanation
- professional evaluation

## 11. Adversarial review (博导审稿)

- If the claimed novelty were removed, is the remainder still meaningful or just standard engineering?
- Would the method hold on a different dataset distribution?
- Are the baselines the strongest available? Any missing recent or stronger baselines?
- Could a simpler approach (a trick, hyperparameter tuning, loss change) achieve similar results?
- Is the improvement worth the added complexity or cost?
- Does every claim in the paper have matching experimental evidence? Any claim-evidence gaps?
