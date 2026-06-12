#!/usr/bin/env python3
"""Shared core helpers for the memory-router skill."""

from __future__ import annotations

import datetime as dt
import re
from pathlib import Path, PurePosixPath


ALIASES = {
    "project": "project-facts",
    "facts": "project-facts",
    "fact": "project-facts",
    "decision": "project-decisions",
    "decisions": "project-decisions",
    "project-decision": "project-decisions",
    "summary": "session-summary",
    "session": "session-summary",
}

TRIVIAL_CHAT_MESSAGES = {
    "hi",
    "hello",
    "thanks",
    "thank you",
    "ok",
    "okay",
    "got it",
    "sounds good",
    "cool",
    "nice",
    "bye",
    "see you",
    "好的",
    "收到",
    "明白了",
    "知道了",
    "先这样",
    "就这样",
    "谢谢",
    "谢谢你",
    "辛苦了",
    "回头见",
}

PREFERENCE_DIRECT_HINTS = (
    "prefer",
    "preference",
    "prefers",
    "concise",
    "detailed",
    "bullet",
    "markdown",
    "language",
    "tone",
    "format",
    "workflow",
    "tool",
    "respond in",
    "answer in",
    "use chinese",
    "use english",
    "请用中文",
    "请用英文",
    "中文回答",
    "中文回复",
    "英文回答",
    "英文回复",
    "简洁一点",
    "详细一点",
    "分点",
    "列表",
    "条列",
    "语气",
    "格式",
    "风格",
)

PREFERENCE_VERB_HINTS = (
    "prefer",
    "preference",
    "prefers",
    "like",
    "likes",
    "偏好",
    "喜欢",
    "更喜欢",
    "习惯",
    "希望",
)

PREFERENCE_TARGET_HINTS = (
    "chinese",
    "english",
    "language",
    "concise",
    "detailed",
    "bullet",
    "markdown",
    "tone",
    "format",
    "style",
    "workflow",
    "tool",
    "python",
    "中文",
    "英文",
    "语言",
    "简洁",
    "详细",
    "分点",
    "列表",
    "条列",
    "语气",
    "格式",
    "风格",
    "工作流",
    "工具",
    "回答",
    "回复",
    "输出",
)

PROFILE_HINTS = (
    "i am ",
    "i'm ",
    "my role",
    "my background",
    "i work as",
    "my goal",
    "long-term goal",
    "timezone",
    "based in",
    "我是",
    "我的角色",
    "我的背景",
    "我从事",
    "我的目标",
    "长期目标",
    "时区",
    "我在",
)

PROJECT_DECISION_HINTS = (
    "decided",
    "decision",
    "choose",
    "chosen",
    "adopt",
    "settled on",
    "switch to",
    "go with",
    "standardize on",
    "we will use",
    "决定",
    "选择",
    "选用",
    "采用",
    "改成",
    "切换到",
    "统一用",
    "定为",
)

PROJECT_FACT_HINTS = (
    "architecture",
    "database",
    "sqlite",
    "postgres",
    "storage",
    "constraint",
    "requires",
    "must ",
    "integration",
    "api",
    "repository",
    "repo",
    "folder",
    "path",
    "架构",
    "数据库",
    "存储",
    "约束",
    "要求",
    "必须",
    "接口",
    "仓库",
    "目录",
    "路径",
    "依赖",
)

TASK_HINTS = (
    "todo",
    "next step",
    "follow-up",
    "need to",
    "should ",
    "remaining",
    "unresolved",
    "fix ",
    "add ",
    "verify",
    "test ",
    "cleanup",
    "refactor",
    "update ",
    "document",
    "implement",
    "待办",
    "下一步",
    "后续",
    "跟进",
    "修复",
    "补上",
    "验证",
    "测试",
    "清理",
    "重构",
    "实现",
    "更新文档",
    "需要确认",
    "需要补",
    "需要做",
)

SESSION_SUMMARY_HINTS = (
    "summary",
    "recap",
    "meeting",
    "discussed",
    "resolved",
    "what changed",
    "during the session",
    "总结",
    "回顾",
    "会议",
    "讨论了",
    "已解决",
    "这次会话",
    "本次会话",
    "这次对话",
)

EPHEMERAL_HINTS = (
    "maybe",
    "possibly",
    "probably",
    "tentative",
    "unclear",
    "might",
    "可能",
    "也许",
    "大概",
    "暂时",
    "不确定",
)

SENSITIVE_HINTS = (
    "password",
    "passwd",
    "passphrase",
    "api key",
    "token",
    "secret",
    "private key",
    "credential",
    "credentials",
    "recovery code",
    "otp",
    "验证码",
    "密码",
    "口令",
    "密钥",
    "令牌",
    "秘钥",
    "凭证",
)

