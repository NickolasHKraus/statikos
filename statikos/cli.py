# -*- coding: utf-8 -*-
"""CLI module."""

import click

from .statikos import Statikos


@click.group(invoke_without_command=True)
@click.version_option(prog_name='Statikos', message='%(prog)s %(version)s')
@click.pass_context
def cli(ctx: click.core.Context) -> None:
    """
    A Python package for generating static websites using AWS CloudFormation.

    \f

    :type ctx: click.core.Context
    :param ctx: Click context object

    :rtype: None
    :return: None
    """
    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())
        ctx.exit(1)


@cli.command()
def create() -> None:
    """
    Create a Statikos service.

    The following artifacts will be created:
      - .statikos/
      - .statikos/cloudformation.json
      - statikos.yml

    \f

    :rtype: None
    :return: None
    """
    click.echo(click.style('Creating Statikos files...'), fg='white')
    s = Statikos()
    s.create()


@cli.command()
@click.option(
    '--dry-run',
    help='Create the CloudFormation template without deploying the stack.')
def deploy(dry_run: bool) -> None:
    """
    Deploy a Statikos service.

    Create and deploy the CloudFormation stack.

    \f

    :type dry_run: bool
    :param dry_run: whether to create the CloudFormation template without
        deploying the stack

    :rtype: None
    :return: None
    """
    click.echo(click.style('Deploying Statikos service...', fg='white'))
    s = Statikos()
    s.deploy(dry_run)


@cli.command()
def publish() -> None:
    """
    Publish content.

    Generate the static content and upload it to Amazon S3.

    \f

    :rtype: None
    :return: None
    """
    click.echo(click.style('Publishing...', fg='white'))
    s = Statikos()
    s.publish()


@cli.command()
@click.option('-a', '--all',
              help='Remove the CloudFormation stack and Statikos artifacts.')
def remove(_all: bool) -> None:
    """
    Remove a Statikos service.

    Removes the CloudFormation stack and, optionally, Statikos artifacts.

    \f

    :type stack_only: bool
    :param stack_only: whether to only remove the CloudFormation stack

    :rtype: None
    :return: None
    """
    click.echo(click.style('Removing Statikos service...', fg='white'))
    s = Statikos()
    s.remove(_all)


if __name__ == '__main__':
    cli()
