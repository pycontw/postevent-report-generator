from invoke import task

from tasks.common import PIPENV_PREFIX, COMMON_TARGETS_AS_STR


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


@task
def black(ctx):
    """Check style through black"""
    black_args = ["-l 119"]

    ctx.run(f"{PIPENV_PREFIX} black {' '.join(black_args)} --check {COMMON_TARGETS_AS_STR}")


@task(pre=[flake8, mypy, black], default=True)
def run(ctx):
    """Check style throguh linter (Note that pylint is not included)"""
    pass


@task
def pylint(ctx):
    """Check style through pylint"""
    ctx.run(f"{PIPENV_PREFIX} pylint {COMMON_TARGETS_AS_STR}")


@task
def reformat(ctx):
    """Reformat python files throguh black"""
    black_args = ["-l 119"]

    ctx.run(f"{PIPENV_PREFIX} black {' '.join(black_args)} {COMMON_TARGETS_AS_STR}")
