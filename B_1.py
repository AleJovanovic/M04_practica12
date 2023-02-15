import json
def crearJSON():
    datas ={
        "book":[


            {
                "titel": "La caperucita Roja",
                "cover":"cuadrada",
                "year": "2000",
                "pages":"20"




            },
            {
                "titel": "Crepusculo",
                "cover":"bordeada",
                "year": "2000",
                "pages":"2000"




            },
            
            {
                "titel": "Maze Runner",
                "cover":"cuadrada",
                "year": "2014",
                "pages":"800"




            },
            
            {
                "titel": "Donde los arboles cantan",
                "cover":"caligrafica",
                "year": "2013",
                "pages":"500"




            }




        ]



    }

    with open('arxiu.json','w') as file:
        json.dump(datas,file)

    print(json.dumps(datas,indent=2))


def leerJSON():
    
    with open("arxiu.json",'r') as file:
       result = json.load(file)
       print(json.dumps(result,indent=2))



#funcion q crea un archivo json

crearJSON()

#funcion que lee del archivo json ya creado

leerJSON()

