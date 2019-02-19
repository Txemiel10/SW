#  -*- coding: utf-8 -*-
#JOSE MIGUEL VEGA DIAZ

import psutil
import httplib
import urllib

CHANNEL_ID = "700367"
WRITE_API_KEY = "ZSEFTAEWM05D0WPE"
FORMATO = "json" #json o xml

print "\r\n----> estableciendo conexion TCP"
server = "api.thingspeak.com"
conn = httplib.HTTPSConnection(server)
conn.connect()
print "---> conexion TCP establecida"

cpuPercent = psutil.cpu_percent(interval=15)
ramPercent = psutil.virtual_memory().percent
print " CPU = " + str(cpuPercent) + " RAM: " + str(ramPercent)

uri = "/update."+FORMATO
parametros = {"api_key": WRITE_API_KEY,
              "field1": str(cpuPercent),
              "field2": str(ramPercent)}

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

