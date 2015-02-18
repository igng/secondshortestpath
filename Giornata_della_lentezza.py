# *-* coding: utf-8 *-*

import time, math, random, os, platform, sys

##########################	STRUCTURES	################################

class Node:
	def __init__(self, value, elem):
		self._value = value							#Valore del nodo
		self._adlist = []							#Lista di adiacenza
		self._child = []							#Lista dei figli nell'heap
		self._elem = elem							#Elemento nel nodo
		self._key = 1e10							#Chiave del nodo
		self._spath = 1e10							#Cammino minimo dal nodo 1
		self._sspath = 1e10							#Secondo cammino minimo dal nodo 1
		self._spar = None							#Padre nel cammino minimo
		self._sspar = None							#Padre nel secondo cammino minimo
		self._heaparent = None						#Padre nell'heap
		self._added = 0								#Flag per l'inserimento nell'heap
	def setShortPath(self, new_spath):
		self._spath = new_spath						#int
	def setSecondShortPath(self, new_sspath):
		self._sspath = new_sspath					#int
	def setShortParent(self, new_short_parent):
		self._spar = new_short_parent				#node
	def setSecondShortParent(self, new_second_short_parent):
		self._sspar = new_second_short_parent		#node
	def getShortPath(self):
		return self._spath							#int
	def getSecondShortPath(self):
		return self._sspath							#int
	def getShortParent(self):
		return self._spar							#node
	def getSecondShortParent(self):
		return self._sspar							#node
	def getValue(self):
		return self._value							#int
	def getKey(self):
		return self._key							#int
	def getElem(self):
		return self._elem							#int
	def setHeaParent(self, new_heaparent):
		self._heaparent = new_heaparent				#node
	def getHeaParent(self):
		return self._heaparent						#node
	def addHeapSon(self, son):
		self._child.append(son)						#node
		
def Link(aNode, bNode, distance):					#appendo [nodo, distanza] alla lista di adiacenza
	aNode._adlist.append([bNode, distance])
	bNode._adlist.append([aNode, distance])
	
class BinomialHeap:
	def __init__(self):			
		self._leaves = []
	def heapInsert(self, node, key):				#O(log(n))
		node._key = key
		self._leaves.append(node)
		node._added = 1
		len_child = len(node._child)
		B[len_child].append(node)
		self.restruct()
	def findMin(self):								#O(log(n))
		min_key = 1e10
		min_node = Node(1e10, 1e10)
		for root in self._leaves:
			if root._key <= min_key:
				min_key = root._key
				min_node = root
		return min_node
	def deleteMin(self):							#O(log(n))
		min_node = self.findMin()
		self._leaves.remove(min_node)
		B[len(min_node._child)].remove(min_node)
		for child in min_node._child:
				self.heapInsert(child, child._key)
		self.restruct()
		elem = min_node.getElem()%(len(Graph)/2)
		return Graph[elem]
	def decreaseKey(self, node, amount):			#O(log(n))
		node._key -= amount		
		moveUp(node)
	def restruct(self):								#O(log(n))
		for i in range(len(B)-1):
			lista = B[i]
			while (len(lista) > 1):
				B[i+1].append(merge(self._leaves, lista[0], lista[1]))
				del lista[0:2]
	def isEmpty(self):
		return len(self._leaves) == 0
					
def merge(heap, aRoot, bRoot):						#O(1)
	if (aRoot.getKey() <= bRoot.getKey()):
		aRoot.addHeapSon(bRoot)
		bRoot.setHeaParent(aRoot)
		heap.remove(bRoot)
		return aRoot
	else:
		bRoot.addHeapSon(aRoot)
		aRoot.setHeaParent(bRoot)
		heap.remove(aRoot)
		return bRoot

def moveUp(node):									#O(log(n))
	parent = node.getHeaParent()
	while ((parent != None) and (node.getKey() < parent.getKey())):
		node._key, parent._key = parent._key, node._key
		node._elem, parent._elem = parent._elem, node._elem

##########################	FUNCTIONS	################################

