# **subprocess** Module

Python's `subprocess` module provides mechanisms to spawn new processes, connect to their input/output/error pipes, and obtain their return codes.

## `subprocess.run()`

**subprocess.run()**
runs the command described by `args`, waits for the command to complete, then returns a `CompletedProcess` instance.

The `args` argument is required and should be a list representing the command to be executed.

### ***Parameters***

- **args**: Specifies command and arguments. Must be a sequence of strings, or a single string if `shell=True`.
- **stdin**: File-like object that provides the standard input for the process. Use `subprocess.PIPE` to create a pipe.
- **stdout / stderr**: File-like objects that receive the process's standard output/error. `subprocess.PIPE` creates a pipe.
- **capture_output**: If `True`, `stdout` and `stderr` are captured. This is equivalent to setting `stdout` and `stderr` to `subprocess.PIPE`.
- **shell**: If `True`, command is run through the shell. This can pose security risks with untrusted input.
- **cwd**: String specifying the working directory for the command. If not specified, the command runs in the current directory.
- **timeout**: Float specifying the maximum execution time in seconds. If the command takes longer, `subprocess.TimeoutExpired` is raised.
- **check**: If `True`, a non-zero exit status of the command raises `subprocess.CalledProcessError`.
- **encoding / errors**: When `text=True`, these specify the encoding for input/output and error handling, respectively.
- **text**: If `True`, standard input/output/error are opened as text streams, and output is decoded to text using locale encoding.
- **env**: Dictionary that defines the environment variables for the command. If not provided, current process environment is used.


```python
import subprocess

result = subprocess.run(["ls", "-l"], capture_output=True, text=True)

print("Return code:", result.returncode)
print("Standard output:", result.stdout)
print("Standard error:", result.stderr)
```

In this example, `subprocess.run()` is used to execute the `ls -l` command. We capture the output using `capture_output=True` and specify that we want the output to be in text format with `text=True`.
Absolutely, let's elaborate on the remaining functions and their parameters.

# `subprocess.call()`

`subprocess.call()` works much like `subprocess.run()`, but it only returns the exit code of the command. It's a more basic way to run a command if you're not interested in the output or error.

The parameters are the same as `subprocess.run()`, except for capture_output and check which are not applicable.


### ***Parameters***

The parameters are the same as subprocess.run(), except for capture_output and check which are not applicable.

```python
import subprocess

# Running a command with subprocess.call
return_code = subprocess.call(["echo", "Hello, World!"])
```

# `subprocess.check_output()`

`subprocess.check_output()` runs a command, waits for the command to complete, and then returns the command's output as a byte string. If the command exits with a non-zero status, a `CalledProcessError` exception is raised.

### ***Parameters***

The parameters are the same as for `subprocess.call()`, except for an additional `input` parameter that can be used to pass input data to the subprocess.

- **input**: Specifies the input as a string. If provided, it will be passed as the input to the subprocess.


```python
import subprocess

# Running a command with subprocess.check_output
output = subprocess.check_output(["ls"], text=True)
```

# `subprocess.Popen()`

`subprocess.Popen()` is a more flexible interface for creating and managing subprocesses. It allows fine control over the input/output/error pipes and manages subprocess's lifecycle.

### ***Parameters***

- **args**: Specifies command and arguments. Must be a sequence of strings, or a single string if `shell=True`.
- **bufsize**: Specifies the I/O buffering policy. `0` means unbuffered, `1` means line-buffered, and larger numbers specify buffer size.
- **executable**: Replaces the executable specified in `args`.
- **stdin / stdout / stderr**: File-like objects that provide/collect the process's standard input/output/error. `subprocess.PIPE` creates a pipe.
- **preexec_fn**: Callable that is called just before the child process is created (Unix only).
- **close_fds**: If `True`, all file descriptors except 0, 1, and 2 are closed before the child process is started (Unix only).
- **shell**: If `True`, command is run through the shell. This can pose security risks with untrusted input.
- **cwd**: String specifying the working directory for the command. If not specified, the command runs in the current directory.
- **env**: Dictionary that defines the environment variables for the command. If not provided, current process environment is used.
- **universal_newlines (or text in Python 3.7+)**: If `True`, standard input/output/error are opened as text streams, and output is decoded to text using locale encoding.
- **startupinfo / creationflags**: Controls specific subprocess attributes. They are available on Windows only.
- **restore_signals (Unix only), start_new_session, pass_fds (Unix only)**: Offer control over process attributes in Unix.

```python
import subprocess

# Running a command with subprocess.Popen
with subprocess.Popen(["ls"], stdout=subprocess.PIPE, text=True) as proc:
    output = proc.stdout.read()
```
Each of these functions and parameters provide gran

# Passing Arguments to the Shell

With the `shell=True` argument, you can pass a simple string as a command, which gets passed to the shell. This can be convenient, but is generally considered a security risk and should be avoided if possible. Use list-based arguments instead.

```python
import subprocess

result = subprocess.run("ls -l", shell=True, capture_output=True, text=True)
print("Output:", result.stdout)
```

In this example, `subprocess.run()` is called with `shell=True`, allowing a string command `ls -l` to be passed. This will output the same result as the first `subprocess.run()` example.

