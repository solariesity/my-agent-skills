#!/usr/bin/env python3
"""Core routing helpers for the file-router skill."""

from __future__ import annotations

import datetime as dt
import hashlib
import json
import re
import shutil
from pathlib import Path, PurePosixPath

DOMAIN_ALIASES = {
    "course": "courses",
    "courses": "courses",
    "class": "courses",
    "lab": "lab",
    "research": "research",
    "paper": "research",
    "dev": "dev",
    "development": "dev",
    "docs": "docs",
    "documents": "docs",
    "media": "media",
    "installers": "installers",
    "systems": "systems",
    "archive": "archive",
    "downloads": "downloads",
}

ROLE_ALIASES = {
    "slide": "slides",
    "slides": "slides",
    "note": "notes",
    "notes": "notes",
    "assignment": "assignments",
    "assignments": "assignments",
    "hw": "assignments",
    "homework": "assignments",
    "lab": "labs",
    "labs": "labs",
    "exam": "exam",
    "meeting": "group-meeting",
    "minutes": "group-meeting",
    "group-meeting": "group-meeting",
    "reimburse": "reimbursement",
    "reimbursement": "reimbursement",
    "task": "task",
    "template": "template",
    "paper": "literature",
    "papers": "literature",
    "literature": "literature",
    "reference": "literature",
    "references": "literature",
    "note-research": "note",
    "raw": "raw-data",
    "raw-data": "raw-data",
    "processed": "processed-data",
    "processed-data": "processed-data",
    "code": "code",
    "experiment": "experiments",
    "experiments": "experiments",
    "writing": "writing",
    "draft": "writing",
    "output": "output",
    "result": "output",
    "archive": "archive",
    "script": "scripts",
    "scripts": "scripts",
    "tool": "tools",
    "tools": "tools",
    "learning": "learning",
    "sandbox": "sandbox",
    "inbox": "inbox",
    "source": "source",
    "work": "work",
    "certificate": "certificate",
    "form": "form",
    "journal": "journal",
    "official": "official",
    "personal": "personal",
    "asset": "asset",
    "audio": "audio",
    "font": "font",
    "image": "image",
    "recording": "recording",
    "screenshot": "screenshot",
    "video": "video",
    "common-app": "common-app",
    "devtool": "devtool",
    "driver": "driver",
    "office": "office",
    "os": "os",
    "portable": "portable",
    "program": "program",
    "vm": "vm",
    "incoming": "incoming",
    "data": "data",
    "thesis": "thesis",
    "admin": "admin",
    "shared": "shared",
    "appdata-local": "appdata-local",
}

CODE_EXTENSIONS = {".py", ".ipynb", ".js", ".ts", ".tsx", ".jsx", ".java", ".c", ".cc", ".cpp", ".h", ".hpp", ".rs", ".go", ".sh", ".ps1", ".bat", ".m", ".r"}
DATA_EXTENSIONS = {".csv", ".tsv", ".json", ".jsonl", ".parquet", ".xlsx", ".xls", ".npy", ".npz", ".pt", ".pth", ".ckpt", ".mat", ".pkl"}
DOC_EXTENSIONS = {".md", ".txt", ".doc", ".docx", ".tex", ".pdf", ".ppt", ".pptx", ".odt", ".rtf"}
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".bmp", ".gif", ".webp", ".svg", ".tif", ".tiff"}
VIDEO_EXTENSIONS = {".mp4", ".mov", ".avi", ".mkv", ".wmv", ".webm"}
AUDIO_EXTENSIONS = {".mp3", ".wav", ".m4a", ".flac", ".aac", ".ogg"}
FONT_EXTENSIONS = {".ttf", ".otf", ".woff", ".woff2"}
ARCHIVE_EXTENSIONS = {".zip", ".7z", ".rar", ".tar", ".gz", ".bz2", ".xz"}
INSTALLER_EXTENSIONS = {".exe", ".msi", ".iso"} | ARCHIVE_EXTENSIONS
VM_EXTENSIONS = {".vhd", ".vhdx", ".vmdk", ".ova", ".ovf", ".qcow2", ".vbox"}

COURSE_HINTS = ("course", "class", "lecture", "lesson", "assignment", "homework", "exam", "slides", "课程", "作业", "考试", "课件")
LAB_HINTS = ("lab", "group meeting", "reimbursement", "invoice", "fapiao", "实验室", "组会", "报销", "发票")
RESEARCH_HINTS = ("research", "paper", "literature", "dataset", "experiment", "model", "thesis", "论文", "文献", "实验", "数据集", "科研")
DEV_HINTS = ("script", "tool", "repo", "repository", "prototype", "sandbox", "开发", "脚本", "工具", "原型")
DOCS_HINTS = ("resume", "cv", "certificate", "official", "contract", "journal", "简历", "证书", "合同", "日志")
MEDIA_HINTS = ("screenshot", "recording", "image", "audio", "video", "素材", "截图", "录屏", "视频", "音频")
INSTALLER_HINTS = ("installer", "setup", "driver", "portable", "devtools", "安装包", "驱动", "镜像")
SYSTEM_HINTS = ("vm", "virtual machine", "cache", "appdata", "portable", "虚拟机", "缓存", "程序环境")
RESEARCH_WRITING_HINTS = ("paper", "manuscript", "report", "proposal", "thesis", "slides", "poster", "论文", "文稿", "汇报", "海报")
EXPERIMENT_HINTS = ("experiment", "result", "metric", "log", "ablation", "benchmark", "实验", "结果", "指标", "日志")
RAW_HINTS = ("raw", "original", "source data", "原始", "未处理")
PROCESSED_HINTS = ("processed", "clean", "cleaned", "derived", "整理后", "清洗", "处理后")
SCREENSHOT_HINTS = ("screenshot", "screen shot", "截图")
RECORDING_HINTS = ("recording", "录屏", "录音")
JOURNAL_HINTS = ("journal", "diary", "日志", "日记")
OFFICIAL_HINTS = ("official", "contract", "证明", "协议", "合同")
PERSONAL_HINTS = ("resume", "cv", "personal", "profile", "简历", "个人")
FORM_HINTS = ("form", "template", "表格", "申请表")
CERTIFICATE_HINTS = ("certificate", "award", "证书", "奖状")
DRIVER_HINTS = ("driver", "驱动")
OFFICE_HINTS = ("office", "word", "excel", "ppt")
DEVTOOL_HINTS = ("git", "vscode", "pycharm", "docker", "cuda", "node", "python")
OS_HINTS = ("windows", "ubuntu", "linux", "macos", "iso", "系统镜像")

GENERAL_PROJECT_DIRS = {
    "inbox": "00_Inbox",
    "admin": "01_Admin",
    "source": "02_Source",
    "work": "03_Work",
    "output": "04_Output",
    "archive": "99_Archive",
}

RESEARCH_PROJECT_DIRS = {
    "literature": "01_Literature",
    "raw-data": "02_Data/raw",
    "processed-data": "02_Data/processed",
    "code": "03_Code",
    "experiments": "04_Experiments",
    "writing": "05_Writing",
    "output": "06_Output",
    "archive": "99_Archive",
}

