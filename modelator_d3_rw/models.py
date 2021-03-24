from sklearn import svm
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression


def lin_r(x_train, y_train, x_test):
    lin = LinearRegression()
    lin.fit(x_train, y_train)
    lin_pred = lin.predict(x_test)
    return lin_pred


def r_forest(x_train, y_train, x_test):
    rfr = RandomForestRegressor(n_estimators=100, min_samples_leaf=10, random_state=1)
    rfr.fit(x_train, y_train)
    predictions = rfr.predict(x_test)
    return predictions


def knn(x_train, y_train, x_test):
    n_neighbors = 2
    knn_m = KNeighborsRegressor(n_neighbors, weights='distance')
    knn_m.fit(x_train, y_train)
    pred_knn = knn_m.predict(x_test)
    return pred_knn


def d3(x_train, y_train, x_test):
    dtr = DecisionTreeRegressor()
    dtr = dtr.fit(x_train, y_train)
    pred_dtc = dtr.predict(x_test)
    return pred_dtc


def svm_model(x_train, y_train, x_test):
    svm_model = svm.SVR(gamma='scale')
    svm_model = svm_model.fit(x_train, y_train)
    pred_svm = svm_model.predict(x_test)
    return pred_svm