def menu():
	global flag
	flag = 1
	if (platform.system() == "Windows"):
		print "|" + "-"*67 + "|"
		print "|" + "-"*25 + " Cosa vuoi fare? " + "-"*25 + "|"
		print "|                                                                   |"
		print "|    1.  Inserire un file di input su cui eseguire l'algoritmo      |" 
		print "|    2.  Eseguire l'algoritmo su un file generato dal generatore    |"
		print "|                                                                   |"
		print "|   -----------------------------------------------------------     |"
		print "|                                                                   |"
		print "|     Per una migliore formattazione dei risultati si consiglia     |"
		print "|            di impostare il terminale a tutto schermo              |"
		print "|                                                                   |"
		print "|" + "-"*67 + "|"
		print "|" + "-"*67 + "|\n"
		flag = 0
	else:
		b = u"\u25BC"
		t = u"\u25B2"
		l = u"\u25C0"
		r = u"\u25B6"
		top = b*26
		print b*69
		print top + " Cosa vuoi fare? " + top
		print r+r+"                                                                 "+l+l
		print r+r+"    1.  Inserire un file di input su cui eseguire l'algoritmo    "+l+l 
		print r+r+"    2.  Eseguire l'algoritmo su un file generato dal generatore  "+l+l
		print r+r+"                                                                 "+l+l
		print r+r+"   -----------------------------------------------------------   "+l+l
		print r+r+"                                                                 "+l+l
		print r+r+"    Per una migliore formattazione dei risultati si consiglia    "+l+l
		print r+r+"            di impostare il terminale a tutto schermo            "+l+l
		print r+r+"                                                                 "+l+l
		print t*69
		print t*69,"\n"
	choice = input("")
	while ((choice != 1) and (choice != 2)):
		choice = input("Errore:\t\tOperazione non supportata. Scegliere solamente una delle opzioni proposte.\n")
	if (choice == 1):
		input_file = insert_input()
		return input_file
	else:
		return 0
		
def insert_input():
	input_file = raw_input("\nInserire il percorso completo del file da aprire:\n")
	while (not os.path.exists(input_file)):
		print "Errore:\t\tImpossibile aprire il file '" + input_file + "'. Riprovare\n"
		input_file = raw_input("\nInserire il percorso completo del file da aprire:\n")
	return input_file

def output_path():										#1 Linux/OS X; 0 Windows
	path = raw_input("\nInserire il percorso in cui salvare il file di output:\n")
	while (not os.path.exists(path)):
		print "Errore:\t\tPercorso non esistente. Riprovare.\n"
		path = raw_input("\nInserire il percorso in cui salvare il file di output:\n")
	name = raw_input("\nInserire il nome del file di output:\n")
	if (flag):
		if (path[-1] != '/'):
			path = path + "/" + name
		else:
			path = path+name
	else:
		if (path[-1] != "\\"):
			path = path + "\\" + name
		else:
			path = path+name
	preview = open(path, 'w')							
	preview.close()
	print "\nPercorso del file di output:",path,"\n"
	return path

