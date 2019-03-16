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
g) The homepage does display the 10 most recent posts, and then pagination comes into play to sift through the pages of posts
h) Users should be able to upload text files as posts (COULDN'T GET THIS TO WORK)
i) Users should be able to type posts into a text field on the post creation page

5. Security
a) Data encryption:
  Data is encrypted.
  Installed django-sslserver and ran that with my local machine to generate SSL cert and key then run 'python manage.py runsslserver' to enable HTTPS instead of HTTP.
  
b) File uploads
c) XSS
d) CSRF
e) SQLite
f) Secure authentication and authorization theme

Message from creator:
Very inexperienced when it comes to web development or software development in general. This is the best I was able to conjure up with a lot of help from the internet. No previous experience with web development(bridged from Comp. Eng.) but I must say that I had a lot of fun creating this website and I learned A LOT. Thank you very much. 
 
