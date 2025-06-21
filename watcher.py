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
        Build a nested tree of .md files (excluding README.md) and write a structured README.md.
        """
        def find_mds() -> List[Path]:
            """Find all .md files excluding README.md and venv paths"""
            return [
                p for p in self.root_path.rglob("*.md")
                if p.name != "README.md" and "venv" not in p.parts and not any(part.startswith('.') for part in p.parts)
            ]

        def build_tree(paths: List[Path]) -> Dict:
            """Convert list of Paths into nested tree structure"""
            tree = {}
            for path in paths:
                relative = path.relative_to(self.root_path)
                parts = list(relative.parts)
                *dirs, file = parts
                current = tree
                for d in dirs:
                    current = current.setdefault(d, {})
                current.setdefault('_files', []).append((file, relative))
            return tree

        def render_tree(tree: Dict, depth: int = 0) -> List[str]:
            lines = []
            indent = "  " * depth
            for key in sorted(k for k in tree if k != '_files'):
                lines.append(f"{indent}- {key}")
                lines.extend(render_tree(tree[key], depth + 1))
            for fname, rel_path in sorted(tree.get('_files', [])):
                link_text = fname[:-3]  # Strip .md
                lines.append(f"{indent}  - [{link_text}]({rel_path.as_posix()})")
            return lines

        mdfiles = find_mds()
        tree = build_tree(mdfiles)
        lines = render_tree(tree)
        content = '\n'.join(lines)

        if not dry:
            with self.readme_path.open("w", encoding="utf-8") as f:
                f.write(content + '\n')
        return content



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

