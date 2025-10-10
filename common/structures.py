from dataclasses import dataclass, field
from typing import Any


@dataclass
class DayInput:
    raw: str
    processed: Any


@dataclass
class GenericList[T]:
    items: list[T] = field(default_factory=list)

    def __iter__(self):
        for item in self.items:
            yield item

    def add(self, item: T):
        self.items.append(item)
