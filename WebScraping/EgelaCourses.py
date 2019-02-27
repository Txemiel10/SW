#JOSE MIGUEL VEGA DIAZ

# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup

#############################################################################################################
#   Nos logeamos en egela introduciendo usuario y la pass
#############################################################################################################

LDAP_usuario = raw_input("Insert your LDAP username: ")
LDAP_password = raw_input("Insert your LDAP password: ")

cuerpo_peticion = {'username': LDAP_usuario,
                  'password': LDAP_password}

#############################################################################################################
#     Almacenamos la respuesta de la peticion y guardamos la cookie
#############################################################################################################

response = requests.post('https://egela1819.ehu.eus/login/index.php/', data=cuerpo_peticion)

cookie = response.request.headers["Cookie"]


#############################################################################################################
#     Hacemos una peticion de la pagina donde tenemos los cursos enviando la cookie que habiamos almacenado
#     como parametro
#############################################################################################################

params = {'Cookie': cookie}
direccion = 'https://egela1819.ehu.eus/?lang=es'
response1 = requests.get(direccion, headers=params)

#############################################################################################################
#     Almacenamos la respuesta de la peticion y guardamos la cookie
#############################################################################################################

cuerpo_respuesta = response1.content
cookie = response1.request.headers["Cookie"]


#############################################################################################################
#     Si el status es 200 hacemos el hatml con Beautiful soup
#############################################################################################################

if response1.status_code == 200 :

    #parseamos la respuesta a html y buscamos los cursos que se encuentran en las etiquetas h3 con la class coursename
    html = BeautifulSoup(cuerpo_respuesta, "html.parser")
    courses = html.find_all("h3", class_="coursename")

    #Buscamos y guardamos el nombre del usuario logeado
    nombre = html.find("span", class_="usertext").getText()

    print "-------------------------------------------------------: "
    print "------------Nombre: " + str(nombre)
    print "-------------------------------------------------------: "
    print "---LAS ASIGNATURAS EN LAS QUE ESTAS MATRICULADO SON----: "
    print "-------------------------------------------------------: "
    print "-------------------------------------------------------: "

    #inicializamos lo necesario para guardar un array con los nombres de los cursos y otros con sus referencias
    i = 0
    cursos = []
    referencias = []
    stri = ""

    #guardamos los nombres de las etiquetas cursos en un string para luego parsearlos
    for course in courses:
        stri = stri + str(course)

        #printeamos los nombres de los cursos por pantalla
        for hijo in course.contents[0].children:
            print str(i) +" "+ hijo
            cursos.append(hijo)

        i = i +1

    #paraseamos los cursos guaradados en el string para poder sacar las referencias posteriormente
    html2 = BeautifulSoup(stri, "html.parser")

    #obtenemos las referencias de los cursos y loss guardamos en el array de referencias
    for enlace in html2.find_all('a'):
        referencias.append(enlace.get("href"))

    #el usuario introduce un indice de curso que selecciona el curso en el array y lo printea
    print "\n"
    curso_seleccionado = raw_input("Introduce el indice del curso seleccionado: ")

    print "-------------------------------------------------------: "
    print "-------------------------------------------------------: "
    print "Has seleccionado: " + cursos[int(curso_seleccionado)]

    #printeamos la referencia de dicho curso
    print "-------------------------------------------------------: "
    print "-------------------------------------------------------: "
    direccion = referencias[int(curso_seleccionado)]
    print "Su referencia es: " + direccion

    print "-------------------------------------------------------: "
    print "-------------------------------------------------------: "
    print "Obteniendo temario de la asignatura..."

    #############################################################################################################
    #     Hacemos una peticion de la pagina donde tenemos la informacion del curso seleccionado enviando la cookie que habiamos almacenado
    #     como parametro y utilizando el href como direccion
    #############################################################################################################

    params = {'Cookie': cookie}
    response2 = requests.get(direccion, headers=params)

    #############################################################################################################
    #     Almacenamos la respuesta de la peticion y guardamos la cookie
    #############################################################################################################
    cuerpo_respuesta = response2.content
    cookie = response2.request.headers["Cookie"]

    #parseamos la respuesta a html y obtenemos las secciones que se encuentran en tags span, con class hidden sectionname
    html = BeautifulSoup(cuerpo_respuesta, "html.parser")
    secciones = html.find_all("span", class_="hidden sectionname")

    #para cada seccion almacenamos su etiqueta en un string para luego parsearlo
    stri = ""
    for seccion in secciones:
        stri = stri + str(seccion)


    #imprimimos el temario a partir del string parseado y obteniendomelo haciendo scrapping
    print "-------------------------------------------------------: "
    print "----------------------TEMARIO--------------------------: "
    print "-------------------------------------------------------: "
    html2 = BeautifulSoup(stri, "html.parser")
    for sec in html2.find_all('span'):
        print str(sec.getText().encode("utf-8"))


#############################################################################################################
#     Si el status no es 200 lo printeamos por pantalla
#############################################################################################################

else:
    print "Status Code:" + response1.status()