import numpy as np
from sklearn.model_selection import train_test_split
# create layer
from keras.layers import Dense
from keras.models import load_model
import keras
dataset = np.loadtxt('diabetes.csv', delimiter=',')

X = dataset[:,0:8]
y = dataset[:,8]

#chia du lieu ra train-val , test
X_train_val, X_test, y_train_val, y_test = train_test_split(X,y, test_size=0.2)
X_train, X_val, y_train, y_val = train_test_split(X_train_val,y_train_val,test_size=0.2)

'''
#thiet ke cau hinh 8 -16 -8 - 1
model = keras.Sequential()
# relu la khu tuyen tinh
model.add(Dense(16, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
# dung ham sigmoid de danh gia 0 va 1
model.add(Dense(1, activation='sigmoid'))
# tom tat
model.summary()

# xay dung ham tinh toan (compile model)
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])


# train model (đi qua tập train 1 lần thì là 1 epoch)
# batch-size: nhóm các phần tử trong 1 vecto


model.fit(X_train,y_train,epochs=100, batch_size=8, validation_data=(X_val,y_val))

# save model lai
model.save('mymodel_001.h5')
'''

# kiem tra tren tap test
model = load_model('mymodel_001.h5')

loss, acc = model.evaluate(X_test,y_test)
print('Loss = ',loss)
print('Accuracy = ', acc)

# kiem tra 1 phan tu nhat dinh
X_new = X_test[10]
y_new = y_test[10]
    # them chieu
X_new = np.expand_dims(X_new, axis=0)
y_predict = model.predict(X_new)
print('Gia tri du doan la: ', y_predict, 'so voi', y_new)