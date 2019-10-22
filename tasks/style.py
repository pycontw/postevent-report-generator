from invoke import task

from tasks.common import PIPENV_PREFIX


@task
def flake8(ctx):
    """Check style through flake8"""
    ctx.run(f"{PIPENV_PREFIX} flake8")


@task
def mypy(ctx):
    """Check style through mypy"""
    mypy_arguments = ["--ignore-missing-imports"]
    packages = ["report_generator", "test"]
    ctx.run(f"{PIPENV_PREFIX} mypy {' '.join(mypy_arguments)} -p {' -p '.join(packages)}")


@task(pre=[flake8, mypy], default=True)
def run(ctx):
    """Check style throguh linter (Note that pylint is not included)"""
    pass


@task
def pylint(ctx):
    """Check style through pylint"""
    targets = ["report_generator", "test", "scripts", "setup.py", "tasks"]
    ctx.run(f"{PIPENV_PREFIX} pylint {' '.join(targets)}")


@task
def reformat(ctx):
    """Reformat python files throguh black"""
    black_args = ["-l 119"]
    target_fils = ["report_generator", "scripts", "test", "setup.py", "tasks"]

    ctx.run(f"{PIPENV_PREFIX} black {' '.join(black_args)} {' '.join(target_fils)}")
