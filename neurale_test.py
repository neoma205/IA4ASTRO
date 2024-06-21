from sklearn.neural_network import MLPClassifier
import decision_tree_test   as dct


if __name__ == "__main__":
    datas, data_test = dct.recuperer_data()
    clf = dct.lancer_afficher_entrainement(MLPClassifier(), datas)
    print()
    dct.lancer_afficher_test(clf, datas, data_test)
