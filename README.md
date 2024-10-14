## Setup

### Requirements

- Python 3.11.3
- [direnv](https://github.com/direnv/direnv)
- [uv](https://github.com/astral-sh/uv)

### Install uv

```
# With pip
pip install uv

# With Homebrew.
brew install uv
```

### Install Python

If Python 3.11 is not installed on your system, install it using the following command:

```
uv python install 3.11
```

### Install packages

To sync the project's development dependencies, use the following command:

```
uv sync --dev
```

When this command is executed, a virtual environment named `.venv` will be automatically created in the project's root directory (if it does not already exist). After that, all the necessary packages for development will be installed in this virtual environment. This includes any features specified as experimental, ensuring a complete set of tools and libraries required for the development of the project.

(Optional): Activate the virtual environment:
Note: If you do not activate you cannot do python xyz.py but you can still do uv run python xyz.py

```
source .venv/bin/activate
```

### Upgrade packages

If you want to upgrade all packages:

```
uv lock --upgrade
```

If you want to upgrade specific package:

```
uv lock --upgrade-package langchain
```

### Execute

If there is an executable main.py, you can run it with a command like this:

```
uv run python main.py
```

### Run

For the package to run, it will require langchain API key and required model's API keys such as OpenAI's Keys.

1. Save the API keys in the .env file
2. Create .envrc

```
echo 'dotenv' > .envrc
```

3. Make the `.env` file accessable to `direnv`. Note: if you are using zsh, run

```
eval "$(direnv hook zsh)"
direnv allow .
```
