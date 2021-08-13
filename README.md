# django-bookstore-app 
### 📚 Production websites with Python & Django (WILLIAM S. VINCENT) 
#
  ##### ✏️ Topics:
    📌 Docker & Postgresql with Django
    📌 Custom User Model
    📌 Unit Tests
    📌 User Registration
    📌 Static Assets
    📌 Advanced User Registration
    📌 Summary
 #
 ### Getting Started
    • Setup Dev Environment
    • Initial Setup Python, Django, Docker, Postgresql
 #
 ### 1. Custom User Model
  ##### ↪️ Commits:
    • Custom User Model
        ❗️ Start custom user model from the very first migrate command you run,
        you’re in for a world of hurt because User is tightly interwoven with the rest of Django
        internally. It is challenging to switch over to a custom user model mid-project.
        
    • Custom User Forms
    • Custom User Admin
    
    • Superuser ($ docker-compose exec web python manage.py createsuperuser)
        A good way to confirm our custom user model is up and running properly is to create a superuser
        account so we can log into the admin. This command will access CustomUserCreationForm under
        the hood
        
    • Unit Tests
        Testing Templates, Testing Creating User, Testing Creating Superuser
 #
 ### 2. Unit Testing
  ##### Django co-founder Jacob Kaplan-Moss, “Code without tests is broken as designed.”
    ❗️ Django projects quickly grow in size where it’s impossible to remember all 
    the working pieces in your head working on a team, it is a nightmare to work
    on an untested codebase. Who knows what will break?
    
    Test Types:
        1. Unit tests are small, fast, and isolated to a specific piece of functionality
        2. Integration tests are large, slow, and used for testing an entire application or a user flow
           like payment that covers multiple screens
           
  ##### ↪️ Commits:
       • Testing URLs // SimpleTestCase
       • Testing Templates // status_code = 200 ?
       • Testing HTML // response contains 'Homepage' ?
       • setUp Method // set response to target so no longer need to define a response variable for each test
       • Resolve // views check can do is that HomePageView “resolves” a given URL path
       
 #   
 ### 3. User Registration
  ##### ↪️ Commits:
    • Auth App // Implementing log in and log out using Django’s own auth app
    • Auth URLs and Views
    • Homepage
    • Log In, Logout, Redirects
    • SignUp and Unit testing 
    
 #   
 ### 4. Static Assets
  ##### ↪️ Commits:
    • static config - url,root,dirs,finders // static files configuration for production 
    • static files and collectstatic // production-ready directory of all the static files in our project
    • HomePage, static AboutPage
    • Django Crispy Forms // The popular 3rd party package django-crispy-forms provides a host of welcome upgrades
    • Testing AboutPage // Unit Tests
    
 #   
 ### 5. Advanced User Registration
  ##### ↪️ Commits:
    Django AllAuth is really simple to integrate into your Django project, Django AllAuth
    will provide you user Registration, login, logout, email update, forgot password, and 
    many more features already implemented and ready to use. Django AllAuth also does data validation
    
    • django-allauth and Auth Backends // auth via e-mail too and django.contrib.sites
    • core mail backend // successful user registration emails to the command line console
    • built-in auth app URLs 
    • templates for allauth // allauth prefers they be located within a templates/account 
    • LogIn, LogOut, SignUp functionalities // {% url 'account_logout' %}
    • Email Only Login // settings.py
    • Tests for SignUp // django-allauth comes with its own tests. Tested only SignUp Page
  
  # 
  ##### 📄 Summary:
     1. Bookstore project is now running with Docker and PostgreSQL and configured a
        custom user model. 
        
     2. Configured templates and added the first page to project, a static homepage.
        Also added tests which should always be included with new code changes.
        
     3. Bookstore project is not the most beautiful site in the world, 
        but it is very functional at this point.
        
     4. Static assets are a core part of every website and in Django we have to 
        take a number of additional steps so they are compiled and 
        hosted efficiently in production
        
     5. We now have a user registration flow that works and can be quickly extended
        into social authentication if needed. In the next chapter we’ll add environment 
        variables to our project for greater security and flexibility
   
 
