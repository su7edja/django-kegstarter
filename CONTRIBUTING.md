How to contribute
=================

* Fork
* Code
* Pull-request =)


A pull request is the start of a conversation on how to do something.
Feel free to make a PR early on so we can all collaborate.

Before a PR is merged it should be squashed down to one or two commits
so that fixes to tickets are one logical step. If there's major movement
that needs to happen it should happen on a branch, but all "Work in
progress" or "fixing derp" commits should be squashed before merging
to master.


Testing Requirements
====================

100% coverage is really nice to have, but not strongly required. Any
features that are added need to have good test coverage both demonstrate
that the code works as intended and any data validation logic is robust.


Getting Setup
=============
* [boot2docker](http://boot2docker.io/)
* [docker-compose](http://docs.docker.com/compose/install/)

Getting a running local server should be pretty easy at this point
* `docker-compose up` should start both a postgres server and a django
server (via `manage.py runserver 0.0.0.0:8000`)
* `docker-compose run web manage.py syncdb` will get your DB setup
* `boot2docker ip` will tell you what to connect to. (probably something
  like 192.168.59.103 or .104)
* In a brower go to that IP with :8000 (just like you would for a
  manage.py runserver if you ran it on your localhost) and you should
  see the site!

Note this does not do any `manage.py migrate` or `manage.py syncdb`
runs, so you'll need to do that via `docker-compose run web [COMMAND]`
