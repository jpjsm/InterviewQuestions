from __future__ import annotations
from collections import OrderedDict
from typing import Any, List, Optional, Tuple


class DLink:
    def __init__(
        self, value: Any, previous: Optional[DLink] = None, next: Optional[DLink] = None
    ):
        if previous is not None and not isinstance(previous, DLink):
            raise ValueError("'previous' must be a DLink type object")

        if next is not None and not isinstance(next, DLink):
            raise ValueError("'next' must be a DLink type object")

        self.Value = value
        self.Previous = previous
        self.Next = next


class LRU_JP:
    def __init__(self, max_capacity: int, not_found_signal: Any = None):
        self.Max_Capacity = max_capacity
        self.Not_Found_Signal = not_found_signal
        self._head = DLink(None)
        self._tail = DLink(None)
        self._dict = {}

    @property
    def Size(self) -> int:
        return len(self._dict)

    @property
    def IsEmpty(self) -> bool:
        return self.Size == 0

    def Put(self, key: Any, value: Any):
        def push(item: DLink, key: Any):
            old_last = self._tail.Previous

            old_last.Next = item
            item.Previous = old_last

            item.Next = self._tail
            self._tail.Previous = item
            self._dict[key] = item

        item = DLink({"key": key, "value": value})
        if self.IsEmpty:
            # Initial case
            item.Previous = self._head
            item.Next = self._tail

            self._head.Next = item
            self._tail.Previous = item

            self._dict[key] = item

        elif self.Size < self.Max_Capacity:
            # There's room to add new (key, value) item
            push(item, key)
        else:
            # We have exceeded Max_Capacity
            # Let's remove the first item
            old_first = self._head.Next
            second = old_first.Next

            item.Previous = self._head
            self._head = item

            item.Next = second
            second.Previous = item.Next
            old_first_key = old_first.Value["key"]
            self._dict.pop(old_first_key)
            push(item)

    def Move_End(self, key: Any):
        if key not in self._dict:
            return  # Let's do nothing if key is not in cache

        item = self._dict[key]
        item_previous = item.Previous
        item_next = item.Next

        old_last = self._tail.Previous

        # Let's connect item_previous to item_next
        item_previous.Next = item_next
        item_next.Previous = item_previous

        # let's insert item in last position
        old_last.Next = item

        item.Previous = old_last
        self._tail.Previous = item
        item.Next = self._tail

    def Get(self, key: Any) -> Any:
        if key in self._dict:
            self.Move_End(key)
            return self._dict[key].Value["key"]
        return self.Not_Found_Signal

    def ToList(self) -> List[Tuple[Any, Any]]:
        results = []
        item = self._head.Next
        while item and item.Value:
            results.append((item.Value["key"], item.Value["value"]))
            item = item.Next

        return results


class LRU_Python:
    def __init__(self, max_capacity: int, not_found_signal: Any = None):
        self.Max_Capacity: int = max_capacity
        self.Not_Found_Signal: Any = not_found_signal
        self._lru: OrderedDict[Any, Any] = OrderedDict()

    def Get(self, key: Any) -> Any:
        if key not in self._lru:
            return self.Not_Found_Signal

        self._lru.move_to_end(key)
        return self._lru[key]

    def Put(self, key: Any, value: Any) -> None:
        if len(self._lru) >= self.Max_Capacity:
            self._lru.popitem(last=True)

        self._lru[key] = value

    def ToList(self) -> List[Tuple[Any, Any]]:
        results = []
        for k, v in self._lru.items():
            results.append((k, v))
        return results


if __name__ == "__main__":
    lru_jp = LRU_JP(15)
    print(lru_jp.Size)
    print(lru_jp.IsEmpty)

    lru_python = LRU_Python(15)
    kvps = [(chr(ord("A") + i), i + 1) for i in range(15)]
    print(kvps)
    for k, v in kvps:
        lru_jp.Put(k, v)
        lru_python.Put(k, v)

    print(lru_jp.ToList())
    print(lru_python.ToList())
    usage = ["M", "K", "G", "E", "C", "B"]
    print(f"usage: {usage}")
    for u in usage:
        print(f"lru_jp.Get({u}): {lru_jp.Get(u)}")
        print(f"lru_python.Get({u}): {lru_python.Get(u)}")

    print(lru_jp.ToList())
    print(lru_python.ToList())
