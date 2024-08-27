import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel


class PluginArch(Enum):
    AMD64 = "amd64"
    ARM64 = "arm64"


class PluginLanguage(Enum):
    PYTHON = "python"


class PluginType(Enum):
    Plugin = "plugin"


class PluginResourceRequirements(BaseModel):
    memory: int
    storage: int

    class Permission(BaseModel):
        class Tool(BaseModel):
            enabled: bool

        class Model(BaseModel):
            enabled: Optional[bool]
            llm: Optional[bool]
            text_embedding: Optional[bool]
            rerank: Optional[bool]
            tts: Optional[bool]
            speech2text: Optional[bool]
            moderation: Optional[bool]

        class Node(BaseModel):
            enabled: bool

        class Endpoint(BaseModel):
            enabled: bool

        tool: Optional[Tool]
        model: Optional[Model]
        node: Optional[Node]
        endpoint: Optional[Endpoint]

    permission: Permission


class PluginConfiguration(BaseModel):
    class Meta(BaseModel):
        class PluginRunner(BaseModel):
            language: PluginLanguage
            version: str
            entrypoint: str

        version: str
        arch: list[PluginArch]
        runner: PluginRunner

    version: str
    type: PluginType
    author: str
    name: str
    created_at: datetime.datetime
    resource: dict
    plugins: list[str]
    meta: Meta


class PluginProviderType(Enum):
    Tool = "tool"
    Model = "model"
    Endpoint = "endpoint"
