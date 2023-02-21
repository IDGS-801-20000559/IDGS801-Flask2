#Estrutura inicial de un proyecto Flask
from flask import Flask, render_template
from flask import request
from collections import Counter
import forms

app = Flask(__name__)

# Indica cual es la raiz principal del proyecto
@app.route("/calcular", methods=['GET'])
def calcular():
    return render_template("calcular.html")

# Crea un decorador
@app.route("/Alumnos", methods=['GET', 'POST'])
def alumnos():
    reg_alumnos = forms.UserForm(request.form)
    nom = ''
    mat = ''
    if request.method == 'POST' :
        #Con la propiedad data obtenemos el valor del campo
        mat = reg_alumnos.matricula.data
        nom = reg_alumnos.nombre.data

    return render_template('Alumnos.html', form=reg_alumnos, mat=mat, nom=nom)

@app.route("/cajaDinamica", methods=['GET', 'POST'])
def cajaDinamica():
    reg_alumnos = forms.UserForm(request.form)
    num = 0
    if request.method == 'POST' :
        #Con la propiedad data obtenemos el valor del campo
        num = reg_alumnos.numero.data

    return render_template('cajasDinamicas.html', form=reg_alumnos, num=num)

@app.route('/calculos', methods=['GET'])
def calculos():
    numeros = []
    caden_num = []
    #Obtenemos los numeros como cadena
    caden_num = request.args.getlist('campo')
    #Mapeamos a una lista de numeros
    numeros = list(map(int, caden_num))

    #Con la función max se calcula el numero máximo
    maxim = max(numeros)
    #Para calcular el promedio se usa la funcion sum (de suma)y len(para calcular la longitud)
    prom = sum(numeros)/len(numeros)
    # La funcion min calcula el minimo de la lista
    minim = min(numeros)
    #El numero repetido se instancia en None para que en caso que no exista, devuelva ese valor
    numeroRep = None 
    # se instancia la función encontrar_numero_repetido
    numeroRep = encontrar_numero_repetido(numeros)

    if numeroRep==None:
        numeroRep='No hay numero repetido'
    
    return render_template('calculos.html', prom=prom, max=maxim, min=minim, rep=numeroRep)


def encontrar_numero_repetido(numeros):
    #La funcion set crea un conjunto que elimina los datos duplicados
    #Este es un conjunto vacío
    numeros_vistos = set()
    # Recorre la lista de numeros que fueron enviados en los parametros
    for numero in numeros:
        #Si encuentra un numero que ya esta en el conjunto(duplicado) lo regresa
        if numero in numeros_vistos:
            return numero
        else:
            # Si encuentra un numero que no esta en el conjunto lo agrega
            numeros_vistos.add(numero)
    #Si no encuentra valores repetidos regresa None        
    return None


if __name__ == '__main__':
    app.run(debug=True, port=8084)