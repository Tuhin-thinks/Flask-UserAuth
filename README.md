# Flask-UserAuth
Simple Flask webapp to demonstrate user-athentication.


_
# Inititalize App Database
On the terminal execute the following lines:

```bash
$ python3

>>> from project import db, create_app
>>> db.create_all(app=createapp())
```

If this runs correctly, congrats! your database is created!

# App Initialization
```bash
$ export FLASK_APP=project
$ export FLASK_ENV=development
$ export FLASK_DEBUG=1
$ flask run
```
_(flask run should launch your flask application on localhost:5000)_

# Requirements
Use pip install \<name\> to install the required modules.
```Text
flask
flask-sqlalchemy
flask-login
```
## Preview of the application
<div class="banner">
    <div style="display:inline-block;">
        <img src="https://github.com/Tuhin-thinks/Flask-UserAuth/blob/main/images/signup.png" width="300" height="auto">
    </div>
    <div style="display:inline-block;">
        <img src="https://github.com/Tuhin-thinks/Flask-UserAuth/blob/main/images/login.png" width="300" height="auto">
    </div>
    <div style="display:inline-block;">
        <img src="https://github.com/Tuhin-thinks/Flask-UserAuth/blob/main/images/home.png" width="300" height="auto">
    </div>
</div>
