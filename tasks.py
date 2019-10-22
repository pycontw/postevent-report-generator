from invoke import task


PIPENV_PREFIX = "pipenv run"


@task
def clean(cmd):
    """Remove all the tmp files in .gitignore"""
    cmd.run("git clean -Xdf")


@task
def clean_env(cmd):
    """Remove virtual environement"""
    cmd.run("pipenv --rm", warn=True)


@task
def init(cmd):
    """Install production dependencies"""
    cmd.run("pipenv install")


@task
def init_dev(cmd):
    """Install development dependencies"""
    cmd.run("pipenv install --dev")


@task
def test(cmd):
    """Run testcase"""
    cmd.run(f"{PIPENV_PREFIX} pytest", pty=True)


@task
def cov(cmd):
    """Run testcase"""
    cmd.run(f"{PIPENV_PREFIX} pytest --cov-report term-missing --cov=report_generator test", pty=True)


@task
def reformat(cmd):
    """Reformat python files throguh black"""
    black_args = ["-l 119"]
    target_fils = ["report_generator", "scripts", "test", "setup.py", "tasks.py"]

    cmd.run(f"{PIPENV_PREFIX} black {' '.join(black_args)} {' '.join(target_fils)}")


@task
def flake8(cmd):
    """Check style through flake8"""
    cmd.run(f"{PIPENV_PREFIX} flake8")


@task
def mypy(cmd):
    """Check style through mypy"""
    mypy_arguments = ["--ignore-missing-imports"]
    packages = ["report_generator", "test"]
    cmd.run(f"{PIPENV_PREFIX} mypy {' '.join(mypy_arguments)} -p {' -p '.join(packages)}")


@task(pre=[flake8, mypy])
def lint(cmd):
    """Check style throguh linter (Note that pylint is not included)"""
    pass


@task
def pylint(cmd):
    """Check style through pylint"""
    targets = ["report_generator", "test", "scripts", "setup.py", "tasks.py"]
    cmd.run(f"{PIPENV_PREFIX} pylint {' '.join(targets)}")


@task
def secure(cmd):
    """Check package security"""
    cmd.run("pipenv check")


@task
def develop(cmd):
    """Install script in pipenv environement in development mode"""
    cmd.run(f"{PIPENV_PREFIX} python setup.py develop")


@task
def install(cmd):
    """Install script in pipenv environement"""
    cmd.run(f"{PIPENV_PREFIX} python setup.py install")


@task(pre=[clean_env, init, install])
def test_cli(cmd):
    """Test whether the cli is runnable"""
    cmd.run(f"{PIPENV_PREFIX} rg-cli --help")
