"""
Install project requirements.
"""

from setuptools import setup, find_packages

setup(
    name="t-hauz_server",
    version="0.1.1",
    description='T-hauz Backend Service',
    packages=find_packages(),
    include_package_data=True,
    scripts=["manage.py"],
    install_requires=[
        "Django==2.2.10",
        "djangorestframework==3.11.2",
        "python-decouple==3.1",
        "dj-database-url==0.5.0",
        "whitenoise==4.1.3",
        "psycopg2-binary==2.8.3",
        "gunicorn==19.9.0",
        "django-cors-middleware==1.4.0",
        "whitenoise==4.1.3",
        "python-dateutil==2.8.0",
        "requests==2.22.0",
        "django-cors-headers==3.1.0",
        "djangorestframework-jwt==1.11.0",
        "django-grappelli==2.13.1",
        "graphene_django==2.6.0",
    ]
)
