## How to contribute

### Step 1. Fork this repository to your GitHub

### Step 2. Clone the repository from your GitHub

```sh
git clone https://github.com/[YOUR GITHUB ACCOUNT]/pycontw-postevent-report-generator.git
```

### Step 3. Add this repository to the remote in your local repository

```sh
git remote add upstream "https://github.com/pycontw/pycontw-postevent-report-generator"
```
You can pull the latest code in master branch through `git pull upstream master` afterward.

### Step 4. Check out a branch for your new feature

```sh
git checkout -b [YOUR FEATURE]
```

### Step 5. Install Prerequsite

```sh
python -m pip install pipx
python -m pipx install pipenv invoke
python -m pipx ensurepath
```

### Step 6. Setup Devlopment Environment

```sh
inv env.init-dev
```

### Step 6. Work on your new feature

### Step 7. Run test cases
Make sure all test cases pass.

```sh
inv test.cov
```

### Step 8. Run test coverage
Check the test coverage and see where you can add test cases.

```sh
inv test.cov
```

### Step 9. Reformat source code

Format your code through `black` and `isort`.

```sh
inv style.reformat
```

### Step 10. Run style check
Make sure your coding style passes all enforced linters.

```sh
inv style
```

[Optional] Check your coding style through `pylint`. Note that you do not have to fix all the issues warned by `pylint`.

```sh
inv style.pylint
```

### Step 11. Run security check

Ensure the packages installed are secure

```sh
inv secure
```

*[Optional]* Check whether there is common security issue in the code. Note that you do not have to fix all the issues warned by `bandit`

```sh
inv secure.bandit
```

### Step 12. Check the installed cli is runnable

```sh
inv build.test-cli
```

### Step 13. Create a Pull Request and celebrate 🎉
