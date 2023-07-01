# Git Status

The `git status` command is used to display the current status of the Git repository. It provides information about the state of files in the working directory, staging area, and branch.

## Usage

```shell
git status [options]
```

## Options

- `-s` or `--short`: Provides a short and concise output format, suitable for scripting or when a compact overview is desired.
- `-b` or `--branch`: Displays the current branch and tracking information.
- `-u` or `--untracked-files`: Shows untracked files in the output.

## Statuses

`??`: Untracked files.
  ```
  ?? path/to/untracked_file1
  ?? path/to/untracked_file2
  ```

`A `: New file in the working directory.
  ```
  A  path/to/new_file
  ```

` M`: Modifications to file in the working directory.
  ```
   M path/to/modified_file
  ```

`MM`: Modifications to file both in the working directory and the staging area.
  ```
  MM path/to/file_with_modifications
  ```

`R `: Renamed file.
  ```
  R  path/to/old_file -> path/to/new_file
  ```

`D `: Deleted file.
  ```
  D  path/to/deleted_file
  ```

`UU`: File with unresolved merge conflicts.
  ```
  UU path/to/file_with_conflicts
  ```

In these examples, the left side indicates the status of the files, and the right side shows the actual file paths. This representation helps you quickly identify the changes and status of files in the Git repository.

## Output

The `git status` command can produce various output variations depending on the state of the repository.

**Untracked files** (when using `-u` or `--untracked-files`):

```
?? file1
?? file2
```
- `??`: Indicates untracked files.

**Changes to be committed** (when using `-s`, `-b`, or no option):

```
A  file1
 M file2
```
- `A`: Represents a new file added to the staging area.
- `M`: Indicates modifications to an existing file in the staging area.

**Changes not staged for commit** (when using `-s`, `-b`, or no option):

```
 M file1
MM file2
```
- `M`: Signifies modifications to an existing file in the working directory.
- `MM`: Indicates modifications to a file in both the staging area and the working directory.

**Renamed files** (when using `-s`, `-b`, or no option):

```
R  old_file1 -> new_file1
```
Indicates a file that has been renamed from `old_file1` to `new_file1`.

**Deleted files** (when using `-s`, `-b`, or no option):

```
D  file1
```
Denotes that `file1` has been deleted.

**File with merge conflicts** (when using `-s`, `-b`, or no option):

```
UU file1
```
Represents a file with unresolved merge conflicts.

## Examples

Display the short status (using `-s`):

```shell
$ git status -s
A  new_file.txt
 M modified_file.txt
?? untracked_file.txt
```

Show the current branch and tracking information (using `-b`):

```shell
$ git status -b
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  modified:   modified_file.txt

Untracked files:
  untracked_file.txt
```

Include untracked files in the output (using `-u`):

```shell
$ git status -u
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  modified:   modified_file.txt

Untracked files:
  untracked_file.txt
```

## Conclusion

The `git status` command is a fundamental tool in Git for checking the state of the repository. It provides essential information about modified files, additions, deletions, untracked files, and branch status. Understanding the output of `git status` helps in managing and tracking changes effectively within a Git project.

---

Feel free to use this updated Markdown documentation as a reference guide for the `git status` command, including output examples with enhanced formatting and clear indications of which option corresponds to each output section.