TOP_LEVEL_WORKSPACE_DIRS = [
    "Archive",
    "Courses",
    "Dev",
    "Docs",
    "Downloads",
    "Installers",
    "Lab",
    "Media",
    "Research",
    "Systems",
]

FILES_ROOT_NAME = "files"
LOW_CONFIDENCE_THRESHOLD = 0.7
DEFAULT_REMINDER_RELATIVE_PATH = PurePosixPath("Docs") / "Personal" / "提醒.md"
DEFAULT_REMINDER_SECTION = "条目"
DEFAULT_REMINDER_TITLE = "提醒"

WINDOWS_RESERVED_RE = re.compile(r'[\\/:*?"<>|]+')
MULTI_DASH_RE = re.compile(r"-{2,}")
DATE_PREFIX_RE = re.compile(r"^\d{4}-\d{2}-\d{2}[-_]")
NON_SAFE_COMPONENT_RE = re.compile(r"[^\w\-.\u0080-\uffff]+", re.UNICODE)

# Stable UTF-8 reminder metadata used by chat-text persistence.
DEFAULT_REMINDER_RELATIVE_PATH = PurePosixPath("Docs") / "Personal" / "\u63d0\u9192.md"
DEFAULT_REMINDER_SECTION = "\u6761\u76ee"
DEFAULT_REMINDER_TITLE = "\u63d0\u9192"

IMPORTANT_CHAT_HINTS = (
    "很重要",
    "非常重要",
    "重要",
    "记一下",
    "记住",
    "记到文件里",
    "存文件",
    "存到文件",
    "存到文件里",
    "写到文件里",
    "写进文件",
    "保存到文件",
    "提醒我",
    "记在提醒里",
    "save this",
    "store this",
    "save to file",
    "store in file",
    "remember this",
    "important",
)


def normalize_text(value: str | None, default: str | None = None) -> str | None:
    if value is None:
        return default
    cleaned = value.replace("\r\n", "\n").replace("\r", "\n").strip()
    cleaned = re.sub(r"\s+", " ", cleaned)
    return cleaned or default


IMPORTANT_CHAT_HINTS = (
    "\u5f88\u91cd\u8981",
    "\u975e\u5e38\u91cd\u8981",
    "\u91cd\u8981",
    "\u8bb0\u4e00\u4e0b",
    "\u8bb0\u4f4f",
    "\u8bb0\u5230\u6587\u4ef6\u91cc",
    "\u5b58\u6587\u4ef6",
    "\u5b58\u5230\u6587\u4ef6",
    "\u5b58\u5230\u6587\u4ef6\u91cc",
    "\u5199\u5230\u6587\u4ef6\u91cc",
    "\u5199\u8fdb\u6587\u4ef6",
    "\u4fdd\u5b58\u5230\u6587\u4ef6",
    "\u63d0\u9192\u6211",
    "\u8bb0\u5728\u63d0\u9192\u91cc",
    "save this",
    "store this",
    "save to file",
    "store in file",
    "remember this",
    "important",
)


def normalize_workspace_root(workspace_root: str | None = None) -> Path:
    return Path(workspace_root or ".").resolve()


def files_root_path(workspace_root: str | None = None) -> Path:
    return normalize_workspace_root(workspace_root) / FILES_ROOT_NAME


def contains_any(text: str, phrases: tuple[str, ...]) -> bool:
    return any(phrase in text for phrase in phrases)


def canonical_domain(domain: str | None) -> str | None:
    if domain is None:
        return None
    lowered = normalize_text(domain, "") or ""
    lowered = lowered.casefold()
    return DOMAIN_ALIASES.get(lowered, lowered or None)


def canonical_role(role: str | None) -> str | None:
    if role is None:
        return None
    lowered = normalize_text(role, "") or ""
    lowered = lowered.casefold()
    return ROLE_ALIASES.get(lowered, lowered or None)


def slugify_component(value: str | None, default: str) -> str:
    if value is None:
        return default
    lowered = normalize_text(value, "") or ""
    lowered = lowered.casefold()
    lowered = lowered.replace("&", " and ")
    lowered = re.sub(r"[\s/\\]+", "-", lowered)
    lowered = WINDOWS_RESERVED_RE.sub("-", lowered)
    lowered = NON_SAFE_COMPONENT_RE.sub("-", lowered)
    lowered = MULTI_DASH_RE.sub("-", lowered).strip("-._")
    return lowered or default


def sanitize_path_component(value: str | None, default: str) -> str:
    if value is None:
        return default
    cleaned = normalize_text(value, "") or ""
    cleaned = cleaned.replace("&", " and ")
    cleaned = re.sub(r"[\s/\\]+", "-", cleaned)
    cleaned = WINDOWS_RESERVED_RE.sub("-", cleaned)
    cleaned = NON_SAFE_COMPONENT_RE.sub("-", cleaned)
    cleaned = MULTI_DASH_RE.sub("-", cleaned).strip("-._")
    return cleaned or default


def normalize_term(term: str | None, when: dt.date) -> str:
    if not term:
        return f"{when.year}-General"
    cleaned = normalize_text(term, "") or ""
    match = re.match(r"^(?P<year>\d{4})[-_\s]?(?P<season>[A-Za-z]+)$", cleaned)
    if match:
        year = match.group("year")
        season = match.group("season").capitalize()
        return f"{year}-{season}"
    return cleaned.replace("_", "-").replace(" ", "-")


def sanitize_filename(name: str, fallback_stem: str = "unnamed") -> str:
    basename = Path(name).name.strip()
    suffix = Path(basename).suffix
    stem = basename[: -len(suffix)] if suffix else basename
    stem = WINDOWS_RESERVED_RE.sub("-", stem)
    stem = re.sub(r"\s+", "-", stem)
    stem = NON_SAFE_COMPONENT_RE.sub("-", stem)
    stem = MULTI_DASH_RE.sub("-", stem).strip("-._")
    if not stem:
        stem = fallback_stem
    suffix = WINDOWS_RESERVED_RE.sub("", suffix)
    return f"{stem}{suffix.lower()}"


def build_target_filename(
    source_name: str,
    target_name: str | None = None,
    date: str | None = None,
    date_prefix: bool = False,
    version: str | None = None,
) -> str:
    source_path = Path(source_name)
    if target_name:
        desired = Path(target_name)
        suffix = desired.suffix or source_path.suffix
        desired_name = desired.stem + suffix
    else:
        desired_name = source_path.name

    safe_name = sanitize_filename(desired_name)
    stem = Path(safe_name).stem
    suffix = Path(safe_name).suffix

    if date_prefix and date and not DATE_PREFIX_RE.match(stem):
        stem = f"{date}_{stem}"

    if version:
        normalized_version = normalize_text(version, "") or ""
        normalized_version = normalized_version.replace(" ", "")
        if normalized_version and not stem.endswith(f"_{normalized_version}"):
            stem = f"{stem}_{normalized_version}"

    return f"{stem}{suffix}"


