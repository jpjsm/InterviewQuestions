from __future__ import annotations  # Enables forward references without quotes

from sys import maxsize
from typing import Any, Optional, TypeVar, Generic
from link import Link

T = TypeVar("T")


class LinkList(Generic[T]):
    def __init__(self, list: Link[T], next: Optional["LinkList[T]"] = None):
        self.List: Link[T] = list
        self.Next: LinkList | None = next

    @staticmethod
    def Zip(list: LinkList[Link[T]]) -> LinkList[T] | None:
        # extract pointers to each sub-list in list
        l = list
        pointers: Link[Any] = Link()
        p = pointers
        while l:
            p.Value = l.List
            p.Next = Link() if l.List else None
            p = p.Next
            l = l.Next

        nils = False
        results: LinkList[T] = LinkList(Link())
        r = results
        p = pointers
        # Iterate over list-pointers
        # Until one of the lists runs out of elements ( nils <- True)
        lk = Link()
        while not nils:
            lkn = lk
            while p and p.Next:
                lkn.Value = p.Value.Value
                lkn.Next = Link() if p.Next.Value else None
                lkn = lkn.Next
                p.Value = p.Value.Next
                if p.Value is None:
                    nils = True

                p = p.Next

            r.List = lk
            if nils:
                break
            lk = Link()
            r.Next = LinkList(lk)
            r = r.Next
            p = pointers

        return results

    @staticmethod
    def Zip2(list: LinkList[Link[T]]) -> LinkList[T] | None:
        rows = []
        lk = list
        min_row = maxsize
        while lk:
            r = []
            l = lk.List
            length = 0
            while l:
                r.append(l.Value)
                l = l.Next
                length += 1

            if min_row > length:
                min_row = length

            rows.append(r)
            lk = lk.Next

        zips = []
        for col in range(min_row):
            z = []
            for r in range(len(rows)):
                z.append(rows[r][col])

            zips.append(z)

        if len(zips) == 0:
            return None

        results = LinkList(Link())
        r = results
        for i in range(len(zips)):
            lk = Link()
            lkn = lk
            for j in range(min_row):
                lkn.Value = zips[i][j]
                lkn.Next = Link() if (j + 1) < min_row else None
                lkn = lkn.Next

            r.List = lk
            r.Next = LinkList(Link()) if (i + 1) < len(zips) else None
            r = r.Next

        return results

    @staticmethod
    def Zip3(list_of_lists: "LinkList[Link[T]]") -> Optional["LinkList[T]"]:
        # Step 1: Collect heads of each sublist
        heads: list[Link[T]] = []
        node = list_of_lists
        while node:
            heads.append(node.List)
            node = node.Next

        # Step 2: Build the zipped rows
        result_head: Optional[LinkList[T]] = None
        result_tail: Optional[LinkList[T]] = None

        while True:
            row_head: Optional[Link[T]] = None
            row_tail: Optional[Link[T]] = None

            # Build one row by taking one element from each list
            for i, h in enumerate(heads):
                if h is None:
                    return result_head  # stop when any list runs out

                new_node = Link(h.Value)

                if row_head is None:
                    row_head = row_tail = new_node
                else:
                    row_tail.Next = new_node
                    row_tail = new_node

                heads[i] = h.Next  # advance pointer

            # Wrap the row in a LinkList node
            new_row_list = LinkList(row_head)

            if result_head is None:
                result_head = result_tail = new_row_list
            else:
                result_tail.Next = new_row_list
                result_tail = new_row_list


if __name__ == "__main__":
    l1 = Link(1, Link(2, Link(3, Link(4))))
    lA = Link("A", Link("B", Link("C")))
    la = Link("a", Link("b", Link("c", Link("d"))))
    linkslist = LinkList(l1, LinkList(lA, LinkList(la)))

    print("=" * 40, "Original LinkList", "=" * 40)
    r = linkslist
    while r:
        l = r.List
        print("[ ", end="")
        while l:
            print(f"{l.Value}, ", end="")
            l = l.Next

        print("]")
        r = r.Next

    print("=" * 40, "Zip 1 Results", "=" * 40)
    r = LinkList.Zip(linkslist)
    while r:
        l = r.List
        print("[ ", end="")
        while l:
            print(f"{l.Value}, ", end="")
            l = l.Next

        print("]")
        r = r.Next

    print("=" * 40, "Original LinkList", "=" * 40)
    r = linkslist
    while r:
        l = r.List
        print("[ ", end="")
        while l:
            print(f"{l.Value}, ", end="")
            l = l.Next

        print("]")
        r = r.Next

    print("=" * 40, "Zip 2 Results", "=" * 40)
    r = LinkList.Zip2(linkslist)
    while r:
        l = r.List
        print("[ ", end="")
        while l:
            print(f"{l.Value}, ", end="")
            l = l.Next

        print("]")
        r = r.Next

    print("=" * 40, "Original LinkList", "=" * 40)
    r = linkslist
    while r:
        l = r.List
        print("[ ", end="")
        while l:
            print(f"{l.Value}, ", end="")
            l = l.Next

        print("]")
        r = r.Next

    print("=" * 40, "Zip 3 Results", "=" * 40)
    r = LinkList.Zip3(linkslist)
    while r:
        l = r.List
        print("[ ", end="")
        while l:
            print(f"{l.Value}, ", end="")
            l = l.Next

        print("]")
        r = r.Next

    print("=" * 40, "Original LinkList", "=" * 40)
    r = linkslist
    while r:
        l = r.List
        print("[ ", end="")
        while l:
            print(f"{l.Value}, ", end="")
            l = l.Next

        print("]")
        r = r.Next
