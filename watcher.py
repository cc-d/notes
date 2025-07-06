#!/usr/bin/env python3
import os
import os.path as op
import sys
import time
import re
import subprocess
from glob import glob

import typing as TYPE
from shlex import split as shx_split
from subprocess import run as sp_run, CompletedProcess


def runcmd(
    cmd: TYPE.Union[str, TYPE.List], output: bool = True, *args, **kwargs
) -> TYPE.Optional[CompletedProcess]:
    """Runs a single command in the shell with subprocess.run
    Args:
        cmd (Union[str, List]): The command to run in the shell.
        output (bool): Whether or not to return the output of the command.
            Defaults to True.
    """
    if isinstance(cmd, str):
        cmd = shx_split(cmd)

    if output:
        return sp_run(
            cmd, check=True, text=True, capture_output=True, *args, **kwargs
        )
    else:
        sp_run(
            cmd, check=False, text=False, capture_output=False, *args, **kwargs
        )

from pathlib import Path
from typing import Optional, List, Tuple, Set, Dict



import logging
logger = logging.getLogger()

class Change:
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
    IGNORE = ['.', 'venv', 'LICENSE', 'requirements.txt', 'README.md']
    ICONS = ['📁',  '💡']

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

    def git_status(self) -> Set[str]:
        """ returns a parsed file changes from git status -s """
        REG = r'^(..) (.*)$'

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

    def update_readme(self, dry: bool = False) -> str:
        """
        Build a nested tree of .md files (excluding README.md) and write a structured README.md.
        """
        
        tree = glob('**', recursive=True)
        tree = [x for x in tree if not any(x.startswith(bl) for bl in self.IGNORE)]

        lines = [] 

        for dirfile in tree:
            dpath = Path(dirfile)
            depth = len(dpath.parts)
            icon = self.ICONS[0] if op.isdir(dirfile) else self.ICONS[1]
            shortname = dpath.parts[-1]

            if dpath.is_file():
                shortname = shortname[:-3] if shortname.lower().endswith('.md') else shortname
            


            line = f"{'- ' * depth} {icon} [{shortname}]({op.join(*dpath.parts[:-1], dpath.parts[-1])})"

            lines.append(line)
            print(line)

        if not dry:
            with self.readme_path.open("w", encoding="utf-8") as f:
                f.write('\n'.join(lines) + '\n')
        return '\n'.join(lines)



    def exec_cmd(self, cmd: Optional[str] = 'run'):
        """ executes watcher cmd passed to script """
        cmd = str(cmd).lower()

        if cmd in ['run', 'readme']:
            self.update_readme()
        elif cmd == 'dry':
            self.update_readme(dry=True)
        elif cmd == 'watch':
            while True:
                self.update_readme()
                time.sleep(1)
        else:
            raise Exception('No valid command was provided.')

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    root_path = None #sys.argv[1] if len(sys.argv) > 1 else None
    cmd = str(sys.argv[1]).lower() if len(sys.argv) > 1 else 'run'

    watcher = NotesWatcher(root_path)
    watcher.exec_cmd(cmd)


