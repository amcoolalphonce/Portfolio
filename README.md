# MY PORTFOLIO USING DJANGO FRAMEWORK

### Table of content
1. [ABOUT](#about)
2. [THE PROCESS](#the-process)
3. [MOULES INSTALLED](#modules-installed)
4. 
## ABOUT

### This Django web app serves as a personal portfolio. It showcases my skills, projects, and contact information.You can easily customize content and styles to make it your own.

## THE PROCESS
* Set the evironment for the project
* Run pip install django
* Start project using django-admin startproject project_name
* Start an app using django-admin startapp app_name . 
Include the dot after the app_name so that django does not create redundant file directory
* Add your app to the list of installed app in the settings.py file
* Create a view in the views.py and return a simple html page
* Add the view to the app_names's urls.py
* Create a templates directory within the app_name
* Create a basic html file home.html in the templates dir
* Create a urls.py file in the project's dir and update it to include the app_name's urls
* Run the server using python manage.py runserver command
Ensure that the app is returning the basic html page before adding more functionalities
* Add a model for the projects
* Run migrations
* Create a superuser.... python manage.py createsuperuser
* Register the model into the admin.py
* Go to the /admin page on the local host and add a project


## MODULES INSTALLED  
