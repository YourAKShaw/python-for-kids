# NOTES

- **floor** and **ceil** are two bounds _(upper and lower)_ of a number with a decimal point.
  - For example, if a number is `3.333`, then it's **floor** value is `3` _(lower bound)_ and it's **ceil** value is `4` _(upper bound)_.
  - In case the number is `-3.333`, then it's **floor** value is `-4` _(lower bound)_ and it's **ceil** value is `-3` _(upper bound)_.
- `a % b` is evaluated as `a - (b * (a // b))`
  - The above statement can easily be understood in terms of the formula for finding remainder on division
  - We can state `a` as the **dividend**, `b` as the **divisor** and `a // b` as the **quotient**.
- Since `True` is `1` and `False` is `0`, they can be added.
  ```py
  a = True + True   # stores 2
  b = True + False  # stores 1
  ```
