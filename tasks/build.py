from invoke import task, Collection

from tasks.common import PIPENV_PREFIX
from tasks.env import clean as clean_env
from tasks.env import init as _init


@task
def develop(ctx):
    """Install script in pipenv environement in development mode"""
    ctx.run(f"{PIPENV_PREFIX} python setup.py develop")


@task
def install(ctx):
    """Install script in pipenv environement"""
    ctx.run(f"{PIPENV_PREFIX} python setup.py install")


@task
def clean(ctx):
    """Remove all the tmp files in .gitignore"""
    ctx.run("git clean -Xdf")


@task(pre=[clean_env, _init, install])
def test_cli(ctx):
    """Test whether the cli is runnable"""
    ctx.run(f"{PIPENV_PREFIX} rg-cli --help")


build_ns = Collection("build")
build_ns.add_task(develop)
build_ns.add_task(install)
build_ns.add_task(clean)
build_ns.add_task(test_cli)
