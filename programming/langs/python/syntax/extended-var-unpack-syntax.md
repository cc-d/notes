As detailed in [PEP 3132](https://peps.python.org/pep-3132/) python allows for the following syntax to be used during variable assignment:

```
>>> a, *c, d = range(-20, 50, 3)
>>> a
-20
>>> c
[-17, -14, -11, -8, -5, -2, 1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46]
>>> d
49
```