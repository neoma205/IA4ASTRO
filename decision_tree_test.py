from sklearn import tree
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import io
import random
import json
from sklearn.ensemble import RandomForestClassifier

def creer_une_liste(pdf):
    pdf_utile = pdf["lc_features_r"]
    classe = pdf["fink_class"][0]
    x = []
    for i in list(pdf_utile):
        if i != None:
            info = [i.get("amplitude"), i.get("mean") ,i.get("mean_variance"), i.get("median"), i.get("skew")]
            if not None in info:           
                x.append(info)
    
    return x[:int(len(x)*0.7)], [classe for r in range(int(len(x)*0.7))], x[int(len(x)*0.7):], [classe for r in range(len(x[int(len(x)*0.7):]))]

def dataset_sam(names):
    X=[]
    Y=[]
    tx=[]
    ty=[]
    for name in names: 
        pdf = pd.read_parquet(name).reset_index(drop=True)
        a, b, t_value, t_etiquettes = creer_une_liste(pdf)
        
        X+=a
        Y+=b
        tx+= t_value
        ty+=t_etiquettes
    return (X,Y), (tx, ty)

def tester(tree, x, y):
    v=0
    t=0
    for i in range(len(x)):
        if clf.predict([x[i]]) == y[i]:
            v+=1    
        t+=1
    return v/t


def entrainer_algo(algo, data, etiquette):
    return algo.fit(data, etiquette)


if __name__ == "__main__":
    datas, data_test=dataset_sam(("dataset/dataset_EB__Candidate.parquet",
                 "dataset/dataset_EB_.parquet",
                 "dataset/dataset_LP__Candidate.parquet",
                 "dataset/dataset_LPV_.parquet",
                 "dataset/dataset_Mira.parquet",
                 "dataset/dataset_QSO.parquet",
                 "dataset/dataset_RRLyr.parquet",
                 "dataset/dataset_Star.parquet",
                 "dataset/dataset_V_.parquet"
                 ))
        
        
    print(np.unique(datas[1][:185000], return_counts=True))
    print(np.unique(datas[1][185001:], return_counts=True))
    
    clf = tree.DecisionTreeClassifier()
    clf = entrainer_algo(clf, datas[0], datas[1])
    print("test sur les données d'entrainement")
    print(tester(clf, datas[0], datas[1]))
    print(tester(clf, data_test[0], data_test[1]))
    
    
    # #clf = clf.fit(datas[0][:185000], datas[1][:185000])
    
    # print(tester(clf, datas[0][:185000], datas[1][:185000]))
    # print(tester(clf, datas[0], datas[1]))
    
    exit()
    clf = RandomForestClassifier(max_depth=2, random_state=0)
    
    print("demarrage de l'entrainement: ")
    clf = entrainer_algo(clf, datas[0][:185000], datas[1][:185000])
    print("fin de l'entrainement")
    
    # print("prediction: ")
    #print(tester(clf, datas[0][:185000], datas[1][:185000]))
    
    # tree.plot_tree(clf)
    # plt.show()