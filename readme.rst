Puliamo Terlizzi
================

Source code for the project Puliamo Terlizzi. This website is heavily based on some other amazing projects:

* Mezzanine + GeoDjango
* Bootleaf
* django-geojson
* OpenStreetMap data

Install
-------

* install SQlite
* install SpatiaLite
* install PySQlite compiling it with C bindings

  https://github.com/ghaering/pysqlite/issues/60

then

..code-block:: bash

  ./manage.py syncdb
