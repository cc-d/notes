#!/usr/bin/env python3
import os
import sys
import time
import re
import subprocess
from logfunc import logf
from myfuncs import runcmd
from pathlib import Path
from typing import Optional, List, Tuple, Set, Dict

import logging
logger = logging.getLogger()

class Change:
    @logf(level='info')
    def __init__(self, action: str, fpath: str):
        self.action = action
        self.fpath = fpath
        logger.info('new action change={} file={}'.format(action, fpath))

    def __repr__(self):
        if hasattr(self, 'action') and hasattr(self, 'fpath'):
            return '{}  {}'.format(self.action, self.fpath)
        return 'Change<pre-__init__>'


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
    def git_commit_and_push(self):
        """Commit the changes to the git repository and push to the remote repository.

        Args:
            action (str): The action taken (e.g., created, updated, deleted).
            files (Set[str]): A set containing files to add specifically.
        """

        # detect any changed files using git status -s (that meet criteria)
        changes = self.git_status()
        changed = []
        addfnames = ['watcher.py', 'requirements.txt', 'README.md', 'LICENSE']
        for change in changes:
            addfile = False
            if change in addfnames:
                addfile = True
            elif str(change).lower().endswith == '.md':
                addfile = True
            elif os.path.isdir(change):
                addfile = True

            if addfile:
                runcmd('git add {}'.format(change))
                changed.append(change)


        if changed != []: # at least 1 file change to commit
            # Commit the changes
            subprocess.run(["git", "commit", "-m",
                        'CHANGED FILES: {}'.format(' '.join([c for c in changed]))],
                        cwd=self.root_path)

            branch = runcmd('git branch --show-current')[0]

            # Push the changes to the remote repository
            subprocess.run(["git", "push", "origin", branch], cwd=self.root_path)

    @logf(level='info')
    def git_status(self) -> Set[str]:
        """ returns a parsed file changes from git status -s """
        REG = r'^(..) (.*)$'

        @logf(level='info')
        def get_changes(lines: List[str]) -> Set[str]:
            changes = set()
            for line in lines:
                match = re.search(REG, line)
                if match is None:
                    continue
                left, right = match.groups()
                left, right = left.strip(), right.strip()
                change = Change(left, right)
                changes.add(change.fpath)
            return changes

        out = runcmd('git status -s')
        return get_changes(out)

    @logf(level='info')
    def update_readme(self, dry: bool = False) -> str:
        """
        Update the root README.md file with a tree-like structure of the provided Markdown files and directories.

        Args:
            dry (bool): dry run? if true don't write file just return

        Returns:
            str: the README.md file contents
        """
        def find_mds() -> List[str]:
            """Find all markdown files in the directory, excluding README.md"""
            return subprocess.check_output(
                "find . -name '*.md' | sed 's/^\.\///g' | sed '/^README.md$/d'",
                cwd=self.root_path, text=True, shell=True).splitlines()

        def find_dirs() -> List[str]:
            """Find all directories in the root path, excluding ones that start with a dot and the 'venv' directory."""
            return subprocess.check_output(
                "find . -type d | sed 's/^\.\///g' | sed '/^\./d' | sed '/^venv/d'",
                cwd=self.root_path, text=True, shell=True).splitlines()

        # Get all markdown files and directories
        mdfiles, dirfiles = find_mds(), find_dirs()

        logger.debug(f'mdfiles: {mdfiles} | dirfiles: {dirfiles}')

        lines = []
        for directory in sorted(dirfiles):
            depth = directory.count('/') + 1
            title = Path(directory).parts[-1]


            # Sort markdown files in directory and add them as list items
            mdfiles_in_directory = sorted([f for f in mdfiles if f.startswith(directory)])

            for mdfile in mdfiles_in_directory:
                mdpath = Path(mdfile)
                mdparent = mdpath.parts[-2]
                mdname = str(mdpath.parts[-1])[:-3]
                if mdparent == title:
                    lines.append(f"**[{mdname}]({mdfile})**&nbsp;&nbsp;&nbsp;")

        if lines:
            # Write the contents to the README file
            with open(self.readme_path, "w", encoding='utf8') as readme_file:
                readme_file.write(''.join(lines))
            return '\n\n'.join(lines)
            
        raise Exception('No lines written to disk.')

    def run(self):
        """ Main run method, checks the root dir for any changes in dir structure or
            *.md files outside of README.md, and then commits those changed to the git repo
            if any are detected.
        """
        if self.git_status() != set():
            logger.info('git_status updated committing')
            self.update_readme()
            self.git_commit_and_push()


    def exec_cmd(self, cmd: Optional[str] = 'run'):
        """ executes watcher cmd passed to script """
        cmd = str(cmd).lower()

        if cmd == 'run':
            self.run()
        elif cmd == 'dry':
            self.update_readme(dry=True)
        elif cmd == 'readme':
            self.update_readme()
        elif cmd == 'watch':
            while True:
                self.run()
                time.sleep(1)
        else:
            raise Exception('No valid command was provided.')

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    root_path = None #sys.argv[1] if len(sys.argv) > 1 else None
    cmd = str(sys.argv[1]).lower() if len(sys.argv) > 1 else 'run'

    watcher = NotesWatcher(root_path)
    watcher.exec_cmd(cmd)

