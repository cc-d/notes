# Environment Variables

Environment variables are dynamically-named values that can affect the way running processes will behave. They are part of the environment in which a process runs.

## Displaying Environment Variables

You can display the value of an environment variable using the `echo` command and the variable name, prefixed with a `$`.

```sh
echo "$HOME"  # Output: /home/username
echo "$PATH"  # Output: /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
```

## Setting Environment Variables

You can set the value of an environment variable using the `export` command.

```sh
export VARNAME=value
```

## Unsetting Environment Variables


```sh
unset VARNAME
```

## Listing All Environment Variables


```sh
env; echo 'or'; printenv
```

## Local vs Global Environment Variables


### **Local Variables:**

```sh
name="John"
count=10

# Usage within the current shell or script
echo "Name: $name"     # Output: Name: John
echo "Count: $count"   # Output: Count: 10
```

Local variables are limited to the current shell or script and can be used for temporary or intermediate data.

### **Global (Environment) Variables:**

```sh
export PATH="/usr/local/bin:$PATH"
export JAVA_HOME="/usr/lib/jvm/java-11"

# Usage in child processes or other shells
echo "$PATH"           # Output: /usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin
echo "$JAVA_HOME"      # Output: /usr/lib/jvm/java-11
```

**Global** (environment) variables are accessible to all shells and child processes. They are commonly used for storing configuration settings or providing information to other processes.

Note that to make a variable global, the `export` command is used along with the assignment. The exported variables can then be accessed in child processes or other shells.

Understanding the distinction between **local** and **global** variables helps manage data effectively and tailor their usage based on specific needs within the "sh" shell.


## Environment Variable Persistence

To make environment variables persistent, they can be set in shell initialization files such as `~/.bashrc`, `~/.bash_profile`, or `~/.profile`.

```sh
# Inside ~/.bashrc
export VARNAME=value
```

These will be loaded each time a new shell is started. For the changes to take effect immediately, you can source the file:

```sh
source ~/.bashrc
```

## Environment Variables in Subprocesses

Child processes inherit the environment variables of their parent process.

```sh
#!/bin/bash
export VAR="Hello, World!"
bash -c 'echo $VAR'
```

This script exports `VAR` and then starts a new bash shell that has access to this new environment variable.

## Special Environment Variables

There are several special environment variables that have predetermined meanings:

- `$HOME`: The current user's home directory.
- `$PATH`: A colon-separated list of directories in which the shell looks for commands.
- `$PS1`: The primary prompt string.
- `$PS2`: The secondary prompt string.
- `$PWD`: The current working directory.
- `$RANDOM`: A random integer between 0 and 32767.
- `$UID`: The numeric, real user ID of the current user.
- `$USER`: The username of the current user.
- `$HOSTNAME`: The hostname of the machine.
- `$SECONDS`: The number of seconds the current shell has been running.
- `$BASH_VERSION`: The version of bash installed on the machine.

## Command Substitution

You can use command substitution to set the value of a variable based on the output of a command.

```sh
export VAR=$(date)
echo $VAR  # Output: Thu Jun 30 16:30:10 PDT 2023
```

## Arithmetic Operations

You can perform arithmetic operations with environment variables using the `$(( ))` syntax.

```sh
export VAR=5
echo $((VAR+5))  # Output: 10
```

Remember to avoid spaces around the `=` when assigning variables. Also, when