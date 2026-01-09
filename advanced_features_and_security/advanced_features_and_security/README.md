\# Managing Permissions and Groups in Django



This application demonstrates how to use Django groups and custom permissions

to control access to different parts of the application.



\## Custom Permissions

The following permissions are defined in the Book model:

\- can\_view

\- can\_create

\- can\_edit

\- can\_delete



\## Groups

The following groups should be created using the Django admin panel:

\- Viewers: can\_view

\- Editors: can\_view, can\_create, can\_edit

\- Admins: can\_view, can\_create, can\_edit, can\_delete



\## Views Protection

Views are protected using Django's @permission\_required decorator to ensure

only authorized users can perform specific actions.



