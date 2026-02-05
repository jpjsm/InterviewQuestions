import json
from math import log10, trunc
from typing import Dict, List

from aboutprimenumbers import is_prime, prime_ceiling, prime_floor

if __name__ == "__main__":
    with open("First100KTwinsLowerOnly.json", "r", encoding="utf-8") as twins_in:
        twins_lower = json.load(twins_in)

    range_length = 5
    composites_by_size: Dict[int, List[int]] = {}

    for lower_twin in twins_lower:
        composite = lower_twin * (lower_twin + 2)
        composite_length = trunc(log10(composite))
        if composite_length not in composites_by_size:
            composites_by_size[composite_length] = []

        if len(composites_by_size[composite_length]) < range_length:
            composites_by_size[composite_length].append(composite)

    composites = []
    for r in composites_by_size.values():
        composites += r
    with open("TestComposites.json", "w", encoding="utf-8") as composites_out:
        json.dump(composites, composites_out)

    floor_ceiling_tests = []
    is_prime_tests = []
    for composite in composites:
        for sign in [-1, 1]:
            signed_composite = sign * composite
            composite_floor = prime_floor(signed_composite)
            composite_ceiling = prime_ceiling(signed_composite)
            floor_ceiling_tests.append(
                (composite_floor, signed_composite, composite_ceiling)
            )
            is_prime_tests += [
                (composite_floor, True),
                (signed_composite, False),
                (composite_ceiling, True),
            ]

    print(f"{floor_ceiling_tests=}")
    print(f"{is_prime_tests=}")
