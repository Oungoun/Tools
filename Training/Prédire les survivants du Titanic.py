import pandas as pd
path_test= "C:/Users/benjamin.schick/Desktop/GitHub/Tools/Training/data/test.csv"
path_train="C:/Users/benjamin.schick/Desktop/GitHub/Tools/Training/data/train.csv"
path_gs="C:/Users/benjamin.schick/Desktop/GitHub/Tools/Training/data/gender_submission.csv"

df_test = pd.read_csv(path_test,sep=',')
df_train = pd.read_csv(path_train, sep=',')
df_gs=pd.read_csv(path_gs, sep=',')

#On indexe le data frame avec la variable PassengerId comme ceci
df_train.set_index('PassengerId', inplace=True, drop=True)

#Les commandes dtype et count vont nous donner des informations utiles
df_train.dtypes
df_train.count()

# Données continues et complètes
# SisSp, Parch, Fare

#La fonction qui suit est une fonction de parsing permettant d’isoler le vecteur à prédire (Survived) et de filtrer uniquement les variables que nous venons de définir.


def parse_model_0(X):
    target = X.Survived #on récupère la colonne Survived
    X = X[['Fare', 'SibSp', 'Parch']] #on redef X après la ligne précédente
    return X, target

X, y = parse_model_0(df_train.copy()) #On récupère le X tel que défini dans la fonction (grace à la ',') et y

from sklearn.model_selection import cross_val_score
import numpy as np
import matplotlib.pyplot as plt

def compute_score(clf, X, y):
    xval = cross_val_score(clf, X, y, cv = 5) #clf is the obhect to use to fit the data
    return np.mean(xval)

from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()
compute_score(lr, X, y)



### Étude des variables ###

survived = df_train[df_train.Survived == 1 ]
dead = df_train[df_train.Survived == 0 ]


def plot_hist(feature, bins = 20):
    x1 = np.array(dead[feature].dropna())
    x2 = np.array(survived[feature].dropna())
    plt.hist([x1, x2], label=['Victime', 'Survivant'], bins = bins)
    # color = ['', 'b'])
    plt.legend(loc = 'upper left')
    plt.title('distribution relative de %s' %feature)
    plt.show()
plot_hist('Pclass')

#La variable Pclass est très importante et à intégrer au modèle


def parse_model_1(X):
    target = X.Survived
    to_dummy = ['Pclass']
    for dum in to_dummy:
        class_dummies = pd.get_dummies(X['Pclass'], prefix='split_'+dum)
    X = X.join(class_dummies)
    to_del = ['Name', 'Age', 'Cabin', 'Embarked', 'Survived', 'Ticket']
    for col in to_del : del X[col]
    return X, target

