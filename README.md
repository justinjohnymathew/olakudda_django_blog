# olakudda_django_blog

`pip install virtualenv` 
above one is used ony if virtualenv is not installed

create a virtualenviornment
`virtualenv olakudda`

`cd olakudda`

activate the virtual enviornment
`./Scripts/activate`

install django
`pip install django`

copy th e git repo to this folder
that is the present working directory is olakudda_django_blog
cd olakudda_django_blog

now the directory is olakudda_django_blog
the below steps are for creating database
`python manage.py makemigrations`

`python manage.py migrate`


the below code is for creating a superuser aka(mutalali) for the blog
`python manage.py createsuperuser`

now its time to run the server
`python manage.py runserver`

adin page can be accesed at localhost:8000/admin
login and add some blog contents

the templates of the blog are defined in blog/templates/blog
