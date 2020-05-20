from invoke import task

from tasks.common import VENV_PREFIX


@task(default=True)
def check_package(ctx):
    """Check package security"""
    ctx.run("export PIPENV_PYUP_API_KEY='' && pipenv check")


@task
def bandit(ctx):
    """Check common software vulnerabilities (Use it as reference only)"""
    ctx.run(f"{VENV_PREFIX} bandit -r -iii -lll --ini .bandit", pty=True)
