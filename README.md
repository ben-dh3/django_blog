# Blog Made Using Django

The blog is designed to be purely functional, with posts written in Markdown and stored using PostgreSQL. It is possible to write posts in markdown, create tags, and display uploaded photos in a post. The posts are displayed on the home page with a date and time of when it was posted, along with a short summary of the post. Click the post and see the full post content.

Made using Python, Django, PostgreSQL, and deployed using Digital Ocean Cloud services.

I used Django to get experience with using frameworks to create websites, I was starting to learn Python at the time and this project was a good introduction.

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