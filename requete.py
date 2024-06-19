import io
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def get_one_object(name,enregistrer=False):
    r = requests.post(
        'https://fink-portal.org/api/v1/objects',
        json={
            'objectId': name,
            'output-format': 'json'
        }
    )
    pdf = pd.read_json(io.BytesIO(r.content))

    if enregistrer:
         pdf.to_json(name)

    return pdf


def get_class_objet(classe_name,nombre,enregistrer=False):
    r = requests.post(
        'https://fink-portal.org/api/v1/latests',
        json={
            'class': classe_name,
            'n': nombre,
            'output-format': 'json'
        }
    )
    pdf = pd.read_json(io.BytesIO(r.content))
    
    if enregistrer:
        pdf.to_json(classe_name)
    return pdf

def get_asteroid(names,enregistrer=False):
    r = requests.post(
        'https://fink-portal.org/api/v1/sso',
        json={
            'n_or_d': ",".join(names),
            'output-format': 'json'
        }
    )
    pdf = pd.read_json(io.BytesIO(r.content))
    return pdf
    
if __name__ == "__main__":
    # pdf_1 = get_one_object("ZTF24aaqxcpz", True)

    # print(pdf_1[["i:objectId", "i:magpsf", "i:jd", "i:ra", "i:dec"]])

    # print()
    # pdf_2 = get_one_object("ZTF24aaqainu", True)

    # print(pdf_2[["i:objectId", "i:magpsf", "i:jd", "i:ra", "i:dec"]])
    
    # print()
    # pdf_3 = get_class_objet("SN candidate", 100, True)

    # print(pdf_3[["i:objectId", "i:magpsf", "i:jd", "i:ra", "i:dec", "d:cdsxmatch", "v:lapse"]])

    # print()
    # pdf_4 = get_class_objet("Solar System MPC", 100, True)
    
    # print(pdf_4[["i:objectId", "i:magpsf", "i:jd", "i:ra", "i:dec", "d:cdsxmatch", "v:lapse", "i:ssnamenr", "i:ssdistnr"]])

    import affichage
    print()
    print("--- Requete sur les asteroides ---")
    pdf_ast = get_asteroid(["8467", "1922", "77799"])

    print(pdf_ast[["i:objectId", "i:ssnamenr", "i:ssdistnr", "i:ra", "i:dec"]])

    ast_8467 = pdf_ast[pdf_ast["i:ssnamenr"] == 8467]
    print(ast_8467)
    affichage.afficher_coordonées(ast_8467)



