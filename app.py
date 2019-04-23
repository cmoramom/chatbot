from flask import Flask

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


@app.route('/consume/api/<url>', methods=['GET'])
def consume_api(url):
    consumeapi.delay(url)
    return 'processing URL'


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
