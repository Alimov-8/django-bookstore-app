# Online Bookstore System
#### https://8soft.pythonanywhere.com/about/
#### Production websites with Python and Django by WILLIAM S. VINCENT π
#
  ### Development Process
 Could apply to almost any new project
 
    π Docker & Postgresql with Django
    π Custom User Model
    π Unit Tests
    π User Registration
    π Static Assets
    π Advanced User Registration
    π Environment Variables
    π Email Services 
    
 Building out the Bookstore site itself
 
    π Books App
    π Reviews App
    π File/Image Uploads
    π Permissions
    π Search
    π Categories App
    π Shopping Cart Sessions
    
    π Summary
    
 #
 ### Getting Started
    β’ Setup Dev Environment
    β’ Initial Setup Python, Django, Docker, Postgresql
 #
 ### 1. Custom User Model
  ##### βͺοΈ Commits:
    β’ Custom User Model
        βοΈ Start custom user model from the very first migrate command you run,
        youβre in for a world of hurt because User is tightly interwoven with the rest of Django
        internally. It is challenging to switch over to a custom user model mid-project.
        
    β’ Custom User Forms
    β’ Custom User Admin
    
    β’ Superuser ($ docker-compose exec web python manage.py createsuperuser)
        A good way to confirm our custom user model is up and running properly is to create a superuser
        account so we can log into the admin. This command will access CustomUserCreationForm under
        the hood
        
    β’ Unit Tests
        Testing Templates, Testing Creating User, Testing Creating Superuser

    β’ CRUD functionality added for CustomUser

    β’ Slug field added for CustomUser // changing pk to slug to improve security

    β’ Profile view and Dashboard View added // Dashboard view is open to every
      registered user to check what kinda books exist on sale in other users profile
 #
 ### 2. Unit Testing
  ##### Django co-founder Jacob Kaplan-Moss, βCode without tests is broken as designed.β
    βοΈ Django projects quickly grow in size where itβs impossible to remember all 
    the working pieces in your head working on a team, it is a nightmare to work
    on an untested codebase. Who knows what will break?
    
    Test Types:
        1. Unit tests are small, fast, and isolated to a specific piece of functionality
        2. Integration tests are large, slow, and used for testing an entire application or a user flow
           like payment that covers multiple screens
           
  ##### βͺοΈ Commits:
       β’ Testing URLs // SimpleTestCase
       β’ Testing Templates // status_code = 200 ?
       β’ Testing HTML // response contains 'Homepage' ?
       β’ setUp Method // set response to target so no longer need to define a response variable for each test
       β’ Resolve // views check can do is that HomePageView βresolvesβ a given URL path
       
 #   
 ### 3. User Registration
  ##### βͺοΈ Commits:
    β’ Auth App // Implementing log in and log out using Djangoβs own auth app
    β’ Auth URLs and Views
    β’ Homepage
    β’ Log In, Logout, Redirects
    β’ SignUp and Unit testing 
    β’ Signup UserCreation form modified
    
 #   
 ### 4. Configure Static Assets Local/Production
  ##### βͺοΈ Commits:
    β’ static config - url,root,dirs,finders // static files configuration for production 
    β’ static files and collectstatic // production-ready directory of all the static files in our project
    β’ HomePage, static AboutPage
    β’ Django Crispy Forms // The django-crispy-forms provides a host of welcome upgrades
    β’ Testing AboutPage // Unit Tests
    
 #   
 ### 5. Advanced User Registration
  ##### AllAuth
    Django AllAuth is really simple to integrate into your Django project, Django AllAuth
    will provide you user Registration, login, logout, email update, forgot password, and 
    many more features already implemented and ready to use. Django AllAuth also does data validation
    
 ##### βͺοΈ Commits:   
    β’ django-allauth and Auth Backends // auth via e-mail too and django.contrib.sites
    β’ core mail backend // successful user registration emails to the command line console
    β’ built-in auth app URLs 
    β’ templates for allauth // allauth prefers they be located within a templates/account 
    β’ LogIn, LogOut, SignUp functionalities // {% url 'account_logout' %}
    β’ Email Only Login // settings.py
    β’ Tests for SignUp // django-allauth comes with its own tests. Tested only SignUp Page
    β’ django authall override password templates // for reset, change cases
  
 #   
 ### 6. Environment Variables
    Environment variables are variables that can be loaded into the operating environment of a
    project at run time as opposed to hard coded into the codebase itself. They are considered an
    integral part of the popular Twelve-Factor App Design methodology and a Django best practice
    because they allow a greater level of security and simpler local/production configurations.
    
    Why Secure? we can store truly secret informationβdatabase credentials, API
    keys, and so onβseparate from the actual code base. This is a good idea because using a version
    control system, like git, means that it only takes one bad commit for credentials to be added in
    there forever. Which means that anyone with access to the codebase has full control over the
    project. https://github.com/Alimov-8/django-bookstore-app/blob/main/config/settings.py#L14
  
  
 #   
 ### 7. [Email Services](https://github.com/pennersr/django-allauth/tree/master/allauth/) | [Documentation](https://docs.djangoproject.com/en/3.2/topics/email/)
 ##### βͺοΈ Commits:   
    β’ Confirmation Emails, Password reset/change 
        Fully configure email and add password change and password reset functionality.
        
  #      
  ### 8. Books App, List&Detail View, and UUID
  ##### βͺοΈ Commits:
    β’ Books App Models and Admin added
        verbosa name added to make admin panel understandable to client
        
    β’ URLs, Views, Templates, context object configs
        context_object_name = 'book_list' // object_list -> book_list: to make code clear 
    
    β’ DetailView with get_absoulte_url | pk,id,slug,uuid
        - get_absolute url
          reverse('book_detail', args=[str(self.id)])
          {% url 'book_detail' book.pk %} -> "{{ book.get_absolute_url }}"
          
        - id is a model field automatically set by Django internally to auto-increment
        
        id not ideal for a real-world project. There are two alternative approaches:
         
        - βslug,β a newspaper term for a short label for something that is often used in URLs
          e.g. django-for-professionals. But The main challenge with slugs is handling duplicates,
          though this can be solved by adding
          random strings or numbers to a given slug field. The synchronization issue remains though
          
        - UUID (Universally Unique IDentifier)  e.g. books/4301d961-0531-4ed8-8cac-396325b1c20c/
        
    β’ Unit Tests
    
    β’ Book CRUD functionality added // feature that allows users to sell thier books in   Bookstore

  
  #      
  ### 9. Reviews App, Foreign Keys
  ##### βͺοΈ Commits:
    β’ There are three possible types of foreign key relationships:
      One-to-one -> user profile
      One-to-many ->  one student can sign up for many classes
      Many-to-many -> each book could have more than one author and each author can write more
      than one book
    
    β’ Reviews App, Models FK, Admin TabularInline
    β’ Unit Tests
    
    β’ Reviews CreateView form added // links review to book and speficies its author
    β’ Context object added to Reviews // speficies book title for review
    β’ Reviews app created // books up become large then reviews app created 
    β’ login via email & username, update review by author 
    β’ Review DeleteView added // CRUD for Reviews ready
    
   #      
  ### 10. File/Image Uploads
  ##### βͺοΈ Commits:
    β’ Media Files Config:
      MEDIA_ROOT -> is the absolute file system path to the directory 
      for user-uploaded files
      MEDIA_URL -> is the URL we can use in our templates for the files

   #      
  ### 11. Permissions
  ##### βͺοΈ Commits:
    β’ Logged-In Users Only:
      login_required() decorator / LoginRequired mixin (class-based views)
      βBooksβ link it will automatically redirect not login user to the Log In 
      page and if you somehow knew the UUID of a specific book page youβd be
      redirected to Log In as well!

    β’ Custom Permissions:
      Can be add into model using Meta Class, and in the view can be used by 
      importing PermissionRequiredMixin and permission_required filed inside CBV

    β’ Groups & UserPassesTestMixin:
      The third permissions mixin available is UserPassesTestMixin which 
      restricts a viewβs access only to users who pass a specific test.
      An example of groups is if you have a premium section on your website,
      a user upgrading could switch them into the premium group and then 
      have access to however many specific extra permissions that involves.
    
    β’ Unit Tests

 #   
 ### 12. Search
  ##### βͺοΈ Commits:
    β’ Search Results Page
       Basic Filtering 
       Q Objects
       Forms and Search Form


 #   
 ### 13. Categories App 
  ##### βͺοΈ Commits:
    β’ Categories added | Books model&admin improved 

    β’ Categories View & Templates added // Categories Menu added into templates


 #   
 ### 14. Shopping cart & Ordering 
  ##### βͺοΈ Commits:
    β’ Cart App added | Session Settings, Expiration | Storing carts in sessions
    β’ Cart Views, Urls, Form & Templates added for sessions
    β’ Orders MVT added to control Cart and Items
    β’ Generating PDF invoices dynamically
      Extending the administration site with custom views


 
  # 
  ##### π Summary:
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
        into social authentication if needed. In the next chapter weβll add environment 
        variables to our project for greater security and flexibility
        
     6. Adding environment variables is a necessary step for any truly professional Django project.
     
     7. Configuring email properly is largely a one-time pain. But it is a necessary 
        part of any production website.  
        
     8. Bookstore project is now much clearer.
        Added a books model, learned how to change the URL structure, and
        switched to the much more secure UUID pattern
        
     9. Review app model added into books app,
        As the project grows it might also make sense to split reviews off into its own dedicated app.
        In general, keeping things as simple as possibleβadding foreign
        keys within an existing app until it becomes too large to 
        easily understandβis a solid approach

    10. This chapter demonstrated how to add user files to a project. 
        In practice it is straightforward,
        but the additional layer of security concerns makes it an 
        area worthy of focus at scale.

    11. Permissions and groups are a highly subjective area that vary widely 
        from project to project.

    12. Basic Searching is ready
        There are several third-party packages with enhanced features such as 
        django-watson or django-haystack however, given that weβre using 
        PostgreSQL as the database, we can take advantage of its full text search
        and other features which are built into Django itself.

    13. Creating the product catalog models, adding them to the administration site,
        and building the basic views to display the catalog
    
    14. 
