# SSD_Assignment2

Software Requirements:
1. Administration
a) The application does have three tiers of users which are the Administrators, Users, and Visitors
b) All user tiers can list/search(primarily through url navigation(.../post/{name of post OR post ID number}/) and view public posts.
c) Admins can list, search, create, edit, update, and delete Users
d) The admin interface and functions aren't visible by Users or Visitors
e) Admins can list, search, enable, and disable posts but still can create/edit/modify 
f) Admins can login from a special administrator portal /admin/ 
g) Admins can logout

2. Users
a) Users can list, search, create, edit, update, and delete ONLY their own posts
b) Users can also list, search, and view private posts which they have been invited to. (COULDN'T GET THIS TO WORK)
c) Users can logout
d) Users can edit, update, and delete their own account and profile 
e) Users can configure "watch" words (COULDN'T GET THIS TO WORK)

3. Visitors 
a) Can create a new User account
b) Can login after creation of an account
c) can perform a password reset

4. Posts
a) Can be marked as Public or Private (COULDN'T GET THIS TO WORK)
b) Private posts can have a list of "invited" users (COULDN'T GET THIS TO WORK)
c) Posts work similarily to pastebin (yes) with the option to download the raw post as a text file (COULDN'T GET THIS TO WORK)
d) Posts have "short" URLS similar to pastebin. Not exactly like pastebin but could receive a shorter URL as long as you know the post id value
e) User should be able to configure a post expiration date (COULDN'T GET THIS TO WORK)
f) Posts can have titles
g) The 