def input_generator():
	MAX_CASES = int(input("Inserire il massimo numero di casi (numero intero compreso tra 1 e 10): "))
	while (not (1 <= MAX_CASES <= 10)):
		print "Errore:\t\tMassimo numero di casi non valido. Riprovare.\n"
		MAX_CASES = int(input("Inserire il massimo numero di casi (numero intero compreso tra 1 e 10): "))
	MAX_NODES = int(input("Inserire il massimo numero di nodi (numero intero compreso tra 1 e 5000): "))
	while (not (1 <= MAX_NODES <= 5000)):
		print "Errore:\t\tMassimo numero di nodi non valido. Riprovare.\n"
		MAX_NODES = int(input("Inserire il massimo numero di nodi (numero intero compreso tra 1 e 5000): "))
	MAX_EDGES = int(input("Inserire il massimo numero di archi (numero intero compreso tra 1 e 10000): "))
	while (not (1 <= MAX_EDGES <= 10000)):
		print "Errore:\t\tMassimo numero di archi non valido. Riprovare.\n"
		MAX_EDGES = int(input("Inserire il massimo numero di archi (numero intero compreso tra 1 e 10000): "))
	MAX_DISTANCE = int(input("Inserire la massima distanza possibile tra due nodi (numero intero compreso tra 1 e 5000): "))
	while (not (1 <= MAX_DISTANCE <= 5000)):
		print "Errore:\t\tMassima distanza non valida. Riprovare.\n"
		MAX_DISTANCE = int(input("Inserire la massima distanza possibile tra due nodi (numero intero compreso tra 1 e 5000): "))
	input_path = raw_input("Inserire il percorso dove salvare il file di input:\n")
	while (not os.path.exists(input_path)):
		print "Errore:\t\tIl percorso specificato non esiste. Riprovare.\n"
		input_path = raw_input("Inserire il percorso dove salvare il file di input:\n")
	input_file = raw_input("Inserire il nome del file di input:\n")
	if (not flag):
		if (input_path[-1] != "\\"):
			input_path = input_path+"\\"
		f = open(input_path+"\\"+input_file, 'w')
	else:
		if (input_path[-1] != "/"):
			input_path = input_path + "/"
		f = open(input_path+input_file, 'w')
	cases = random.randrange(1,MAX_CASES+1)
	f.write(str(cases) + "\n")
	print "Casi:",cases
	print "Generazione del file di input..."
	for i in range(1, cases+1):
		done = 0
		nodes = random.randrange(1, MAX_NODES+1)		#MASSIMO NUMERO DI NODI
		if (nodes == 1):
			f.write("1 0\n")
			continue
		edges = random.randrange(1, MAX_EDGES+1)		#MASSIMO NUMERO DI ARCHI
		f.write(str(nodes) + " " + str(edges) + "\n")
		indiv_edges = edges/nodes
		if (indiv_edges != 0):
			for j in range(1, nodes):
				for k in range(indiv_edges):
					end = random.randrange(j+1, nodes+1)			#nodo di "arrivo"
					dist = random.randrange(1, MAX_DISTANCE+1)		#peso dell'arco
					f.write(str(j) + " " + str(end) + " " + str(dist) + "\n")
				done += indiv_edges
			remains = edges-done
			j = 0
			while j < remains:
				start = random.randrange(1, nodes+1)
				end = random.randrange(1, nodes+1)
				if (start != end):
					dist = random.randrange(1, MAX_DISTANCE+1)
					f.write(str(start) + " " + str(end) + " " + str(dist) + "\n")
					j += 1
		else:
			j = 0
			while j < edges:
				start = random.randrange(1, nodes+1)
				end = random.randrange(1, nodes+1)
				if (start != end):
					dist = random.randrange(1, MAX_DISTANCE+1)
					f.write(str(start) + " " + str(end) + " " + str(dist) + "\n")
					j += 1			
	f.close()
	return input_path+input_file	

def map_file(input_file):
	mfile = []
	with open(input_file, 'r' ) as file:
		mfile = [map(int, line.split(' ')) for line in file]
	return mfile

def get_infos(seek, mfile):					
	infos = []
	infos.append(mfile[seek][0])
	infos.append(mfile[seek][1])		
	return infos
	
def initialize_graph(mfile, seek, nodes, edges):
	start = time.time()
	global Graph
	Graph = [0]*2*(nodes+1)
	for i in range(1, len(Graph)):
		Graph[i] = Node(i, i)	
	for i in range(1, 1+edges):
		index = seek+i					
		start = mfile[index][0]			
		end = mfile[index][1]			
		distance = mfile[index][2]			
		start_node = Graph[start]
		end_node = Graph[end]
		Link(start_node, end_node, distance)
		
def check_graph(nodes):
	if (isinstance(Graph[1], int) or (isinstance(Graph[nodes], int)) or (nodes == 1)):
		return 0
	Graph[1]._spath = 0					#come default la distanza tra la radice e se stessa è 0
	return 1
	
