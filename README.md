
# Automation-Bot — Repo creation helpers

This small toolkit demonstrates multiple ways to create GitHub repos:
- PyGithub (`create_repo_pygithub.py`)
- REST API with `requests` (`create_repo_requests.py`)
- GitHub CLI wrapper (`create_repo_gh_cli.sh`)

## Setup
1. Copy `.env.example` → `.env` and add your `GITHUB_TOKEN`.
2. `pip install -r requirements.txt`
3. Run any script to create repos.

Use with care — do not commit `.env`.
