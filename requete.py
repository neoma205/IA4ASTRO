import io
import requests
import pandas as pd

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





if __name__ == "__main__":
    pdf_1 = get_one_object("ZTF24aaqxcpz", True)

    print(pdf_1[["i:objectId", "i:magpsf", "i:jd", "i:ra", "i:dec"]])

    print()
    pdf_2 = get_one_object("ZTF24aaqainu", True)

    print(pdf_2[["i:objectId", "i:magpsf", "i:jd", "i:ra", "i:dec"]])
    
    print()
    pdf_3 = get_class_objet("SN candidate", 100, True)

    print(pdf_3[["i:objectId", "i:magpsf", "i:jd", "i:ra", "i:dec", "d:cdsxmatch", "v:lapse"]])
    