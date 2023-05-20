# sed Documentation

`sed`, which stands for "stream editor," is a powerful and versatile command-line utility used for text manipulation. It works by reading input from a file or standard input (stdin), applying a set of rules, and writing the output to standard output (stdout) or a file. `sed` is particularly useful for working with large text files or streams of data.

In this documentation, we will cover the most commonly used `sed` usage patterns, flags, and examples, particularly focusing on filtering output from `ls` and `find`.

## Basic Syntax

The basic syntax of `sed` is as follows:

```
sed [OPTIONS] 'COMMAND' inputfile
```

- `OPTIONS`: The command-line options that control the behavior of `sed`.
- `COMMAND`: The `sed` command(s) that define the operation to perform on the input text.
- `inputfile`: The file to read as input.

## Commonly Used Options

- `-n`: Suppress the automatic printing of the pattern space. By default, `sed` prints every line after applying the commands. With `-n`, only the lines explicitly specified by a command will be printed.
- `-e`: Allows you to specify multiple `sed` commands.
- `-f`: Specifies a file that contains `sed` commands.
- `-i[SUFFIX]`: Edit the input file in-place, optionally creating a backup with the specified `SUFFIX`.
- `-r` or `-E`: Use extended regular expressions instead of basic regular expressions.

## Commonly Used Commands

- `p`: Print the current pattern space.
- `d`: Delete the pattern space.
- `s/regexp/replacement/[flags]`: Substitute the first (or all, with the `g` flag) occurrences of `regexp` with the `replacement`.
- `q`: Quit immediately.

## Examples

### Replace a String

Replace all occurrences of "apple" with "orange":

```
sed 's/apple/orange/g' inputfile
```

### Delete Lines Containing a Pattern

Delete all lines containing the word "apple":

```
sed '/apple/d' inputfile
```

### Print Lines Matching a Pattern

Print all lines containing the word "apple":

```
sed -n '/apple/p' inputfile
```

### Replace a String In-place

Replace all occurrences of "apple" with "orange" in the input file and save the changes in-place:

```
sed -i '' 's/apple/orange/g' inputfile
```

### Filter `ls` Output

Filter the output of `ls` to show only files that have the `.txt` extension:

```
ls | sed -n '/\.txt$/p'
```

### Filter `find` Output

Filter the output of `find` to show only files that contain the word "report":

```
find . -type f | sed -n '/report/p'
```

Here are more examples of `sed` usage, demonstrating various flags and options:

### Multiple Commands with `-e`

Replace all occurrences of "apple" with "orange" and "banana" with "grape":

```
sed -e 's/apple/orange/g' -e 's/banana/grape/g' inputfile
```

### Commands from a File with `-f`

Suppose you have a file named `commands.sed` with the following content:

```
s/apple/orange/g
s/banana/grape/g
```

Apply the commands from the file to the input file:

```
sed -f commands.sed inputfile
```

### In-place Editing with Backup using `-i`

Replace all occurrences of "apple" with "orange" in the input file,

Replace all occurrences of "apple" with "orange" in the input file, saving the original file with a `.bak` extension:

```
sed -i.bak 's/apple/orange/g' inputfile
```

### Using Extended Regular Expressions with `-E`

Replace all occurrences of "apple" or "banana" with "fruit":

```
sed -E 's/(apple|banana)/fruit/g' inputfile
```

### Replace String and Keep Case with Regex Capture Groups

Replace "apple" with "orange" while keeping the case (uppercase or lowercase) of the first letter:

```
sed -E 's/([Aa])pple/\1range/g' inputfile
```

### Replace Only on Lines Matching a Pattern

Replace "apple" with "orange" only on lines containing the word "fruit":

```
sed '/fruit/s/apple/orange/g' inputfile
```

### Add Line Numbers to the Output

```
sed = inputfile | sed 'N; s/\n/. /'
```

### Delete Empty Lines

```
sed '/^$/d' inputfile
```

### Delete Lines Matching Multiple Patterns

Delete lines containing either "apple" or "banana":

```
sed -E '/apple|banana/d' inputfile
```

### Insert a Line Before a Match

Insert a line containing "FRUITS:" before each line containing "apple":

```
sed '/apple/i\FRUITS:' inputfile
```

### Append a Line After a Match

Append a line containing "TASTY!" after each line containing "apple":

```
sed '/apple/a\TASTY!' inputfile
```

Note that the `-I` flag you mentioned is not a standard `sed` flag. If you meant the `-i` flag for in-place editing, it has been covered in the examples above.

These examples cover a wide range of `sed` functionality, including the use of various flags and options to perform complex text manipulations. By combining these examples and customizing the commands and patterns, you can accomplish a vast array of text processing tasks with `sed`.