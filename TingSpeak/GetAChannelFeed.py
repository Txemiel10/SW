#  -*- coding: utf-8 -*-
#JOSE MIGUEL VEGA DIAZ

import httplib
import urllib

CHANNEL_ID = "700367"
READ_API_KEY = "4RD66XCAKNP3J92R"
FORMATO = "json" #json o xml

print "\r\n----> estableciendo conexion TCP"
server = "api.thingspeak.com"
conn = httplib.HTTPSConnection(server)
conn.connect()
print "---> conexion TCP establecida"

parametros = {"api_key": READ_API_KEY}

params_encoded = urllib.urlencode(parametros)
uri = "/channels/"+CHANNEL_ID+"/feeds."+FORMATO+"?"+params_encoded

headers = {"Host": server}

conn.request("GET", uri, headers=headers, body=params_encoded)

respuesta = conn.getresponse()
datos = respuesta.read()
print "STATUS " + str(respuesta.status)
print "CONTENT " + datos

conn.close()
