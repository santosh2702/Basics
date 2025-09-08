def mse(y_true, y_pred):  #mean-squared-error
    return np.mean((y_true - y_pred) ** 2)
def rmse(y_true, y_pred):  #root-mean-squared-error
    return np.sqrt(mse(y_true, y_pred))
def mae(y_true, y_pred): #mean-squared-error
    return np.mean(np.abs(y_true - y_pred))
def accuracy(y_true, y_pred):
    return np.mean(y_true = y_pred)