def detect_extension(source_name: str | None) -> str:
    if not source_name:
        return ""
    return Path(source_name).suffix.casefold()


def current_timestamp() -> str:
    return dt.datetime.now().astimezone().replace(microsecond=0).isoformat()


def ensure_note_file(note_path: Path, title: str, section: str) -> None:
    note_path.parent.mkdir(parents=True, exist_ok=True)
    if note_path.exists():
        return
    note_path.write_text(f"# {title}\n\n## {section}\n", encoding="utf-8")


def ensure_markdown_section(lines: list[str], section: str) -> tuple[list[str], int]:
    header = f"## {section}"
    for idx, line in enumerate(lines):
        if line.strip() == header:
            return lines, idx
    if lines and lines[-1].strip():
        lines.append("")
    lines.append(header)
    lines.append("")
    return lines, len(lines) - 2


def find_markdown_section_end(lines: list[str], section_idx: int) -> int:
    for idx in range(section_idx + 1, len(lines)):
        if lines[idx].startswith("## ") and idx != section_idx:
            return idx
    return len(lines)


def normalize_note_text(text: str) -> list[str]:
    lines = text.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    cleaned = [line.rstrip() for line in lines]
    while cleaned and not cleaned[0].strip():
        cleaned.pop(0)
    while cleaned and not cleaned[-1].strip():
        cleaned.pop()
    if not cleaned:
        raise ValueError("text cannot be empty.")
    return cleaned


def sanitize_relative_note_path(target_file: str) -> PurePosixPath:
    normalized = target_file.replace("\\", "/").strip()
    if not normalized:
        raise ValueError("target_file cannot be empty.")
    parts = [part for part in PurePosixPath(normalized).parts if part not in {"", ".", ".."}]
    if not parts:
        raise ValueError("target_file cannot be empty.")
    if parts[0] == FILES_ROOT_NAME:
        parts = parts[1:]
    if len(parts) == 1:
        filename = parts[0]
        if "." not in filename:
            filename = f"{filename}.md"
        return DEFAULT_REMINDER_RELATIVE_PATH.parent / sanitize_filename(filename)

    safe_dirs = [sanitize_path_component(part, "General") for part in parts[:-1]]
    filename = parts[-1]
    if "." not in filename:
        filename = f"{filename}.md"
    safe_filename = sanitize_filename(filename)
    return PurePosixPath(*safe_dirs) / safe_filename


def resolve_chat_note_path(workspace_root: str, target_file: str | None = None) -> tuple[Path, str]:
    files_root = files_root_path(workspace_root)
    if target_file:
        relative = sanitize_relative_note_path(target_file)
    else:
        relative = DEFAULT_REMINDER_RELATIVE_PATH
    note_path = files_root / Path(relative)
    title = Path(relative).stem or DEFAULT_REMINDER_TITLE
    return note_path, title


def should_store_chat_text(text: str, force: bool = False) -> dict[str, object]:
    normalized = normalize_text(text, "") or ""
    lowered = normalized.casefold()
    if force:
        return {
            "should_store": True,
            "confidence": 1.0,
            "reason": "Forced persistence requested.",
        }
    if contains_any(lowered, IMPORTANT_CHAT_HINTS):
        return {
            "should_store": True,
            "confidence": 0.95,
            "reason": "Explicit importance or save-to-file cue detected.",
        }
    return {
        "should_store": False,
        "confidence": 0.2,
        "reason": "No explicit persistence cue detected in chat text.",
    }


def format_chat_entry(
    text: str,
    created_at: str,
    source: str = "chat",
    project: str | None = None,
) -> str:
    header = f"- {created_at} | source: {source}"
    if project:
        header += f" | project: {slugify_component(project, 'general')}"
    lines = [header]
    for line in normalize_note_text(text):
        lines.append(f"  {line}" if line else "  ")
    return "\n".join(lines)


def append_markdown_entry(note_path: Path, section: str, entry: str, title: str) -> dict[str, object]:
    ensure_note_file(note_path, title=title, section=section)
    original = note_path.read_text(encoding="utf-8")
    lines = original.splitlines()
    lines, section_idx = ensure_markdown_section(lines, section)
    insert_at = find_markdown_section_end(lines, section_idx)
    block = entry.splitlines()
    if insert_at > 0 and lines[insert_at - 1].strip():
        lines.insert(insert_at, "")
        insert_at += 1
    for offset, line in enumerate(block):
        lines.insert(insert_at + offset, line)
    lines.insert(insert_at + len(block), "")
    content = "\n".join(lines).rstrip() + "\n"
    note_path.write_text(content, encoding="utf-8")
    return {
        "path": str(note_path),
        "changed": True,
    }


def store_chat_text(
    workspace_root: str,
    text: str,
    target_file: str | None = None,
    project: str | None = None,
    source: str = "chat",
    section: str | None = None,
    created_at: str | None = None,
    force: bool = False,
) -> dict[str, object]:
    decision = should_store_chat_text(text=text, force=force)
    note_path, title = resolve_chat_note_path(workspace_root=workspace_root, target_file=target_file)
    workspace_root_path = normalize_workspace_root(workspace_root)
    relative_path = note_path.relative_to(workspace_root_path).as_posix()

    payload: dict[str, object] = {
        "command": "remember-text",
        "workspace_root": str(workspace_root_path),
        "path": str(note_path),
        "relative_path": relative_path,
        "target_file": target_file,
        "project": project,
        "source": slugify_component(source, "chat"),
        "section": normalize_text(section, DEFAULT_REMINDER_SECTION) or DEFAULT_REMINDER_SECTION,
        "should_store": bool(decision["should_store"]),
        "stored": False,
        "decision": decision,
        "reason": decision["reason"],
    }

    if not decision["should_store"]:
        return payload

    existed_before = note_path.exists()
    timestamp = created_at or current_timestamp()
    entry = format_chat_entry(
        text=text,
        created_at=timestamp,
        source=slugify_component(source, "chat"),
        project=project,
    )
    result = append_markdown_entry(
        note_path=note_path,
        section=payload["section"],
        entry=entry,
        title=title,
    )
    payload.update(
        {
            "stored": True,
            "created_at": timestamp,
            "created_file": not existed_before,
            "entry": entry,
            "changed": bool(result["changed"]),
        }
    )
    return payload


