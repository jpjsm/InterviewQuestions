# Find Key in Segments Combinations

Combine the items in the segments list, in pairs, to see if the key is contained
in any of those combinations; and return the combinations where the key is
found.

For example:

List: [ "12", "123", "312", "1412", "012", "4321"]

Key: "1212"

Answer:

```txt
[
    (0, 1, "12123"),
    (2, 0, "31212"),
    (2, 1, "312123"),
    (3, 0, "141212"),
    (3, 1, "1412123"),
    (4, 0, "01212"),
    (4, 1, "012123"),
]
```
