# AddressBook
Simple Address Book application to store and maintain contacts.

## Features:
1. User sign-up
2. User log-in
3. User log-out
4. View all contacts
5. Add contact
6. View contact
7. Delete contact
8. Search contacts
9. Filter contacts based on first letter

## Install and Run
Prerequisite - python 2.7.10

Install django

  ```python pip -m install django==1.11```

Try sudo if permission denied

  ```sudo python -m pip install django==1.11```

Clone the git repo

  ```git clone https://github.com/jagadeesh545/AddressBook.git```

Move to project folder

  ```cd path/to/project/AddressBook/```

Create project database schema

  ```python manage.py migrate```

Create super user

  ```python manage.py createsuperuser```

Run the django local server

  ```python manage.py runserver```

Open http://127.0.0.1:8000
