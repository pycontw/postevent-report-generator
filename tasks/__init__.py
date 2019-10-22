from invoke import task


PIPENV_PREFIX = "pipenv run"


@task
def clean(ctx):
    """Remove all the tmp files in .gitignore"""
    ctx.run("git clean -Xdf")


@task
def clean_env(ctx):
    """Remove virtual environement"""
    ctx.run("pipenv --rm", warn=True)


@task
def init(ctx):
    """Install production dependencies"""
    ctx.run("pipenv install")


@task
def init_dev(ctx):
    """Install development dependencies"""
    ctx.run("pipenv install --dev")


@task
def test(ctx):
    """Run testcase"""
    ctx.run(f"{PIPENV_PREFIX} pytest", pty=True)


@task
def cov(ctx):
    """Run testcase"""
    ctx.run(f"{PIPENV_PREFIX} pytest --cov-report term-missing --cov=report_generator test", pty=True)


@task
def reformat(ctx):
    """Reformat python files throguh black"""
    black_args = ["-l 119"]
    target_fils = ["report_generator", "scripts", "test", "setup.py", "tasks.py"]

    ctx.run(f"{PIPENV_PREFIX} black {' '.join(black_args)} {' '.join(target_fils)}")


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


@task(pre=[flake8, mypy])
def lint(ctx):
    """Check style throguh linter (Note that pylint is not included)"""
    pass


@task
def pylint(ctx):
    """Check style through pylint"""
    targets = ["report_generator", "test", "scripts", "setup.py", "tasks.py"]
    ctx.run(f"{PIPENV_PREFIX} pylint {' '.join(targets)}")


@task
def secure(ctx):
    """Check package security"""
    ctx.run("pipenv check")


@task
def develop(ctx):
    """Install script in pipenv environement in development mode"""
    ctx.run(f"{PIPENV_PREFIX} python setup.py develop")


@task
def install(ctx):
    """Install script in pipenv environement"""
    ctx.run(f"{PIPENV_PREFIX} python setup.py install")


@task(pre=[clean_env, init, install])
def test_cli(ctx):
    """Test whether the cli is runnable"""
    ctx.run(f"{PIPENV_PREFIX} rg-cli")
