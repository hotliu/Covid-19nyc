## Covid-19nyc
Dashboard for visualizing Covid-19 cases in NYC

### Create Virtualenv
Follow this [AWS tutorial](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html)

### Set Up CodeCommit
From: [Youtube Tutorial](https://www.youtube.com/watch?v=ND8hujOoZ14)
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

### Prepare Flask app for Elastic Beanstalk

* Rename run.py to application.py 
* Replace code at the very bottom with:
```
# Run app server: https://dash.plot.ly/getting-started
if __name__ == '__main__':
    application.run(debug=True)
```
* In app.py, replace the last line with:
```
application = app.server
```
After deploying on elastic beanstalk, one might run into this error:
```
Script timed out before returning headers: application.py
```
[Link to fix the above error](https://stackoverflow.com/questions/41812497/aws-elastic-beanstalk-script-timed-out-before-returning-headers-application-p)

### Set up Elastic Beanstalk
Keep on doing everything from IAM user
Use Windows Power Shell where possible as eb config opens a file

```
$ eb init -p python-3.6 <project name>
$ eb create <environment name>
$ eb status <environment name>
$ eb deploy <environment name>
$ eb open <environment name>
$ eb logs <environment name>
$ eb config
```
Checklist:
* Do you have a default VPC? 
* Are all your regions consistent?
* Is your run.py named application.py?

### Redirect Custom Domain NameCheap to Elastic Beanstalk 
```
coronaviruscasesnyc.com 
covid19casesnyc.com
```

* Click on: Manage > Advanced DNS 
```
URL Redirect | Host: @ | Value: Elastic Beanstalk URL | Unmasked
URL Redirect | Host: www | Value: Elastic Beanstalk URL | Unmasked
```
* Wait 30 min
