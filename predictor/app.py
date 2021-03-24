import os
import time
import atexit
import vars

from flask import Flask, jsonify
from apscheduler.schedulers.background import BackgroundScheduler
from predictor import make_predictions, get_prediction_for, update_predictions

vars.init()

scheduler = BackgroundScheduler()
# comment for production
scheduler.add_job(func=update_predictions, trigger="interval", seconds=10)
# uncomment for production
# scheduler.add_job(func=make_predictions, trigger="cron", hour="4")
scheduler.start()

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())

app = Flask(__name__)


@app.route('/')
def welcome():
    # return a json
    return jsonify({'status': 'predictor working'})


@app.route('/predictions/<commodity>', methods=['GET'])
def get_latest_prediction(commodity):
    if commodity not in ['GLD']:
        return jsonify({'avalable predictions': ['GLD']})
    return get_prediction_for(commodity)


if __name__ == '__main__':
    # define the localhost ip and the port that is going to be used
    # in some future article, we are going to use an env variable instead a hardcoded port
    app.run(host='0.0.0.0', port=os.getenv('PORT'))
