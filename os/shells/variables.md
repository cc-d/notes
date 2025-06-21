# Variables

## String Variables:
String variables store textual data. Assign a value to a string variable using the `=` operator with quotes (single or double).

```sh
name="John"
```

## Numeric Variables:
 Numeric variables hold numerical values. Assign a value to a numeric variable using the `=` operator without quotes.

```sh
count=10
```

## Array Variables:
 In the "sh" shell, arrays are not directly supported. However, you can simulate arrays using positional parameters (`$1`, `$2`, etc.) or the `set` command.

```sh
set -- value1 value2 value3
echo "First value: $1"   # Output: First value: value1
echo "Second value: $2"  # Output: Second value: value2
echo "Third value: $3"   # Output: Third value: value3
```

## Local Variables:
 Local variables are specific to a shell function or script. Declare a local variable using the `local` keyword.

```sh
local var="value"
```

## Special Variables:
 Special variables have predefined meanings in the "sh" shell.

- `$0`: The name of the shell or script.
- `$1`, `$2`, etc.: The positional parameters or command-line arguments.
- `$#`: The number of command-line arguments.
- `$?`: The exit status of the last executed command.
- `$$`: The process ID of the current shell.
- `$!`: The process ID of the last background command.

```sh
echo "Script name: $0"       # Output: Script name: script.sh
echo "First argument: $1"    # Output: First argument: argument1
echo "Number of arguments: $#"  # Output: Number of arguments: 3
```

## Environment Variables:
 Environment variables store information about the environment. They are usually uppercase and accessed using the `$` prefix.

```sh
echo "$PATH"  # Output: /usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin
echo "$HOME"  # Output: /home/username
```

### see also: [environment variables expanded](shells/envvars.md)