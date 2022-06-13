## 1.5.1 (2022-06-13)

### Fix

- **jinja2**: release jinja2 version compatibility fix
- **jinja2**: release jinja2 version compatibility fix

## 1.5.0 (2020-12-13)

### Feat

- **2020**: 2020 customization
- **2019-2020**: 2019-2020 transition

### Fix

- **plot**: re-order seniority from lower to higher
- **io:yaml**: use safe_load to remove warning

## 1.4.0 (2020-05-20)

### Refactor

- **tasks**: apply tasks genertaed from the latest Lee-W/cookiecutter-python-template

## 1.3.0 (2020-04-26)

### Refactor

- **github-action**: regroup github actions

## 1.1.0 (2020-04-17)

### Refactor

- **tasks/build**: add clean flag to test_cli
- **contribute**: rename contribution.md as contribute.md
- **pre-commit**: set style related hooks stages to push
- **github-action**: rename publish job as check
- **config**: add mypy, flake8
- **pyproject**: add commitizen config in pyproject.toml
- **config**: add pytest, pytest-cov, commitizen config

### Fix

- **setup**: fix setup documentation path
- **setup**: fix documentaion path in setup.py
- **pipfile**: update pyyaml to 5.3.1
- **pre-commit**: fix run test hook
- **pre-commit**: do not pass_filenames to invoke tasks
- **tasks/style**: remove default from reformat
- fix path due to name change

### Feat

- **tasks**: add doc command for documentation related tasks
- **tasks/env**: add commitizen pre-commit hook to tasks
- **pre-commit**: add commitizen pre-commit hook
- **tasks/style**: add isort into reformat and rename original black task as black_check
- **tasks/env**: add setup-pre-commit-hook task

## 1.0.2 (2019-12-15)

## 1.0.1 (2019-12-15)

## 1.0.0 (2019-12-15)

### Feat

- **.cz**: add .cz for specifing version
- **tasks/git**: add commit for `cz commit` and bump for `cz bump`
- **tasks**: add black check into enforced style check
- **task**: add git authors, changelog tasks
- **task**: make secure a package and add bandit check task
- **tasks.py**: add test_cli, secure, init, clean_env tasks
- **report_generator**: rename atta to report_generator
- **setup**: rename command atta to rg-cli in setup
- **atta_cli**: support configrable output_path
- 🎸 fetch excel and fetch opass data
- **atta_cli**: support configrable output_path
- 🎸 fetch excel and fetch opass data
- **tasks**: add cov task to check test coverage
- **scripts**: make scripts a package
- **tasks.py**: add pylint task
- **tasks**: add mypy, flake8 style check
- **tasks**: add reformat task to reformat code through black
- **tasks.py**: add install, develop tasks

### Refactor

- **exporter**: include tr in _generate_html_rows
- **exporter**: implement _generate_html_rows and _generate_html_link utility functions
- **exporter**: replace old style string formation with f string
- **tasks**: separate tasks into different namespaces
- **tasks**: make tasks a package
- **tasks.py**: fix test-cli task and add it into drone ci
- **tasks.py**: use "git clean -Xdf" to clean files in .gitignore
- **tasks.py**: use "git clean -Xdf" to clean files in .gitignore
- 💡 remove unuse section 'topic'
- 💡 remove unuse section 'topic'

### Fix

- **Pipfile**: fix invoke version
- **.drone.yml**: fix invoke command change due to refactor
- **tasks**: add secure into invoke task
- **tasks**: fix build.test-cli
- **setup**: add manifest.in which is needed for packaging non-code file
- **atta_cli**: make options requried
- **Pipfile**: fix click version

## v1.0 (2018-08-26)
