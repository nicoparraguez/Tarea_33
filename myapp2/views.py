from django.shortcuts import render, render_to_response
import requests
import json
import urllib
from django.http import HttpResponse


def index(request):
	films = []
	ruta = "https://swapi-graphql-integracion-t3.herokuapp.com/"
	headers = {'content-type': 'application/json'}
	consulta = {"query": "{allFilms { edges { node { id episodeID title releaseDate director producers episodeID }}}}"}
	respuesta = requests.post(ruta, data=json.dumps(consulta), headers=headers).json()
	print(respuesta)
	for peliculas2 in respuesta["data"]["allFilms"]["edges"]:
		peli = peliculas2["node"]
		films.append({"title": peli['title'], "id": peli['id'],
         "year": peli["releaseDate"], "director": peli["director"], "productor": peli["producers"], "episodeID": peli['episodeID']
         })

	dic_aux = {"pelis" : films}
	return render_to_response('inicial.html',dic_aux)

def pelis(request):
	film = request.GET.get("id_")
	info = {}
	ruta = "https://swapi-graphql-integracion-t3.herokuapp.com/"
	headers = {'content-type': 'application/json'}
	consulta = {"query": "{film(id: \""+film+"\") { id title created edited director producers episodeID openingCrawl releaseDate characterConnection { edges { node { id name }}} planetConnection { edges {node {id name}  }} starshipConnection {  edges {node {id name}  }}}}"}
	respuesta = requests.post(ruta, data=json.dumps(consulta), headers=headers).json()
	planetas = {}
	personajes = {}
	naves = {}

	for persona in respuesta["data"]["film"]["characterConnection"]["edges"]:
		pers = persona["node"]
		personajes[pers["name"]] = pers["id"]

	for planeta in respuesta["data"]["film"]["planetConnection"]["edges"]:
		plane = planeta["node"]
		planetas[plane["name"]] = plane["id"]

	for nave in respuesta["data"]["film"]["starshipConnection"]["edges"]:
		nav = nave["node"]
		naves[nav["name"]] = nav["id"]

	info["personajes"] = personajes
	info["planetas"] = planetas
	info["naves"] = naves
	info["director"] = respuesta["data"]["film"]["director"]
	info["producers"] = respuesta["data"]["film"]["producers"]
	info["episodeID"] = respuesta["data"]["film"]["episodeID"]
	info["openingCrawl"] = respuesta["data"]["film"]["openingCrawl"]
	info["title"] = respuesta["data"]["film"]["title"]
	info["created"] = respuesta["data"]["film"]["created"]
	info["edited"] = respuesta["data"]["film"]["edited"]
	info["releaseDate"] = respuesta["data"]["film"]["releaseDate"]
	dict_aux2 = {'infox2': info}
	return render_to_response('pelicula.html', dict_aux2)


def naves(request):
	star = request.GET.get("id_")
	info = {}
	ruta = "https://swapi-graphql-integracion-t3.herokuapp.com/"
	headers = {'content-type': 'application/json'}
	consulta = {"query": "{starship(id: \""+star+"\") {id name model starshipClass manufacturers costInCredits length crew passengers maxAtmospheringSpeed hyperdriveRating MGLT cargoCapacity consumables created edited filmConnection {  edges {node {  title  id}  }} pilotConnection {  edges {node {  name  id}  }}}}"}
	respuesta = requests.post(ruta, data=json.dumps(consulta), headers=headers).json()
	peliculas = {}
	personajes = {}

	for peli in respuesta["data"]["starship"]["filmConnection"]["edges"]:
		pel = peli["node"]
		peliculas[pel["title"]] = pel["id"]

	for persona in respuesta["data"]["starship"]["pilotConnection"]["edges"]:
		person = persona["node"]
		personajes[person["name"]] = person["id"]





	
	info["personajes"] = personajes
	info["peliculas"] = peliculas
	info["id"] = respuesta["data"]["starship"]["id"]
	info["name"] = respuesta["data"]["starship"]["name"]
	info["model"] = respuesta["data"]["starship"]["model"]
	info["starshipClass"] = respuesta["data"]["starship"]["starshipClass"]
	info["manufacturers"] = respuesta["data"]["starship"]["manufacturers"]
	info["costInCredits"] = respuesta["data"]["starship"]["costInCredits"]
	info["length"] = respuesta["data"]["starship"]["length"]
	info["crew"] = respuesta["data"]["starship"]["crew"]
	info["passengers"] = respuesta["data"]["starship"]["passengers"]
	info["hyperdriveRating"] = respuesta["data"]["starship"]["hyperdriveRating"]
	info["MGLT"] = respuesta["data"]["starship"]["MGLT"]
	info["cargoCapacity"] = respuesta["data"]["starship"]["cargoCapacity"]
	info["consumables"] = respuesta["data"]["starship"]["consumables"]
	info["created"] = respuesta["data"]["starship"]["created"]
	info["edited"] = respuesta["data"]["starship"]["edited"]

	dict_aux2 = {"infox2":info}
	return render_to_response('nave.html', dict_aux2)


