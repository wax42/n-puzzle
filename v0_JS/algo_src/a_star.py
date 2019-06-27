from utils import Taquin, map_str, check_pos_empty
from copy import deepcopy
import heapq

class Node():
	def __init__(self, parent=None, taquin=None):
			# case precedente
			self.parent = parent
			# map du taquin
			self.map = taquin
			# distance depuis le depart
			self.g = 0
			# g + h
			self.f = 0

#	# transform la map actuel en string
	def map_str(self, dim):
		string = ""
		for y in range(0, dim):
			for x in range(0, dim):
				string += str(self.map[y][x])
		return (string)

	def __lt__(self, other):
		return self.f < other.f

	def __eq__(self, other):
		if(other == None):
			return False
		return self.f == other.f


def astar_start(taquin):
	# tableau de 4 element qui 
	# initialisation des data
	start_node = Node(None, taquin.map)
	goal_str = map_str(taquin.goal, taquin.dim)
	# permet e checker les voisiin par simple addition de pos via une boucle
	neightbours = [(0, -1), (0, 1), (-1, 0), (1, 0)]
	total =  0

	# initialisation des liste de priorite

	# utiliser comme un tableau associatif
	# on stoque ici la string de la map de taquin comme une emprinte
	# remplace la closed list
	hash = set()

	# queue bitch:
	pqueue = []

        # ici on store le premier noeud qui a un cout dez zero
	heapq.heappush(pqueue, (1, start_node))
	taquin.nb_all_node += 1
	# we store just the key not a value
	hash.add(start_node.map_str(taquin.dim))
	# algo:
	# pop open list
	# gen neightbours withtout in closedlist
	# add g, h, f
	while len(pqueue):
		data = (heapq.heappop(pqueue))[1] # ici on recupere l object
		#########################################
		# NEW SON GENERATION
                # recuperer la position dwe l empty node
		pos = check_pos_empty(data.map)
		for i in neightbours:
			pos_y = pos[0] + i[0]
			pos_x = pos[1] + i[1]
			# checker si notre noeud actuel n est pas dans la closed list
			# checker si on est encore dans le range
			# pour l opti on va eviter le len
			if pos_x >= 0 and pos_y >= 0 and pos_x < taquin.dim and pos_y < taquin.dim:
				new_matrice = deepcopy(data.map)
				# swap value
				#penser a faire la verification de non duplication de notre list
				new_matrice[pos[0]][pos[1]] = new_matrice[pos_y][pos_x]
				new_matrice[pos_y][pos_x] = 0

				# checker si la nouvelle matrice nexiste pas deja dans la closed list ou l open list
				newnode = Node(data, new_matrice)
				newnode_map_str = newnode.map_str(taquin.dim)
				if (newnode_map_str not in hash):
					# calculer le g h and f
					newnode.g = data.g + taquin.factor
					newnode.h = taquin.heuristique(new_matrice, taquin.goal)
					heapq.heappush(pqueue, (newnode.g + newnode.h, newnode))
					hash.add(newnode_map_str)
					taquin.nb_all_node += 1

		#######################################################
                # add dans la closed list the father node
                # si on arrive sur la target alors reconstituer le chemin
                # end condition

                # END CONDITION
		if goal_str in hash:
			data = (heapq.heappop(pqueue))[1]
			break

	############################################################################
	### Build path
	answer = []
	while (data != None):
			try:
					answer.append(data.map)
					data = data.parent
			except:
					print ("end bitch")
	taquin.len_path = len(answer)
	taquin.nb_open = len(pqueue)
	return (answer)

# heuristique : heuristique function
# map of origin
# dim : dimension of the taquin
def astar_setting(heuristique, map, dim):
	taquin = Taquin(heuristique, dim, 0, map)
	if (dim == 3):
		taquin.set_goal([[1,2,3],[8,0,4],[7,6,5]])
	elif (dim == 4):
		taquin.set_goal([[1, 2, 3, 4], [12, 13, 14, 5], [11, 0, 15, 6], [10, 9, 8, 7]])
	elif (dim == 5):
		taquin.set_goal([[1, 2, 3, 4, 5], [16, 17, 18, 19, 6], [15, 24, 0, 20, 7], [14, 23, 22, 21, 8], [13, 12, 11, 10, 9]])
	return (taquin)

# heuristique : heuristique function
# map of origin
# dim : dimension of the taquin
def astar_launch(heuristique, taquin, dim, factor=0):
	Astar = astar_setting(heuristique, taquin, dim)
	Astar.factor = factor
	path = astar_start(Astar)
	print ("*********************************")
	print ("************* PATH *************")
	print (path)

	# STATS DISPLAYIN
	print ("*********************************")
	print ("************* STATS *************")
	print ("DIMENSION     : " + str(dim) + " * " + str(dim))
	print ("LEN PATH      : " + str(Astar.len_path))
	print ("NB NODE OPEN  : " + str(Astar.nb_all_node))
	print ("NB OPEN       : " + str(Astar.nb_open))
	print ("NB CLOSE      : " + str((Astar.nb_all_node - Astar.nb_open)))
	return (path)