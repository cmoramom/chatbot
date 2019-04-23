# chatbot

this project uses Flask, Celery as tasker and Redis as Broker, in order to run the flask server , you have to active the virtual enviroment and then run the following to initiate the Flask server 

python -m flask run --port 8050 under the main project folder (chatbot)

to run the celery server run the follwing command under the main folder (chatbot)

celery -A app.celery worker


to install the redison on windows 

https://github.com/rgl/redis/downloads

to install redis linux https://redis.io/topics/quickstart

to install celery http://www.celeryproject.org/install/



#Todo get the response from task a send it to the chatroom api 
