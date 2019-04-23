# chatbot

this project uses Flask, Celery as tasker and Redis as Broker, in order to run the flask server , you have to active the virtual enviroment and then run the following to initiate the Flask server 

Requirements list

amqp==2.4.2
aniso8601==6.0.0
billiard==3.6.0.0
celery==4.3.0
certifi==2019.3.9
chardet==3.0.4
Click==7.0
Flask==1.0.2
Flask-RESTful==0.3.7
idna==2.8
itsdangerous==1.1.0
Jinja2==2.10.1
kombu==4.5.0
MarkupSafe==1.1.1
pika==1.0.1
PyJWT==1.7.1
pytz==2019.1
redis==3.2.1
requests==2.21.0
six==1.12.0
SQLAlchemy==1.3.3
urllib3==1.24.2
vine==1.3.0
Werkzeug==0.15.2

python -m flask run --port 8050 under the main project folder (chatbot)

to run the celery server run the following command under the main folder (chatbot)

celery -A app.celery worker


to install the redison on windows 

https://github.com/rgl/redis/downloads

to install redis linux https://redis.io/topics/quickstart

to install celery http://www.celeryproject.org/install/

in order to run both projects make sure that the flask servers are running in different port numbers 

#Todo get the response from task a send it to the chatroom api 
