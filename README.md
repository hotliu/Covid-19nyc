### Covid-19nyc
Dashboard for visualizing Covid-19 cases in NYC

### Deploy to Elastic Beanstalk
### Set Up CodeCommit
* Grant IAM user CodeCommitAllAccess
* Go to console.aws.amazon.com and type in CodeCommit
* Create a new repository
* Create a new ssh key 
* upload .pub content to to IAM user > Security credentials > Upload SSH public key
* Copy new key after upload
* In root .ssh file do:
```
vi conifg
```
* Inside the file do:
```
Host git-codecommit.*.amazonaws.com
User <new, just copied key from IAM>
IdentityFile ~/.ssh/<ssh file name stored in root>
```
* In CodeCommit console, next to your repo, click "SSH"
* In git bash do:
```
ssh <copied ssh git-codecommit.us-....>
```
* Do regular git add ., git commit -m etc. 
* git remote -v should have the copied ssh git-codecommit.us... route

### Set up Elastic Beanstalk
```
$ eb init -p python-3.6 <project name>
$ eb create <environment name>
$ eb status
$ eb deploy
$ eb open
$ eb logs
$ eb config
```