def Dijkstra(Graph, start_node, nodes):
	global B
	flag = 0
	B = [[] for x in xrange(int(math.log(len(Graph),2))+1)]
	S = BinomialHeap()
	S.heapInsert(start_node, 0)
	start_node._added = 1
	while (not S.isEmpty()):
		node = S.deleteMin()
		if (node == Graph[nodes]):
			if (flag == 0):
				flag = 1
			else:
				return
		for edge in node._adlist:
			child = edge[0]
			fake = Graph[child.getValue() + nodes + 1]
			distance = edge[1]
			new_short = node.getShortPath() + distance
			new_second = node.getSecondShortPath() + distance
			######### Serie di controlli per la gestione della coda con priorità #########
			if ((child.getShortPath() == 1e10) and (child._added == 0)):
				S.heapInsert(child, new_short)
				child._added = 1
				child.setShortPath(new_short)
				child.setShortParent(node)
			elif (child.getShortPath() == new_short):
				if (child.getSecondShortPath() == 1e10):
					S.heapInsert(fake, new_second)
					fake._added = 1
					child.setSecondShortPath(new_second)
					child.setSecondShortParent(node)
				elif (child.getSecondShortPath() > new_second):
					S.decreaseKey(fake, child.getSecondShortPath() - new_second)
					child.setSecondShortPath(new_second)
					child.setSecondShortParent(node)					
			elif (new_short < child.getShortPath()):
				if (new_second < child.getShortPath()):
					if (new_short != new_second):
						S.decreaseKey(fake, child.getSecondShortPath() - new_second)
						child.setSecondShortPath(new_second)
						child.setSecondShortParent(node)
					else:
						S.decreaseKey(fake, child.getSecondShortPath() - child.getShortPath())
						child.setSecondShortPath(child.getShortPath())
						child.setSecondShortParent(child.getShortParent())
				elif (child.getSecondShortPath() == 1e10):
					S.heapInsert(fake, new_second)
					fake._added = 1
					child.setSecondShortPath(new_second)
					child.setSecondShortParent(node)
				S.decreaseKey(child, child.getShortPath() - new_short)
				child.setShortPath(new_short)
				child.setShortParent(node)
			elif (new_short > child.getShortPath()):
				if (new_short < child.getSecondShortPath()):
					if (fake._added == 0):
						S.heapInsert(fake, new_short)
						child.setSecondShortParent(node)
						child.setSecondShortPath(new_short)
					else:
						S.decreaseKey(fake, child.getSecondShortPath() - new_short)
						child.setSecondShortPath(new_short)
						child.setSecondShortParent(node)
	
def write_ssp(path, start, edges, nodes, case, shortest):
	f = open(path,'a+')
	f.write("Caso " + str(case) + ": " + str(shortest) + "\n")
	if (case < 10):
		print "Case",case,"\t\t\tNodes",nodes,"\tEdges",edges,"\tSecond Shortest Path:",shortest,"\t\t",time.time()-start,"seconds"
	else:
		print "Case",case,"\t\tNodes",nodes,"\tEdges",edges,"\tSecond Shortest Path:",shortest,"\t\t",time.time()-start,"seconds"
	f.close()

def main():
	input_file = menu()
	if (input_file == 0):
		ifile = input_generator()
		mfile = map_file(ifile)
	else:
		mfile = map_file(input_file)
	path = output_path()
	cases = mfile[0][0]
	seek = 1								
	for i in range(cases):
		infos = []
		infos = get_infos(seek, mfile)
		nodes = infos[0]
		edges = infos[1]
		initialize_graph(mfile, seek, nodes, edges)
		if not check_graph(nodes):
			write_ssp(path, time.time(), edges, nodes, i+1, "Impossibile")
			seek += edges+1
			continue
		start = time.time()
		Dijkstra(Graph, Graph[1], nodes)
		if (Graph[nodes].getSecondShortPath() == 1e10):
			write_ssp(path, time.time(), edges, nodes, i+1, "Impossibile")
		else:
			write_ssp(path, start, edges, nodes, i+1, Graph[nodes].getSecondShortPath())
		seek += edges+1
	fin = input("Premere un tasto per continuare")
		
main()
