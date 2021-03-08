import pandas as pd
import models
from responder import respond
from splitter import splitter

def standard_model(model, train, target_column, split, test):
    train = pd.read_csv(train)
    if split:
        x_train, x_test, y_train, y_test = splitter(df, target_column, test_size)
    else:
        test = df.read_csv(test)
        y_train = train[target_column]
        x_train = train.drop(target_column, axis=1)
        x_test = test.drop(target_column, axis=1)

    method_to_call = getattr(models, model)
    y_test = method_to_call(x_train, y_train, x_test)
    return respond(y_test)