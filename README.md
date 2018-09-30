# README - TwelveTraitsChallenge project #

This README documents approach taken to design and implement 12traits challenge along with the steps necessary to get this application up and running.

## Problem ##
Design application that will satisfy specifications found at https://github.com/12traits/coding-challenges/blob/master/bed-challenge.md

## Implementation ##
This project consist of two Django applications: Survey and Dashboard.

### Survey application ###
Survey app is designed to be used twofold:
 1) as an API for creating respondents and submitting their answers on predefined surveys.
    API has been designed to be RESTful and has exposed endpoints to work with respondent and answer data models.
 2) as a tool for creating and managing surveys and respondents by an administrator using Django admin pages (http://127.0.0.1:8000/admin/)

### Dashboard application ###
Dashboard app is designed to be an API that has two end points post and get.
Post endpoint (http://127.0.0.1:8000/dash-api/dashboard/) should gather data from different external sources and persist that data into a (in this case local) database.
This was not implemeted in great detail and is here just to demonstrate a basic idea on how this kind of service can work.
Get endpoint is basically there to query the database and retrieve aggregated information about respondets and their psychological traits in .json format.

## Installation ##
* pull code from git repo from https://github.com/nebojsatrumic/twelvetraits.git
* install pip dependencies (```pip -r install requirements.txt```)
* restore database from "survey_database_23032017tar.backup" using  pg_restore command
    https://www.postgresql.org/docs/9.2/static/app-pgrestore.html
* make sure you have restored "survey" database and adjust settings.py to use restored database with appropriate user
* run the server ```python manage.py runserver```

## Usage ##

* Use http://127.0.0.1:8000/admin/ (if ran locally) for administrating Surveys (super admin for this purpose from the restored database should be admin with password asdf1234)
* Use http://127.0.0.1:8000/api/respondent/ to see documentation about available respondent API calls
* Use http://127.0.0.1:8000/api/answer/ to see documentation about available respondent API calls
* Use http://127.0.0.1:8000/api/respondent/answers/ to see documentation about available respondent answers API calls

* Use get and post to http://127.0.0.1:8000/dash-api/dashboard/ for Dashboard intrection


## List of components that used ##
* Django (https://www.djangoproject.com/)
* djangorestframework (http://www.django-rest-framework.org/) - Used for creating RESTful API
* psycopg2 (http://initd.org/psycopg/)
* drf-extensions (https://pypi.org/project/drf-extensions/)
* django-rest-swagger (https://django-rest-swagger.readthedocs.io/en/latest/) - Used for API documentation in Survey app
* django-import-export (https://django-import-export.readthedocs.io/en/latest/) - Used for importing and exporting data in admin view of Survey app

## Considerations ##

I've tried to emulate Git flow in my dealing with Git and so I have master, devlop and feature branches.

Deployment of the solution would be made to AWS EC2 instances. As for the two instances of the survey service this could be accomplished by using AWS load balancers.

Stuff that is missing due to a shortness and nature of the challange:
 1) Authorization/authentication implementation - I would use token based authentication
 2) Logging - I would used Django native logging to files that could be later ingested by online services like https://logentries.com/ or https://www.splunk.com/en_us/solutions/solution-areas/log-management.html
    This would largerly help in monitoring and troubleshooting the apps.
 3) Dashboard app could have (and maybe should have) been made as a different project and deployed and managed separately from the Survey application
 4) I'm not proficient with docker do I didn't do that part of a challenge. From what I've heard and seen this part is certainly feasible and with a sufficient amount of time I'm sure it can be done.
 5) Automated testing. No test were written in and the code was tested manually. In the real world this would be a big part of everyday work.