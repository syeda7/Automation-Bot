
#!/usr/bin/env bash
# Requires: gh CLI installed and authenticated 'gh auth login'
# Usage: ./create_repo_gh_cli.sh repo-name --private

REPO_NAME="$1"
PRIVATE_FLAG="$2"  # use --private or --public
if [ -z "$REPO_NAME" ]; then
  echo "Usage: $0 repo-name [--private | --public]"
  exit 1
fi

gh repo create "$REPO_NAME" ${PRIVATE_FLAG:-"--private"} --confirm --description "Created with Automation-Bot"
echo "Created $REPO_NAME"
