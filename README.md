Activate Virtual enviroment - source myenv/bin/activate
get into the project - cd blog
now commmand - python maange.py runserver

/admin - admin access where you can create post , comment and category
username - AbhishekShakya
password - blog123#


blog/register  --- thought this you first register the if you you are and the loggedin into it.
blog/create-post/ --  here you can create a post if you are logged in.
blog/posts/ --  It will list all the posts.
blog/posts/<int:pk>/ -- this will give you the post details with the id associated to it and here you can also edit it if you have the permission(if you are the owner of the post).
blog/users/ --  this will list all the users', UserList.as_view(), name='user-list' ),
blog/users/<int:pk>/ -- this will give you the specific user with the userid accociated with user , you can also edit '.
blog/comments/  -- for comments.
blog/comments/<int:pk>/', -- this will give the comments with the specific id passed to it and may edit if you are the author.
blog/posts/<int:post_id>/comments/' -- this will give the post id and you can also edit it here .
blog/user/comments -- this will give all the comments done by the user who is loggedin.
