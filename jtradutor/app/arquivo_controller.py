#coding: utf-8

#  
#  @JSagon - Jhonatan dos S. Gonçalves
#  http://www.jsagon.com
#
#  Classe responsável pelo controle padrão de arquivo
#  Versão 1.0 - Novas funcionalidades serão adicionadas
#

class Arquivo(object) :

	def __init__(self, nome_arq):
		self.nome_arquivo = nome_arq

	def abrir_arquivo_leitura (self):
		self.arquivo = open (self.nome_arquivo, encoding='utf-8')

	def abrir_arquivo_escrita (self):
		self.arquivo = open (self.nome_arquivo, "w")

	def fechar (self):
		self.arquivo.close()

	def ler_todo (self):
		return self.arquivo.read()

	def ler_linha (self):
		return self.arquivo.readline()

	def set_posicao (self, pos):
		self.arquivo.seek(pos)

	def pegar_ocorrencia_linhas(self, nome, limit = 10) :
		self.set_posicao(0)
		
		linhas = []
		countLimit = 0

		for linha in self.arquivo:
			linhaA = linha.split("=")
			result = linhaA[0].strip()
			#Todas as palavras que começam com o texto informado
			#if(linha.startswith(nome)):

			#Todas as palavras que contem o texto informado
			#if(nome in result[0]):
			
			#if nome == result:
			if(result.startswith(nome)):
				linhas.append({'word' : result, 'translate' : linhaA[1].strip()})
				countLimit+=1

			if countLimit == limit:
				break

		return linhas