import os 
import sys
from sys import path
from os.path import dirname as dir

path.append(dir(path[0]))

from github import App

# Path to your GitHub app's private key 
if os.environ.get("PRIVATE_KEY_FILE") is None:
    print("Export the path to your GitHub app's private key via PRIVATE_KEY_FILE ")

if os.environ.get("APP_ID") is None:
    print("Export your GitHub app's ID via APP_ID")

if len(sys.argv) < 2:
    print("Usage: %s [githuborg/repository]" % (sys.argv[0]))
    exit()

github_repository = sys.argv[1]

gh = App()

(org, repository) = github_repository.split("/")

installation = gh.get_installation(org)

repo_url = installation.get_repository_url(github_repository)

print(repo_url)

