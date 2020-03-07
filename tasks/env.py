from invoke import task


@task
def clean(ctx):
    """Remove virtual environement"""
    ctx.run("pipenv --rm", warn=True)


@task
def init(ctx):
    """Install production dependencies"""
    ctx.run("pipenv install --deploy")


@task
def init_dev(ctx):
    """Install development dependencies"""
    ctx.run("pipenv install --dev")


@task
def setup_pre_commit_hook(ctx):
    """Setup pre-commit hook to automate check before git commit and git push"""
    ctx.run(
        "pipenv run pre-commit install -t pre-commit \\"
        "pipenv run pre-commit install -t pre-push"
    )
