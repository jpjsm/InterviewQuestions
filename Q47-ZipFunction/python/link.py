from __future__ import annotations  # Enables forward references without quotes
from typing import Any, Optional, TypeVar, Generic

T = TypeVar("T")


class Link(Generic[T]):
    def __init__(self, item: Optional[T] = None, next: Optional["Link[T]"] = None):
        self.Value: T | None = item
        self.Next: Link[T] | None = next
