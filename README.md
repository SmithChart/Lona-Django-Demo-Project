Lona Django Database Demo Project
=================================

This is a simple demo project with Lona, Picocss and Django as Database backend.

This project is intended as a simple starting point to create your own Web App with a full-blown database backend :-)

In this demo, we will use SQLite as database backend.
But once you figure out how the Django database stuff works, you can still switch to something full-blown, eg.
Postgres.

Try the Demo
------------

```
$ make db
$ make super-user
$ make server
```

And then go to `http://localhost:8080`.
Log in with the credentials you've just entered :-)

Make Changes
------------

* Your own Django models go into `lona_project/database/models.py`.
* Migrations live here: `lona_project/database/migrations/`.
* If you want it to be available in the Django Admin register your model in `lona_project/_django/admin.py`.
* The Django `manage.py` can be used as follows: First `source env/bin/activate`, then run `lona_project/manage.py`.
* Add your views to `lona_project/views/`.
* Afterwards define routes to the views in `lona_project/routes.py`.
* Want to change the Picocss menu? This resides in `lona_project/settings.py`.

How to host
-----------

I am just running the lona application server with systemd and
serve it using my apache webserver.
The database is just *sqlite* since I do not expect any heave load on this tooling.
See examples in `contrib/`.
