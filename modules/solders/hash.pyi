from typing import ClassVar

class Hash:
    LENGTH: ClassVar[int]
    def __init__(self, hash_bytes: bytes) -> None: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    @staticmethod
    def from_string(s: str) -> "Hash": ...
    @staticmethod
    def new_unique() -> "Hash": ...
    @staticmethod
    def default() -> "Hash": ...
    def __bytes__(self) -> bytes: ...
    def __richcmp__(self, other: "Hash", op: int) -> bool: ...
    @staticmethod
    def hash(val: bytes) -> "Hash": ...
    def __hash__(self) -> int: ...
    @staticmethod
    def from_bytes(raw_bytes: bytes) -> "Hash": ...
    def to_json(self) -> str: ...
    @staticmethod
    def from_json(raw: str) -> "Hash": ...

class ParseHashError(Exception): ...