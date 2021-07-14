import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import warnings
import pickle
warnings.filterwarnings("ignore")

data = pd.read_csv('C:\\Users\\Ankita Duraphe\\Documents\\WINTER SEMESTER 2020-21\\CSE3506 - Essentials of Data Analytics\\EDA - Project\EDA Final Review\\Dashboard\\Deploy Batsmen Innings Match Output Final 2018\\gt20_2018_all_common_final_1_modified1.csv')
data = np.array(data)

X = data[:, :8]
y = data[:, -1]
y = y.astype('int')
X = X.astype('int')
# print(X,y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
log_reg = DecisionTreeClassifier()


log_reg.fit(X_train, y_train)

inputt=[int(x) for x in "1 1 0 6 3 0 3 54".split(' ')]
final=[np.array(inputt)]

b = log_reg.predict_proba(final)


pickle.dump(log_reg,open('model.pkl','wb'))
model=pickle.load(open('model.pkl','rb'))

