from invoke import task, Collection

from tasks import env, test, style
from tasks.build import build_ns


@task
def secure(ctx):
    """Check package security"""
    ctx.run("pipenv check")


ns = Collection()
ns.add_collection(env)
ns.add_collection(test)
ns.add_collection(style)
ns.add_collection(build_ns)
ns.add_task(secure)
