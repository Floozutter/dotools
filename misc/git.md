# Git
## alt identity
[source: "How to configure multiple Git accounts in your computer" by Abhay Srivastav](https://blog.bitsrc.io/how-to-use-multiple-git-accounts-378ead121235)
1. generate and [link](https://github.com/settings/keys) alt ssh key:
```
ssh-keygen -t rsa -C tarkitten@vesselnest.site
cat ~/.ssh/tark_rsa.pub
```
2. append alt host to `~/.ssh/config`:
```
Host github-tark.com
  HostName github.com
  User git
  IdentityFile ~/.ssh/tark_rsa
```
extra - [test ssh key](https://stackoverflow.com/a/47250227):
```
ssh -T git@github-tark.com
```
3. clone repo using alt host:
```
git clone git@github-tark.com:tarkitten/dotools.git
```
4. [edit local config](https://stackoverflow.com/a/42167480):
```
git config user.name tarkitten
git config user.email tarkitten@vesselnest.site
```
3. [check global vs local config](https://stackoverflow.com/a/12254105):
```
git config --list
git config --list --local
```
4. [have fun!](https://opensource.com/article/19/7/create-pull-request-github)

## edit email globally
```
git config --global user.email me@floozutter.site
```

## edit AuthorDate and CommitDate
[source: "How can one change the timestamp of an old commit in Git?" on Stack Overflow](https://stackoverflow.com/questions/454734)
```
t="date"
GIT_COMMITTER_DATE="$t" git commit --amend --no-edit --date "$t"
```
