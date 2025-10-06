"""Tool input/output models for Mix agent tools.

This module provides Pydantic models for interacting with Mix agent tools.
These models provide type safety, validation, and IDE autocomplete support.

Example:
    from mix_python_sdk.tool_models import MediaOutput, MediaType

    output = MediaOutput(
        path="http://localhost:8088/files/video.mp4",
        type=MediaType.VIDEO,
        title="Analysis Results",
        description="Portfolio performance analysis"
    )
"""

from enum import Enum
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field


# ===== Core Tool Names =====

class CoreToolName(str, Enum):
    """Core built-in tool names."""
    BASH = "bash"
    READ_TEXT = "ReadText"
    GLOB = "glob"
    READ_MEDIA = "ReadMedia"
    GREP = "grep"
    WRITE = "write"
    EDIT = "edit"
    PYTHON_EXECUTION = "python_execution"
    SEARCH = "search"
    TODO_WRITE = "todo_write"
    EXIT_PLAN_MODE = "exit_plan_mode"
    SHOW_MEDIA = "show_media"
    TASK = "task"


# ===== show_media Tool =====

class MediaType(str, Enum):
    """Supported media types for show_media tool."""
    IMAGE = "image"
    VIDEO = "video"
    AUDIO = "audio"
    GSAP_ANIMATION = "gsap_animation"
    PDF = "pdf"
    CSV = "csv"


class MediaOutput(BaseModel):
    """Single media output for show_media tool.

    Attributes:
        path: Absolute path or URL to the media file (required except for gsap_animation)
        type: Type of media (image, video, audio, gsap_animation, pdf, csv)
        title: Title or name for the media output
        description: Optional description or context
        config: Configuration data for gsap_animation type (JSON object with animation settings)
        start_time: Optional start time in seconds for video/audio segments
        duration: Optional duration in seconds for video/audio segments
    """
    path: Optional[str] = None
    type: MediaType
    title: str
    description: Optional[str] = None
    config: Optional[Dict[str, Any]] = None
    start_time: Optional[int] = Field(None, alias="startTime", ge=0)
    duration: Optional[int] = Field(None, ge=1)

    class Config:
        populate_by_name = True  # Allow both snake_case and camelCase


class MediaShowcaseParams(BaseModel):
    """Parameters for show_media tool.

    Attributes:
        outputs: Array of media outputs to showcase
    """
    outputs: List[MediaOutput]


# ===== ReadMedia Tool =====

class MediaAnalysisType(str, Enum):
    """Supported media types for ReadMedia tool."""
    IMAGE = "image"
    AUDIO = "audio"
    VIDEO = "video"
    PDF = "pdf"


class ReadMediaParams(BaseModel):
    """Parameters for ReadMedia tool.

    Attributes:
        file_path: Path to file or URL for analysis
        media_type: Type of media analysis to perform
        prompt: Analysis prompt for the media content
        pdf_pages: PDF page selection (e.g., '5' or '1-3,7,10-12') - PDF only
        video_interval: Video time interval (e.g., '00:20:50-00:26:10') - video only
    """
    file_path: str
    media_type: MediaAnalysisType
    prompt: str
    pdf_pages: Optional[str] = None
    video_interval: Optional[str] = None


class ReadMediaResult(BaseModel):
    """Single result from ReadMedia tool.

    Attributes:
        file_path: Path to the analyzed file
        media_type: Type of media that was analyzed
        analysis: Analysis results from the AI
        error: Error message if analysis failed
    """
    file_path: str
    media_type: str
    analysis: str
    error: Optional[str] = None


class ReadMediaResponse(BaseModel):
    """Response from ReadMedia tool.

    Attributes:
        results: List of analysis results
        summary: Overall summary of the analysis
    """
    results: List[ReadMediaResult]
    summary: str


# ===== TodoWrite Tool =====

class TodoStatus(str, Enum):
    """Todo item status."""
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"


class TodoPriority(str, Enum):
    """Todo item priority."""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class Todo(BaseModel):
    """Single todo item.

    Attributes:
        id: Unique identifier for the todo item
        content: The todo task description
        status: Current status (pending, in_progress, completed)
        priority: Priority level (low, medium, high)
    """
    id: str
    content: str
    status: TodoStatus
    priority: TodoPriority


class TodoWriteParams(BaseModel):
    """Parameters for TodoWrite tool.

    Attributes:
        todos: Array of todo items to manage
    """
    todos: List[Todo]
