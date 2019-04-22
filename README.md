# chatbot

this project uses Flask Celery as tasker and Redis as Broker, in order to run the flask server run, you have to active the virtual enviroment 
and run the following to initiate the Flask server 

python -m flask run --port 8050 under the main project folder (chatbot)

to run the celery server run the follwing command

celery -A app.celery worker

