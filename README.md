# Alphonce's Portfolio

## ABOUT

### This Django web app serves as a personal portfolio. It showcases my skills, projects, and contact information.You can easily customize content and styles to make it your own.

## THE PROCESS
* Set the evironment for the project
* Run pip install django
* Start project using django-admin startproject project_name
* Start an app using django-admin startapp app_name . 
Include the dot after the app_name so that django does not create redundant file directory
* Add your app to the list of installed app in the settings.py file
# 6. Create a view in the views.py and return a simple html page
# 7. Add the view to the app_names's urls.py
# 8. Create a templates directory within the app_name
# 9. Create a basic html file home.html in the templates dir
# 8. Create a urls.py file in the project's dir and update it to include the app_name's urls
# 10. Run the server using python manage.py runserver command
Ensure that the app is returning the basic html page before adding more functionalities
# 11. Add a model for the projects
# 12. Run migrations
# 13. Create a superuser.... python manage.py createsuperuser
# 14. Register the model into the admin.py
Go to the /admin page on the local host and add a project
