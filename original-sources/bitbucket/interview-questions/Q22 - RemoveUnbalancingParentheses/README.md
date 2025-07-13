# Q22 - Remove Unbalancing Parentheses

Given a string _s_ which has '(', ')', and letters. 
Can you find the minimum number of removals to make it valid (aka the parentheses are balanced)?

For example:
| Input | ¦ |  Output |
| :---: | :---: | :---: |
| `hi,(H(e)l)lo)` | ¦ | `hi,(H(e)l)lo` |
| `hi,(((( Hello` | ¦ | `hi, Hello` |
| `hi, Hello)))` | ¦ | `hi, Hello` |
| `(h(i,)) (H)(e)((l(l(o))))` | ¦ | `(h(i,)) (H)(e)((l(l(o))))` |
| `hi, (H)(e)((l)((l)o` | ¦ | `hi, (H)(e)((ll))o` ∧ `hi, (H)(e)(l)(l)o` 
