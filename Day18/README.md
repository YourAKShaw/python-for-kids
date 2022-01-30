# NOTES

### Precedence and Associativity

- When multiple operators are used in an expression, the evaluation of that expression is done on the basis of precedence (priority) of the operators used.
- Operators in decreasing order of their priority (PEMDAS):
  - `()` ...# Parentheses
  - `**` ...# Exponentiation
  - `*`, `/`, `//`, `%` ...# Multiplication, Division
  - `+`, `-` ...# Addition, Subtraction
- If there is a tie between operators of the same precedence, it is settled using associativity of operators.
- Each operator has either left to right associativity or right to left associativity.
- In expression `c = a * b / c`, `*` is done before `/` since arithmetic operators have left to right associativity.
