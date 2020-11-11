# Guidestar Mock Endpoint

This is a service to set up your own mock endpoint for the Guidestar Essentials API. This was created to mock the response when testing in Salesforce
so developers don't have to setup a trial.

# Setup

Install python3: https://www.python.org/downloads/

Install requirements for project: `python3 -m pip install -r requirements.txt`

This will install:

* Flask: https://flask.palletsprojects.com/en/1.1.x/installation/
* gunicorn: https://gunicorn.org/

Install Heroku CLI: https://devcenter.heroku.com/articles/getting-started-with-python#set-up

From the base of this project run

```
heroku create
```

You should see something like this confirming that the app was created:
```
Creating app... done, ⬢ serene-caverns-82714
https://serene-caverns-82714.herokuapp.com/ | https://git.heroku.com/serene-caverns-82714.git
```

Push this code to heroku
```
git push heroku main
```

Your browser should open, displaying the JSON payload

# JSON Response Information:
In `app.py`, the variable `guidestar_info` holds the JSON payload that mocks the Guidestar info. It is based on the sample JSON provided in their documentation: https://apiportal.guidestar.org/api-static-documentation-v3