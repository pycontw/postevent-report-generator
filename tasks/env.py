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
