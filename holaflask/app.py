from flask import Flask
app=Flask(__name__)
    
@app.route("/")
def holaflask():
    return "<h1>¡hola flask!</h1> <hr>"

#primer punto
@app.route("/notas")
@app.route("/notas/<float:nota1>/<float:nota2>/<float:nota3>")
def notas(nota1=0,nota2=0,nota3=0):
    resultado=round((nota1*30)/100+(nota2*30)/100+(nota3*40)/100,2)
    return f"<h1> El resultado es: {resultado}</h1> <hr>"

#segundo punto
@app.route("/edades")
@app.route("/edades/<int:edad>")
def edades(edad=0):
    if edad<18:
        R="Menor de edad"
    elif(edad<60):
        R="Adulto"
    else:
        R="Adulto mayor"
    return f"<h1>La persona es: {R}</h1> <hr>"

#tercer punto
import numpy as np
@app.route("/arreglos")
@app.route("/arreglos/<int:valores>/<int:columnas>") 
@app.route("/arreglos/<int:valores>/<int:columnas>/<int:filas>")
def arreglos(valores=0,columnas=0,filas=0):
    if filas==0:
        arreglo=np.random.randint(valores, size=columnas)
    else:
        arreglo=np.random.randint(valores, size=(filas,columnas))
        
    return f"<h1> El arreglo aleatorio es: {arreglo} </h1> <hr>"

#1.) Haga un programa que calcule la siguiente ecuación: Y = X * Z + Z + X
import numpy as np
@app.route("/calculos")
@app.route("/calculos/<int:x>/<int:z>")
def valores(x=0,z=0):
    resultado=x * z + z + x
    return f"<hr><h1> y es = {resultado}</h1></hr>"

#2.) Realizar programa que, capturado un número, realice la tabla de multiplicar de ese número  hasta el 10.
import numpy as np
@app.route("/multiplicacion")
@app.route("/multiplicacion/<int:num>")
def multiplicacion(num=0):
    resultado=(num*1,num*2,num*3,num*4,num*5,num*6,num*7,num*8,num*9,num*10,)
    return f"<hr><h1>{resultado}</h1></hr>"

#3.) Realizar el programa que calcule las áreas de un círculo, cuadrado y triangulo.
import numpy as np
@app.route("/areacu/cuadrado")
@app.route("/areacu/cuadrado/<int:num>")
def areacu(num=0):
    resp=(num*2)
    return f"<h1>El area del cuadrado es:{resp}</h1>"

@app.route("/areatr/triangulo")
@app.route("/areatr/triangulo/<int:b>/<int:a>")
def areatr(b=0,a=0):
    resp=(b*a)/2
    return f"<h1>El area del triangulo es:{resp}</h1>"

@app.route("/areaci/circulo")
@app.route("/areaci/circulo/<int:r>")
def areaci(r=0):
    resultado=((r*2)*3.14)
    return f"<h1>El area del circulo es:{resultado}</h1>"

                       

if __name__ == '__main__':
    app.run(debug=True)