import models
from responder import respond
import pandas as pd
from splitter import splitter_rolling


def roller(model, train, frame_size, target_column):
    train = pd.read_csv(train)
    method_to_call = getattr(models, model)
    if method_to_call:
        while i < (len(df.index) - 1):
            i += 1
            x_train, y_train, x_test = splitter_rolling(train, frame_size, i, target_column)
            y_test = method_to_call(x_train, y_train, x_test)
            return respond(y_test)
    else:
        return jsonify({'error': 'selected model not available'})
