# Closest value to target in tree

Given a binary tree find the closest value to target.

Example:

```txt
               |
              31
            /    \
          17      61
         /  \     /  \ 
        7    29  47   89
         \   /       /  \
         13 23     71    97
```

if target =  31 ; return 31
if target =   5 ; return  7
if target = 106 ; return 97
if target =  30 ; return 31 or 29
if target =  26 ; return 23 or 29