PROFILE_INTEREST_HINTS = (
    "favorite",
    "favourite",
    "likes to watch",
    "watchlist",
    "music taste",
    "favorite singer",
    "favorite singers",
    "favorite artist",
    "favorite artists",
    "favorite band",
    "favorite bands",
    "favorite character",
    "favorite characters",
    "anime",
    "movie",
    "movies",
    "tv show",
    "song",
    "songs",
    "singer",
    "singers",
    "band",
    "bands",
    "musician",
    "musicians",
    "喜欢的歌手",
    "喜欢的音乐人",
    "喜欢的角色",
    "喜欢的动漫",
    "待看的动漫",
    "歌手",
    "音乐人",
    "动漫",
    "角色",
    "追番",
)

PROJECT_ENVIRONMENT_HINTS = (
    "workspace",
    "worktree",
    "project path",
    "root directory",
    "working directory",
    "repository path",
    "repo path",
    "directory",
    "folder",
    "path",
    "local file",
    "installed",
    "installation path",
    "workspace root",
    "skill is installed",
    "tool is installed",
    "工作区",
    "项目路径",
    "根目录",
    "目录",
    "路径",
    "本地文件",
    "安装",
    "已安装",
    "限制在",
    "不越界",
)

PROJECT_POLICY_HINTS = (
    "rule",
    "rules",
    "policy",
    "policies",
    "mechanism",
    "workflow rule",
    "we decided",
    "from now on",
    "must always",
    "always use",
    "standardize",
    "store in memrouter",
    "keep data in local files",
    "分类规则",
    "行为规则",
    "规则",
    "机制",
    "以后都",
    "统一",
    "必须",
    "固定",
    "存到 memrouter",
    "数据留本地",
)

PREFERENCE_EXCLUSION_HINTS = PROFILE_INTEREST_HINTS + (
    "favorite",
    "favourite",
    "watchlist",
    "song",
    "songs",
    "music",
    "anime",
    "character",
    "characters",
    "歌手",
    "音乐",
    "动漫",
    "角色",
)

ENTRY_HEADER_RE = re.compile(
    r"^- (?P<date>\d{4}-\d{2}-\d{2})(?: \| created_at: (?P<created_at>[^|]+))? \| topic: (?P<topic>.+?) \| source: (?P<source>.+?)$"
)
CJK_CHAR_RE = re.compile(r"[\u3400-\u9fff]")
LATIN_WORD_RE = re.compile(r"[A-Za-z0-9]+(?:['_-][A-Za-z0-9]+)*")
TRIVIAL_SEGMENT_SPLIT_RE = re.compile(r"[,.!?;:，。！？；：、/]+")


def normalize_metadata_value(value: str | None, default: str | None = None) -> str | None:
    if value is None:
        return default

    cleaned = value.replace("\r\n", "\n").replace("\r", "\n")
    cleaned = cleaned.replace("|", "/")
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    return cleaned or default


def normalize_text_lines(text: str) -> list[str]:
    lines = text.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    lines = [line.rstrip() for line in lines]

    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()

    if not lines:
        raise ValueError("memory text cannot be empty.")

    return lines


def normalize_query_text(query: str) -> str:
    normalized = query.strip()
    if not normalized:
        raise ValueError("query cannot be empty.")
    return normalized


def normalize_created_at(value: str | None = None) -> str:
    if value is None:
        return dt.datetime.now().astimezone().replace(microsecond=0).isoformat()

    normalized = value.strip()
    if not normalized:
        raise ValueError("created_at cannot be empty.")

    if normalized.endswith("Z"):
        normalized = normalized[:-1] + "+00:00"

    try:
        parsed = dt.datetime.fromisoformat(normalized)
    except ValueError as exc:
        raise ValueError("created_at must be an ISO 8601 datetime.") from exc

    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=dt.datetime.now().astimezone().tzinfo)

    return parsed.replace(microsecond=0).isoformat()


def contains_any(text: str, phrases: tuple[str, ...] | set[str]) -> bool:
    return any(phrase in text for phrase in phrases)


def count_text_units(text: str) -> int:
    latin_units = len(LATIN_WORD_RE.findall(text))
    cjk_units = (len(CJK_CHAR_RE.findall(text)) + 1) // 2
    return latin_units + cjk_units


def strip_wrapping_punctuation(text: str) -> str:
    return text.strip().strip(" \t\r\n.,!?;:，。！？；：、")


def is_trivial_chat(text: str) -> bool:
    normalized = strip_wrapping_punctuation(text)
    if normalized in TRIVIAL_CHAT_MESSAGES:
        return True

    segments = [segment.strip() for segment in TRIVIAL_SEGMENT_SPLIT_RE.split(normalized) if segment.strip()]
    return 1 < len(segments) <= 3 and all(segment in TRIVIAL_CHAT_MESSAGES for segment in segments)


