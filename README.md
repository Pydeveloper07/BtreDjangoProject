# BtreDjangoProject
This is a sample working dynamic webapplication built onto Django Framework and using PostgreSQL database-server. 
In this web application you can do following things as a user:
1. See the list of Properties by Rieltors
2. Get an additional information about a particular listing
*3. Make an inquiry for that property by filling out the make inquiry form
    # In this case both the rieltor and admin will be informed by email
4. You can register to the website
5. You can log in and log out form the website
6. If you are logged in, in a dashboard section you can see all your inquiries

As an admin
1. You can create, update and delete Rieltors
2. You can create, update and delete Listings
3. You also can monitor all the inquiries and users

#Extra
*3 - To configure email sending job, do the following tasks:
  1. Inside btre/settings.py file bottom enter the EMAIL_HOST_USER (which is your email)
    and EMAIL_HOST_PASSWORD (which is your email's password) and if it is not gmail
    change the EMAIL_HOST too.
  2. Inside contacts/views.py edit the send_mail() function
