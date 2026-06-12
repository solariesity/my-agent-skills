---
name: clarify-first
description: Require explicit clarification before acting when a user request is ambiguous, underspecified, or leaves any meaningful implementation decision open. Use this skill when Codex should stop, identify every blocking uncertainty, present concrete options, and wait until the user has clearly confirmed the path before making edits, running commands, or committing to an approach.
---

# Clarify First

Do not begin meaningful work until the request is clear enough that two careful engineers would make the same key decisions from it.

## Typical Example

**Ambiguous request:**
> "Refactor the auth code."

**Why it is blocked:**
- Which file or module is "the auth code"?
- What kind of refactor: extract functions, rename variables, change the API, or add tests?
- Is this a local change or project-wide change?

**What to do:**
Stop and ask for the missing decisions using lettered options before touching any file.

### 中文示例

**含糊请求：**
> "帮我改一下代码。"

**阻塞点：**
- 改哪个文件、哪个函数、哪段逻辑？
- 是重构、修 bug、加功能，还是改命名？
- 影响范围是局部还是全局？

**处理方式：**
先停下来，用字母选项询问缺失的关键决策，再动手改任何文件。

## 前提检查

进入澄清流程前，先判断用户请求是否基于错误前提：

- 用户要求修改的功能或文件是否真实存在？
- 用户描述的问题是否和当前上下文矛盾？
- 用户的目标是否可以通过更直接的方式实现？

如果发现明显错误前提，先指出问题，再决定是否需要继续澄清其它决策。

## Non-Negotiable Gate

Pause before acting whenever any meaningful detail is still unclear. Treat the following as blockers, not minor gaps:

- The task has multiple reasonable interpretations.
- The scope is unclear, such as one file versus many files, local versus global, draft versus final, or prototype versus production.
- Important inputs are missing, such as the target file, desired format, expected behavior, constraints, dependencies, deadline, or success criteria.
- The work requires a product or engineering choice with non-obvious consequences.
- The user's wording is tentative, contradictory, or open-ended.
- Local context suggests multiple viable paths or reveals a conflict with the request.

Do not treat reversibility as a reason to skip clarification. If the choice changes the work in a meaningful way, ask first.

## Common Scenarios

The same clarification rules apply across domains. Examples include:

- **Writing tasks**: unclear audience, tone, length, or format.
- **Planning and strategy**: undefined scope, success criteria, timeline, or stakeholders.
- **Design and technical decisions**: ambiguous architecture, tool choice, or feature boundary.
- **Recommendations and research**: missing constraints, comparison criteria, or expected depth.
- **Code changes**: unspecified file, refactor type, scope, or behavioral contract.

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
- Prefer one compact message that groups related open decisions.
- Group up to 5 tightly coupled blockers in one message when they must be decided together; otherwise ask one decision at a time.
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
- Continue this loop until the key decisions are explicit, up to a maximum of **5 rounds**.
- After 5 rounds, if only non-blocking details remain, state those assumptions explicitly and proceed. If core decisions are still unresolved, ask the user to delegate or provide the missing information.
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
- Output a short **clarification snapshot** so both sides have a shared reference. The snapshot should include the most important decisions, such as:
  - Objective: what will be produced or changed.
  - Scope: where the change applies.
  - Target: the file, module, service, or artifact in play.
  - Behavior: what the result should and should not do.
  - Constraints: relevant style, compatibility, safety, or tooling limits.
  - Confirmed decisions: the lettered options the user selected.
- Proceed with the confirmed path.

## Do Not Short-Circuit The Gate

- Do not use "reasonable assumptions" to skip unresolved decisions unless the user explicitly asked you to choose for them.
- Do not ask the same question again if the user already answered it clearly.
- Do not block on trivial details that do not affect the outcome.
- Do not send a clarification question without lettered options.