def looks_like_preference(text: str) -> bool:
    if contains_any(text, PREFERENCE_EXCLUSION_HINTS):
        return False

    if contains_any(text, PREFERENCE_DIRECT_HINTS):
        return True

    return contains_any(text, PREFERENCE_VERB_HINTS) and contains_any(text, PREFERENCE_TARGET_HINTS)


def looks_like_project_fact(text: str, has_project: bool) -> bool:
    if contains_any(text, PROJECT_ENVIRONMENT_HINTS):
        return True

    if contains_any(text, PROJECT_FACT_HINTS):
        return True

    if not has_project:
        return False

    return contains_any(text, ("仓库", "目录", "路径", "架构", "数据库", "接口", "依赖", "约束", "要求", "存储"))


def looks_like_profile_interest(text: str) -> bool:
    return contains_any(text, PROFILE_INTEREST_HINTS)


def looks_like_project_policy(text: str) -> bool:
    if looks_like_preference(text):
        return False
    return contains_any(text, PROJECT_POLICY_HINTS)


def _contains_sensitive_information_legacy(text: str) -> bool:
    lowered = text.casefold()
    if contains_any(lowered, SENSITIVE_HINTS):
        return True

    return bool(re.search(r"(password|passwd|passphrase|token|secret|api key)\s*[:：]\s*\S+", lowered))

    return bool(re.search(r"(password|passwd|passphrase|token|secret|api key|密码|令牌|密钥)\s*[:：]\s*\S+", lowered))


def contains_sensitive_information(text: str) -> bool:
    lowered = text.casefold()
    if contains_any(lowered, SENSITIVE_HINTS):
        return True

    return bool(re.search(r"(password|passwd|passphrase|token|secret|api key|密码|令牌|密钥)\s*[:：]\s*\S+", lowered))


def slugify(value: str | None, default: str) -> str:
    if not value:
        return default
    slug = value.strip().casefold()
    slug = re.sub(r"[_\W]+", "-", slug, flags=re.UNICODE)
    slug = re.sub(r"-{2,}", "-", slug).strip("-")
    return slug or default


def canonical_memory_type(value: str) -> str:
    raw = value.strip().lower()
    return ALIASES.get(raw, raw)


def _infer_topic_legacy(memory_type: str, lowered_text: str) -> str | None:
    if memory_type == "preferences":
        if contains_any(lowered_text, ("chinese", "english", "language", "中文", "英文", "语言")):
            return "language"
        if contains_any(
            lowered_text,
            ("concise", "detailed", "bullet", "markdown", "format", "tone", "style", "简洁", "详细", "分点", "列表", "条列", "格式", "语气", "风格"),
        ):
            return "output-style"
        if contains_any(lowered_text, ("workflow", "tool", "python", "r ", "工作流", "工具", "脚本", "命令行")):
            return "workflow"
        return "preference"

    if memory_type == "profile":
        if contains_any(lowered_text, ("goal", "long-term goal", "目标", "长期目标")):
            return "goals"
        if contains_any(lowered_text, ("role", "background", "i am ", "i'm ", "i work as", "角色", "背景", "我是", "我从事")):
            return "identity"
        if contains_any(lowered_text, ("timezone", "based in", "constraint", "时区", "位于", "限制")):
            return "constraints"
        if contains_any(lowered_text, ("favorite", "favourite", "watchlist", "music", "song", "singer", "artist", "band", "anime", "character")):
            return "personal-interests"
        return "profile"

    if memory_type == "project-facts":
        if contains_any(lowered_text, ("sqlite", "postgres", "database", "storage", "数据库", "存储")):
            return "storage"
        if contains_any(lowered_text, ("architecture", "folder", "path", "repo", "repository", "架构", "目录", "路径", "仓库")):
            return "architecture"
        if contains_any(lowered_text, ("integration", "api", "dependency", "集成", "接口", "依赖")):
            return "integrations"
        if contains_any(lowered_text, ("constraint", "requires", "must ", "约束", "要求", "必须", "限制")):
            return "constraints"
        if contains_any(lowered_text, ("workspace", "project path", "root directory", "working directory", "local file", "installed")):
            return "environment"
        return "project-fact"

    if memory_type == "project-decisions":
        if contains_any(lowered_text, ("architecture", "storage", "router", "架构", "存储", "路由")):
            return "architecture"
        if contains_any(lowered_text, ("name", "naming", "folder", "slug", "convention", "命名", "目录", "规范")):
            return "naming-convention"
        if contains_any(lowered_text, ("tool", "python", "framework", "工具", "框架", "选型")):
            return "tool-choice"
        if contains_any(lowered_text, ("rule", "policy", "mechanism", "workflow")):
            return "policy"
        return "decision"

    if memory_type == "task":
        if contains_any(lowered_text, ("test", "verify", "测试", "验证")):
            return "testing"
        if contains_any(lowered_text, ("document", "readme", "docs", "文档", "说明")):
            return "docs"
        if contains_any(lowered_text, ("cleanup", "refactor", "清理", "重构")):
            return "cleanup"
        return "next-step"

    if memory_type == "session-summary":
        return "session-summary"

    if memory_type == "ephemeral":
        return "ephemeral"

    return None


