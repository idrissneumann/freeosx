#!/bin/bash

REPO_PATH="${PROJECT_HOME}/freeosx/"

cd "${REPO_PATH}" && git pull origin main || :
git push github main 
git push pgitlab main
git push bitbucket main
exit 0
