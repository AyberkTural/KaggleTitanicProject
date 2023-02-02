import pandas as pd
from sklearn.preprocessing import OneHotEncoder
import seaborn as sb

import matplotlib.pyplot as plt
data = pd.read_csv('E:\\train.csv');

#for i in range (0,data.columns.__len__()):


#for i in range (0,data.columns.__len__()):

 #print(data[data.columns[i]].unique())


one_hot_encoded_data = pd.get_dummies(data, columns = ['CryoSleep','VIP','Transported'])

print(one_hot_encoded_data)

for i in range (0,one_hot_encoded_data.columns.__len__()):
 print(one_hot_encoded_data[one_hot_encoded_data.columns[i]].dtype)
 if(one_hot_encoded_data[one_hot_encoded_data.columns[i]].dtype != 'object' ):


   if(((one_hot_encoded_data[one_hot_encoded_data.columns[i]].corr(one_hot_encoded_data['Transported_False']))>=0.45)or((one_hot_encoded_data[one_hot_encoded_data.columns[i]].corr(one_hot_encoded_data['Transported_True']))>=0.45)):
    print(one_hot_encoded_data[one_hot_encoded_data.columns[i]].corr(one_hot_encoded_data['Transported_True']))
    print(one_hot_encoded_data[one_hot_encoded_data.columns[i]].corr(one_hot_encoded_data['Transported_False']))
    sb.pairplot(one_hot_encoded_data,hue='Transported_True')
# print(one_hot_encoded_data[one_hot_encoded_data.columns[i]].corr(one_hot_encoded_data[one_hot_encoded_data.columns[i]]))

    plt.show()