def infer_topic(memory_type: str, lowered_text: str) -> str | None:
    if memory_type == "preferences":
        if contains_any(lowered_text, ("chinese", "english", "language", "中文", "英文", "语言")):
            return "language"
        if contains_any(
            lowered_text,
            ("concise", "detailed", "bullet", "markdown", "format", "tone", "style", "简洁", "详细", "分点", "列表", "条列", "格式", "语气", "风格"),
        ):
            return "output-style"
        if contains_any(lowered_text, ("workflow", "tool", "python", "r ", "工作流", "工具", "脚本", "命令行")):
            return "workflow"
        return "preference"

    if memory_type == "profile":
        if contains_any(lowered_text, ("goal", "long-term goal", "目标", "长期目标")):
            return "goals"
        if contains_any(lowered_text, ("role", "background", "i am ", "i'm ", "i work as", "角色", "背景", "我是", "我从事")):
            return "identity"
        if contains_any(lowered_text, ("timezone", "based in", "constraint", "时区", "位于", "限制")):
            return "constraints"
        if contains_any(
            lowered_text,
            (
                "favorite",
                "favourite",
                "watchlist",
                "music",
                "song",
                "singer",
                "artist",
                "band",
                "anime",
                "character",
                "喜欢的歌手",
                "喜欢的音乐人",
                "待看的动漫",
                "喜欢的角色",
                "歌手",
                "音乐人",
                "动漫",
                "角色",
            ),
        ):
            return "personal-interests"
        return "profile"

    if memory_type == "project-facts":
        if contains_any(lowered_text, ("workspace", "project path", "root directory", "working directory", "local file", "installed", "工作区", "项目路径", "根目录", "本地文件", "安装", "已安装")):
            return "environment"
        if contains_any(lowered_text, ("sqlite", "postgres", "database", "storage", "数据库", "存储")):
            return "storage"
        if contains_any(lowered_text, ("architecture", "folder", "path", "repo", "repository", "架构", "目录", "路径", "仓库")):
            return "architecture"
        if contains_any(lowered_text, ("integration", "api", "dependency", "集成", "接口", "依赖")):
            return "integrations"
        if contains_any(lowered_text, ("constraint", "requires", "must ", "约束", "要求", "必须", "限制")):
            return "constraints"
        return "project-fact"

    if memory_type == "project-decisions":
        if contains_any(lowered_text, ("rule", "policy", "mechanism", "workflow", "规则", "机制", "行为规则", "分类规则", "数据留本地")):
            return "policy"
        if contains_any(lowered_text, ("architecture", "storage", "router", "架构", "存储", "路由")):
            return "architecture"
        if contains_any(lowered_text, ("name", "naming", "folder", "slug", "convention", "命名", "目录", "规范")):
            return "naming-convention"
        if contains_any(lowered_text, ("tool", "python", "framework", "工具", "框架", "选型")):
            return "tool-choice"
        return "decision"

    if memory_type == "task":
        if contains_any(lowered_text, ("test", "verify", "测试", "验证")):
            return "testing"
        if contains_any(lowered_text, ("document", "readme", "docs", "文档", "说明")):
            return "docs"
        if contains_any(lowered_text, ("cleanup", "refactor", "清理", "重构")):
            return "cleanup"
        return "next-step"

    if memory_type == "session-summary":
        return "session-summary"

    if memory_type == "ephemeral":
        return "ephemeral"

    return None


