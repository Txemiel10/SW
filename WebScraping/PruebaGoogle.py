import requests
from bs4 import BeautifulSoup

response = requests.get("http://google.com/")

print " STATUS: " + str(response.status_code)
print " CABECERAS: " + str(response.headers)

cuerpo_respuesta = response.content

if response.status_code == 200 :
    html = BeautifulSoup(cuerpo_respuesta, "html.parser")

    print "-----------------------"
    print html.head

    print "-----------------------"
    print html.head.name
    print "---------------------------------------"

    print html.head.string
    print "---------------------------------------"
    print "---------------------------------------"
    print html.p.a
    print "---------------------------------------"

    print "---------------CUERPO DE LA RESPUESTA------------------------"
    print html.head.meta['content']
    print "---------------------------------------"
    print html.title
    print "---------------------------------------"
    print html.title.string
    print html.p.a.string
    print "---------------------------------------"
    print html.a
    print "---------------------------------------"
    print html.p.a.parent.name
    print "---------------------------------------"
    print "---------------------------------------"
    print html.p
    print "---------------------------------------"
    print html.p.name
    print "---------------------------------------"
    print html

    print "---------------------------------------"
    print html.a.parent.name
    print "---------------------------------------"
    print html.p.a
    print "---------------------------------------"
    print html.a
    print html.p.string
    print "---------------------------------------"
    print html.p['style']
    print html.p.get('style')
    print html.p.text

    print "---------------------------------------"
    print "-- Todos los enlaces ------------------"
    for enlace in html.find_all('a'):
        print enlace
    print "---------------------------------------"
    print "-- Todos los textos ------------------"
    print(html.get_text())
    print "---------------------------------------"
    for link in html.find_all('a'):
        print(link.get('href'))

else:
    print "Status Code:" + response.status()

