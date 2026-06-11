# Memory Taxonomy

Use this file when you need to decide what kind of memory a conversation detail represents.

## Canonical Types

Use this decision order before choosing a type:

1. If the content contains a password, secret, API key, token, recovery code, or other credential, do not persist it in MemRouter.
2. If the content is trivial chat or one-off wording with no future value, do not persist it.
3. Decide the primary scope:
   - user identity -> `profile`
   - user-to-agent interaction preference -> `preferences`
   - project or workspace fact / constraint / environment detail -> `project-facts`
   - project or workspace rule / choice / policy -> `project-decisions`
   - actionable next step -> `task`
   - recap of a session -> `session-summary`
   - useful but ambiguous detail -> `ephemeral`

### `profile`

Store stable facts about a person or durable identity context.

Examples:

- role or background
- long-term goals
- durable constraints tied to the user

Use this for things that stay true about the user across projects.

Do use this for:

- personal background
- stable identity labels
- long-term goals
- durable user-level constraints such as timezone
- personal interests or favorites when they matter as user context

Do not use this for:

- style preferences about how the agent should answer
- project paths, repositories, or workspace layout
- installed tools or environment details that belong to a project or workspace
- passwords, secrets, tokens, or private credentials

Distinguish it from nearby types:

- "Who the user is" -> `profile`
- "How the user wants the agent to respond" -> `preferences`
- "What is true about the current project or workspace" -> `project-facts`

### `preferences`

Store repeated preferences about interaction style, output format, tools, or language.

Examples:

- prefers Chinese answers
- prefers concise replies
- prefers bullet points
- prefers a specific workflow or tool

Use this only for user-to-agent interaction preferences.

Do use this for:

- response language
- response length
- formatting style
- tool-use preferences
- collaboration or workflow preferences for the agent

Do not use this for:

- personal hobbies, fandoms, or entertainment tastes
- project rules adopted by the team or workspace
- project constraints, paths, or storage locations

Distinguish it from nearby types:

- "How should the agent work with the user?" -> `preferences`
- "What does the user personally like?" -> usually `profile`
- "What rules has this project adopted?" -> usually `project-decisions`

### `project-facts`

Store project-specific facts and constraints that should remain true unless explicitly changed.

Examples:

- architecture constraints
- storage rules
- required integrations
- hard boundaries or assumptions

This includes workspace and environment facts when they are specific to the current project.

Do use this for:

- project paths and repository locations
- workspace boundaries
- directory layout
- storage backends
- installed integrations or dependencies that are part of the project environment
- reminder or automation data locations

Do not use this for:

- explicit choices or policies that were deliberately adopted
- personal user identity facts
- interaction style preferences

Distinguish it from nearby types:

- "What is true right now about the project or workspace?" -> `project-facts`
- "What did we decide to do?" -> `project-decisions`

### `project-decisions`

Store explicit decisions, pivots, and chosen approaches.

Examples:

- choose file-based routing over a single log
- adopt a naming convention for project memory

Use this when the detail is a decision, not just a fact.

Do use this for:

- architecture choices
- naming conventions
- policies for how the agent should behave in this workspace
- reminder or automation mechanisms that were intentionally adopted
- rules such as "store mechanism in MemRouter, keep data in local files"

Do not use this for:

- static environment facts with no decision aspect
- user identity or preference data

Distinguish it from nearby types:

- "This is how the workspace is configured" -> `project-facts`
- "We decided this is how the workspace should work" -> `project-decisions`

### `task`

Store actionable work items, progress, or next steps.

Examples:

- add a CLI entrypoint
- verify recall against direct-note matches

### `session-summary`

Store a recap of a conversation or working session that may be useful later.

Examples:

- what was decided in a meeting
- what changed during a debugging session
- what remains unresolved

### `ephemeral`

Store low-confidence or short-lived context that is still worth keeping temporarily.

Examples:

- tentative context
- unclear user/project scope
- notes that may expire soon

Prefer this over inventing a precise category when confidence is low.

## What Not to Persist

- trivial pleasantries
- one-off wording with no future value
- raw transcript fragments with no durable meaning
- repetitive content already stored clearly elsewhere
- passwords
- API keys
- access tokens
- recovery codes
- secrets or private credentials

## Migration Boundaries

When importing from a legacy memory system, migrate durable memory rather than copying every old file verbatim.

Good candidates for migration:

- stable user facts
- user-to-agent preferences
- project facts and constraints
- project decisions and adopted rules
- useful session recaps

Usually do not migrate as raw memory entries:

- todo lists
- reminder files
- diaries
- raw transcripts
- other chronological operational files

Keep those external, or summarize only their durable conclusions before routing them into MemRouter.
