#coding: utf-8

#  
#  @JSagon - Jhonatan dos S. Gonçalves
#  http://www.jsagon.com
#
#  Classe principal para controle das funcionalidades do programa
#  Versão 1.0
#
from jtradutor.app import arquivo_controller as arq_controller

class Programa (object) :

	def getTranslate (self, indice, word) :
		
		if indice == 'pt_eng' :
			self.arquivo = arq_controller.Arquivo("jtradutor/app/idiomas_arq/pt_eng.txt")

		elif indice == 'eng_pt' : 
			self.arquivo = arq_controller.Arquivo("jtradutor/app/idiomas_arq/eng_pt.txt")
			
		self.arquivo.abrir_arquivo_leitura()
		return self.arquivo.pegar_ocorrencia_linhas(word)
		

