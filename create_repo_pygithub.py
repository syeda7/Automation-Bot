
#!/usr/bin/env python3
"""
Create repositories using PyGithub
usage:
    python create_repo_pygithub.py repo_name1 repo_name2 --private
"""
import os
import sys
from github import Github
from dotenv import load_dotenv
import argparse

load_dotenv()

TOKEN = os.getenv("GITHUB_TOKEN")
USER = os.getenv("GITHUB_USER")
DEFAULT_PRIVATE = os.getenv("DEFAULT_PRIVATE", "true").lower() in ("1","true","yes")

if not TOKEN:
    print("GITHUB_TOKEN missing in environment")
    sys.exit(1)

g = Github(TOKEN)

def create_repo(name, private=DEFAULT_PRIVATE, description=None):
    user = g.get_user() if not USER else g.get_user(USER)
    try:
        repo = user.create_repo(
            name=name,
            private=private,
            description=description or os.getenv("DEFAULT_DESCRIPTION", "")
        )
        print(f"Created repo: {repo.full_name} — {repo.html_url}")
    except Exception as e:
        print(f"Failed to create {name}: {e}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("names", nargs="+", help="Repository name(s) to create")
    parser.add_argument("--private", action="store_true", help="Make repo private")
    parser.add_argument("--public", action="store_true", help="Make repo public")
    parser.add_argument("--desc", help="Description")
    args = parser.parse_args()

    private = args.private if (args.private or args.public) else DEFAULT_PRIVATE
    if args.public:
        private = False

    for n in args.names:
        create_repo(n, private=private, description=args.desc)

if __name__ == "__main__":
    main()
#create single or multiple repos using PyGithub