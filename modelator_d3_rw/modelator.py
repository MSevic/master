from rolling_window import roller
from standard_model import standard_model


def modelator(model, split, rolling_window, train, test, target_column, frame_size=10, test_size=0.8):
    if rolling_window:
        return roller(model, train, frame_size, target_column)
    else:
        return standard_model(model, train, target_column, split, test)