def decide_route(
    source: str | None = None,
    context: str | None = None,
    origin: str = "incoming",
    domain: str | None = None,
    role: str | None = None,
    project: str | None = None,
    project_type: str | None = None,
    course: str | None = None,
    term: str | None = None,
) -> dict[str, object]:
    source_name = Path(source).name if source else ""
    extension = detect_extension(source_name)
    lowered_context = (normalize_text(context, "") or "").casefold()
    lowered_name = source_name.casefold()
    combined = f"{lowered_name} {lowered_context}".strip()

    resolved_domain = canonical_domain(domain)
    resolved_role = canonical_role(role)
    resolved_project_type = normalize_text(project_type)
    confidence = 0.99 if resolved_domain and resolved_role else 0.0
    reason = "Explicit domain and role provided." if resolved_domain and resolved_role else None

    if not resolved_domain:
        if course or term or contains_any(combined, COURSE_HINTS):
            resolved_domain = "courses"
            confidence = 0.86
            reason = "Course-related keywords or course metadata detected."
        elif contains_any(combined, LAB_HINTS):
            resolved_domain = "lab"
            confidence = 0.84
            reason = "Lab-related keywords detected."
        elif contains_any(combined, DOCS_HINTS):
            resolved_domain = "docs"
            confidence = 0.82
            reason = "Personal-document keywords detected."
        elif extension in IMAGE_EXTENSIONS | VIDEO_EXTENSIONS | AUDIO_EXTENSIONS | FONT_EXTENSIONS or contains_any(combined, MEDIA_HINTS):
            resolved_domain = "media"
            confidence = 0.78
            reason = "Media extension or media keywords detected."
        elif extension in INSTALLER_EXTENSIONS or contains_any(combined, INSTALLER_HINTS):
            resolved_domain = "installers"
            confidence = 0.76
            reason = "Installer or package signal detected."
        elif extension in VM_EXTENSIONS or contains_any(combined, SYSTEM_HINTS):
            resolved_domain = "systems"
            confidence = 0.75
            reason = "System-environment or VM signal detected."
        elif resolved_project_type == "research" or contains_any(combined, RESEARCH_HINTS):
            resolved_domain = "research"
            confidence = 0.8
            reason = "Research keywords or research project type detected."
        elif extension in CODE_EXTENSIONS or project or contains_any(combined, DEV_HINTS):
            resolved_domain = "dev"
            confidence = 0.72 if project else 0.68
            reason = "Project or development signal detected."
        else:
            resolved_domain = "downloads"
            confidence = 0.35
            reason = "Route is ambiguous, so stage in Downloads first."

    if not resolved_project_type and project:
        resolved_project_type = "research" if resolved_domain == "research" else "general"

    if not resolved_role:
        if resolved_domain == "courses":
            if contains_any(combined, ("assignment", "homework", "作业", "hw")):
                resolved_role = "assignments"
                reason = "Course assignment language detected."
                confidence = max(confidence, 0.9)
            elif contains_any(combined, ("lab", "实验")):
                resolved_role = "labs"
                reason = "Course lab language detected."
                confidence = max(confidence, 0.86)
            elif contains_any(combined, ("exam", "midterm", "final exam", "考试")):
                resolved_role = "exam"
                reason = "Exam-related language detected."
                confidence = max(confidence, 0.88)
            elif extension in {".ppt", ".pptx"} or contains_any(combined, ("slide", "lecture", "slides", "课件")):
                resolved_role = "slides"
                reason = "Course slide signal detected."
                confidence = max(confidence, 0.88)
            else:
                resolved_role = "notes"
                reason = "Course material defaults to notes."
                confidence = max(confidence, 0.7)

        elif resolved_domain == "lab":
            if contains_any(combined, ("reimbursement", "invoice", "fapiao", "报销", "发票")):
                resolved_role = "reimbursement"
                reason = "Reimbursement signal detected."
                confidence = max(confidence, 0.9)
            elif contains_any(combined, ("meeting", "minutes", "group meeting", "组会")):
                resolved_role = "group-meeting"
                reason = "Meeting signal detected."
                confidence = max(confidence, 0.88)
            elif contains_any(combined, ("template", "模板")):
                resolved_role = "template"
                reason = "Template signal detected."
                confidence = max(confidence, 0.82)
            elif contains_any(combined, ("task", "todo", "待办", "任务")):
                resolved_role = "task"
                reason = "Task signal detected."
                confidence = max(confidence, 0.8)
            else:
                resolved_role = "admin"
                reason = "Lab material defaults to admin."
                confidence = max(confidence, 0.65)

        elif resolved_domain == "research":
            if project:
                if extension in CODE_EXTENSIONS:
                    resolved_role = "code"
                    reason = "Code file inside a project."
                    confidence = max(confidence, 0.92)
                elif extension == ".pdf" and contains_any(combined, ("paper", "literature", "reference", "论文", "文献")):
                    resolved_role = "literature"
                    reason = "Paper PDF for a research project."
                    confidence = max(confidence, 0.92)
                elif extension in DATA_EXTENSIONS and contains_any(combined, RAW_HINTS):
                    resolved_role = "raw-data"
                    reason = "Raw-data signal detected."
                    confidence = max(confidence, 0.9)
                elif extension in DATA_EXTENSIONS and contains_any(combined, PROCESSED_HINTS):
                    resolved_role = "processed-data"
                    reason = "Processed-data signal detected."
                    confidence = max(confidence, 0.9)
                elif extension in DATA_EXTENSIONS and origin == "incoming":
                    resolved_role = "raw-data"
                    reason = "Incoming dataset defaults to raw-data."
                    confidence = max(confidence, 0.84)
                elif contains_any(combined, EXPERIMENT_HINTS):
                    resolved_role = "experiments"
                    reason = "Experiment signal detected."
                    confidence = max(confidence, 0.84)
                elif extension in DOC_EXTENSIONS and contains_any(combined, RESEARCH_WRITING_HINTS):
                    resolved_role = "writing"
                    reason = "Research writing signal detected."
                    confidence = max(confidence, 0.86)
                elif origin == "generated":
                    resolved_role = "output"
                    reason = "Generated research artifact defaults to output."
                    confidence = max(confidence, 0.74)
                elif extension in IMAGE_EXTENSIONS | VIDEO_EXTENSIONS:
                    resolved_role = "output"
                    reason = "Visual research artifact defaults to output."
                    confidence = max(confidence, 0.72)
                elif extension in DOC_EXTENSIONS:
                    resolved_role = "writing"
                    reason = "Research project document defaults to writing."
                    confidence = max(confidence, 0.72)
                else:
                    resolved_role = "raw-data"
                    reason = "Incoming project artifact defaults to raw-data."
                    confidence = max(confidence, 0.58)
            else:
                if extension == ".pdf":
                    resolved_role = "literature"
                    reason = "Standalone PDF defaults to research literature."
                    confidence = max(confidence, 0.76)
                elif contains_any(combined, ("thesis", "dissertation", "论文", "学位")):
                    resolved_role = "thesis"
                    reason = "Thesis signal detected."
                    confidence = max(confidence, 0.84)
                elif extension in DATA_EXTENSIONS:
                    resolved_role = "data"
                    reason = "Standalone data artifact detected."
                    confidence = max(confidence, 0.74)
                else:
                    resolved_role = "note"
                    reason = "Research material defaults to note."
                    confidence = max(confidence, 0.62)

        elif resolved_domain == "dev":
            if project:
                if extension in CODE_EXTENSIONS:
                    resolved_role = "source"
                    reason = "Code file inside a general project."
                    confidence = max(confidence, 0.9)
                elif contains_any(combined, ("readme", "spec", "plan", "requirement", "说明", "需求", "计划")):
                    resolved_role = "admin"
                    reason = "Project-administration signal detected."
                    confidence = max(confidence, 0.82)
                elif origin == "incoming":
                    resolved_role = "inbox"
                    reason = "Incoming general-project artifact defaults to inbox."
                    confidence = max(confidence, 0.76)
                elif origin == "generated" and extension in DOC_EXTENSIONS | IMAGE_EXTENSIONS | VIDEO_EXTENSIONS:
                    resolved_role = "output"
                    reason = "Generated project artifact defaults to output."
                    confidence = max(confidence, 0.8)
                else:
                    resolved_role = "work"
                    reason = "General-project artifact defaults to work."
                    confidence = max(confidence, 0.68)
            else:
                if extension in {".py", ".ps1", ".sh", ".bat"}:
                    resolved_role = "scripts"
                    reason = "Standalone automation script detected."
                    confidence = max(confidence, 0.86)
                elif contains_any(combined, ("sandbox", "prototype", "temp", "临时", "原型")):
                    resolved_role = "sandbox"
                    reason = "Sandbox signal detected."
                    confidence = max(confidence, 0.82)
                elif contains_any(combined, ("tutorial", "learn", "lesson", "学习")):
                    resolved_role = "learning"
                    reason = "Learning signal detected."
                    confidence = max(confidence, 0.78)
                else:
                    resolved_role = "tools"
                    reason = "Development artifact defaults to tools."
                    confidence = max(confidence, 0.64)

        elif resolved_domain == "docs":
            if contains_any(combined, CERTIFICATE_HINTS):
                resolved_role = "certificate"
                reason = "Certificate signal detected."
                confidence = max(confidence, 0.9)
            elif contains_any(combined, FORM_HINTS):
                resolved_role = "form"
                reason = "Form signal detected."
                confidence = max(confidence, 0.84)
            elif contains_any(combined, JOURNAL_HINTS):
                resolved_role = "journal"
                reason = "Journal signal detected."
                confidence = max(confidence, 0.86)
            elif contains_any(combined, OFFICIAL_HINTS):
                resolved_role = "official"
                reason = "Official document signal detected."
                confidence = max(confidence, 0.86)
            else:
                resolved_role = "personal"
                reason = "Document defaults to personal."
                confidence = max(confidence, 0.68)

        elif resolved_domain == "media":
            if extension in FONT_EXTENSIONS:
                resolved_role = "font"
                reason = "Font extension detected."
                confidence = max(confidence, 0.98)
            elif extension in AUDIO_EXTENSIONS:
                resolved_role = "audio"
                reason = "Audio extension detected."
                confidence = max(confidence, 0.98)
            elif extension in VIDEO_EXTENSIONS or contains_any(combined, RECORDING_HINTS):
                resolved_role = "recording" if contains_any(combined, RECORDING_HINTS) else "video"
                reason = "Recording or video signal detected."
                confidence = max(confidence, 0.92)
            elif contains_any(combined, SCREENSHOT_HINTS):
                resolved_role = "screenshot"
                reason = "Screenshot signal detected."
                confidence = max(confidence, 0.94)
            elif extension in IMAGE_EXTENSIONS:
                resolved_role = "image"
                reason = "Image extension detected."
                confidence = max(confidence, 0.9)
            else:
                resolved_role = "asset"
                reason = "Media artifact defaults to reusable assets."
                confidence = max(confidence, 0.66)

        elif resolved_domain == "installers":
            if contains_any(combined, DRIVER_HINTS):
                resolved_role = "driver"
                reason = "Driver signal detected."
                confidence = max(confidence, 0.9)
            elif contains_any(combined, OS_HINTS) or extension == ".iso":
                resolved_role = "os"
                reason = "Operating-system image signal detected."
                confidence = max(confidence, 0.9)
            elif contains_any(combined, DEVTOOL_HINTS):
                resolved_role = "devtool"
                reason = "Development-tool signal detected."
                confidence = max(confidence, 0.82)
            elif contains_any(combined, OFFICE_HINTS):
                resolved_role = "office"
                reason = "Office-tool signal detected."
                confidence = max(confidence, 0.8)
            else:
                resolved_role = "common-app"
                reason = "Installer defaults to common applications."
                confidence = max(confidence, 0.64)

        elif resolved_domain == "systems":
            if extension in VM_EXTENSIONS or contains_any(combined, ("vm", "virtual machine", "虚拟机")):
                resolved_role = "vm"
                reason = "VM artifact detected."
                confidence = max(confidence, 0.92)
            elif contains_any(combined, ("appdata", "cache", "workspace", "聊天", "同步")):
                resolved_role = "appdata-local"
                reason = "Application data or cache signal detected."
                confidence = max(confidence, 0.76)
            elif contains_any(combined, ("portable", "绿色版", "便携")):
                resolved_role = "portable"
                reason = "Portable-program signal detected."
                confidence = max(confidence, 0.82)
            else:
                resolved_role = "program"
                reason = "System artifact defaults to programs."
                confidence = max(confidence, 0.62)

        elif resolved_domain == "archive":
            resolved_role = "archive"
            reason = "Archive domain always uses archive role."
            confidence = max(confidence, 0.99)

        elif resolved_domain == "downloads":
            resolved_role = "incoming"
            reason = "Ambiguous file staged in Downloads."
            confidence = max(confidence, 0.35)

    return {
        "source": source_name or None,
        "domain": resolved_domain,
        "role": resolved_role,
        "project": normalize_text(project),
        "project_type": resolved_project_type,
        "course": normalize_text(course),
        "term": normalize_text(term),
        "origin": origin,
        "confidence": round(confidence, 2),
        "reason": reason,
    }


