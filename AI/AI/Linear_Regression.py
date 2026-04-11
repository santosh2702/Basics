# Linear Regression (manual understanding)

x = [1,2,3]
y = [2,4,6]

m = 0
b = 0
lr = 0.01

for i in range(1000):
    y_pred = [m * xi + b for xi in x]

    #calculate gradients
    dm = sum((yp - ya) * xi for xi, yp, ya in zip(x, y_pred, y)) / len(X)
    db = sum((yp - ya) for yp, ya in zip(y_pred, y)) / len(x)

    #update
    m -= lr * dm
    b -= lr * db

print(m,b)



#names = ["Alice","Bob", "Max"]
#ages = [ 25,26,28]

#score = zip(names, ages)
#print(list(score))

#Output: [('Alice', 25), ('Bob', 26), ('Max', 28)]
