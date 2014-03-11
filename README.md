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

Usage Instructions
====

In order to send Python code to the API, you need to use the POST variable **code**. Here's some sample POST data to use:
```
code=def%20f(x)%3A%20%0A%20%20%20%20return%20x*2%0A%0Af(5)
```
That same POST data without the url encoding looks like:
```
code=def f(x): 
    return x*2

f(5)
```

Quirks
====

1. Right now, you're probably going to want to use an HTTP Client such as GraphicalHttpClient - [Mac App Store Link](https://itunes.apple.com/us/app/graphicalhttpclient/id433095876?mt=12) - to test. 
2. Right now, only POST requests to the base URL works. There are no other API endpoints at this point (as it's still in prototype).
3. Whichever HTTP client you're using, then you might have to set the **Content-Type** header to *application/x-www-form-urlencoded*.
4. You may have to urlencode the input before sending it to the API. You can use an [online url encoder](http://meyerweb.com/eric/tools/dencoder/) if you don't want to go through the pain of doing it in Python just for testing purposes.
5. You may have to put at least one blank line between Python statements that move backwards in the tab index. Look at the sample code above for an example of what we mean.