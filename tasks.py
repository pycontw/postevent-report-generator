from invoke import task


PIPENV_PREFIX = "pipenv run"


@task
def clean(cmd):
    """Remove all the tmp files in .gitignore"""
    files_to_remove = []
    with open(".gitignore") as input_file:
        for line in input_file.readlines():
            if not line.startswith("#"):
                files_to_remove.append(line.strip())

    cmd.run(f"rm -rf {' '.join(files_to_remove)}")


@task
def init_dev(cmd):
    """Install development dependencies"""
    cmd.run("pipenv install --dev")


@task
def test(cmd):
    """Run testcase"""
    cmd.run(f"{PIPENV_PREFIX} pytest", pty=True)


@task
def develop(cmd):
    """Install script in pipenv environement in development mode"""
    cmd.run(f"{PIPENV_PREFIX} python setup.py develop")


@task
def install(cmd):
    """Install script in pipenv environement"""
    cmd.run(f"{PIPENV_PREFIX} python setup.py install")


@task
def reformat(cmd):
    """Reformat python files throguh black"""
    black_args = ["-l 119"]
    target_fils = ["atta", "scripts", "test", "setup.py", "tasks.py"]

    cmd.run(f"black {' '.join(black_args)} {' '.join(target_fils)}")


@task
def flake8(cmd):
    """Check style through flake8"""
    cmd.run(f"flake8")


@task
def mypy(cmd):
    """Check style through mypy"""
    mypy_arguments = ["--ignore-missing-imports"]
    packages = ["atta", "test"]
    cmd.run(f"mypy {' '.join(mypy_arguments)} -p {' -p '.join(packages)}")


@task(pre=[flake8, mypy])
def lint(cmd):
    """Check style throguh linter (Note that pylint is not included)"""
    pass


@task
def pylint(cmd):
    """Check style through pylint"""
    targets = ["atta", "test", "scripts", "setup.py", "tasks.py"]
    cmd.run(f"pylint {' '.join(targets)}")
