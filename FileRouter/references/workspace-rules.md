# Workspace Rules

Use this file when you need the underlying storage rules that FileRouter follows.
FileRouter applies these rules under a local `files/` directory in the current working directory.

## Core Goals

- make new files easy to place quickly
- keep related project material together
- preserve long-term retrievability
- reduce clutter from temporary downloads and duplicated copies

## Top-Level Domains

Use stable top-level directories under `files/` instead of inventing ad hoc roots:

```text
files/
  Archive/
  Courses/
  Dev/
  Docs/
  Downloads/
  Installers/
  Lab/
  Media/
  Research/
  Systems/
```

## High-Level Principles

- classify top-level storage by purpose, not by year or file type alone
- keep the top-level layout stable over time
- separate source, work, and output for serious projects
- keep `Downloads` as a staging area rather than a final home
- add a `README.md` to durable project directories

## Course Storage

Route course files by `term -> course -> role`.

Recommended course subfolders:

```text
Slides/
Notes/
Assignments/
Labs/
Exam/
```

## Lab Storage

Use these long-lived lab areas:

```text
Admin/
GroupMeeting/
Reimbursement/
Shared/
Tasks/
Templates/
```

## Research Storage

Top-level research areas:

```text
Papers/
Notes/
Projects/
Data/
Thesis/
```

Formal research projects should distinguish:

- literature
- raw data
- processed data
- code
- experiments
- writing
- output
- archive

## Dev Storage

Use these long-lived development areas:

```text
Learning/
Sandbox/
Scripts/
Tools/
```

General development projects may live under `Dev/Tools/<project>/` when they need a full project skeleton.

## Docs Storage

Preferred document categories:

```text
Certificates/
Forms/
Journal/
Official/
Personal/
```

## Media Storage

Preferred media categories:

```text
Assets/
Audio/
Fonts/
Images/
Recordings/
Screenshots/
Templates/
Videos/
```

## Installers Storage

Preferred installer categories:

```text
CommonApps/
DevTools/
Drivers/
Office/
OS/
```

## Systems Storage

Preferred systems categories:

```text
AppData_Local/
Portable/
Programs/
VM/
```

## Naming Rules

- use `YYYY-MM-DD` for dates
- prefer descriptive names over vague names like `test` or `misc`
- avoid Windows-reserved filename characters
- normalize whitespace and punctuation into stable separators
- keep final paths reasonably short for Windows compatibility

## Version Rules

- use explicit file versions like `v01`, `v02`, or `final` for non-Git artifacts
- rely on Git rather than filename versions for code repositories when possible
- move obsolete versions into `Archive/` or `99_Archive/`

## Lifecycle Rules

- delete low-value temporary files when safe
- archive inactive but still useful files
- preserve irreplaceable source material
- never overwrite raw data as the only surviving copy
