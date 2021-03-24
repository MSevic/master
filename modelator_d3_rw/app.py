import os
from flask import Flask, jsonify, request
from modelator import modelator

app = Flask(__name__)


@app.route('/')
def welcome():
    return jsonify({'status': 'modelator working'})


@app.route('/rw/<model>', methods=['POST'])
def rw(model=False):
    if request.method != 'POST':
        return 404

    if not model:
        return jsonify({'available models': ['d3', 'lin_r', 'r_forest', 'knn', 'svm_model']})

    split = True
    rolling_window = True

    # dataframes
    test = False
    if 'test.csv' in request.files:
        split = False
        test = request.files.get('test.csv')
    train = request.files['train.csv']

    frame_size = 10
    test_size = 0.8
    if rolling_window:
        frame_size = int(request.form['frame_size'])
        if frame_size < 3:
            frame_size = 10
    else:
        test_size = request.form['test_size']

    target_column = request.form['target_column']

    return modelator(model, split, rolling_window, train, test, target_column, frame_size, test_size)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('PORT'))
