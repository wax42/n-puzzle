from .utils import Taquin, map_str, check_pos_empty, spiral
from copy import deepcopy
import heapq, time
from .heuristique import *

#  TODO DELETE

import pprint

def find_pos_in_tab(tab, val):
        count = 0
        for i in tab:
                if (i == val):
                        return (count)
                count += 1
        return (count)

def find_n_simple_tab(map):
        size = len(map)
        n = 0
        for x in range(0, size):
                for xx in range(x+1, size):
                        if (map[x] > 0 and map[xx] > 0 and map[x] > map[xx]):
                                n = n + 1
        return (n)

def is_solvable(puzzle, goal, dim):
        # PUZZLE VERIF SOLVABLE
        tab_map = []
        tab_goal = []
        for i in puzzle:
                tab_map = tab_map + i
        for i in goal:
                tab_goal = tab_goal + i

        v1 = find_n_simple_tab(tab_map)
        v2 = find_n_simple_tab(tab_goal)

        if (dim % 2 == 0):
                v1 += (find_pos_in_tab(tab_map, 0) / dim)
                v2 += (find_pos_in_tab(tab_goal, 0) / dim)
        if (v1 % 2 == v2 % 2):
                return (1)
        else:
                return (0)

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

# TODO clean l'initialisation / nom des variables etc

def astar_start(taquin):
	# tableau de 4 element qui 
	# initialisation des data
	start_node = Node(None, taquin.map)
	goal_str = map_str(taquin.goal, taquin.dim)
	# permet e checker les vopar simple addition de pos via une boucle
	neightbours = [(0, -1), (0, 1), (-1, 0), (1, 0)]
	total =  0

	# initialisation des liste de priorite

	# utiliser comme un tableau associatif
	# on stoque ici la string de la map de taquin comme une emprinte
	# remplace la closed list
	closed_list = set()

	# queue bitch:
	opened_list = []

        # ici on store le premier noeud qui a un cout dez zero
	heapq.heappush(opened_list, (1, start_node))
	taquin.nb_all_node += 1
	# we store just the key not a value
	closed_list.add(start_node.map_str(taquin.dim))
	# algo:
	# pop open list
	# gen neightbours withtout in closedlist
	# add g, h, f
	while len(opened_list):
		data = (heapq.heappop(opened_list))[1] # ici on recupere l object
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
				newnode_map_str = newnode.map_str(taquin.dim) # [ victor]

				if newnode_map_str not in closed_list:
					newnode.g = data.g + taquin.factor
					newnode.h = taquin.heuristique(new_matrice, taquin.goal1d)
					heapq.heappush(opened_list, (newnode.g + newnode.h, newnode))
					closed_list.add(newnode_map_str) # [ victor]
					taquin.nb_all_node += 1
					if (newnode_map_str == goal_str):
						path = []
						node_actual = newnode
						while (node_actual != None):
							try:
								path.append(node_actual.map)
								node_actual = node_actual.parent
							except:
								print ("***")
						taquin.len_path = len(path)
						taquin.nb_open = len(opened_list)
						path = path[::-1]
						return (path)
	return (-1)



# heuristique : heuristique function
# map of origin
# dim : dimension of the taquin
def astar_setting(heuristique, map, dim):
	taquin = Taquin(heuristique, dim, 0, map)
	if (dim >= 3 and dim <= 10):
		taquin.set_goal(spiral(dim))
		print("GOAL: ", taquin.goal)
	else:
		taquin.error = 2

	if (is_solvable(taquin.map, taquin.goal, dim) == 0):
		taquin.error = 1

	return (taquin)

# heuristique : heuristique function
# map of origin
# dim : dimension of the taquin
def astar_launch(heuristique, taquin, dim, factor=0):
	
	Astar = astar_setting(heuristique, taquin, dim)
	Astar.factor = factor
	if (Astar.error == 1):
		print("Taquin invalide. Try another file.")
		exit(1)
	if (Astar.error == 2):
		print ("Bad dim. Need to be [2 < dim < 6]")
		exit(1)

	start_time = time.time()
	path = astar_start(Astar)
	time_duration = time.time() - start_time
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
	print ("TIME DURATION : %.3f" % time_duration)

	send_dico = {}
	send_dico['path'] = path
	send_dico['size_puzzle'] = dim
	send_dico['len_path'] = Astar.len_path
	send_dico['all_node'] = Astar.nb_all_node
	send_dico['node_open'] = Astar.nb_open
	send_dico['node_close'] = Astar.nb_all_node - Astar.nb_open
	send_dico['time_duration'] = str(time_duration)

	return (send_dico)