def decide_memory_action(
    text: str,
    user_id: str | None = None,
    project: str | None = None,
    context: dict[str, object] | None = None,
) -> dict[str, object]:
    lines = normalize_text_lines(text)
    body = "\n".join(lines)
    flat_text = " ".join(line.strip() for line in lines if line.strip())
    lowered_text = flat_text.casefold()
    context = context or {}

    resolved_user_id = normalize_metadata_value(user_id)
    resolved_project = normalize_metadata_value(project)
    resolved_source = normalize_metadata_value(
        context.get("source") if isinstance(context.get("source"), str) else None,
        default="chat",
    )
    context_kind = normalize_metadata_value(
        context.get("kind") if isinstance(context.get("kind"), str) else None
    )
    text_units = count_text_units(flat_text)

    if is_trivial_chat(lowered_text):
        return {
            "should_persist": False,
            "confidence": 0.98,
            "memory_type": None,
            "topic": None,
            "dedupe_mode": "exact",
            "user_id": resolved_user_id,
            "project": resolved_project,
            "source": resolved_source,
            "reason": "Trivial chatter with no durable value.",
            "text": body,
        }

    if contains_sensitive_information(flat_text):
        return {
            "should_persist": False,
            "confidence": 0.99,
            "memory_type": None,
            "topic": None,
            "dedupe_mode": "exact",
            "user_id": resolved_user_id,
            "project": resolved_project,
            "source": resolved_source,
            "reason": "Sensitive credential-like information should not be stored in markdown memory.",
            "text": body,
        }

    hint = context.get("memory_type_hint") if isinstance(context.get("memory_type_hint"), str) else None
    hinted_type = canonical_memory_type(hint) if hint else None

    if context_kind in {"meeting", "summary", "session-summary"} or contains_any(lowered_text, SESSION_SUMMARY_HINTS):
        memory_type = "session-summary"
        confidence = 0.88
        reason = "Conversation recap or meeting-style summary."
    elif looks_like_project_policy(lowered_text):
        memory_type = "project-decisions"
        confidence = 0.9 if resolved_project else 0.78
        reason = "Adopted project or workspace rule, policy, or mechanism."
    elif looks_like_preference(lowered_text):
        memory_type = "preferences"
        confidence = 0.9
        reason = "Stable user-to-agent interaction preference."
    elif looks_like_profile_interest(lowered_text):
        memory_type = "profile"
        confidence = 0.78
        reason = "Durable personal interest or identity-adjacent user context."
    elif contains_any(lowered_text, PROJECT_DECISION_HINTS):
        memory_type = "project-decisions"
        confidence = 0.84
        reason = "Explicit project choice or decision language."
    elif contains_any(lowered_text, TASK_HINTS):
        memory_type = "task"
        confidence = 0.82
        reason = "Actionable task or next-step language."
    elif contains_any(lowered_text, PROFILE_HINTS):
        memory_type = "profile"
        confidence = 0.8
        reason = "Durable identity or user background signal."
    elif hinted_type in {
        "profile",
        "preferences",
        "project-facts",
        "project-decisions",
        "task",
        "session-summary",
        "ephemeral",
    }:
        memory_type = hinted_type
        confidence = 0.68
        reason = "Context supplied a memory type hint."
    elif looks_like_project_fact(lowered_text, has_project=bool(resolved_project)):
        memory_type = "project-facts"
        confidence = 0.84 if resolved_project else 0.72
        reason = "Project or workspace fact, environment detail, or constraint."
    elif contains_any(lowered_text, EPHEMERAL_HINTS) or text_units >= 8:
        memory_type = "ephemeral"
        confidence = 0.58
        reason = "Potentially useful but ambiguous, so route to low-confidence memory."
    else:
        return {
            "should_persist": False,
            "confidence": 0.35,
            "memory_type": None,
            "topic": None,
            "dedupe_mode": "exact",
            "user_id": resolved_user_id,
            "project": resolved_project,
            "source": resolved_source,
            "reason": "No strong durable-memory signal detected.",
            "text": body,
        }

    topic = infer_topic(memory_type, lowered_text)
    if memory_type in {"preferences", "profile", "project-facts", "project-decisions"} and topic:
        dedupe_mode = "topic"
    else:
        dedupe_mode = "exact"

    return {
        "should_persist": True,
        "confidence": confidence,
        "memory_type": memory_type,
        "topic": topic,
        "dedupe_mode": dedupe_mode,
        "user_id": resolved_user_id,
        "project": resolved_project,
        "source": resolved_source,
        "reason": reason,
        "text": body,
    }


