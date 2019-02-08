"""
The main entry point for the CMDr program.
"""
import click

from .project import Project

@click.command()
@click.argument('project-name')
def main(project_name):
    """
    The root command to CMDr
    """
    project = Project(project_name)
    project.spawn_job("ls")

    return 0

