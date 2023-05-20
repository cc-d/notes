# Useful ls Commands

`ls` is a command used to list files and directories in a directory. It comes with several options that can modify its behavior and output.

## Basic Commands

- `ls`: List files and directories in the current directory.
- `ls <directory>`: List files and directories in the specified directory.

## Sorting Options

- `ls -t`: Sort files and directories by modification time, newest first.
- `ls -S`: Sort files and directories by size, largest first.
- `ls -r`: Reverse the order of the sort.
- `ls -X`: Sort files and directories by extension.
- `ls -v`: Sort files and directories by version (natural sort of numbers within the text).

## Display Options

- `ls -l`: Display files and directories in long format, showing additional details like permissions, ownership, size, and modification date.

```bash
-rw-r--r-- 1 user group 2345 Jan 01 12:34 file.txt
drwxr-xr-x 2 user group 4096 Jan 01 12:35 directory
```

- `ls -a`: Show hidden files and directories (those starting with a dot `.`).

```bash
.  ..  .hidden_file  file.txt  directory
```

- `ls -A`: Show hidden files and directories, but exclude `.` and `..`.
```bash
.hidden_file  file.txt  directory
```
- `ls -h`: Display file sizes in human-readable format (e.g., 1K, 234M, 2G).
```bash
1K file.txt
4.0K directory
```
- `ls -1`: Display one file or directory per line.
```bash
file.txt
directory
```
- `ls -R`: List files and directories recursively, including subdirectories.
```bash
./directory:
subfile.txt
```
- `ls -d */`: List only directories.
```bash
directory/
```

## Combining Options

You can combine multiple options together. Here are some examples:

- `ls -la`: List all files and directories, including hidden ones, in long format.
- `ls -lrt`: List files and directories sorted by modification time in ascending order, in long format.
- `ls -lhS`: List files and directories sorted by size in human-readable format, in long format.


