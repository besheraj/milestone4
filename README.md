[![WebSite](media/stepuni.png)]((https://stepuni-milestone4.herokuapp.com/))
# Stepuni "Milestone 4" Project:
Stepuni is a web application designed to help match students with the right education or university program.
easy to use.
live version on: [link to live version!](https://stepuni-milestone4.herokuapp.com/)

# User Experience (UX):

## User Stories:

### First Time Visitor Goals:
a. As a First Time Visitor, I want be able to easily navigate throughout the site to find content or use features and access the website from any device.
b. As a First Time Visitor, I want to be able to sign up for new account.
c. As a First Time Visitor, I want to be able to change my account's password.
d. As a First Time Visitor, I want to be able to change my account's email.
e. As a First Time Visitor, I want to be able to access services list within my account.
f. As a First Time Visitor, I want to be able to place order on any service.
g. As a First Time Visitor, I want to be able to get confirmation of my order by email and after checkout.
h. As a First Time Visitor, I want to be able to change my billing information within my account and save it there.
i. As a First Time Visitor, I want to be able to repurchase the service if my first payment wasn't a success.
j. As a First Time Visitor, I want to be able to access the service page after purchasing a service.

### Returning User Goals:
a. As a Returning Visitor, I want to be able to access my order history.
b. As a Returning Visitor, I want to be able to check my current services.

### Frequent User Goals:
a. As a Frequent User, I want to check if there is any new services available.

# Features:
[link to screenshots of the website](design.md)

## Current Features:
* Responsive design that works perfectly on any device.
* Ability to Sign up for new account.
* Ability to login.
* Ability to change account's password.
* Ability to change account's email.
* Ability to Access service list only after login.
* Ability to checkout and pay for the service.
* Ability to access the service after successful payment.
* Ability to change billing information and save it.
* Ability to access the purchased service within my account.
* Confirmation email to verify my email.
* Confirmation email after a successful order.
* The purchased services will become visible in the service list as the button will change from checkout to access service.

## Future Features:
* Ability to do the quiz within the application instead of using google forms.
* Ability to get full report directly after completing the quiz.
* Ability to Login using social media accounts such as facebook or google account.

# Technology:
* **Languages**:HTML5, CSS3, Javascript, Python.
* **Frameworks**: Bootstrap, Django, Jingja, Jquery.
* **Databases**: Sqlite3 and PostgresSQL.
* **Pycharm**: This whole project code written using pycharm and the code following PEP8.
* **Github**: The whole project committed and pushed to github repository and published on Github pages.
* **Google Forms**: Used to design the service (quiz).
* **Payments**: Stripe.
* **Heroku**: Deployed on Heroku.
* **AWS S3 Bucket**: Used to load static and media files for the project.

# Testing:
## UI Testing:
UI testing has been done Manually check this link for [details](testing.md)
## Code validation:
* CSS code passed by W3schools CSS jigsaw without errors.
* Python code is consistent in style and conforms to the PEP8 style guide using Pycharm.

# Deployment:
This site is deployed to heroku and the versioning was done with git and the Repository is hosted on Github.

**Required tools**:
* IDE of Choice.
* Python3, PIP & Git should be installed.
**Required accounts**:
* Stripe
* AWS S3 Bucket
* Gmail
* Google forms
## Local Deployment: 
Official Github Documentation on cloning a repository: [Github-cloning](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository)

1. Navigate to Main Page of the repository
2. Click on "Code" button
3. Choose "Clone with HTTPs" & copy URL
4. Open Terminal
5. Change the current working directory to preferred location
6. Type git clone and past copied URL git clone https://github.com/besheraj/milestone4.git
7. Press Enter to create local Clone - Make sure your environment supports python3 -
8. Type pip3 install -r requirements.txt into Terminal
9. Setup the environment variables. This process is different depending on the used IDE. Gitpod supports global Environments for the development process. Therefore they were stored in the settings. The following variables are needed:    
`DEVELOPMENT=True`     
`STRIPE_PUBLIC_KEY = <YOUR STRIPE_PUBLIC_KEY>`     
`STRIPE_SECRET_KEY = <YOUR STRIPE_SECRET_KEY>`      
`STRIPE_WH_SECRET = <YOUR STRIPE_WH_SECRET>`     
10. Migrate the models and create the database by typing the following commands into the terminal:
python3 manage.py makemigrations
python3 manage.py migrate
11.Create a superuser for accessing the django admin view with the following command: python3 manage.py createsuperuser You will be asked for an email address, username and password.
12.You should be all set and when using the command python3 manage.py runserver the project should run.
13.You can access the django admin view by adding ~/admin to the end of your (local) URL.
14. you can add a service using admin access by clicking on "services" then "add service" or you can use your superuser login directly to the website click on "My Account" then "add quiz", in order to add quiz you will need the put the ifram src link in the "Quiz" field, [more about how to get the link from google forms here](https://support.google.com/a/users/answer/9308623?hl=en).

## Deployment to Heroku: Step-by-Step Instructions
This project is deployed to Heroku. For the deployment the following steps were/are necessary:

1. Create/Log in to your Heroku account and create a new App.
2. Install Heroku Add-on Heroku Postgres from the Resources tab. The free Hobby Dev version is fine. Now click the Provision button to add it to your project.
3. Create requirements.txt from your project with the help of pip3 freeze --local > requirements.txt (already provided within the repository)
4. Create a Procfile `echo web: gunicorn puffins.wsgi:application > Procfile `(already provided within the repository)
5. Commit changes to Git git add . followed by `git commit -m "Deploy: Updated Procfile"` (already provided within the repository)
6. Set the environment variables in Heroku Settings > Reveal Config Variables The following Variables must be set:
`USE_AWS = TRUE`  
`AWS_ACCESS_KEY_ID = <YOUR AWS_ACCESS_KEY_ID> `  
`AWS_SECRET_ACCESS_KEY = <YOUR AWS_SECRET_ACCESS_KEY>`  
`DATABASE_URL = <YOUR DATABASE_URL>` (Set by Heroku Postgres)  
`EMAIL_HOST_USER = <YOUR EMAIL_HOST_USER>`  
`EMAIL_HOST_PASSWORD = <YOUR EMAIL_HOST_PASSWORD>`  
`DEFAULT_FROM_EMAIL = <YOUR DEFAULT_FROM_EMAIL>`    
`STRIPE_PUBLIC_KEY = <YOUR STRIPE_PUBLIC_KEY>`    
`STRIPE_SECRET_KEY = <YOUR STRIPE_SECRET_KEY>`     
`STRIPE_WH_SECRET = <YOUR STRIPE_WH_SECRET>`  
7. Extract the DATABASE_URL Value from the Heroku Settings and set it up in your IDE or local .env file. Make sure to keep this DATABASE_URL a secret and definitely don't commit it to Github.
8. To test if the Postgres database is connected to your IDE you can make use of the command python3 manage.py showmigrations. This should show undone migrations for all models.
9. Now migrate the models and create the postgres database on heroku by typing the following commands into the terminal:
python3 manage.py makemigrations
python3 manage.py migrate
10. Create a superuser for the Postgres database for accessing the django admin view with the following command: python3 manage.py createsuperuser You will be asked for an email address, username and password.
11. Log in to heroku from your terminal heroku login
12. Add existing repository to Heroku heroku `git:remote -a <your repository>`
13. Push changes to Heroku git push heroku master
14. Now go to your S3 account. There bucket should already contain a folder called static. To upload the product images create a new folder called media. And add the files to this folder. Make sure to grant public read access to these objects.
15. Finally, visit the app url from heroku and check out your great site!

# Future Improvement 
Will fix the misspelling variables and page names allover the code. 

# Credits:
* I got the inspiration to make this project as I used some of the styling applied on it from code institute "Project - Boutique Ado".
* The background hero image and main page theme was imported from https://startbootstrap.com/ 

