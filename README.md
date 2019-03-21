# project2-osvaldo-s-children

Example of a basic Django file structure:

[projectname]/                  <- project root
├── [projectname]/              <- Django root
│   ├── __init__.py
│   ├── settings/
│   │   ├── common.py
│   │   ├── development.py
│   │   ├── i18n.py
│   │   ├── __init__.py
│   │   └── production.py
│   ├── urls.py
│   └── wsgi.py
├── apps/
│   └── __init__.py
├── configs/
│   ├── apache2_vhost.sample
│   └── README
├── doc/
│   ├── Makefile
│   └── source/
│       └── *snap*
├── manage.py
├── README.rst
├── run/
│   ├── media/
│   │   └── README
│   ├── README
│   └── static/
│       └── README
├── static/
│   └── README
└── templates/
    ├── base.html
    ├── core
    │   └── login.html
    └── README

Source: https://django-project-skeleton.readthedocs.io/en/latest/structure.html