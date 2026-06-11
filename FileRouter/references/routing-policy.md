# Routing Policy

Use this file when you need the exact route model that FileRouter applies.
All routed storage lives under a `files/` directory inside the agent's current working directory unless another workspace root is explicitly supplied.

## Route Inputs

FileRouter resolves storage from a combination of:

- `domain`
- `role`
- `origin`
- `project`
- `project_type`
- `course`
- `term`
- `date`
- `filename`

## Safety Defaults

- default organize mode is `copy`
- default collision mode is `rename`
- use `move` only when the user explicitly wants to relocate the original file
- use `files/Downloads/` only as a low-confidence staging destination

## Domain Routes

### Courses

Requires or benefits from `term` and `course`.

- `slides` -> `files/Courses/<term>/<course>/Slides/`
- `notes` -> `files/Courses/<term>/<course>/Notes/`
- `assignments` -> `files/Courses/<term>/<course>/Assignments/`
- `labs` -> `files/Courses/<term>/<course>/Labs/`
- `exam` -> `files/Courses/<term>/<course>/Exam/`

### Lab

- `admin` -> `files/Lab/Admin/`
- `group-meeting` -> `files/Lab/GroupMeeting/`
- `reimbursement` -> `files/Lab/Reimbursement/`
- `shared` -> `files/Lab/Shared/`
- `task` -> `files/Lab/Tasks/`
- `template` -> `files/Lab/Templates/`

### Research Without A Project

- `literature` -> `files/Research/Papers/`
- `note` -> `files/Research/Notes/`
- `data` -> `files/Research/Data/`
- `thesis` -> `files/Research/Thesis/`

### Research Project Template

Use when `project_type=research` or when the file clearly belongs to a formal research project.

- `literature` -> `files/Research/Projects/<project>/01_Literature/`
- `raw-data` -> `files/Research/Projects/<project>/02_Data/raw/`
- `processed-data` -> `files/Research/Projects/<project>/02_Data/processed/`
- `code` -> `files/Research/Projects/<project>/03_Code/`
- `experiments` -> `files/Research/Projects/<project>/04_Experiments/`
- `writing` -> `files/Research/Projects/<project>/05_Writing/`
- `output` -> `files/Research/Projects/<project>/06_Output/`
- `archive` -> `files/Research/Projects/<project>/99_Archive/`

### Dev Without A Project

- `learning` -> `files/Dev/Learning/`
- `sandbox` -> `files/Dev/Sandbox/`
- `scripts` -> `files/Dev/Scripts/`
- `tools` -> `files/Dev/Tools/`

### General Project Template

FileRouter places general projects under `files/Dev/Tools/<project>/` by default.

- `inbox` -> `files/Dev/Tools/<project>/00_Inbox/`
- `admin` -> `files/Dev/Tools/<project>/01_Admin/`
- `source` -> `files/Dev/Tools/<project>/02_Source/`
- `work` -> `files/Dev/Tools/<project>/03_Work/`
- `output` -> `files/Dev/Tools/<project>/04_Output/`
- `archive` -> `files/Dev/Tools/<project>/99_Archive/`

### Docs

- `certificate` -> `files/Docs/Certificates/`
- `form` -> `files/Docs/Forms/`
- `journal` -> `files/Docs/Journal/<year>/`
- `official` -> `files/Docs/Official/`
- `personal` -> `files/Docs/Personal/`

### Media

- `asset` -> `files/Media/Assets/`
- `audio` -> `files/Media/Audio/`
- `font` -> `files/Media/Fonts/`
- `image` -> `files/Media/Images/`
- `recording` -> `files/Media/Recordings/`
- `screenshot` -> `files/Media/Screenshots/`
- `template` -> `files/Media/Templates/`
- `video` -> `files/Media/Videos/`

### Installers

- `common-app` -> `files/Installers/CommonApps/`
- `devtool` -> `files/Installers/DevTools/`
- `driver` -> `files/Installers/Drivers/`
- `office` -> `files/Installers/Office/`
- `os` -> `files/Installers/OS/`

### Systems

- `appdata-local` -> `files/Systems/AppData_Local/`
- `portable` -> `files/Systems/Portable/`
- `program` -> `files/Systems/Programs/`
- `vm` -> `files/Systems/VM/`

### Archive

Archive routes include the year:

- `archive` -> `files/Archive/<year>/`

### Downloads

Low-confidence staging fallback:

- `incoming` -> `files/Downloads/`

## Role Heuristics

When explicit route metadata is missing, FileRouter uses practical heuristics:

- screenshots and screen recordings prefer `media`
- PDFs with research or paper cues prefer research literature
- code files in a project prefer project code or source
- generated figures, reports, or exports in a project prefer project output
- incoming ambiguous files in a general project prefer project inbox
- raw datasets prefer `raw-data`
- cleaned tables or transformed datasets prefer `processed-data`

## Naming Rules

FileRouter sanitizes unsafe file names:

- remove Windows-reserved characters
- collapse repeated separators
- preserve the extension
- optionally prefix the route date
- optionally append a version tag before the extension

When a collision occurs and `rename` mode is active, FileRouter appends `_copyNN`.

## Find Behavior

Use `find` with the same scope that was used for storage.

Search order:

1. the most specific candidate directory for the supplied scope
2. sibling directories within the same domain if the scope is still narrow
3. broader fallback only when the specific scope does not exist

`find` matches against:

- file name
- relative path

It does not do semantic search or file-content indexing.
