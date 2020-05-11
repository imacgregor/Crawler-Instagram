## Autor Erick Macgregor Santos Lima

import requests
import json
import os,sys
import fileinput
from datetime import datetime
import time
from random import randint

#lista de perfis
perfil = []
a = 0

#lendo os perfis adicionados no arquivo 'perfil.txt' para poder fazer a coleta
arquivo = open('perfis.txt','r')
for linha in arquivo:
	linha = linha.rstrip()
	perfil.append(linha)
	a+=1

#definir tempo de pausa entre as coletas em segundos
tempo = 3600

#verificando se a pasta coleta ja existe, ou criando ela
if os.path.isdir('coleta'):
    print('A pasta coleta existe')
else:
    path = "coleta"
    os.mkdir(path)
    print('A pasta coleta foi criada')

#criando as pastas para colocar os dados coletado de cada perfil ou verificando se ja existe
for a in range(0,len(perfil)):
	if os.path.isdir('coleta/'+perfil[a]):
	    print('O diretório {} existe'.format(perfil[a]))
	else:
	    path = "coleta/{}".format(perfil[a])
	    os.mkdir(path)
	    print('A pasta {} foi criada'.format(perfil[a]))


while(True):
	for a in range(0,len(perfil)):
		#lendo o perfil do instagram
		try:
			response = requests.get('https://www.instagram.com/{}/?__a=1'.format(perfil[a]))

			now = datetime.now()
			timestamp = datetime.timestamp(now)
			horario = str(timestamp)

			arq = 'coleta/'+perfil[a]+'/'+perfil[a]+horario+'.txt'

			#colocando as informacoes do perfil em um arquivo json
			with open(arq, mode = 'wb') as file:
				file.write(response.content)

			f = arq
			records = [json.loads(line) for line in open(f)]
			records[0]

	#criacao do dicionario que ira conter as informacoes sobre a midia do perfil
			midias = {
					'id' : 0,
					'curtidas' : 1,
					'comentarios' : 2,
					'timestamp' : 3,
					#'legenda' : "h",  @@ cancelado pois nem toda midia possui legenda
					'descricao_foto' : "S",
					'url_midia' : "4"
					#'localiza' : "c"    @@ cancelada pois nem toda midia possui localizacao
				}

			# lendo o arquivo json
			conteudo = open(arq).read()

			# salvando os dados do json em um dicionario
			infor_perfil = json.loads(conteudo)

			#filtrando as informacoes
			midias_para_salvar = 0
			seguidores = infor_perfil['graphql']['user']['edge_followed_by']['count']
			seguindo = infor_perfil['graphql']['user']['edge_follow']['count']
			numero_midias = int(infor_perfil['graphql']['user']['edge_owner_to_timeline_media']['count'])

			# verificando a quantidade de midias, a api so libera as ultimas 11 fotos
			# se tiver menos que onze fotos, mostrar todas as fotos, se tiver mais, mostrar so as 11
			if numero_midias < 11:
				midias_para_salvar = numero_midias
			else:
				midias_para_salvar = 11
			
			#salvando as informacoes das midias no dicionario
			for b in range(0,midias_para_salvar):

				midias[b] = {
					'id' : int(infor_perfil['graphql']['user']['edge_owner_to_timeline_media']['edges'][b]['node']['id']),
					'curtidas' : infor_perfil['graphql']['user']['edge_owner_to_timeline_media']['edges'][b]['node']['edge_liked_by']['count'],
					'comentarios' : infor_perfil['graphql']['user']['edge_owner_to_timeline_media']['edges'][b]['node']['edge_media_to_comment']['count'],
					'timestamp' : infor_perfil['graphql']['user']['edge_owner_to_timeline_media']['edges'][b]['node']['taken_at_timestamp'],
					'descricao_foto' : infor_perfil['graphql']['user']['edge_owner_to_timeline_media']['edges'][b]['node']['accessibility_caption'],
					#'legenda' : infor_perfil['graphql']['user']['edge_owner_to_timeline_media']['edges'][b]['node']['edge_media_to_caption']['edges'][0]['node']['text'],
					'url_midia' : infor_perfil['graphql']['user']['edge_owner_to_timeline_media']['edges'][b]['node']['display_url']
					#'localiza' : infor_perfil['graphql']['user']['edge_owner_to_timeline_media']['edges'][b]['node']['location']['slug']
				}

			#excluindo arquivo do json para poder rescrever com as informacoes filtradas
			def etc():
				path = 'coleta/'+perfil[a]
				dir = os.listdir(path)

				for file in dir:
					if file == perfil[a]+horario+'.txt':
						os.remove(file)

			
			#salvando as informacoes no arquivo
			with open(arq, 'w') as arquivo:
				arquivo.write('DATA/HORARIO: {}\n'.format(now))
				arquivo.write('SEGUIDORES: {}\n'.format(seguidores))
				arquivo.write('SEGUINDO {}\n'.format(seguindo))
				arquivo.write('NUMEROMIDIAS {}\n'.format(numero_midias))
				arquivo.write('MIDIAS: \n')
				for b in range(0,midias_para_salvar):
					arquivo.write("ID: {}\n".format(midias[b]['id']))
					arquivo.write("CURTIDAS: {}\n".format(midias[b]['curtidas']))
					arquivo.write("COMENTARIOS: {}\n".format(midias[b]['comentarios']))
					arquivo.write("TIMESTAMP: {}\n".format(midias[b]['timestamp']))
					timesta = midias[b]['timestamp']
					dt_object = datetime.fromtimestamp(timesta)
					arquivo.write("DTHRMIDIA: {}\n".format(dt_object))
					#arquivo.write("LEGENDA: {}\n".format(midias[b]['legenda']))
					arquivo.write("DESCRICAO: {}\n".format(midias[b]['descricao_foto']))
					arquivo.write("URL: {}\n".format(midias[b]['url_midia']))
					arquivo.write('\n')

			agora = datetime.fromtimestamp(timestamp)
			print('{} | Arquivo {} gravado com sucesso'.format(agora,arq))

			espera = randint(1,3)
			time.sleep(espera)
		#print(espera)
		except:
			print("!!!!!! ERRO COM O PERFIL {} !!!!!!!!".format(perfil[a]))
	#tempo de pausa entre a coleta
	time.sleep(tempo)