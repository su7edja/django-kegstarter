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

This guide is written primarily for OSX users.

Prequisite Software
-------------------

* [boot2docker](http://boot2docker.io/)
* [docker-compose](http://docs.docker.com/compose/install/)

Bootstrapping
-------------

* Run `boot2docker up` and copy the export commands it prints (you can print these commands again by running
  `boot2docker shellinit`).
* Connect `docker-compose` to the new VM by running the export commands from `boot2docker` in the terminal tab you want
  to use.
* `docker-compose up` should start a postgres server a django
  developement server (via `manage.py runserver 0.0.0.0:8000`) and an
  ember server.

Common Tasks
------------

* `docker-compose run backend manage.py migrate` will get your DB setup.
* `boot2docker ip` will tell you what to connect to. (probably something
  like 192.168.59.103 or .104)
  * To reach the frontend, enter that IP with :8080 in a browser.
  * To reach the backend (Django), enter that IP with :8000 in a browser.
* `docker-compose run backend py.test` will run the tests locally. [Travis](https://travis-ci.org) runs the full set of
  tests and static analysis tools (see travis.yaml), but it can be handy to run the Python tests before pushing.
* `docker-compose stop; boot2docker down` will stop the platform without deleting the VMs, which means the next
  start will be fast.
