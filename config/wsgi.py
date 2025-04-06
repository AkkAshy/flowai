"""
WSGI config for FlowAI project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()


"""{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc0Mzc2MDI2MCwiaWF0IjoxNzQzNjczODYwLCJqdGkiOiJhNWUxYjQxNmJjMTI0ZGJmOTc3NTBkNjdkOWExMDgwMyIsInVzZXJfaWQiOjF9.Dg5wfjjqgCl4AeSLVIXq7TOh013pqMhsbPyGQ7Aau9I",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQzNjc0MTYwLCJpYXQiOjE3NDM2NzM4NjAsImp0aSI6IjFhMzdjMDIyOTVmODQzZDJiZTQ2NDc1YjYzYjgwMWJlIiwidXNlcl9pZCI6MX0.nL8bIvG_MXjEh4aLaMmc4xQAeoU-u80PhfZYtXhhzk0"""