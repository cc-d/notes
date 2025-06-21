# Multiline Commands in Terminals

## Backslash

In terminals, you can use backslashes (`\`) to split long commands across multiple lines. This is useful for improving readability and organizing complex commands.

```
$ command \
  part1 \
  part2 \
  part3
```

```bash
command1 \
  && command2 \
  && command3
```

The backslash `\` at the end of each line indicates that the command continues on the next line.

## Using Parentheses

```bash
$ (
  command1
  command2
  command3
)
```

Commands within parentheses are treated as a single command, allowing you to span multiple lines.


## Heredocs

**Heredocs** allow multiline content in scripts or as input to commands in shells like `Bash` `Sh` `Zsh`:

```bash
command << DELIMITER
...
Text content
...
DELIMITER
```

- `DELIMITER` marks the start and end of the heredoc.
- Use heredocs for command input or content redirection.

**Input Example**

To provide input using a heredoc:

```bash
cat << EOF
Line 1
Line 2
Line 3
EOF
```

This example uses `cat` to display the lines:

```
Line 1
Line 2
Line 3
```

**Redirecting to a File Example**

To redirect heredoc content to a file:

```bash
cat > myfile.txt << EOF
Line 1
Line 2
Line 3
EOF
```

This redirects the content to `myfile.txt` (overwriting if exists).


## Using the Backtick (\`) Character

Backticks are used to capture the output of a command and can be used for multiline commands in shell scripts:

```bash
output=`command1 \
  && command2 \
  && command3`
```

The backticks wrap the multiline command, allowing you to capture the output as a variable.
