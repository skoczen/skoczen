Artechetype (terrible pun) is a grab-and-go starter django+js I use when making new digital projects.  You're welcome to as well, and if you come across improvements, pull requests are welcome.

NOTE: I'm still working on it. Don't use it quite yet.

Grab it
=======

1. Set up your new repo, say `github.com:myusername/mynewproject.git`
2. Grab artechetype, and point it to your repo (sort of a manual fork.)
	
	```bash
	git clone git@github.com:skoczen/artechetype.git mynewproject.git
	git remote rename origin artechetype
	git remote set-url origin git@github.com:myusername/mynewproject.git
	git push -u origin
	```
3. Now, set up your virtualenv, `pip install` the requirements, and you're running. 

Set up, then go.
================

1. Replace 'my-new-project' in 

	* fabfile

2. Set your keys

	* If you have a private repo, you can use `keys_and_passwords.py`.
	* If you have a public repo, you're best off setting them as environment variables in your deployment environment.  AKA:
	```config:add AWS_ACCESS_KEY_ID=foo-bar-1```

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