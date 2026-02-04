# Short URL generator

People want to store short strings (less than 2048 chars) and access them with
a short URL.

How would you generate those strings?

What would you change in your design if the number of different URLs to store
is less than:

| Different URLs |
| --: |
| `65,536` |
| `16,777,216` |
| `4,294,967,296` |
| `1,099,511,627,776` |
| `281,474,976,710,656` |
| `72,057,594,037,927,900` |
| `18,446,744,073,709,600,000` |

How would you generate those URLs if there's a maximum number of chars to
generate the URL and an expected maximum number of URLs?

| Different URLs | Max Chars |
| --: | --: |
| `65,536` | `4` |
| `16,777,216` | `5` |
| `4,294,967,296` | `6` |
| `1,099,511,627,776` | `7` |
| `281,474,976,710,656` | `9` |
| `72,057,594,037,927,900` | `10` |
| `18,446,744,073,709,600,000` | `11` |
