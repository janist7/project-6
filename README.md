# Recipe Website

## Description

This site is a recipe site that has authentification/authorization and uses CRUD operations to manipulate user added data.

### Prerequisites

Requires vagrant virtual machine
Requires a client secrets file at flask-bones/client_secrets.json. And changes to data-clientid in app/auth/templates/components/google_login.html

Requires .env file at flask-bones/.env with contents:
```
export DATABASE_URL=postgresql://$USER@localhost/flask_bones > /dev/null
export SERVER_NAME=localhost:5000 > /dev/null
export MAILCATCHER_PORT_1025_TCP_ADDR=0.0.0.0 > /dev/null
export MAILCATCHER_PORT_1025_TCP_PORT=1025 > /dev/null
export REDIS_PORT_6379_TCP_ADDR=0.0.0.0 > /dev/null
export REDIS_PORT_6379_TCP_PORT=6379 > /dev/null
export MEMCACHED_PORT_11211_TCP_ADDR=0.0.0.0 > /dev/null
export MEMCACHED_PORT_11211_TCP_PORT=11211 > /dev/null
export DB_PORT_5432_TCP_ADDR=0.0.0.0 > /dev/null
export DB_PORT_5432_TCP_PORT=5432 > /dev/null
export MAIL_USERNAME= _______ > /dev/null
export MAIL_PASSWORD= _______ > /dev/null
```
Last 2 rows are empty as they require a real gmail adress with a app password.

## Instalation and usage

1. Install Javascript dependencies:

    ```
    $ make assets
    ```

2. Setup database and seed with test data:

    ```
    $ make db
    ```

3. Run a local SMTP server:

    ```
    $ mailcatcher
    ```

4. Run the celery worker: (**note** - Celery needs to be running in seperate windows from server)

    ```
    $ make celery
    ```

5. Run local server:

    ```
    $ make server
    ```

## File structure

Has folowing main folders:
* **flask-bones** - *Contains project*
* **i18n** - *Translation file ---Not Used---*
* **instance** - *Contains secret key file*
* **migrations** - *---Not Used---*
* **app** - *Contains all files for the webpage*
* **auth** - *Contains all views, templates, controllers and forms for login/logout*
* **categories** - *Contains all views, templates, controllers and forms for Category CRUD operations*
* **database** - *Contains init file for creating the database*
* **recipes** - *Contains all views, templates, controllers and forms for Reecipe CRUD operations*
* **static** - *Contains static content, like css, js etc.*
* **templates** - *Contains main template and all modules and components for views.*
* **user** - *Contains all views, templates, controllers and forms for User accaunt management*
* **flask-bones/manag.py** runs server, **app/\__init__.py** initializes all needed data/extensions. **app/config.py** contains app configuration.
* **requirements.txt** contains all library requirements for project. (It is important to not change versions)

Content is generated from index.html, uses main.html layout.

## Built With

Project built with flask-bones

## Future plans

Integrate multiple projects into this page.

## Authors

* **Jānis Tidriķis** - *Initial work*

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/janist7/recipe-website/blob/master/flask-bones/LICENSE) file for details

## Acknowledgments and Thanks

Thanks to Billie Thompson for providing a nice readme [template](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2).
Thanks to Corey Burmeister for making a [flask mvc](https://github.com/cburmeister/flask-bones) base/example.