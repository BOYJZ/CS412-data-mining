import numpy as np
import random
import math
from xgboost import XGBClassifier
from sklearn.svm import SVC, LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def my_train_test(method,X,y,pi,k):
    
    errors = []

    if method=='LinearSVC':
        for i in range(k):
            X_train,X_test,y_train,y_test = split(X,y,pi)
            model=LinearSVC(max_iter=2000)
            model.fit(X_train,y_train)
            errors.append(1-LinearSVC.score(model,X_test,y_test))
    if method=='SVC':
        for i in range(k):
            X_train,X_test,y_train,y_test = split(X,y,pi)
            model=SVC(gamma='scale', C=10)
            model.fit(X_train,y_train)
            errors.append(1-SVC.score(model,X_test,y_test))
    if method=='LogisticRegression':
        for i in range(k):
            X_train,X_test,y_train,y_test = split(X,y,pi)
            model=LogisticRegression(penalty='l2', solver='lbfgs', multi_class='multinomial')
            model.fit(X_train,y_train)
            errors.append(1-LogisticRegression.score(model,X_test,y_test))
    if method=='RandomForestClassifier':
        for i in range(k):
            X_train,X_test,y_train,y_test = split(X,y,pi)
            model=RandomForestClassifier(max_depth=20, random_state=0, n_estimators=500)
            model.fit(X_train,y_train)
            errors.append(1-RandomForestClassifier.score(model,X_test,y_test))
    if method=='XGBClassifier':
        for i in range(k):
            X_train,X_test,y_train,y_test = split(X,y,pi)
            model=XGBClassifier(penalty='l2', solver='lbfgs', multi_class='multinomial')
            model.fit(X_train,y_train)
            errors.append(1-XGBClassifier.score(model,X_test,y_test))
        
    return np.array(errors)

def split(X,y,train_size):
    X_train,X_test,y_train,y_test=[],[],[],[]
    test_time=len(X)
    for i in range(test_time):
        random_signal=random.random()
        if random_signal<=train_size:
            X_train.append(X[i])
            y_train.append(y[i])
        if random_signal>train_size:
            X_test.append(X[i])
            y_test.append(y[i])
    return X_train,X_test,y_train,y_test