def resolve_relative_dir(
    domain: str,
    role: str,
    when: dt.date,
    project: str | None = None,
    project_type: str | None = None,
    course: str | None = None,
    term: str | None = None,
) -> PurePosixPath:
    resolved_domain = canonical_domain(domain)
    resolved_role = canonical_role(role)
    if resolved_domain is None or resolved_role is None:
        raise ValueError("domain and role are required for route resolution.")

    project_slug = slugify_component(project, "general")
    course_slug = slugify_component(course, "general-course")
    normalized_term = normalize_term(term, when)
    year = str(when.year)

    if resolved_domain == "courses":
        mapping = {
            "slides": "Slides",
            "notes": "Notes",
            "assignments": "Assignments",
            "labs": "Labs",
            "exam": "Exam",
        }
        subdir = mapping.get(resolved_role, "Notes")
        return PurePosixPath("Courses") / normalized_term / course_slug / subdir

    if resolved_domain == "lab":
        mapping = {
            "admin": "Admin",
            "group-meeting": "GroupMeeting",
            "reimbursement": "Reimbursement",
            "shared": "Shared",
            "task": "Tasks",
            "template": "Templates",
        }
        return PurePosixPath("Lab") / mapping.get(resolved_role, "Admin")

    if resolved_domain == "research":
        if project and (project_type == "research" or resolved_role in RESEARCH_PROJECT_DIRS):
            subpath = RESEARCH_PROJECT_DIRS.get(resolved_role, "06_Output")
            return PurePosixPath("Research") / "Projects" / project_slug / PurePosixPath(subpath)

        mapping = {
            "literature": PurePosixPath("Research") / "Papers",
            "note": PurePosixPath("Research") / "Notes",
            "data": PurePosixPath("Research") / "Data",
            "thesis": PurePosixPath("Research") / "Thesis",
        }
        return mapping.get(resolved_role, PurePosixPath("Research") / "Notes")

    if resolved_domain == "dev":
        if project:
            subpath = GENERAL_PROJECT_DIRS.get(resolved_role, "03_Work")
            return PurePosixPath("Dev") / "Tools" / project_slug / PurePosixPath(subpath)

        mapping = {
            "learning": "Learning",
            "sandbox": "Sandbox",
            "scripts": "Scripts",
            "tools": "Tools",
        }
        return PurePosixPath("Dev") / mapping.get(resolved_role, "Tools")

    if resolved_domain == "docs":
        if resolved_role == "journal":
            return PurePosixPath("Docs") / "Journal" / year
        mapping = {
            "certificate": "Certificates",
            "form": "Forms",
            "official": "Official",
            "personal": "Personal",
            "journal": "Journal",
        }
        return PurePosixPath("Docs") / mapping.get(resolved_role, "Personal")

    if resolved_domain == "media":
        mapping = {
            "asset": "Assets",
            "audio": "Audio",
            "font": "Fonts",
            "image": "Images",
            "recording": "Recordings",
            "screenshot": "Screenshots",
            "template": "Templates",
            "video": "Videos",
        }
        return PurePosixPath("Media") / mapping.get(resolved_role, "Assets")

    if resolved_domain == "installers":
        mapping = {
            "common-app": "CommonApps",
            "devtool": "DevTools",
            "driver": "Drivers",
            "office": "Office",
            "os": "OS",
        }
        return PurePosixPath("Installers") / mapping.get(resolved_role, "CommonApps")

    if resolved_domain == "systems":
        mapping = {
            "appdata-local": "AppData_Local",
            "portable": "Portable",
            "program": "Programs",
            "vm": "VM",
        }
        return PurePosixPath("Systems") / mapping.get(resolved_role, "Programs")

    if resolved_domain == "archive":
        return PurePosixPath("Archive") / year

    if resolved_domain == "downloads":
        return PurePosixPath("Downloads")

    raise ValueError(f"unsupported domain: {resolved_domain}")


