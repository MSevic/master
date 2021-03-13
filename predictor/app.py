import os
import time
import atexit

from flask import Flask, jsonify
from apscheduler.schedulers.background import BackgroundScheduler

def print_date_time():
    print(time.strftime("%A, %d. %B %Y %I:%M:%S %p"))


scheduler = BackgroundScheduler()
# comment for production
scheduler.add_job(func=make_predictions, trigger="interval", hours=2)
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
    if not commodity:
        return jsonify({'avalable predictions': ['GLD']})
    get_prediction_for(commodity)

if __name__ == '__main__':
    # define the localhost ip and the port that is going to be used
    # in some future article, we are going to use an env variable instead a hardcoded port
    app.run(host='0.0.0.0', port=os.getenv('PORT'))
