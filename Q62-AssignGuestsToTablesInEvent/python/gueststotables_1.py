from typing import Dict, List


def AssignGuestsToTables(
    guests: list[str], tables: Dict[str, List[str]], table_capacity: int = 8
) -> List[str]:
    if (
        not isinstance(guests, (list, tuple))
        or not all(isinstance(g, str) for g in guests)
        or not isinstance(tables, dict)
        or not all(isinstance(k, str) for k in tables.keys())
        or not all(isinstance(v, list) for v in tables.values())
    ):
        raise ValueError("One or more arguments are not valid.")

    if len(tables) == 0:
        return guests

    seated_guests = set()
    i = 0
    total_guests = len(guests)

    for table_id in tables.keys():
        # clear table
        tables[table_id] = []
        j = 0
        while j < table_capacity and i < total_guests:
            if guests[i] in seated_guests:
                # duplicate guest in list, ignoring her/him
                i += 1
                continue

            tables[table_id].append(guests[i])
            j += 1
            i += 1

    return guests[i:] if i < total_guests else []
