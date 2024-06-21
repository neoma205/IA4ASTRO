import decision_tree_test as dct
from sklearn.ensemble import RandomForestClassifier

if __name__ == "__main__":
    datas, data_test = dct.recuperer_data()
    clf = dct.lancer_afficher_entrainement(RandomForestClassifier(), datas)
    print()
    dct.lancer_afficher_test(clf, datas, data_test)