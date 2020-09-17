# portofolio
This website will be our (@frannajaya and @ryanrustandi) portofolio.

# Getting Started
Get the repository use this command
```git clone https://github.com/frannajaya/portofolio.git```

Then you should using an isolated python package so this project will not affect by other project you are doing follow this instruction below

Install python 3 on your machine, then run this command below 
```pip install virtualenv```
```virtualenv venv```

after create the virtual env, then run this command below (if your machine is Windows) to activate the virtual environment for development
```venv/Scripts/activate```

Then after that command you should install all the package already used in this project by running this command below
```pip install -r requirements.txt```

Then you are ready to go to running this Django Project

### Updating requirements
Updating requirements is important before you want to push your implementations to github, use this command below
```pip freeze > requirements.txt```
