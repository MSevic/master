import models
from responder import respond
import pandas as pd
import numpy as np
from splitter import splitter_rolling


def roller(model, train, frame_size, target_column):
    train = pd.read_csv(train, index_col=0, dtype=np.float32)
    train = train.astype(np.float32)
    train = train[~train.isin([np.nan, np.inf, -np.inf]).any(1)]
    method_to_call = getattr(models, model)
    if method_to_call:
        i = frame_size
        exclude_column = 'prediction_' + str(model)
        train[exclude_column] = 0
        while i < (len(train.index) - 1):
            i += 1
            x_train, y_train, x_test = splitter_rolling(train, frame_size, i, target_column, exclude_column)
            train.loc[[i], 'prediction_' + str(model)] = method_to_call(x_train, y_train, x_test)[0]
        return respond(train)
    else:
        return jsonify({'error': 'selected model not available'})
