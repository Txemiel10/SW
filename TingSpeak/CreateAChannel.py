#  -*- coding: utf-8 -*-
#JOSE MIGUEL VEGA DIAZ

import httplib
import urllib

API_KEY = "WJACDJKAYY1VGY00"
NAME = "Prueba crear canal"
FORMATO = "json" #json o xml

print "\r\n----> estableciendo conexion TCP"
server = "api.thingspeak.com"
conn = httplib.HTTPSConnection(server)
conn.connect()
print "---> conexion TCP establecida"

uri = "/channels."+FORMATO
parametros = {"api_key": API_KEY,
              "name": NAME}

params_encoded = urllib.urlencode(parametros)
headers = {"Host": server,
           "Content-Type": "application/x-www-form-urlencoded",
           "Content-Length": str(len(params_encoded))}

conn.request("POST", uri, headers=headers, body=params_encoded)

respuesta = conn.getresponse()
respuesta_read = respuesta.read()
print "STATUS " + str(respuesta.status)
print "CONTENT " + respuesta_read

conn.close()
