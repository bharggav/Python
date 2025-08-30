# Git Commands Cheat Sheet

## Basic Commands
- `git init`  
    Initialize a new Git repository.

- `git clone <repository-url>`  
    Clone an existing repository.

- `git status`  
    Show the working directory status.

- `git add <file>`  
    Stage changes for commit.

- `git commit -m "message"`  
    Commit staged changes with a message.

## Branching
- `git branch`  
    List all branches.

- `git branch <branch-name>`  
    Create a new branch.

- `git checkout <branch-name>`  
    Switch to a branch.

- `git checkout -b <branch-name>` 
    Create a new branch & Switch to a branch.

- `git merge <branch-name>`  
    Merge a branch into the current branch.

## Remote Repositories
- `git remote -v`  
    Show remote repository URLs.

- `git push origin <branch-name>`  
    Push changes to a remote branch.

- `git pull origin <branch-name>`  
    Fetch and merge changes from a remote branch.

## Undo Changes
- `git reset <file>`  
    Unstage a file.

- `git checkout -- <file>`  
    Discard changes in a file.

- `git revert <commit-hash>`  
    Revert a specific commit.

## Logs and History
- `git log`  
    Show commit history.

- `git log --oneline`  
    Show a compact commit history.

- `git diff`  
    Show changes between commits or the working directory.

## Stashing
- `git stash`  
    Save changes for later.

- `git stash apply`  
    Reapply stashed changes.

- `git stash drop`  
    Remove a stash.

## Tags
- `git tag <tag-name>`  
    Create a new tag.

- `git push origin <tag-name>`  
    Push a tag to the remote repository.

- `git tag -d <tag-name>`  
    Delete a tag locally.

## For raising pr via git bash
- Install this application on windows (https://cli.github.com/?utm_source)

- `gh auth login`  
    Run in cmd and Authenticate .


## Create a feature branch
- `git checkout -b <branch-name>`

## Make changes, commit & push
- git add .
- ``git commit -m "Added new feature"``
- `git push origin <branch-name>`

## Create PR
- ``gh pr create --base main --head <branch-name> --title "New Feature" --body "This PR adds a new feature"``

## Add reviewers
- ``gh pr edit --add-reviewer alice --add-reviewer bob``