def build_route(
    root: str,
    memory_type: str,
    user_id: str,
    project: str | None,
    when: dt.date,
) -> dict[str, str]:
    year = str(when.year)
    day = when.isoformat()
    root_path = PurePosixPath(root)
    project_slug = slugify(project, "general")
    user_slug = slugify(user_id, "default-user")

    if memory_type == "profile":
        path = root_path / "users" / user_slug / "profile.md"
        section = "Facts"
        scope = "user"
    elif memory_type == "preferences":
        path = root_path / "users" / user_slug / "preferences.md"
        section = "Entries"
        scope = "user"
    elif memory_type == "project-facts":
        path = root_path / "projects" / project_slug / "facts.md"
        section = "Entries"
        scope = "project"
    elif memory_type == "project-decisions":
        path = root_path / "projects" / project_slug / "decisions.md"
        section = "Entries"
        scope = "project"
    elif memory_type == "task":
        if project:
            path = root_path / "projects" / project_slug / "tasks.md"
            scope = "project"
        else:
            path = root_path / "users" / user_slug / "tasks.md"
            scope = "user"
        section = "Entries"
    elif memory_type == "session-summary":
        if project:
            path = root_path / "projects" / project_slug / "sessions" / year / f"{day}.md"
            scope = "project-session"
        else:
            path = root_path / "sessions" / user_slug / year / f"{day}.md"
            scope = "user-session"
        section = "Summary"
    elif memory_type == "ephemeral":
        path = root_path / "inbox" / year / f"{day}.md"
        section = "Entries"
        scope = "inbox"
    else:
        raise ValueError(
            "unsupported memory type: "
            f"{memory_type}. Use one of: profile, preferences, project-facts, "
            "project-decisions, task, session-summary, ephemeral."
        )

    return {
        "root": root,
        "memory_type": memory_type,
        "user_id": user_slug,
        "project_slug": project_slug,
        "scope": scope,
        "path": path.as_posix(),
        "section": section,
        "date": day,
    }


def resolve_route(
    memory_type: str,
    user_id: str = "default-user",
    project: str | None = None,
    date: str | None = None,
    root: str = "memory-router",
) -> dict[str, str]:
    canonical = canonical_memory_type(memory_type)
    when = dt.date.fromisoformat(date) if date else dt.date.today()
    return build_route(root=root, memory_type=canonical, user_id=user_id, project=project, when=when)


def ensure_file(note_path: Path, title: str | None, section: str) -> None:
    note_path.parent.mkdir(parents=True, exist_ok=True)
    if note_path.exists():
        return

    heading = title or note_path.stem.replace("-", " ").replace("_", " ").title()
    content = f"# {heading}\n\n## {section}\n"
    note_path.write_text(content, encoding="utf-8")


def ensure_section(lines: list[str], section: str) -> tuple[list[str], int]:
    header = f"## {section}"
    for idx, line in enumerate(lines):
        if line.strip() == header:
            return lines, idx

    if lines and lines[-1].strip():
        lines.append("")
    lines.append(header)
    lines.append("")
    return lines, len(lines) - 2


def find_section_end(lines: list[str], section_idx: int) -> int:
    for idx in range(section_idx + 1, len(lines)):
        line = lines[idx]
        if line.startswith("## ") and idx != section_idx:
            return idx
    return len(lines)


def normalize_entry(entry: str) -> str:
    return "\n".join(line.rstrip() for line in entry.strip().splitlines()).strip()


def dedupe_signature(entry: str) -> str:
    normalized = normalize_entry(entry)
    if not normalized:
        return normalized

    lines = normalized.splitlines()
    header = lines[0].strip()
    match = ENTRY_HEADER_RE.match(header)
    if not match:
        return normalized

    body = "\n".join(lines[1:]).strip()
    topic = match.group("topic")
    source = match.group("source")
    return f"topic:{topic}\nsource:{source}\n{body}"


def contains_exact_entry(lines: list[str], start: int, end: int, entry: str) -> bool:
    signature = dedupe_signature(entry)
    blocks = iter_entry_blocks(lines, start, end)
    if blocks:
        for block_start, block_end in blocks:
            current = dedupe_signature("\n".join(lines[block_start:block_end]))
            if current == signature:
                return True
        return False

    haystack = dedupe_signature("\n".join(lines[start:end]))
    return signature == haystack


def iter_entry_blocks(lines: list[str], start: int, end: int) -> list[tuple[int, int]]:
    blocks: list[tuple[int, int]] = []
    idx = start
    while idx < end:
        while idx < end and not lines[idx].strip():
            idx += 1
        if idx >= end:
            break

        block_start = idx
        idx += 1
        while idx < end and not (lines[idx].startswith("- ") and ENTRY_HEADER_RE.match(lines[idx].strip())):
            idx += 1
        blocks.append((block_start, idx))

    return blocks


def find_topic_block(
    lines: list[str],
    start: int,
    end: int,
    topic: str,
    source: str,
) -> tuple[int, int] | None:
    for block_start, block_end in iter_entry_blocks(lines, start, end):
        match = ENTRY_HEADER_RE.match(lines[block_start].strip())
        if not match:
            continue
        if match.group("topic") == topic and match.group("source") == source:
            return block_start, block_end
    return None


def replace_entry_block(lines: list[str], block_start: int, block_end: int, entry: str) -> tuple[list[str], bool]:
    normalized = normalize_entry(entry)
    current = normalize_entry("\n".join(lines[block_start:block_end]))
    if current == normalized:
        return lines, False

    replacement = normalized.splitlines()
    replacement.append("")
    updated = lines[:block_start] + replacement + lines[block_end:]
    return updated, True