def route_file(
    workspace_root: str,
    domain: str,
    role: str,
    filename: str,
    project: str | None = None,
    project_type: str | None = None,
    course: str | None = None,
    term: str | None = None,
    date: str | None = None,
    target_name: str | None = None,
    version: str | None = None,
    date_prefix: bool = False,
) -> dict[str, object]:
    when = dt.date.fromisoformat(date) if date else dt.date.today()
    workspace_root_path = normalize_workspace_root(workspace_root)
    storage_root = files_root_path(workspace_root)
    routed_dir = resolve_relative_dir(
        domain=domain,
        role=role,
        when=when,
        project=project,
        project_type=project_type,
        course=course,
        term=term,
    )
    routed_name = build_target_filename(
        source_name=filename,
        target_name=target_name,
        date=when.isoformat(),
        date_prefix=date_prefix,
        version=version,
    )
    relative_dir = PurePosixPath(FILES_ROOT_NAME) / routed_dir
    relative_path = relative_dir / routed_name
    absolute_path = workspace_root_path / Path(relative_path)
    return {
        "workspace_root": str(workspace_root_path),
        "storage_root": str(storage_root),
        "domain": canonical_domain(domain),
        "role": canonical_role(role),
        "project": normalize_text(project),
        "project_type": normalize_text(project_type),
        "course": normalize_text(course),
        "term": normalize_text(term),
        "date": when.isoformat(),
        "relative_dir": relative_dir.as_posix(),
        "relative_path": relative_path.as_posix(),
        "absolute_path": str(absolute_path),
        "filename": routed_name,
    }


