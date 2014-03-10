yoda
====

Youth Oriented Development Advisor

The name is a work in progress. However, this is a RESTful API that allows remote compilation of Python code. Once compiled, the code can be tested against certain conditions to determine the efficacy of the code submitted.

Required Packages
====

* [Flask](http://flask.pocoo.org)
* [flask-restful](http://flask-restful.readthedocs.org)

Installation Instructions
====

After cloning this repository, just go to the base directory and type the following at the command prompt:
```
python runserver.py
```

Quirks
====

1. Right now, you're probably going to want to use a HTTP Client such as GraphicalHttpClient - [Mac App Store Link](https://itunes.apple.com/us/app/graphicalhttpclient/id433095876?mt=12) - to test. 
2. Right now, only POST requests to the base URL works. There are no other API endpoints at this point (as it's still in prototype).
3. Whichever HTTP client you're using, then you might have to set the **Content-Type** header to *application/x-www-form-urlencoded*.