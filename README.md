Cloud Assistant
===============
[![Build Status]][Travis CI] 

Numbers of fabric scripts to help build some services in cloud hosting fastly.

Install
-------

What you need to do is simply install fabric.

You can install it via pip(officially recommended) or easy_install(older, but still works fine)

`pip install fabric`

Or you may also opt to use your operating system’s package manager; the package is typically called fabric or python-fabric. 

`sudo apt-get install python-fabric`

*Warning:* Please DO NOT install it on windows. It would be a nightmare.

If you insist on installing it on Windows then you should read [one of my blog][1] to solve some Problem.

Usage
-----

`fab -f ./filename.py some_function`

Wiki
----
[GitHub wiki page][3]

License
-------
MIT

Bugs and Issues
----------------
* Feel free to create issue at [issue tracker][2]

* And please feel free to make pull requests.

[1]:http://www.ivancaiblog.tk/2014/07/03/install-fabric-on-windows.html
[2]:https://github.com/caizixian/cloudassistant/issues
[3]:https://github.com/caizixian/cloudassistant/wiki
[Build Status]:  https://api.travis-ci.org/caizixian/cloudassistant.png
[Travis CI]:  https://travis-ci.org/caizixian/cloudassistant