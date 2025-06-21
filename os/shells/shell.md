# Unix/Linux Shell

A Unix/Linux shell is a command-line interpreter or a program that provides a user interface for various operating systems. It enables users to interact with the system by executing commands and running scripts.

```sh
$ echo "Hello, World!"

Hello, World!
```

## Types of Shells

Certainly! Here's a non-numbered, well-formatted list of common shell initialization files:

- **`~/.bashrc`**: Executed for interactive, non-login Bash shells.
- **`~/.bash_profile`**: Executed for login shells in Bash.
- **`~/.profile`**: Used by many Unix-like systems, including Bash, for login shells.
- **`~/.zshrc`**: Used by the Zsh shell for interactive Zsh shells.
- **`~/.cshrc`**: Used by the C shell (csh) and its derivatives for interactive C shells.
- **`/etc/profile`**: System-wide initialization file executed for all users.
- **`/etc/bash.bashrc`**: System-wide Bash initialization file for non-login shells.
- **`/etc/bashrc`**: Another system-wide Bash initialization file.
- **`/etc/zshrc`**: System-wide Zsh initialization file.
- **`/etc/csh.cshrc`**: System-wide C shell (csh) initialization file.

These files allow you to customize the shell environment and define settings that persist across shell sessions. They are commonly used to set environment variables, define aliases and functions, customize the shell prompt, and execute other commands or scripts during shell startup.

Sure, let's dive into each of these shell initialization files and their specific usage.

## **Bash Shell Initialization Files**

Bash is the default shell on many Unix-like systems, including most Linux distributions and macOS (before Catalina). It reads one or several configuration files during startup, depending on the type of the shell instance.

### **~/.bashrc**

This is the individual per-user initialization file for all interactive non-login Bash shells. It's commonly used to set environment variables, define aliases and functions, customize the shell prompt, and more. When you start a new terminal window, this file is read.

### **~/.bash_profile**

This is the individual per-user initialization file for login Bash shells. On some systems, this file is called `~/.bash_login` or `~/.profile`. Typically, it's used to start processes that you want to run when you log in to the system. However, many users source `~/.bashrc` from `~/.bash_profile` to keep the same settings across both login and non-login shells:

```sh
if [ -f ~/.bashrc ]; then
   source ~/.bashrc
fi
```

### **~/.profile**

This file is a legacy from the Bourne shell. Bash reads this file if it can't find the `~/.bash_profile` or `~/.bash_login` files. Many other shells also read this file, making it a good place for environment variables that should be available to graphical applications, not just shells started from a terminal.

### **/etc/profile**

This is the system-wide initialization file, executed for all users for login shells. It's typically used to set system-wide environment variables and startup programs.

### **/etc/bash.bashrc**

This is the system-wide equivalent to `~/.bashrc`. It's executed for interactive non-login shells. On some systems, this file doesn't exist by default.

## **Zsh Shell Initialization Files**

Zsh is a popular shell that includes many enhancements over Bash. It's the default shell in macOS Catalina and later. It reads different configuration files during startup.

### **~/.zshrc**

This file is the individual per-user initialization file for interactive Zsh shells. It's analogous to `~/.bashrc` for Bash. When you start a new terminal window, this file is read.

### **/etc/zshrc**

This is the system-wide equivalent to `~/.zshrc`, executed for all users' interactive Zsh shells.

## **Differences in When They Are Used**

### **Login Shells**

A login shell is the first process that executes under your user ID when you log in for an interactive session. The login process tells the shell to behave as a login shell with a convention: passing argument 0 (which is normally the name of the shell executable), with a `-` character prepended.

### **Non-login Shells**

When you open a terminal emulator (like `gnome-terminal`, `konsole`, `xterm`, etc), you're starting a new shell process. But these are non-login shells. Your shell also behaves as a non-login shell when you start a new shell from an existing one (for example, by running `bash` from your login shell).

### **Interactive Shells**

Interactive shells are those that are connected to a terminal (you can type commands and see the results). Your login shell is typically interactive, as are the shells that you spawn in a terminal emulator.

### **Non-interactive Shells**

Shells running scripts are typically non-interactive shells, as are shells that are receiving commands piped in from another process (like `echo ls | bash`).

**Loading Order**
-------------

The loading order of these files depends on whether the shell is a login shell and whether it is interactive. Here is the common loading order:

For an interactive login shell: `/etc/profile` → `~/.bash_profile` (or `~/.bash_login`/`~/.profile`)

For an interactive non-login shell (bash): `~/.bashrc`

For an interactive non-login shell (zsh): `~/.zshrc`

In practice, the situation can be more complex because these files can source each other. For example, it's common to have `~/.bash_profile` source `~/.bashrc` to unify settings for interactive shells.