def ensure_directory(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def same_file_contents(source: Path, target: Path) -> bool:
    if not source.exists() or not target.exists():
        return False
    if source.stat().st_size != target.stat().st_size:
        return False
    source_hash = hashlib.sha256()
    target_hash = hashlib.sha256()
    with source.open("rb") as source_handle:
        for chunk in iter(lambda: source_handle.read(1024 * 1024), b""):
            source_hash.update(chunk)
    with target.open("rb") as target_handle:
        for chunk in iter(lambda: target_handle.read(1024 * 1024), b""):
            target_hash.update(chunk)
    return source_hash.digest() == target_hash.digest()


def choose_collision_path(path: Path) -> Path:
    if not path.exists():
        return path
    stem = path.stem
    suffix = path.suffix
    counter = 2
    while True:
        candidate = path.with_name(f"{stem}_copy{counter:02d}{suffix}")
        if not candidate.exists():
            return candidate
        counter += 1


def route_needs_review(decision: dict[str, object]) -> bool:
    confidence = float(decision.get("confidence") or 0.0)
    domain = decision.get("domain")
    role = decision.get("role")
    return confidence < LOW_CONFIDENCE_THRESHOLD or domain == "downloads" or not role


def organize_file(
    workspace_root: str,
    source: str,
    origin: str = "incoming",
    domain: str | None = None,
    role: str | None = None,
    project: str | None = None,
    project_type: str | None = None,
    course: str | None = None,
    term: str | None = None,
    context: str | None = None,
    date: str | None = None,
    target_name: str | None = None,
    version: str | None = None,
    date_prefix: bool = False,
    mode: str = "copy",
    collision: str = "rename",
) -> dict[str, object]:
    source_path = Path(source)
    if not source_path.exists():
        raise FileNotFoundError(f"source file not found: {source}")
    if not source_path.is_file():
        raise ValueError("organize only supports files, not directories.")

    decision = decide_route(
        source=source_path.name,
        context=context,
        origin=origin,
        domain=domain,
        role=role,
        project=project,
        project_type=project_type,
        course=course,
        term=term,
    )
    route = route_file(
        workspace_root=workspace_root,
        domain=decision["domain"],
        role=decision["role"],
        filename=source_path.name,
        project=decision["project"],
        project_type=decision["project_type"],
        course=decision["course"],
        term=decision["term"],
        date=date,
        target_name=target_name,
        version=version,
        date_prefix=date_prefix,
    )

    destination = Path(route["absolute_path"])
    ensure_directory(destination.parent)

    action = "copied" if mode == "copy" else "moved"
    if destination.exists() and same_file_contents(source_path, destination):
        return {
            "command": "organize",
            "changed": False,
            "action": "skipped",
            "reason": "An identical file already exists at the target path.",
            "decision": decision,
            "route": route,
            "source": str(source_path),
            "target": str(destination),
        }

    if destination.exists():
        if collision == "skip":
            return {
                "command": "organize",
                "changed": False,
                "action": "skipped",
                "reason": "Target exists and collision mode is skip.",
                "decision": decision,
                "route": route,
                "source": str(source_path),
                "target": str(destination),
            }
        if collision == "rename":
            destination = choose_collision_path(destination)
            route["absolute_path"] = str(destination)
            route["relative_path"] = str(Path(route["relative_dir"]) / destination.name).replace("\\", "/")
            route["filename"] = destination.name
        elif collision != "overwrite":
            raise ValueError("unsupported collision mode. Use rename, skip, or overwrite.")

    if mode == "copy":
        shutil.copy2(source_path, destination)
    elif mode == "move":
        shutil.move(str(source_path), str(destination))
    else:
        raise ValueError("unsupported mode. Use copy or move.")

    return {
        "command": "organize",
        "changed": True,
        "action": action,
        "decision": decision,
        "route": route,
        "source": str(source_path),
        "target": str(destination),
    }


def intake_file(
    workspace_root: str,
    source: str,
    domain: str | None = None,
    role: str | None = None,
    project: str | None = None,
    project_type: str | None = None,
    course: str | None = None,
    term: str | None = None,
    context: str | None = None,
    date: str | None = None,
    target_name: str | None = None,
    version: str | None = None,
    date_prefix: bool = False,
    mode: str = "copy",
    collision: str = "rename",
    dry_run: bool = False,
) -> dict[str, object]:
    source_path = Path(source)
    decision = decide_route(
        source=source_path.name,
        context=context,
        origin="incoming",
        domain=domain,
        role=role,
        project=project,
        project_type=project_type,
        course=course,
        term=term,
    )
    route = route_file(
        workspace_root=workspace_root,
        domain=decision["domain"],
        role=decision["role"],
        filename=source_path.name,
        project=decision["project"],
        project_type=decision["project_type"],
        course=decision["course"],
        term=decision["term"],
        date=date,
        target_name=target_name,
        version=version,
        date_prefix=date_prefix,
    )
    needs_review = route_needs_review(decision)
    if dry_run:
        return {
            "command": "intake",
            "applied": False,
            "needs_review": needs_review,
            "recommended_next_step": "ask-user" if needs_review else "organize",
            "decision": decision,
            "route": route,
            "source": str(source_path),
        }

    result = organize_file(
        workspace_root=workspace_root,
        source=source,
        origin="incoming",
        domain=domain,
        role=role,
        project=project,
        project_type=project_type,
        course=course,
        term=term,
        context=context,
        date=date,
        target_name=target_name,
        version=version,
        date_prefix=date_prefix,
        mode=mode,
        collision=collision,
    )
    result["command"] = "intake"
    result["applied"] = True
    result["needs_review"] = needs_review
    result["recommended_next_step"] = "ask-user" if needs_review else "done"
    return result


def capture_output(
    workspace_root: str,
    source: str,
    domain: str | None = None,
    role: str | None = None,
    project: str | None = None,
    project_type: str | None = None,
    course: str | None = None,
    term: str | None = None,
    context: str | None = None,
    date: str | None = None,
    target_name: str | None = None,
    version: str | None = None,
    date_prefix: bool = False,
    mode: str = "copy",
    collision: str = "rename",
    dry_run: bool = False,
) -> dict[str, object]:
    source_path = Path(source)
    decision = decide_route(
        source=source_path.name,
        context=context,
        origin="generated",
        domain=domain,
        role=role,
        project=project,
        project_type=project_type,
        course=course,
        term=term,
    )
    route = route_file(
        workspace_root=workspace_root,
        domain=decision["domain"],
        role=decision["role"],
        filename=source_path.name,
        project=decision["project"],
        project_type=decision["project_type"],
        course=decision["course"],
        term=decision["term"],
        date=date,
        target_name=target_name,
        version=version,
        date_prefix=date_prefix,
    )
    needs_review = route_needs_review(decision)
    if dry_run:
        return {
            "command": "capture",
            "applied": False,
            "needs_review": needs_review,
            "recommended_next_step": "ask-user" if needs_review else "organize",
            "decision": decision,
            "route": route,
            "source": str(source_path),
        }

    result = organize_file(
        workspace_root=workspace_root,
        source=source,
        origin="generated",
        domain=domain,
        role=role,
        project=project,
        project_type=project_type,
        course=course,
        term=term,
        context=context,
        date=date,
        target_name=target_name,
        version=version,
        date_prefix=date_prefix,
        mode=mode,
        collision=collision,
    )
    result["command"] = "capture"
    result["applied"] = True
    result["needs_review"] = needs_review
    result["recommended_next_step"] = "ask-user" if needs_review else "done"
    return result


def candidate_search_roots(
    workspace_root: str,
    domain: str | None = None,
    project: str | None = None,
    project_type: str | None = None,
    course: str | None = None,
    term: str | None = None,
    date: str | None = None,
) -> list[Path]:
    root = files_root_path(workspace_root)
    when = dt.date.fromisoformat(date) if date else dt.date.today()
    resolved_domain = canonical_domain(domain)
    paths: list[Path] = []

    if resolved_domain == "research" and project:
        project_slug = slugify_component(project, "general")
        paths.append(root / "Research" / "Projects" / project_slug)
    elif resolved_domain == "dev" and project:
        project_slug = slugify_component(project, "general")
        paths.append(root / "Dev" / "Tools" / project_slug)
    elif resolved_domain == "courses":
        term_name = normalize_term(term, when)
        course_slug = slugify_component(course, "general-course")
        paths.append(root / "Courses" / term_name / course_slug)
    elif resolved_domain == "lab":
        paths.append(root / "Lab")
    elif resolved_domain == "research":
        paths.append(root / "Research")
    elif resolved_domain == "dev":
        paths.append(root / "Dev")
    elif resolved_domain == "docs":
        paths.append(root / "Docs")
    elif resolved_domain == "media":
        paths.append(root / "Media")
    elif resolved_domain == "installers":
        paths.append(root / "Installers")
    elif resolved_domain == "systems":
        paths.append(root / "Systems")
    elif resolved_domain == "archive":
        paths.append(root / "Archive" / str(when.year))
    elif resolved_domain == "downloads":
        paths.append(root / "Downloads")

    if not paths:
        for name in TOP_LEVEL_WORKSPACE_DIRS:
            paths.append(root / name)

    deduped: list[Path] = []
    seen: set[str] = set()
    for path in paths:
        key = str(path)
        if key not in seen:
            deduped.append(path)
            seen.add(key)
    return deduped


def find_files(
    workspace_root: str,
    query: str,
    domain: str | None = None,
    project: str | None = None,
    project_type: str | None = None,
    course: str | None = None,
    term: str | None = None,
    date: str | None = None,
    limit: int = 20,
) -> dict[str, object]:
    normalized_query = normalize_text(query, "") or ""
    if not normalized_query:
        raise ValueError("query cannot be empty.")
    lowered_query = normalized_query.casefold()
    workspace_root_path = normalize_workspace_root(workspace_root)
    roots = candidate_search_roots(
        workspace_root=workspace_root,
        domain=domain,
        project=project,
        project_type=project_type,
        course=course,
        term=term,
        date=date,
    )
    matches: list[dict[str, object]] = []
    scanned_dirs = 0

    for root in roots:
        if not root.exists():
            continue
        scanned_dirs += 1
        for path in root.rglob("*"):
            if not path.is_file():
                continue
            relative_path = path.relative_to(workspace_root_path).as_posix()
            haystack = f"{path.name} {relative_path}".casefold()
            if lowered_query in haystack:
                stat = path.stat()
                matches.append(
                    {
                        "path": str(path),
                        "relative_path": relative_path,
                        "size": stat.st_size,
                        "modified_at": dt.datetime.fromtimestamp(stat.st_mtime).astimezone().replace(microsecond=0).isoformat(),
                    }
                )
                if len(matches) >= limit:
                    return {
                        "command": "find",
                        "query": normalized_query,
                        "search_roots": [str(item) for item in roots],
                        "scanned_dirs": scanned_dirs,
                        "matches": matches,
                    }

    return {
        "command": "find",
        "query": normalized_query,
        "search_roots": [str(item) for item in roots],
        "scanned_dirs": scanned_dirs,
        "matches": matches,
    }


def write_readme(path: Path, title: str, lines: list[str]) -> None:
    content = "\n".join([f"# {title}", ""] + lines).rstrip() + "\n"
    path.write_text(content, encoding="utf-8")


def scaffold_workspace(workspace_root: str) -> dict[str, object]:
    workspace_root_path = normalize_workspace_root(workspace_root)
    root = files_root_path(workspace_root)
    created: list[str] = []
    if not root.exists():
        root.mkdir(parents=True, exist_ok=True)
        created.append(str(root))
    for name in TOP_LEVEL_WORKSPACE_DIRS:
        path = root / name
        if not path.exists():
            path.mkdir(parents=True, exist_ok=True)
            created.append(str(path))

    nested_paths = [
        root / "Research" / "Papers",
        root / "Research" / "Notes",
        root / "Research" / "Projects",
        root / "Research" / "Data",
        root / "Research" / "Thesis",
        root / "Dev" / "Learning",
        root / "Dev" / "Sandbox",
        root / "Dev" / "Scripts",
        root / "Dev" / "Tools",
        root / "Docs" / "Certificates",
        root / "Docs" / "Forms",
        root / "Docs" / "Journal",
        root / "Docs" / "Official",
        root / "Docs" / "Personal",
        root / "Lab" / "Admin",
        root / "Lab" / "GroupMeeting",
        root / "Lab" / "Reimbursement",
        root / "Lab" / "Shared",
        root / "Lab" / "Tasks",
        root / "Lab" / "Templates",
        root / "Media" / "Assets",
        root / "Media" / "Audio",
        root / "Media" / "Fonts",
        root / "Media" / "Images",
        root / "Media" / "Recordings",
        root / "Media" / "Screenshots",
        root / "Media" / "Templates",
        root / "Media" / "Videos",
        root / "Installers" / "CommonApps",
        root / "Installers" / "DevTools",
        root / "Installers" / "Drivers",
        root / "Installers" / "Office",
        root / "Installers" / "OS",
        root / "Systems" / "AppData_Local",
        root / "Systems" / "Portable",
        root / "Systems" / "Programs",
        root / "Systems" / "VM",
    ]
    for path in nested_paths:
        if not path.exists():
            path.mkdir(parents=True, exist_ok=True)
            created.append(str(path))

    return {
        "command": "scaffold",
        "template": "workspace",
        "workspace_root": str(workspace_root_path),
        "storage_root": str(root),
        "created": created,
    }


def scaffold_general_project(workspace_root: str, project: str, domain: str = "dev") -> dict[str, object]:
    domain = canonical_domain(domain) or "dev"
    project_slug = slugify_component(project, "general")
    storage_root = files_root_path(workspace_root)
    if domain == "research":
        project_root = storage_root / "Research" / "Projects" / project_slug
    elif domain == "lab":
        project_root = storage_root / "Lab" / "Tasks" / project_slug
    else:
        project_root = storage_root / "Dev" / "Tools" / project_slug

    created: list[str] = []
    ensure_directory(project_root)
    for subdir in ["00_Inbox", "01_Admin", "02_Source", "03_Work", "04_Output", "99_Archive"]:
        path = project_root / subdir
        if not path.exists():
            path.mkdir(parents=True, exist_ok=True)
            created.append(str(path))

    readme = project_root / "README.md"
    if not readme.exists():
        write_readme(
            readme,
            project_slug,
            [
                "## Purpose",
                "",
                "Store the main material for this general project.",
                "",
                "## Structure",
                "",
                "- `00_Inbox/` - incoming files waiting for classification",
                "- `01_Admin/` - plans, requirements, process notes",
                "- `02_Source/` - source material and original inputs",
                "- `03_Work/` - working drafts and intermediate artifacts",
                "- `04_Output/` - final exports and deliverables",
                "- `99_Archive/` - obsolete or historical material",
            ],
        )
        created.append(str(readme))

    return {
        "command": "scaffold",
        "template": "general-project",
        "project_root": str(project_root),
        "created": created,
    }


def scaffold_research_project(workspace_root: str, project: str) -> dict[str, object]:
    project_slug = slugify_component(project, "general")
    project_root = files_root_path(workspace_root) / "Research" / "Projects" / project_slug
    created: list[str] = []
    ensure_directory(project_root)
    for subdir in [
        "01_Literature",
        "02_Data/raw",
        "02_Data/processed",
        "03_Code",
        "04_Experiments",
        "05_Writing",
        "06_Output",
        "99_Archive",
    ]:
        path = project_root / subdir
        if not path.exists():
            path.mkdir(parents=True, exist_ok=True)
            created.append(str(path))

    readme = project_root / "README.md"
    if not readme.exists():
        write_readme(
            readme,
            project_slug,
            [
                "## Purpose",
                "",
                "Store the main material for this research project.",
                "",
                "## Structure",
                "",
                "- `01_Literature/` - reference papers and reading material",
                "- `02_Data/raw/` - immutable raw data",
                "- `02_Data/processed/` - cleaned or transformed data",
                "- `03_Code/` - source code",
                "- `04_Experiments/` - logs, metrics, experiment notes",
                "- `05_Writing/` - manuscripts, slides, reports",
                "- `06_Output/` - figures, exports, final deliverables",
                "- `99_Archive/` - obsolete or historical material",
            ],
        )
        created.append(str(readme))

    return {
        "command": "scaffold",
        "template": "research-project",
        "project_root": str(project_root),
        "created": created,
    }


def scaffold(
    workspace_root: str,
    template: str,
    project: str | None = None,
    domain: str | None = None,
) -> dict[str, object]:
    if template == "workspace":
        return scaffold_workspace(workspace_root)
    if template == "general-project":
        if not project:
            raise ValueError("project is required for general-project scaffolds.")
        return scaffold_general_project(workspace_root, project=project, domain=domain or "dev")
    if template == "research-project":
        if not project:
            raise ValueError("project is required for research-project scaffolds.")
        return scaffold_research_project(workspace_root, project=project)
    raise ValueError("unsupported template. Use workspace, general-project, or research-project.")


def to_json(data: dict[str, object]) -> str:
    return json.dumps(data, indent=2, ensure_ascii=False)
