#!/bin/sh

echo "Project summary:"

# List all file types
echo "\nFile types in the project:"
find . -type f | perl -ne 'print $1 if m/\.([^.\/]+)$/' | sort -u

# Count lines of code, separated by file type
echo "\nLines of code by file type:"
find . -name '*.*' | xargs -n1 file | cut -d: -f2 | sort | uniq -c

# Give a brief summary of the file and folder structure
echo "\nFile and folder structure:"
tree -L 2

# If the project is a git repo, summarize the commit history
if [ -d .git ] || git rev-parse --git-dir > /dev/null 2>&1; then
    echo "\nGit commit summary:"
    git shortlog -sn
else
    echo "\nNo git repository detected."
fi

