import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import io
import random
import json
import requete as rq
import utils

def afficher_magnitude(pdf, name):
    pdf_utile = pdf[pdf["i:objectId"]==name]
    fig, ax = plt.subplots()
    ax.scatter(
        list(pdf_utile[pdf_utile["i:fid"]==1]["i:jd" ]),   
        list(pdf_utile[pdf_utile["i:fid"]==1]["i:magpsf"]), 
        color='green',
        label="g band"
    )

    ax.scatter(
        list(pdf_utile[pdf_utile["i:fid"]==2]["i:jd" ]), 
        list(pdf_utile[pdf_utile["i:fid"]==2]["i:magpsf"]), 
        color='red',
        label="r band"
    )
    plt.gca().invert_yaxis()
    plt.xlabel('Jordan date')
    plt.ylabel('magnitude')
    ax.set_title(name +" ("+list(pdf_utile["v:classification"])[0]+")")
    plt.legend()

    plt.show()                             


def afficher_coordonées(pdf):
    noms=[]
    for i in list(pdf["i:objectId"]):
        if i not in noms:
            noms.append(i)
    
    fig = plt.figure()
    ax = plt.subplot(111, projection="mollweide")
    plt.grid(True)
    for name in noms:
        pdf_utile = pdf[pdf["i:objectId"]==name]
        
        ax.scatter(
            np.radians(list(utils.shift_ra(pdf_utile["i:ra"], 0))[0]),
            np.radians(list(pdf_utile["i:dec"])[0]),
            color=(random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)),
            # label= name +" ("+list(pdf_utile["v:classification"])[0]+")"
            
        ) 
        ax.annotate(name +" ("+list(pdf_utile["v:classification"])[0]+")", (
                    np.radians(list(utils.shift_ra(pdf_utile["i:ra"], 0))[0]), 
                    np.radians(list(pdf_utile["i:dec"])[0]), ))
    plt.xlabel('ra')
    plt.ylabel('dec')
    ax.set_title("alerts location")
    # plt.legend()

    plt.show() 
    
def afficher_trajectoire(pdf): 
    noms=[]
    for i in list(pdf["i:objectId"]):
        if i not in noms:
            noms.append(i)
    fig = plt.figure()
    ax = plt.subplot(111, projection="mollweide")
    plt.grid(True)
    for name in noms:
        pdf_utile = pdf[pdf["i:objectId"]==name]
        ax.scatter(
            np.radians(list(utils.shift_ra(pdf_utile["i:ra"], 0))),
            np.radians(list(pdf_utile["i:dec"])),
            color=(random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)),
            # label= name +" ("+list(pdf_utile["v:classification"])[0]+")"
            
        ) 
        print(np.radians(list(utils.shift_ra(pdf_utile["i:ra"], 0))))
        
        ax.annotate(name +" ("+list(pdf_utile["v:classification"])[0]+")", (
                    np.radians(list(utils.shift_ra(pdf_utile["i:ra"], 0))[-1]), 
                    np.radians(list(pdf_utile["i:dec"])[-1]), ))
    plt.xlabel('ra')
    plt.ylabel('dec')
    ax.set_title("alerts location")
    plt.show()
            

donne = pd.read_json("dataset_sn.json")
# afficher_magnitude(donne, list(donne["i:objectId"])[random.randint(0,len(list(donne["i:objectId"])))])

# afficher_coordonées(rq.get_class_objet("Planet",100, False))

# afficher_coordonées(get_class_objet("SN",6))



