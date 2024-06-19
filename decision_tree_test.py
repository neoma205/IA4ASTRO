from sklearn import tree
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import io
import random
import json

def creer_une_liste(pdf):
    pdf_utile = pdf["lc_features_r"]
    classe = pdf["fink_class"][0]
    x = []
    for i in list(pdf_utile):
        if i != None:
            info = [i.get("amplitude"), i.get("mean") ,i.get("mean_variance"), i.get("median"), i.get("skew")]
            if not None in info:           
                x.append(info)
    
    return x, [classe for r in range(len(x))]

def dataset_sam(names):
    X=[]
    Y=[]
    for name in names: 
        pdf = pd.read_parquet(name).reset_index(drop=True)
        a, b = creer_une_liste(pdf)
        X+=a
        Y+=b
    return (X,Y)

def tester(tree, x, y):
    v=0
    t=0
    for i in range(len(x)):
        if clf.predict([x[i]]) == y[i]:
            v+=1    
        t+=1
    return v/t

if __name__ == "__main__":
    clf = tree.DecisionTreeClassifier()
    datas=dataset_sam(("dataset/dataset_EB__Candidate.parquet",
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
    exit()
    clf = clf.fit(datas[0][:185000], datas[1][:185000])
    
    print(tester(clf, datas[0][:185000], datas[1][:185000]))
    print(tester(clf, datas[0][185001:], datas[1][185001:]))
    
    # tree.plot_tree(clf)
    # plt.show()