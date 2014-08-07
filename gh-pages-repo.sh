#!/bin/bash
set -o nounset
set -o errexit

GITHUB_REPO=git@github.com:Triztian/triztian.github.io.git
OUTPUTDIR=$1

commit_msg=$(git log | grep '^\s\s*' | head -n1)
echo "Commit message: $commit_msg"

cd $OUTPUTDIR
ls $(pwd)

git init
git remote add origin $GITHUB_REPO
git add .
git commit -m "$commit_msg"
git push -f origin master