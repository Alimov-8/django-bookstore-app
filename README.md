# django-bookstore-app 
### 📚 Production websites with Python & Django (WILLIAM S. VINCENT) 
#
 ### Getting Started
    • Setup Dev Environment
    • Initial Setup Python, Django, Docker, Postgresql
 #
 ### 1. Custom User Model
  ##### ↪️ Commits:
    • Custom User Model
        Important: Start custom user model from the very first migrate command you run,
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

 ### Unit Testing
  ##### Django co-founder Jacob Kaplan-Moss, “Code without tests is broken as designed.”
    Test Types:
        1. Unit tests are small, fast, and isolated to a specific piece of functionality
        2. Integration tests are large, slow, and used for testing an entire application or a user flow
           like payment that covers multiple screens
    
  #  
  ##### ✏️ Topics:
    📌 Docker & Postgresql with Django
    📌 Custom User Model
    📌 Unit Tests

  
  # 
  ##### 📄 Summary:
     1. Bookstore project is now running with Docker and PostgreSQL and configured a
        custom user model. 
 
