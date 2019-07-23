# Dajngo Basic Blog
This is a basic blog application created using django
Inorder to run this blog create a virtual enviornment and install all the required libraries.
## Steps

 
#### 1.Creating the virtual enviornment

    virtualenv blog
#### 2.Activating the virtual enviornment

    cd blog 
    ./Scripts/activate
the above command is used on windows
#### 3.Cloning the Repository

    git clone https://github.com/justinjohnymathew/olakudda_django_blog.git
#### 4.Installing the required libraries

    cd olakudda_django_blog
    pip install -r requirments.txt
#### 5.Applying the database migrations
This migrations are done inorder to create database tables depending on the model used

    python manage.py makemigrations
    python manage.py migrate
#### 6.Creating a Superuser
Inoreder to access the admin panel a superuser account is necessary 

    python manage.py create superuser
#### 7.Running The Server

    python manage.py runserver

