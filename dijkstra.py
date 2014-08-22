#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from os import system
from os import name

#Limpa o terminal de acordo com o S.O.
def clear():
	system(['clear','cls'][name == 'nt'])

class dijkstra:
	vertices = None #Lista de vertices.
	matrix = {} #Matriz de transição.
	initial = None #Vertice inicial.
	distances = {} #Lista de distancia.
	predecessors = {} #Lista de antecessores.

	#Carrega um grafo salvo em uma arquivo.
	def read(self, name):
		try:
			if name == '':
				name = 'entrada.txt'
			graphFile = open(name)
			
			self.vertices = graphFile.readline()
			self.vertices = self.vertices.replace(' ', '').replace('\n', '').split(',')

			#Le a matriz de transição, substituindo o caracter '-' pelo maior inteiro suportado pelo sistema.
			for line in self.vertices:
				counter = 0
				distances = graphFile.readline().split()
				for column in self.vertices:
					if distances[counter] == '-':
						distances[counter] = sys.maxint
					self.matrix[(line,column)] = int(distances[counter])
					counter += 1

			graphFile.close()

			print 'Grafo carregado com sucesso.'
			return True

		except:
			print "Falha ao carregar o grafo."
			return False

	#Executa o algoritmo no grafo carregado. Obs: No modo interativo, todos os passos são apresentados ao usuario.
	def run(self, interactive = False, initial = ''):
		row = {}

		for vertice in self.vertices:
			self.distances[vertice] = sys.maxint
			row[vertice] = True
		
		self.distances[initial] = 0
		new = initial

		counter = 1

		while row != {}:
			header = ''
			body = ''
			body2 = ''
			
			smaller = sys.maxint
			actual = new
			new = None

			for vertice in self.vertices:
				header += '{: ^10}'.format(vertice) + '|'
				if self.distances[vertice] == sys.maxint:
					body +=	'{: ^10}'.format('-') + '|'
				else:
					body += '{: ^10}'.format(str(self.distances[vertice])) + '|'
				try:
					body2 += '{: ^10}'.format(str(self.predecessors[vertice])) + '|'
				except:
					body2 += '{: ^10}'.format('-') + '|'
				
				if self.distances[actual] + self.matrix[actual, vertice] < self.distances[vertice]:
					self.distances[vertice] = self.distances[actual] + self.matrix[actual, vertice]
					self.predecessors[vertice] = actual
				
			row.pop(actual)

			for i in row:
				if self.distances[i] < smaller:
					new = i
					smaller = self.distances[i]
			
			if interactive:
				print '\nPasso ', counter
				print header
				print body
				print body2
			counter += 1

		if not interactive:
			self.result()

	#Exibe o resultado.
	def result(self):
		header = '{: ^20}'.format('Vertice - ')
		body= '{: ^20}'.format('Distancia - ')
		body2 = '{: ^20}'.format('Antecessor - ')

		for vertice in self.vertices:
				header += '{: ^10}'.format(vertice) + '|'
				if self.distances[vertice] == sys.maxint:
					body +=	'{: ^10}'.format('-') + '|'
				else:
					body += '{: ^10}'.format(str(self.distances[vertice])) + '|'
				
				try:
					body2 += '{: ^10}'.format(str(self.predecessors[vertice])) + '|'
				except:
					body2 += '{: ^10}'.format('-') + '|'
		print header
		print body
		print body2

	#Salva o resultado em um arquivo.
	def save(self):
		resultFile = open("resutado.txt", 'w')

		header = '{: ^20}'.format('Vertice - ')
		body= '{: ^20}'.format('Distancia - ')
		body2 = '{: ^20}'.format('Antecessor - ')

		for vertice in self.vertices:
				header += '{: ^10}'.format(vertice) + '|'
				if self.distances[vertice] == sys.maxint:
					body +=	'{: ^10}'.format('-') + '|'
				else:
					body += '{: ^10}'.format(str(self.distances[vertice])) + '|'
				
				try:
					body2 += '{: ^10}'.format(str(self.predecessors[vertice])) + '|'
				except:
					body2 += '{: ^10}'.format('-') + '|'
		
		resultFile.write(header)
		resultFile.write('\n')
		resultFile.write(body)
		resultFile.write('\n')
		resultFile.write(body2)

		resultFile.close()

def main():
	grafo = dijkstra()
	functional = grafo.read("entrada.txt")

	done = False
	while not done:
		
		if functional:
			option = str(raw_input("Deseja consultar um vertice? (Y/n): "))
			if option.lower() == 'y' or option == '':
				vertice = str(raw_input("Informe o vertice: "))

				option = str(raw_input("Deseja executar em modo interativo? (Y/n): "))
				if option.lower() == 'y' or option == '':
					option = True
				else:
					option = False
				clear()
				grafo.run(option, vertice)
				grafo.save()

			else:
				option = str(raw_input("Deseja carregar um novo grafo? (Y/n): "))
				if option.lower() == 'y' or option == '':
					fileName = str(raw_input("Informe o nome do arquivo (ou deixe em branco para carregar o arquivo default): "))
					functional = grafo.read(fileName)
				else:
					done = True
		else:
			option = str(raw_input("Deseja carregar um novo grafo? (Y/n): "))
			if option.lower() == 'y' or option == '':
				fileName = str(raw_input("Informe o nome do arquivo (ou deixe em branco para carregar o arquivo default): "))
				functional = grafo.read(fileName)
			else:
				done = True

if __name__ == '__main__':
	clear()
	main()
	clear()