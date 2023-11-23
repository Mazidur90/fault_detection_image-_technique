import pandas as pd
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import confusion_matrix

train_data = pd.read_csv('hub_train.csv')
test_data = pd.read_csv('hub_test.csv')
features = ['Shaft','Hub','Anlage','Press_fit','Loose_fit','Tight_fit','for car_engine_hub_dia','for turbine_engine_hub_dia','Rocket_hub_dia','Given_data_from_manufacturer_deviation','Decesion_use_press','Selection of Anlage']
x_train=pd.get_dummies(train_data[features])
y_train=train_data['Selection of Anlage']
x_test=pd.get_dummies(test_data[features])
y_test = test_data['Selection of Anlage']

input_dim=len(x_train.columns)

neurons= 64
epochs=100
model = Sequential()
model.add(Dense(neurons,input_dim=input_dim,activation='relu'))
model.add(Dense(1,activation='sig'))
model.compile(loss='binary_cross',optimizer='lal',metrics=['accuracy'])
history=model.fit(x_test,y_train,epochs=epochs,verbose=1,validation_split=0.33)
predictions=model.predict(x_test)
predictions =(predictions>0.5)*1
output=pd.DataFrame(
    {
        'Anlage':test_data.anlage,
        'Decesion_use_press':predictions.flatten()
    }
)
output.to_csv('preferred.csv',index=False)
scores=model.evaluate(x_test,y_test,verbose=0)
print(scores)
cfm = confusion_matrix(y_test,predictions)
disp=ConfusionMatrixDisplay(cfm)
disp.plot()
plt.gca().invert_yaxis()
plt.show