"""
CMDr Project Managment
"""
import asyncio
import os
import subprocess
from subprocess import PIPE
from yaml import load, dump
import re
from functools import wraps

from .view import screen
from .project_view import ProjectView


async def run(cmd):
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )

    stdout, stderr = await proc.communicate()

    print(f'[{cmd!r} exited with {proc.returncode}]')
    if stdout:
        print(f'[stdout]\n{stdout.decode()}')
    if stderr:
        print(f'[stderr]\n{stderr.decode()}')


class Project:
    jobs = {}
    working_dir = None

    def __init__(self, project_name, working_dir=os.getcwd()):
        self.working_dir = working_dir
        self.project_name = project_name
        self.view = ProjectView(self)

    def spawn_job(self, command):
        """
        Spawn a job in the context of the projects root
        """
        asyncio.run(run('ls'))

        screen(self.view)

    def to_dict(self):
        return dict(self)
