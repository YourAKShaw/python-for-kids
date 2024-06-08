# Notes

### Identifiers and keywords

- Python is a case sensitive language.
- You can print a list of Python keywords through the statements:

    ```python
    import keyword
    print(keyword.kwlist)
    ```

### Python Types

- Python supports 3 categories of data types:
    
    Basic types - int, float, complex, bool, string, bytes

    Container types - list, tuple, set, dict
    
    User-defined types - class
    
- Type of particular data can be checked using a function called `type()` as shown below:

    ```python
    print(type(35))     # prints <class 'int'>
    print(type(3.14))   # prints <class 'float'>
    ```

### Variable Type and Assignment

- There is no need to define type of a variable.
- Type of a function can be checked using the built-in function `type()`.
- Simple variable assignment:

    ```python
    a = 10
    pi = 3.14
    name = 'Sanjay'
    ```

- Multiple variable assignment:

    ```python
    a = 10; pi = 31.4; name = 'Sanjay' # use ; as statement separator
    a, pi, name = 10, 3.14, 'Sanjay'
    a = b = c = d = 5
    ```

### Arithmetic Operators

- Arithmetic operators: `+ - * / % // **`
- ***In-place assignment*** operators offer a good shortcut for arithmetic operations. These include `+= -= *= /= %= //= **=`.

    ```python
    a**=3 # same as a = a ** 3
    b%=10 # same as b = b % 10
    a+=1 # same as a = a + 1
    ```

### Side Notes

- On a daily basis, humans rely on the decimal number system. 
    > The decimal number system comprises of numerics containing the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9.
- `3.5e2` means `3.5 * 10 ^ 2` [NOTE: `e` and `E` are equivalent.]
- `bool` type can take any of the two Boolean values both starting in caps: `True` or `False`.
- `int` can be of any arbitrary size.

