# ArithExpressionEvaluator

## Prefix notation

You get as input a single string (of characters, text) containing an expression
that has the following format:

- It is enclosed in parentheses;
- These contain an operator, either '+' or '*';
- Which is followed by two (no more and no less) operands,
  each of which is either an integer or another expression in the same format.
- Evaluate the expression:
  - The value of an expression is the sum of the values of the two operands if
  its operator is a '+' character;
  - on the other hand, when the operator is a '*' character, the value is the
  product of the two operands.
  - The value of an integer is the integer itself.

Note:
Each pair of parentheses contain exactly one operator and two operands;
parentheses determine order of precedence.

For example: "( \* 2 ( + 3 4 ) )" evaluates to 14 [ via 3+4=7, 2*7=14 ].
