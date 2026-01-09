\# Security Best Practices in Django



This project implements Django security best practices to protect against

common vulnerabilities such as XSS, CSRF, and SQL Injection.



\## Security Settings

\- DEBUG is set to False

\- SECURE\_BROWSER\_XSS\_FILTER enabled

\- SECURE\_CONTENT\_TYPE\_NOSNIFF enabled

\- X\_FRAME\_OPTIONS set to DENY

\- CSRF\_COOKIE\_SECURE and SESSION\_COOKIE\_SECURE enabled



\## CSRF Protection

All forms include Django's CSRF token.



\## Secure Data Handling

\- Django ORM is used to prevent SQL injection

\- Django Forms are used for input validation



\## Content Security Policy

A basic Content Security Policy (CSP) is applied via HTTP headers.



