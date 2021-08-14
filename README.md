# django-bookstore-app 
### 📚 Production websites with Python & Django (WILLIAM S. VINCENT) 
#
  ##### ✏️ Topics:
    # Could apply to almost any new project
    📌 Docker & Postgresql with Django
    📌 Custom User Model
    📌 Unit Tests
    📌 User Registration
    📌 Static Assets
    📌 Advanced User Registration
    📌 Environment Variables
    📌 Email Services 
    
    # Building out the Bookstore site itself
    📌 Books App
    
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
 ### 4. Configure Static Assets Local/Production
  ##### ↪️ Commits:
    • static config - url,root,dirs,finders // static files configuration for production 
    • static files and collectstatic // production-ready directory of all the static files in our project
    • HomePage, static AboutPage
    • Django Crispy Forms // The django-crispy-forms provides a host of welcome upgrades
    • Testing AboutPage // Unit Tests
    
 #   
 ### 5. Advanced User Registration
  ##### AllAuth
    Django AllAuth is really simple to integrate into your Django project, Django AllAuth
    will provide you user Registration, login, logout, email update, forgot password, and 
    many more features already implemented and ready to use. Django AllAuth also does data validation
    
 ##### ↪️ Commits:   
    • django-allauth and Auth Backends // auth via e-mail too and django.contrib.sites
    • core mail backend // successful user registration emails to the command line console
    • built-in auth app URLs 
    • templates for allauth // allauth prefers they be located within a templates/account 
    • LogIn, LogOut, SignUp functionalities // {% url 'account_logout' %}
    • Email Only Login // settings.py
    • Tests for SignUp // django-allauth comes with its own tests. Tested only SignUp Page
  
 #   
 ### 6. Environment Variables
    Environment variables are variables that can be loaded into the operating environment of a
    project at run time as opposed to hard coded into the codebase itself. They are considered an
    integral part of the popular Twelve-Factor App Design methodology and a Django best practice
    because they allow a greater level of security and simpler local/production configurations.
    
    Why Secure? we can store truly secret information–database credentials, API
    keys, and so on–separate from the actual code base. This is a good idea because using a version
    control system, like git, means that it only takes one bad commit for credentials to be added in
    there forever. Which means that anyone with access to the codebase has full control over the
    project. https://github.com/Alimov-8/django-bookstore-app/blob/main/config/settings.py#L14
  
  
 #   
 ### 7. [Email Services](https://github.com/pennersr/django-allauth/tree/master/allauth/) | [Documentation](https://docs.djangoproject.com/en/3.2/topics/email/)
 ##### ↪️ Commits:   
    • Confirmation Emails, Password reset/change 
        Fully configure email and add password change and password reset functionality.

 
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
        
     6. Adding environment variables is a necessary step for any truly professional Django project.
     
     7. Configuring email properly is largely a one-time pain. But it is a necessary 
        part of any production website.  
 
