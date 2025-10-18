
#!/usr/bin/env python3
"""
Create a repo using GitHub REST API (requests)
"""

import os, sys, argparse, json
from dotenv import load_dotenv
import requests

load_dotenv()

TOKEN = os.getenv("GITHUB_TOKEN")
USER = os.getenv("GITHUB_USER")

if not TOKEN:
    print("Set GITHUB_TOKEN in environment")
    sys.exit(1)

API = "https://api.github.com"

def create_user_repo(name, private=True, description=""):
    url = f"{API}/user/repos"
    payload = {
        "name": name,
        "private": private,
        "description": description
    }
    headers = {"Authorization": f"token {TOKEN}", "Accept": "application/vnd.github.v3+json"}
    r = requests.post(url, json=payload, headers=headers)
    if r.ok:
        print("Created:", r.json().get("html_url"))
    else:
        print("Error:", r.status_code, r.text)

def create_org_repo(org, name, private=True, description=""):
    url = f"{API}/orgs/{org}/repos"
    payload = {"name": name, "private": private, "description": description}
    headers = {"Authorization": f"token {TOKEN}", "Accept": "application/vnd.github.v3+json"}
    r = requests.post(url, json=payload, headers=headers)
    if r.ok:
        print("Created:", r.json().get("html_url"))
    else:
        print("Error:", r.status_code, r.text)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("name", help="repo name")
    parser.add_argument("--org", help="create repo in org")
    parser.add_argument("--private", action="store_true", default=False)
    parser.add_argument("--desc", default="")
    args = parser.parse_args()

    if args.org:
        create_org_repo(args.org, args.name, private=args.private, description=args.desc)
    else:
        create_user_repo(args.name, private=args.private, description=args.desc)

if __name__ == "__main__":
    main()
