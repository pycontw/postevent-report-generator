from invoke import task

from tasks.common import PIPENV_PREFIX


@task(optional=["clean"])
def build(ctx, clean=True):
    """Build documentation locally"""
    argument = ""
    if clean:
        argument += " --clean"

    ctx.run(f"{PIPENV_PREFIX} mkdocs build {argument}")


@task
def serve(ctx):
    """Run local server"""
    ctx.run(f"{PIPENV_PREFIX} mkdocs serve")


@task
def deploy(ctx):
    """Deploy to github page"""
    ctx.run(f"{PIPENV_PREFIX} mkdocs gh-deploy")
