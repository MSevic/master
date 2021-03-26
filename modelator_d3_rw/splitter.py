from sklearn.model_selection import train_test_split


def splitter(df, target_column, test_size):
    columns = df.columns.tolist()
    columns = [c for c in columns if c not in [target_column]]

    X = df[columns]
    y = df[target_column]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=123)
    return X_train, X_test, y_train, y_test


def splitter_rolling(df, frame_size, start_index, target_column, exclude_columns):
    start_index = start_index - frame_size - 1
    end_index = start_index + frame_size
    columns = df.columns.tolist()
    excludeArray =  [target_column] + exclude_columns
    columns = [c for c in columns if c not in excludeArray]

    x = df[columns]
    y = df[target_column]

    # Delimo podatke na train i test set
    x_test = x.iloc[[end_index + 1]]
    x_train = x.iloc[[start_index, end_index]]
    y_train = y.iloc[[start_index, end_index]]
    return x_train, y_train, x_test
