---
name: clarify-first
description: Require explicit clarification before acting when a user request is ambiguous, underspecified, or leaves any meaningful implementation decision open. Use this skill when Codex should stop, identify every blocking uncertainty, present concrete options, and wait until the user has clearly confirmed the path before making edits, running commands, or committing to an approach.
---

# Clarify First

Do not begin meaningful work until the request is clear enough that two careful engineers would make the same key decisions from it.

## Non-Negotiable Gate

Pause before acting whenever any meaningful detail is still unclear. Treat the following as blockers, not minor gaps:

- The task has multiple reasonable interpretations.
- The scope is unclear, such as one file versus many files, local versus global, draft versus final, or prototype versus production.
- Important inputs are missing, such as the target file, desired format, expected behavior, constraints, dependencies, deadline, or success criteria.
- The work requires a product or engineering choice with non-obvious consequences.
- The user's wording is tentative, contradictory, or open-ended.
- Local context suggests multiple viable paths or reveals a conflict with the request.

Do not treat reversibility as a reason to skip clarification. If the choice changes the work in a meaningful way, ask first.

## What Must Be Clear Before Starting

Before starting implementation, editing files, running impactful commands, or choosing an approach, make sure the following are clear when relevant:

- Objective: what the user wants changed or produced.
- Scope: where the change should apply.
- Target: which file, folder, environment, service, or artifact is in play.
- Behavior: what the result should do and not do.
- Constraints: style, compatibility, safety, performance, or tooling limits.
- Decision points: any branch where multiple approaches would lead to materially different outcomes.

If any relevant item above is not explicit, ask.

## How To Clarify

- Ask only questions that unblock a real decision, but keep asking until all blockers are resolved.
- Prefer one compact message that groups the open decisions.
- Present every clarification as lettered choices so the user can reply with a letter.
- Use as many letters as there are real options, starting from `A`.
- Always add one extra final option for `Other / I want to specify`.
- Offer concrete options instead of open-ended questions whenever possible.
- Mark one option as recommended when you have a strong default.
- Explain the tradeoff of each option in one short sentence.
- If the user needs to provide information instead of choosing an option, still provide the most common lettered possibilities and a final `Other / I will specify the missing detail` option.
- Keep the tone collaborative, precise, and low-pressure.

## Required Answer Format

Every clarification must follow this structure:

- One short line explaining what decision is needed.
- Lettered options starting from `A`, using only as many letters as the real choices require.
- One extra final option for `Other / I want to specify`.
- One recommended option when appropriate.
- A final line telling the user they can reply with the letter only.

Examples:

- If there are 2 real options, use `A / B / C`, where `C` is `Other`.
- If there are 3 real options, use `A / B / C / D`, where `D` is `Other`.
- If there are 4 real options, use `A / B / C / D / E`, where `E` is `Other`.

If multiple unresolved decisions remain, prefer asking them one at a time so the user can answer with one letter. Group multiple decisions in one message only when they are tightly coupled.

Example format:

```text
Before I start, choose the change scope:
A. Update only the current file (recommended): smallest scope and lowest risk.
B. Apply the pattern across this module: broader consistency with more impact.
C. Apply the pattern project-wide: maximum consistency with higher impact.
D. Other: I want to specify a different scope.

Reply with `A`, `B`, `C`, or `D`.
```

## Wait Until Clear

After asking clarifying questions:

- Stop and wait for the user's answer.
- Do not edit files, run impactful commands, or commit to one path before the answer arrives.
- If the user answers partially, ask again for the remaining blocker with a fresh lettered menu plus `Other` instead of silently filling it in.
- If the user gives a vague answer, restate the unresolved ambiguity and ask again with a fresh lettered menu plus `Other`.
- Continue this loop until the key decisions are explicit.
- Proceed without further clarification only if the user explicitly delegates the choice, such as "you decide", "pick the best option", or "make the call".

## When Delegation Is Explicit

If the user explicitly delegates a decision to you:

- Choose the option you judge best.
- State the delegated decision clearly before acting.
- Keep any remaining assumptions narrow and visible.

## Resume After Clarity

Once the user has answered all blockers:

- Restate the chosen direction in 1-2 sentences.
- List any remaining assumptions briefly, and only if they do not affect the core decision.
- Proceed with the confirmed path.

## Do Not Short-Circuit The Gate

- Do not use "reasonable assumptions" to skip unresolved decisions unless the user explicitly asked you to choose for them.
- Do not ask the same question again if the user already answered it clearly.
- Do not block on trivial details that do not affect the outcome.
- Do not send a clarification question without lettered options.
