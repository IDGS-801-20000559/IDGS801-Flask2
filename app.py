#Estrutura inicial de un proyecto Flask
from flask import Flask, render_template
from flask import request
from collections import Counter
import forms
# Manejo de Cookies
from flask import make_response
# Para manejo de mensajes Flash
from flask import flash
from flask_wtf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY']="Esta es tu clave encriptada"
#
csrf = CSRFProtect()

# Indica cual es la raiz principal del proyecto
@app.route("/calcular", methods=['GET'])
def calcular():
    return render_template("calcular.html")

@app.route("/cookie", methods=['GET', 'POST'])
def cookie():
    reg_user = forms.LoginForm(request.form)
    response = make_response(render_template("cookie.html", form=reg_user))

    if request.method=='POST' and reg_user.validate():
        user = reg_user.username.data
        pwd = reg_user.password.data
        datos = user+"@"+pwd
        success_message = 'Bienvenido {}'.format(user)
        response.set_cookie('datos', datos)
        flash(success_message)
        # print(user+" "+pwd)    
    
    return response

@app.route("/Traductor", methods=['GET', 'POST'])
def Traductor():
    reg_alumnos = forms.transForm(request.form)

    if request.method == 'POST' and reg_alumnos.validate():
        wordSpa = reg_alumnos.espaniol.data
        wordEng = reg_alumnos.ingles.data
        # Para ingresar más datos en un txt
        file = open('diccionario.txt', 'a')
        file.write(wordSpa.lower()+" "+wordEng.lower()+"\n")
        file.close()
    
    return render_template('traductor.html', form=reg_alumnos, word = "")

@app.route("/TraductorB", methods=['GET', 'POST'])
def TraductorB():
    reg = forms.transForm(request.form)
    if request.method == 'POST':
        word = ""
        res = ""
        opt = request.form['grupo_opciones']
        campo = reg.trad.data.lower()
        if opt == 'opcion1':
            result = buscar(campo)
            if(result):
                result = result.split()
                word = "{} en {} es {}".format(campo, "español", result[0])
                res = 'success'
            else:
                word = 'No se encuentra la palabra en el diccionario'
                res = 'error'
        elif opt == 'opcion2':
            result = buscar(campo)
            if(result):
                result = result.split()
                word = "{} en {} es {}".format(campo, "inglés", result[1])
                res = 'success'
            else:
                word = 'No se encuentra la palabra en el diccionario'
                res = 'error'
        word = word.upper()
    return render_template('traductor.html', form=reg, word = word, res = res)

# Crea un decorador
@app.route("/Alumnos", methods=['GET', 'POST'])
def alumnos():
    reg_alumnos = forms.UserForm(request.form)
    nom = ''
    mat = ''
    if request.method == 'POST' and reg_alumnos.validate():
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
    cont = {}
    cont = contar_numeros(numeros)
    

    if numeroRep==None:
        numeroRep='No hay numero repetido'
    
    return render_template('calculos.html', prom=prom, max=maxim, min=minim, rep=numeroRep)

def buscar(parametro):
    with open('diccionario.txt', 'r') as f:
        lineas = f.readlines()
        for linea in lineas:
            datos = linea.split()
            if datos[0] == parametro:
                return linea.strip()
            elif datos[1] == parametro:
                return linea.strip()
            

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

def contar_numeros(lista):
    contador = {}
    for numero in lista:
        if numero in contador:
            contador[numero] += 1
        else:
            contador[numero] = 1
    return contador
    
if __name__ == '__main__':
    #csrf.init_app(app)
    app.run(debug=True, port=8084)