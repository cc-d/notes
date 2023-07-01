
# Operator Guide

## Arithmetic Operators

Addition (`+`), subtraction (`-`), multiplication (`*`), division (`/`), modulus (`%`)

```bash
a=10; b=5
echo $((a + b))  # 15
echo $((a - b))  # 5
echo $((a * b))  # 50
echo $((a / b))  # 2
echo $((a % b))  # 0
```

## Array Operators

Assignment (`=`), Index Access (`[]`)

```bash
arr=(1 2 3 4 5)
echo ${arr[0]}  # 1
```

## Assignment Operator

Assignment (`=`)

```bash
a=10
echo $a  # 10
```

## Bitwise Operators

Bitwise AND (`&`), OR (`|`), XOR (`^`), left shift (`<<`), right shift (`>>`)

```bash
a=60; b=13
echo $((a & b))  # 12
echo $((a | b))  # 61
echo $((a ^ b))  # 49
echo $((a << 2))  # 240
echo $((a >> 2))  # 15
```

## Command Substitution

```bash
echo "Today is $(date)"  # Today is Fri Jun 30 13:30:10 PDT 2023
echo "Today is `date`"  # Same as above
```

## Comparison Operators

Equality (`-eq`), greater than or equal (`-ge`), greater than (`-gt`), less than or equal (`-le`), less than (`-lt`), not equal (`-ne`)

```bash
a=10; b=20
[ $a -eq $b ] && echo "Equal" || echo "Not Equal"  # Not Equal
```

## Conditional Operator

```bash
a=10; b=20
echo $(( a > b ? a : b ))  # 20
```

## Default Value Operator

```bash
default="default value"
echo ${var:-$default}  # default value
```

## File Operators

File exists (`-e`), file is directory (`-d`), file is regular file (`-f`), file is readable (`-r`), file has size greater than zero (`-s`), file is writable (`-w`), file is executable (`-x`)

```bash
file="/etc/passwd"
[ -e $file ] && echo "Exists" || echo "Not Exists"  # Exists
```

## Grouping Operators

```bash
a=10; b=20; c=30
echo $(( (a + b) * c ))  # 900
```

## Increment/Decrement Operators

```bash
a=10
echo $((a++))  # 10
echo $((a--))  # 11
```

## Logical Operators

NOT (`!`), AND (`&&`), OR (`||`)

```bash
a=10; b=20
[ $a -eq 10 ] && echo "Equal" || echo "Not Equal"  # Equal
```

## Redirection Operators

```bash
echo "Hello" > file.txt  # Writes "Hello" to file.txt
echo "World" >> file.txt  # Appends "World" to file

.txt
command 2> error.log  # Redirects stderr to error.log
command > output.log 2>&1  # Redirects both stdout and stderr to output.log
command >/dev/null 2>&1  # Discards both stdout and stderr
```

## String Comparison Operators

```bash
str1="Hello"; str2="World"
[ $str1 = $str2 ] && echo "Equal" || echo "Not Equal"  # Not Equal
[ $str1 != $str2 ] && echo "Not Equal" || echo "Equal"  # Not Equal
```

## String Operators

Concatenation (`+`), Length (`${#var}`)

```bash
str1="Hello"; str2="World"
echo ${str1}${str2}  # HelloWorld
echo ${#str1}  # 5
```

## Substring Extraction

```bash
str="Hello World"
echo ${str:6:5}  # World
```

## Substring Replacement

```bash
str="Hello World"
echo ${str/World/Everyone}  # Hello Everyone
```

## Variable Substitution

```bash
var="Hello"
echo ${var}  # Hello
```

