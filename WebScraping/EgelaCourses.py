# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup
#import getpass
#import urllib

#############################################################################################################
# 1.- https://egela1718.ehu.eus/login/index.php/
#############################################################################################################
#     Nos logeamos en eGela, pasamos como parámetros el LDAP y Passwd
#############################################################################################################

LDAP_usuario = raw_input("Insert your LDAP username: ")
LDAP_password = raw_input("Insert your LDAP password: ")

cuerpo_peticion = {'username': LDAP_usuario,
                  'password': LDAP_password}

response = requests.post('https://egela1819.ehu.eus/login/index.php/', data=cuerpo_peticion)

cookie = response.request.headers["Cookie"]

params = {'Cookie': cookie}
direccion = 'https://egela1819.ehu.eus/?lang=es'


response1 = requests.get(direccion, headers=params)
cuerpo_respuesta = response1.content
cookie = response1.request.headers["Cookie"]

if response1.status_code == 200 :

    html = BeautifulSoup(cuerpo_respuesta, "html.parser")
    courses = html.find_all("h3", class_="coursename")
    nombre = html.find("span", class_="usertext").getText()

    print "-------------------------------------------------------: "
    print "------------Nombre: " + str(nombre)
    print "-------------------------------------------------------: "
    print "---LAS ASIGNATURAS EN LAS QUE ESTAS MATRICULADO SON----: "
    print "-------------------------------------------------------: "
    print "-------------------------------------------------------: "

    i = 0
    cursos = []
    referencias = []
    stri = ""

    for course in courses:
        stri = stri + str(course)

        #print course
        for hijo in course.contents[0].children:
            print str(i) +" "+ hijo
            cursos.append(hijo)

        i = i +1

    html2 = BeautifulSoup(stri, "html.parser")
    for enlace in html2.find_all('a'):
        referencias.append(enlace.get("href"))

    print "\n"
    curso_seleccionado = raw_input("Introduce el indice del curso seleccionado: ")

    print "-------------------------------------------------------: "
    print "-------------------------------------------------------: "
    print "Has seleccionado: " + cursos[int(curso_seleccionado)]

    print "-------------------------------------------------------: "
    print "-------------------------------------------------------: "
    direccion = referencias[int(curso_seleccionado)]
    print "Su referencia es: " + direccion

    print "-------------------------------------------------------: "
    print "-------------------------------------------------------: "
    print "Obteniendo temario de la asignatura..."


    params = {'Cookie': cookie}
    response2 = requests.get(direccion, headers=params)
    cuerpo_respuesta = response2.content
    cookie = response2.request.headers["Cookie"]

    html = BeautifulSoup(cuerpo_respuesta, "html.parser")
    secciones = html.find_all("span", class_="hidden sectionname")

    stri = ""
    for seccion in secciones:
        stri = stri + str(seccion)

    print "-------------------------------------------------------: "
    print "----------------------TEMARIO--------------------------: "
    print "-------------------------------------------------------: "
    print "-------------------------------------------------------: "
    html2 = BeautifulSoup(stri, "html.parser")
    for sec in html2.find_all('span'):
        print str(sec.getText().encode("utf-8"))




else:
    print "Status Code:" + response1.status()