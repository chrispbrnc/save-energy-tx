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
    - entry is `main.scss`
  * **scripts** - Holds the `.js` files
    - entry is `index.js`
- **migrations** - SQLAlchemy (ORM) migrations, don't mess with this
- **app**
  * **\_\_init\_\_.py** - Main flask entry into the app
  * **config.py** - Configuration class
  * **email.py** - Email functionality
  * **cli.py** - CLI configuration
  * **auth** - Auth blueprint
  * **control** - Admin blueprint
  * **main** - Main blueprint
  * **payments** - Payments (Stripe) blueprint
  * **errors** - Errors blueprint
  * **models** - ORM models
  * **templates** - Jinja2 templates
    - **partials** - partials/components
    - **auth** - Auth templates
    - **control** - Admin templates
    - **email** - Email templates
    - **error** - Error templates
    - **user** - User templates
    - **layouts** - Base layouts that other templates build on
    - **general** - Main templates (FAQ, homepage)
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

The master branch on Github is also rigged to trigger a build on Heroku.

### Environment Variables

```
FLASK_APP = This is the entry to the flask app, currently energy_saver.py

SECRET_KEY = This is a random string used for backend security

NOREPLY_EMAIL - This email sends out the verify-email/reset-password/etc. emails
ADMIN_EMAIL - This email gets the contact-me emails and the more-information alerts

SENDGRID_API_KEY - found in Sendgrid control panel inside the Heroku control panel

STRIPE_SECRET_KEY - found in the Stripe control panel
STRIPE_PUBLISHABLE_KEY - found in the Stripe control panel
```


Copyright 2019, Save Energy Tx, Chris Branca, All rights reserved.
