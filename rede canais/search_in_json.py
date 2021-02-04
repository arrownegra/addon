# -*- coding: utf-8 -*-
#
import os
import json


file_path = 'filmes.json'
parameter = input('DIGITE O NOME DO FILME QUE DESEJA BUSCAR: ')

if ' ' in parameter:
    list_parameter = []
    for item in parameter.split(' '):
        list_parameter.append(item.capitalize())
    parameter = ' '.join(list_parameter)
else:
    parameter = parameter.capitalize()

with open(file_path) as json_file:
    data = json.load(json_file)
    list_films = []
    for i, item in enumerate(data):
        films = json.dumps(item)
        try:
            if parameter in str(item['title']):
                list_films.append(item)
        except:
            pass
print(list_films)
