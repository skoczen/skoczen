Artechetype (terrible pun) is a grab-and-go starter django+js I use when making new digital projects.  You're welcome to as well, and if you come across improvements, pull requests are welcome.

Grab it
=======

1. Set up your new repo, say `github.com:myusername/mynewproject.git`
2. Grab artechetype, and point it to your repo (sort of a manual fork.)
	
	```bash
	git clone git@github.com:skoczen/artechetype.git mynewproject.git
	git remote set-url origin git@github.com:myusername/mynewproject.git
	git push -u origin
	```
3. Now, set up your virtualenv, `pip install` the requirements, and you're running. 

Set up, then go.
================

1. Replace 'my-new-project' in 

	* fabfile

2. Set your keys

3. `./manage.py runserver`



Deploy to Heroku 
================


Preparing
---------

* Heroku Auth
* Add addons
* Set config vars

Deploying
---------

* `fab deploy`