def insert_entry(lines: list[str], section_idx: int, entry: str) -> tuple[list[str], bool]:
    start = section_idx + 1
    while start < len(lines) and not lines[start].strip():
        start += 1

    end = find_section_end(lines, section_idx)
    normalized = normalize_entry(entry)
    if contains_exact_entry(lines, start, end, normalized):
        return lines, False

    insert_at = end
    block = normalized.splitlines()

    if insert_at > 0 and lines[insert_at - 1].strip():
        lines.insert(insert_at, "")
        insert_at += 1

    for offset, line in enumerate(block):
        lines.insert(insert_at + offset, line)

    lines.insert(insert_at + len(block), "")
    return lines, True


def format_entry(text: str, topic: str, source: str, when: dt.date, created_at: str) -> str:
    entry_lines = [f"- {when.isoformat()} | created_at: {created_at} | topic: {topic} | source: {source}"]
    for line in normalize_text_lines(text):
        entry_lines.append(f"  {line}" if line else "  ")
    return "\n".join(entry_lines)


def upsert_markdown_entry(
    vault_root: str,
    note: str,
    section: str,
    entry: str,
    create_title: str | None = None,
    dedupe_mode: str = "exact",
    topic: str | None = None,
    source: str | None = None,
) -> dict[str, object]:
    note_path = Path(vault_root) / Path(note)
    ensure_file(note_path, create_title, section)

    original = note_path.read_text(encoding="utf-8")
    lines = original.splitlines()
    lines, section_idx = ensure_section(lines, section)

    if dedupe_mode == "none":
        normalized = normalize_entry(entry)
        insert_at = find_section_end(lines, section_idx)
        block = normalized.splitlines()
        if insert_at > 0 and lines[insert_at - 1].strip():
            lines.insert(insert_at, "")
            insert_at += 1
        for offset, line in enumerate(block):
            lines.insert(insert_at + offset, line)
        lines.insert(insert_at + len(block), "")
        changed = True
    elif dedupe_mode == "topic":
        if not topic or not source:
            raise ValueError("topic-aware upsert requires both topic and source.")

        start = section_idx + 1
        while start < len(lines) and not lines[start].strip():
            start += 1

        end = find_section_end(lines, section_idx)
        normalized = normalize_entry(entry)
        if contains_exact_entry(lines, start, end, normalized):
            changed = False
        else:
            block = find_topic_block(lines, start, end, topic=topic, source=source)
            if block is None:
                lines, changed = insert_entry(lines, section_idx, entry)
            else:
                lines, changed = replace_entry_block(lines, block[0], block[1], entry)
    elif dedupe_mode == "exact":
        lines, changed = insert_entry(lines, section_idx, entry)
    else:
        raise ValueError("unsupported dedupe mode. Use one of: none, exact, topic.")

    content = "\n".join(lines).rstrip() + "\n"
    if content != original:
        note_path.write_text(content, encoding="utf-8")

    return {
        "note": note.replace("\\", "/"),
        "path": str(note_path).replace("\\", "/"),
        "section": section,
        "changed": changed,
        "timestamp": dt.datetime.now().astimezone().replace(microsecond=0).isoformat(),
    }


def candidate_dirs(root: Path, memory_type: str | None, user_id: str | None, project: str | None) -> list[Path]:
    user_slug = slugify(user_id, "default-user") if user_id else None
    project_slug = slugify(project, "general") if project else None

    if memory_type == "profile":
        return [root / "users" / (user_slug or "default-user")]
    if memory_type == "preferences":
        return [root / "users" / (user_slug or "default-user")]
    if memory_type == "project-facts":
        return [root / "projects" / (project_slug or "general")]
    if memory_type == "project-decisions":
        return [root / "projects" / (project_slug or "general")]
    if memory_type == "task":
        if project_slug:
            return [root / "projects" / project_slug]
        return [root / "users" / (user_slug or "default-user")]
    if memory_type == "session-summary":
        if project_slug:
            return [root / "projects" / project_slug / "sessions"]
        return [root / "sessions" / (user_slug or "default-user")]
    if memory_type == "ephemeral":
        return [root / "inbox"]

    dirs: list[Path] = []
    if project_slug:
        dirs.append(root / "projects" / project_slug)
    if user_slug:
        dirs.append(root / "users" / user_slug)
        dirs.append(root / "sessions" / user_slug)
    if not dirs:
        dirs.append(root)
    return dirs


def should_scan_file(path: Path, memory_type: str | None, project: str | None) -> bool:
    if memory_type in {"project-facts", "project-decisions"}:
        return "sessions" not in path.parts
    if memory_type == "task" and project:
        return "sessions" not in path.parts
    return True


