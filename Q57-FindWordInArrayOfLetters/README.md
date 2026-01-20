# Find `word` in rectangular array of letters

Given rectangular shaped array of letters, find if a given `word` exists in the
array. The letters in the array are connected when they are either above, or
below, or to the left, or to the right of one letter; diagonal proximity is not
allowed. Cell letters can only be used once.

For example, given the following array:

```txt
R P L I S C T K G A R Y H F U G Y Y Y R E K K J A Y B V A O
A U H Q Z G J J A S H J L B V E D B K V Z X K W A X D Q A Y
P E O V S O Y H J K R T M J L N I N R V P O F V Y L V O H O
S G O B Y H J E A G Z O T D Y K T W F V N N E X A J S Q A A
E G Z V H V T B B P R O R T O L R J W T V C Y B X K S L B P
G S O A W V V E Z L D D D U B T I Y N F O U K G Z U H J W B
X Y K I D X X E M B H F J Q A J K D X Z C W E Z C F Y O K B
X D P Y S A I X L V G Z L N K S G H U J Q F M J Y O W E T L
W C R M Z R H G D W H H W Y V F G Z U A D M V V E Y W P S O
R A S F M T M V C E G D L Z G V G Q X G R J J L H B G L Z N
S B P N M I G T N R T R A E O T R R P T S P W W R U J E Y T
D D Q K D A G T P T J X X G P U R B W P E T U X X P I Z F B
Y W I M W W T U Y F X I H J L R Z S C I E T V U S P K A X Y
K Y O D U A Z Y J A E P D M Q I I B I L X Z F X T J H F N Z
Y W B X Q I A I W B E T N A B Y G Z S M Q X P D B N F Z H S
```

Verify the following keywords:

- Are IN the array    : `and`, `as`, `await`, `in`, `is`, `or`
- Are NOT in the array: `False`, `None`, `True`, `assert`, `async`, `break`,
`class`, `continue`, `def`, `del`, `elif`, `else`, `except`, `finally`, `for`,
`from`, `global`, `if`, `import`, `lambda`, `nonlocal`, `not`, `pass`, `raise`,
`return`, `try`, `while`, `with`, `yield`
