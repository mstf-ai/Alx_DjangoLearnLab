\# Managing Permissions and Groups in Django



This project demonstrates how to use Django custom permissions and groups

to control access to different parts of the application.



\## Custom Permissions

The Book model defines the following custom permissions:

\- can\_view

\- can\_create

\- can\_edit

\- can\_delete



\## Groups

The following groups should be created using the Django admin interface:

\- Viewers: can\_view

\- Editors: can\_view, can\_create, can\_edit

\- Admins: can\_view, can\_create, can\_edit, can\_delete



\## Views Protection

All sensitive views are protected using Django's @permission\_required decorator.