def search_file(path: Path, pattern: re.Pattern[str]) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    text = path.read_text(encoding="utf-8")
    for lineno, line in enumerate(text.splitlines(), start=1):
        if pattern.search(line):
            results.append(
                {
                    "path": str(path).replace("\\", "/"),
                    "line": lineno,
                    "text": line.strip(),
                }
            )
    return results


def search_markdown_memory(
    vault_root: str,
    query: str,
    memory_type: str | None = None,
    user_id: str | None = None,
    project: str | None = None,
    root: str = "memory-router",
    limit: int = 10,
) -> dict[str, object]:
    root_path = Path(vault_root) / Path(root)
    normalized_query = normalize_query_text(query)
    pattern = re.compile(re.escape(normalized_query), re.IGNORECASE)
    scoped_dirs = candidate_dirs(root_path, memory_type, user_id, project)
    results: list[dict[str, object]] = []
    scanned_files = 0

    for scoped_dir in scoped_dirs:
        if not scoped_dir.exists():
            continue
        for path in scoped_dir.rglob("*.md"):
            if not should_scan_file(path, memory_type=memory_type, project=project):
                continue
            scanned_files += 1
            results.extend(search_file(path, pattern))
            if len(results) >= limit:
                break
        if len(results) >= limit:
            break

    return {
        "query": normalized_query,
        "root": str(root_path).replace("\\", "/"),
        "scoped_dirs": [str(p).replace("\\", "/") for p in scoped_dirs],
        "scanned_files": scanned_files,
        "matches": results[:limit],
    }


def remember_memory(
    vault_root: str,
    memory_type: str,
    text: str,
    user_id: str = "default-user",
    project: str | None = None,
    date: str | None = None,
    root: str = "memory-router",
    topic: str | None = None,
    source: str | None = "chat",
    dedupe_mode: str = "exact",
    created_at: str | None = None,
) -> dict[str, object]:
    resolved_created_at = normalize_created_at(created_at)
    route_date = date or resolved_created_at[:10]
    route = resolve_route(memory_type=memory_type, user_id=user_id, project=project, date=route_date, root=root)
    when = dt.date.fromisoformat(route["date"])
    resolved_topic = normalize_metadata_value(topic)
    resolved_source = normalize_metadata_value(source, default="chat")
    if dedupe_mode == "topic" and not resolved_topic:
        raise ValueError("topic-aware upsert requires a non-empty topic label.")
    if not resolved_source:
        raise ValueError("source cannot be empty.")

    stored_topic = resolved_topic or "general"
    entry = format_entry(
        text=text,
        topic=stored_topic,
        source=resolved_source,
        when=when,
        created_at=resolved_created_at,
    )
    write_result = upsert_markdown_entry(
        vault_root=vault_root,
        note=route["path"],
        section=route["section"],
        entry=entry,
        dedupe_mode=dedupe_mode,
        topic=stored_topic,
        source=resolved_source,
    )
    return {
        "command": "remember",
        "changed": write_result["changed"],
        "route": route,
        "entry": entry,
        "path": write_result["path"],
        "created_at": resolved_created_at,
    }


def recall_memory(
    vault_root: str,
    query: str,
    memory_type: str,
    user_id: str = "default-user",
    project: str | None = None,
    date: str | None = None,
    root: str = "memory-router",
    limit: int = 5,
) -> dict[str, object]:
    route = resolve_route(memory_type=memory_type, user_id=user_id, project=project, date=date, root=root)
    note_path = Path(vault_root) / Path(route["path"])
    matches: list[dict[str, object]] = []
    searched_exact_note = False
    normalized_query = normalize_query_text(query)

    if note_path.exists():
        searched_exact_note = True
        pattern = re.compile(re.escape(normalized_query), re.IGNORECASE)
        for match in search_file(note_path, pattern):
            item = dict(match)
            item["match_source"] = "direct-note"
            matches.append(item)

    if not matches:
        scoped = search_markdown_memory(
            vault_root=vault_root,
            query=normalized_query,
            memory_type=route["memory_type"],
            user_id=route["user_id"],
            project=project,
            root=root,
            limit=limit,
        )
        matches = [dict(match, match_source="scoped-search") for match in scoped["matches"]]
        scanned_files = scoped["scanned_files"]
        scoped_dirs = scoped["scoped_dirs"]
    else:
        scanned_files = 1
        scoped_dirs = [str(note_path.parent).replace("\\", "/")]

    return {
        "command": "recall",
        "route": route,
        "path": str(note_path).replace("\\", "/"),
        "searched_exact_note": searched_exact_note,
        "scoped_dirs": scoped_dirs,
        "scanned_files": scanned_files,
        "matches": matches[:limit],
    }
