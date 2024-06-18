import io
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def get_one_object(name,enregistrer):
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


def get_class_objet(classe_name,nombre,enregistrer):
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

fig, ax = plt.subplots()
r = requests.post(
  'https://fink-portal.org/api/v1/random',
  json={
      'n': 100,
      'class': 'SN candidate',
    'output-format': 'json',
    'columns': 'i:fid,i:magpsf,i:objectId'
  }
)

def get_info_asteroid(name):
    r = requests.post(
    'https://fink-portal.org/api/v1/sso',
    json={
    'n_or_d': name,
    'output-format': 'json'
  }
)
    pdf = pd.read_json(io.BytesIO(r.content))


    print(pdf.columns)
    noms=[]
    for i in list(pdf['i:objectId']):
        if i not in noms:
            noms.append(i)
    for name in noms:
        print(name)
        a = pdf[pdf["i:objectId"]==name]
        pdf_fid_1 = a[a["i:fid"] == 1]
        pdf_fid_2 = a[a["i:fid"] == 2]
        
        print(pdf_fid_1)
        print()
        print(pdf_fid_2)
        
        ax.scatter(
            a["i:magpsf"].mean(),
            pdf_fid_1["i:magpsf"].mean() - pdf_fid_2["i:magpsf"].mean(),
            color='green',
            label="systeme solar"
        )
    plt.gca().invert_xaxis()
    plt.xlabel('magnitude')
    plt.ylabel('g-r')

    plt.legend()

    plt.show()


if __name__ == "__main__":
    pdf_1 = get_one_object("ZTF24aaqxcpz", True)

    print(pdf_1[["i:objectId", "i:magpsf", "i:jd", "i:ra", "i:dec"]])

    print()
    pdf_2 = get_one_object("ZTF24aaqainu", True)

    print(pdf_2[["i:objectId", "i:magpsf", "i:jd", "i:ra", "i:dec"]])
    
    print()
    pdf_3 = get_class_objet("SN candidate", 100, True)

    print(pdf_3[["i:objectId", "i:magpsf", "i:jd", "i:ra", "i:dec", "d:cdsxmatch", "v:lapse"]])

    print()
    pdf_4 = get_class_objet("Solar System MPC", 100, True)
    
    print(pdf_4[["i:objectId", "i:magpsf", "i:jd", "i:ra", "i:dec", "d:cdsxmatch", "v:lapse", "i:ssnamenr", "i:ssdistnr"]])

