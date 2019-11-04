from invoke import task

@task
def authors(ctx):
    """Print all the authors in this project"""
    
    result = ctx.run(
        "git log --pretty=format:\"%an <%ae>\"",
        encoding="utf-8",
        hide=True
    )

    authors = set(result.stdout.splitlines())
    authors = sorted(authors)

    for author in authors:
        print(author)


@task
def changelog(ctx, since):
    """Print the changelog since given git ref"""
    result = ctx.run(
        f"git log {since}..HEAD --format=%s",
        encoding="utf-8",
        hide=True
    )
    changes = result.stdout.splitlines()

    print(f"Changelog sine {since}:")
    for change in changes:
        print(f"- {change}")