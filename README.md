# Energy Saver Application

### Overview

This project was started in February 18, 2019 by Patrick Burris for Chris Branca. This application manages users for the purpose of finding them better electric bills.

### Technology Stack

This application is built using Python and HTML/CSS/JavaScript. The main services used are:

- **Heroku**: Deployment and Application management SaaS
- **PostgreSQL**: Relational database hosted by Heroku
- **SendGrid**: Email service hosted by Heroku
- **Stripe**: Payment platform

The backend is built with [Flask](http://flask.pocoo.org/) and deployed to [Heroku](https://heroku.com) using [Git](https://git-scm.com/). I am also using flask blueprints to keep the application as flexible as possible.

The frontend is built using [Parcel](https://parceljs.org/).

### Folder Structure

- **energy\_saver.py** - Application entry
- **Procfile** - Tells Heroku how to start the application
- **package.json** - Application information for the frontend build process
- **requirements.txt** - All of the Python packages that need to be installed
- **frontend**
  * **styles** - Holds the `.scss` files
  * **scripts** - Holds the `.js` files
  * **styles.js** - Script that parcel uses to build the `.scss` files into `.css` files
  * **scripts.js** - Script that parcel uses to transpile the `.js` files
- **migrations** - SQLAlchemy (ORM) migrations, don't mess with this
- **app**
  * **\_\_init\_\_.py** - Main flask entry into the app
  * **config.py** - Configuration class
  * **email.py** - Email functionality
  * **cli.py** - CLI configuration
  * **auth** - Auth blueprint
  * **main** - Main blueprint
  * **payments** - Payments (Stripe) blueprint
  * **errors** - Errors blueprint
  * **models** - ORM models
  * **templates** - Jinja2 templates
    - **partials** - partials/components
    - **auth** - Auth templates
    - **email** - Email templates
    - **error** - Error templates
    - **user** - User templates
    - **layouts** - Base layouts that other templates build on
    - **main** - Main templates (FAQ, homepage)
  * **static** - Static files
  * **tests** - All tests


### Running Locally


**Set up**

Make sure you have Python 3.5+ and Node 8.0+

1. Run `python -m venv venv` to create you virtual environment
2. Run `pip install -r requirements.txt`
3. Run `npm install`
4. Set up your `.env` file using the variables seen bellow in the environment section

**Running**

1. Run `flask frontend run && flask run`
2. Open your browser and go to `http://localhost:5000`
3. To develop scripts/styles, open another terminal and in the application folder run `flask frontend watch`


### Deploying

Make sure you are logged into Heroku and have the remote repository set. Once you do you can run `git push heroku master`


Copyright 2019, Patrick Burris, Chris Branca, All rights reserved.
