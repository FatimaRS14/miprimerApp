#Gestion de solicitudes HTTP
#importacion del objeto flask

from flask import Flask

app = Flask(__name__) #se crea la instancia app. Se utiliza para gestionar las solicitudes web entrantes y enviar las respuestas al usuario
#variable especial __name__ marcara el nombre del modulo donde este guardada 



@app.route('/') 
def hello():
    #Creacion de de funcion que devilvera las respuestas
    return 'Hello, World!'
