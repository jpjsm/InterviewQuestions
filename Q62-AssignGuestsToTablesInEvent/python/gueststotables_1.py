from typing import Dict, List


def AssignGuestsToTables(
    guests: list[str], tables: Dict[str, set[str]], table_capacity: int = 8
) -> List[str]:
    if (
        not isinstance(guests, (list, tuple))
        or not all(isinstance(g, str) for g in guests)
        or not isinstance(tables, dict)
        or not all(isinstance(k, str) for k in tables.keys())
        or not all(isinstance(v, set) for v in tables.values())
    ):
        raise ValueError("One or more arguments are not valid.")

    if len(tables) == 0:
        return guests

    seated_guests = set()
    i = 0
    total_guests = len(guests)

    for table_id in tables.keys():
        # clear table
        tables[table_id] = set()
        j = 0
        while j < table_capacity and i < total_guests:
            if guests[i] in seated_guests:
                # duplicate guest in list, ignoring her/him
                i += 1
                continue

            tables[table_id].add(guests[i])
            j += 1
            i += 1

    return guests[i:] if i < total_guests else []


if __name__ == "__main__":

    tests = [
        (
            (["1", "2", "3", "4", "5", "6", "7", "8", "9"], {"10": {"1"}}),
            ({"10": {"1", "2", "3", "4", "5", "6", "7", "8"}}, ["9"]),
        ),
        (
            (
                ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
                {
                    "10": {"100", "101", "102", "2", "7"},
                    "20": {"200", "201", "203"},
                    "30": {"300"},
                },
            ),
            (
                {
                    "10": {"1", "2", "3", "4", "5", "6", "7", "8"},
                    "20": {"9"},
                    "30": set(),
                },
                [],
            ),
        ),
    ]

    for (guests, tables), (tables_expected, overflow_expected) in tests:
        overflow_actual = AssignGuestsToTables(guests, tables)
        if set(overflow_actual) != set(overflow_expected) or tables != tables_expected:
            if set(overflow_actual) != set(overflow_expected):
                print(
                    f"[Overflow ERROR] actual  {overflow_actual} "
                    f"{'!=' if set(overflow_actual) != set(overflow_expected) else '=='} {overflow_expected} expected."
                )
            if tables != tables_expected:
                print(
                    f"[Tables ERROR] actual {tables} {'!=' if tables != tables_expected else '=='} {tables_expected} expected."
                )

    print("Tests completed")
