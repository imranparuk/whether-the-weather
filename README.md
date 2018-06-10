
# Whether the Weather

> A weather forecasting frontend

## Getting Started

To get up and running, make sure you have [Python 3.4](https://www.python.org/) installed, preferable in a virtual environment.

This project work's through the API of [Weather24 Cape Town](http://weather.news24.com/sa/capetown). 

### Prerequisites

This project depends on [Django](https://www.djangoproject.com) and the [Django Rest Framework](www.django-rest-framework.org/) 

to install them:

Django:
```
pip install django
```
Django Rest Framework:
```
pip install djangorestframework
pip install markdown       # Markdown support for the browsable API.
pip install django-filter  # Filtering support
```
don't forget to add Add ```rest_framework``` to your ```INSTALLED_APPS``` setting.
```python
INSTALLED_APPS = (
    ...
    'rest_framework',
)
```
#### The Cron-Job
(Linux Only!)
As mentioned before the project relies on its data from weather24. We access this through their API using the python requests library. 

However, to always have the most up-to-date forcast, we have a Django management command get the forecast data, and save it in the database if it is new. We use a cron-job to schedule this task.

To list all the current scheduled tasks
```
$ sudo crontab -l
```

To create a new task

```
$ sudo crontab -e
```
Before we schedule our task (a script) we need to edit it for our specific directories.
* If you are using a virutal environment, change the directory by ```source``` to your relevant directory. Otherwise delete this line. 
* Change the directory by ```cd``` to the path to the project directory that contains ```manage.py```

Job.sh
```bash
#!/bin/bash
source /home/imran/Documents/personal/projects/Git/whether_the_weather/bin/activate
cd /home/imran/whether_the_weather
#Django Management Command 
python manage.py get_forecast
```

To schedule our task above in minute intervals we use this command

```
* * * * * /bin/execute/this/script.sh
```
Make sure to change all the relevant directories. 
You database should start populating immidately. 

### Starting up Django
When starting up django, a few commands are required to get you up and running. 

```
python manage.py makemigrations
```
```
python manage.py migrate
```
```
python manage.py createsuperuser
```
and finally
```
python manage.py runserver
```

## Contributing

Please read [CONTRIBUTING.md](/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.


## Authors

* **Imran Paruk** - *Initial work* 

See also the list of [contributors](/contributors.md) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](/LICENSE.md) file for details

## Acknowledgments

Thank you to:
+ https://kvz.io/blog/2007/07/29/schedule-tasks-on-linux-using-crontab/
+ http://janetriley.net/2014/11/quick-how-to-custom-django-management-commands.html