def personajes(request):
	person = request.GET.get('id_')
	ruta = "https://swapi-graphql-integracion-t3.herokuapp.com/"
	headers = {'content-type': 'application/json'}
	info = {}
	consulta = {"query": "{person(id: \""+person+"\") {id name birthYear eyeColor gender hairColor height mass created edited filmConnection {  edges {node {  title  id}  }} starshipConnection {  edges {node {  name  id}  }} homeworld {name id}  }}"}
	respuesta = requests.post(ruta, data=json.dumps(consulta), headers=headers).json()
	peliculas = {}
	naves = {}
	planetas = {}

	for peli in respuesta["data"]["person"]["filmConnection"]["edges"]:
		pel = peli["node"]
		peliculas[pel["title"]] = pel["id"]

	for nave in respuesta["data"]["person"]["starshipConnection"]["edges"]:
		nav = nave["node"]
		naves[nav["name"]] = nav["id"]

	planetas[respuesta["data"]["person"]["homeworld"]["name"]] = respuesta["data"]["person"]["homeworld"]["id"]

	info["peliculas"] = peliculas
	info["naves"] = naves
	info["planetas"] = planetas
	info["id"] = respuesta["data"]["person"]["id"]
	info["name"] = respuesta["data"]["person"]["name"]
	info["birthYear"] = respuesta["data"]["person"]["birthYear"]
	info["eyeColor"] = respuesta["data"]["person"]["eyeColor"]
	info["gender"] = respuesta["data"]["person"]["gender"]
	info["hairColor"] = respuesta["data"]["person"]["hairColor"]
	info["height"] = respuesta["data"]["person"]["height"]
	info["mass"] = respuesta["data"]["person"]["mass"]
	info["created"] = respuesta["data"]["person"]["created"]
	info["edited"] = respuesta["data"]["person"]["edited"]

	dict_aux2 = {"infox2":info}
	return render_to_response('personaje.html', dict_aux2)


def planetas(request):
	planet = request.GET.get("id_")
	info = {}
	ruta = "https://swapi-graphql-integracion-t3.herokuapp.com/"
	headers = {'content-type': 'application/json'}
	consulta = {"query": "{planet(id: \""+planet+"\") {id name diameter rotationPeriod orbitalPeriod gravity population climates terrains surfaceWater created edited filmConnection {  edges {node {  title  id}  }}residentConnection {  edges {node {  name  id}  }}}}"}
	respuesta = requests.post(ruta, data=json.dumps(consulta), headers=headers).json()
	peliculas = {}
	personajes = {}

	for peli in respuesta["data"]["planet"]["filmConnection"]["edges"]:
		pel = peli["node"]
		peliculas[pel["title"]] = pel["id"]

	for persona in respuesta["data"]["planet"]["residentConnection"]["edges"]:
		person = persona["node"]
		personajes[person["name"]] = person["id"]

	info["personajes"] = personajes
	info["peliculas"] = peliculas
	info["id"] = respuesta["data"]["planet"]["id"]
	info["name"] = respuesta["data"]["planet"]["name"]
	info["diameter"] = respuesta["data"]["planet"]["diameter"]
	info["rotationPeriod"] = respuesta["data"]["planet"]["rotationPeriod"]
	info["orbitalPeriod"] = respuesta["data"]["planet"]["orbitalPeriod"]
	info["gravity"] = respuesta["data"]["planet"]["gravity"]
	info["population"] = respuesta["data"]["planet"]["population"]
	info["climates"] = respuesta["data"]["planet"]["climates"]
	info["terrains"] = respuesta["data"]["planet"]["terrains"]
	info["surfaceWater"] = respuesta["data"]["planet"]["surfaceWater"]
	info["created"] = respuesta["data"]["planet"]["created"]
	info["edited"] = respuesta["data"]["planet"]["edited"]

	dict_aux2 = {"infox2":info}
	return render_to_response('planetas.html', dict_aux2)





