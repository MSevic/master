from predictor import make_predictions


def init():
    global dfGLD
    dfGLD = make_predictions()
    # dfGLD = 1


def update():
    global dfGLD
    dfGLD = make_predictions()
    # dfGLD += 1
