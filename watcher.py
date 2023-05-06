#!/usr/bin/env python3
import os
import sys
import time
import subprocess
from myfuncs import logf
from pathlib import Path
from typing import Optional, List, Tuple, Set, Dict

import logging
logger = logging.getLogger()


class NotesWatcher:
    """A class to watch for changes in Markdown files and update the root README.md accordingly."""
    IGNORE_DIRS = ['.', 'venv']

    def __init__(self, root_path: Optional[str] = None):
        """
        Initialize the NotesWatcher with the provided root path or use the script's directory.

        Args:
            root_path (str, optional): The root path to watch for changes. Defaults to the script's directory.
        """
        if root_path is None:
            self.root_path = Path(__file__).parent.resolve()
        else:
            self.root_path = Path(root_path).resolve()

        self.readme_path = self.root_path / "README.md"

    @logf(level='info')
    def get_files(self) -> Set[str]:
        """Retrieve a list of newly created Markdown files and non-hidden directories in the root path.

        Returns:
            Set[str]: A set containing newly created Markdown files and non-hidden directories.
        """
        output = subprocess.check_output(["git", "status", "-s"], cwd=self.root_path, text=True)
        lines = output.splitlines()

        files = set()

        for line in lines:
            status, path = line[:2], line[3:]
            if path.endswith(".md") and path != 'README.md':
                files.add(path)
            elif os.path.isdir(os.path.join(self.root_path, path)) and not path.startswith('.'):
                files.add(path + '/')

        return files

    @logf(level='info')
    def git_commit_and_push(self, action: str, files: Set[str]):
        """Commit the changes to the git repository and push to the remote repository.

        Args:
            action (str): The action taken (e.g., created, updated, deleted).
            files (Set[str]): A set containing files to add specifically.
        """
        # Add the specified files and directories
        subprocess.run(["git", "add", '.'], cwd=self.root_path)

        # Commit the changes
        commit_msg = f"{action} {files}"
        subprocess.run(["git", "commit", "-m", commit_msg], cwd=self.root_path)

        # Push the changes to the remote repository
        subprocess.run(["git", "push"], cwd=self.root_path)

    import os
    import subprocess
    from pathlib import Path
    from typing import List


    @logf(level='info')
    def update_readme(self) -> str:
        """
        Update the root README.md file with a tree-like structure of the provided Markdown files and directories.

        Returns:
            str: the README.md file contents
        """
        def find_mds() -> List[str]:
            """Find all markdown files in the directory, excluding README.md"""
            return [str(path) for path in Path(self.root_path).rglob('*.md') if path.name != "README.md"]

        def find_dirs() -> List[str]:
            """Find all directories in the root path, excluding ones that start with a dot and the 'venv' directory."""
            return [str(path) for path in Path(self.root_path).rglob('*') if path.is_dir() and not path.name.startswith('.') and not path.name.startswith('venv')]

        # Get all markdown files and directories
        mdfiles, dirfiles = find_mds(), find_dirs()
        logger.debug(f'mdfiles: {mdfiles} | dirfiles: {dirfiles}')

        # Prepare the lines for the README
        lines = []

        for directory in sorted(dirfiles):
            depth = len(Path(directory).parts)
            title = Path(directory).parts[-1]

            # Write a header for each directory. Depth is used to determine header level.
            lines.append(f"{'#' * (depth + 1)} {title}")

            # Sort markdown files in directory and add them as list items
            mdfiles_in_directory = sorted([f for f in mdfiles if f.startswith(directory)])

            for mdfile in mdfiles_in_directory:
                lines.append(f"[{mdfile}]({mdfile})")

        # Write the contents to the README file
        with open(self.readme_path, "w", encoding='utf8') as readme_file:
            readme_file.write('\n\n'.join(lines))

        return '\n\n'.join(lines)



    @logf(level='debug')
    def changes(self) -> bool:
        """ Detects .md/dir changes in the notes dir.

        Returns:
            bool: True if any changes otherwise False
        """
        git_status_output = subprocess.check_output(
            ["git", "status", "-s"], cwd=self.root_path, text=True)

        md_changes = [
            line.split()[-1] for line in git_status_output.splitlines() if line.endswith(".md")]

        # Changes related to directories
        dir_changes = [
            line.split()[-1] for line in git_status_output.splitlines()
            if os.path.isdir(line.split()[-1])]

        if md_changes == [] and dir_changes == []:
            return False
        return True

    def run(self):
        """ Main run method, checks the root dir for any changes in dir structure or
            *.md files outside of README.md, and then commits those changed to the git repo
            if any are detected.
        """
        if self.changes():
            action = "Updated"
            self.update_readme()
            files = self.get_files()
            files.add("README.md")
            self.git_commit_and_push(action, files)

    def watch(self):
        """Watch for changes in the root path and update the README.md accordingly."""

        while True:
            self.run()
            time.sleep(0.5)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    root_path = None #sys.argv[1] if len(sys.argv) > 1 else None
    cmd = str(sys.argv[1]).lower() if len(sys.argv) > 1 else 'run'

    watcher = NotesWatcher(root_path)

    if cmd == 'readme':
        watcher.update_readme()
    if cmd == 'watch':
        watcher.watch()
    else:
        watcher.run()
