# Django Blog

I wrote this project to develop my Python skills, while learning Django, SQL and some DevOps - using DigitalOcean cloud services. It is possible to write posts, create tags, and display uploaded photos in a post. The posts are displayed on the home page with the date and time of when it was posted, along with a short summary. Click the post and see the full content.

Made using Python, Django, PostgreSQL.

In the future I intend to add the option to add more than one photo to a post and select where in the post to arrange them.

# How to Install and Run the Project

`pip install -r requirements.txt`

`python manage.py migrate` 

`python manage.py runserver`

### See Blog Post Creation Function:

`python manage.py createsuperuser`

Set the following in the terminal:
- username
- email
- password

`python manage.py runserver`

- Go to '/admin/' on local domain.

- Login using previously created details.

- Select 'Posts'

- Fill in the post and save.

- Now go back to the home page and see your post.

- Click the post and see the content.
