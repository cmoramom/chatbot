from flask import Flask, request

from tasker.task_celery import make_celery
from utils import mylogger
from utils.consume_api import Consume

logger = mylogger.get_logger()
app = Flask(__name__)

app.config.update(
    broker_url='amqp://localhost:5672//',
    result_backend='redis://localhost:6379'
)

celery = make_celery(app)


@app.route('/consume/api/', methods=['GET'])
def consume_api():

    json_data = request.get_json(force=True)
    if not json_data:
        return {'message': 'No input data provided'}, 400
    data = json_data['data']
    consumeapi.delay(data)
    return 'processing URL'

# this celery task process the URL sent by the chatroom and consume and return the data
# todo process the celery response
@celery.task(name='app.consumeapi')
def consumeapi(url):
    api = Consume(url=url)
    data = api.consume_api()
    if data is not None:
        return data
    else:
        raise Exception(f'GET {url} returned unexpected response code:')


if __name__ == '__main__':
    app.run(port=5001)
