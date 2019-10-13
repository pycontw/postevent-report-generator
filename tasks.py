from invoke import task


@task
def clean(cmd):
    """Remove all the tmp files in .gitignore"""
    files_to_remove = []
    with open('.gitignore') as input_file:
        for line in input_file.readlines():
            if not line.startswith('#'):
                files_to_remove.append(line.strip())

    cmd.run(f"rm -rf {' '.join(files_to_remove)}")


@task
def init_dev(cmd):
    """Install development dependencies"""
    cmd.run("pipenv install --dev")


@task
def test(cmd):
    cmd.run("pytest", pty=True)
