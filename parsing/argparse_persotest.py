import argparse
import sys

class Parsing():
	def __init__(self):
		self.dim = 0
		self.matrice = 0
		self.graphic = 0
		self.save = 0
		self.stats = 0
		self.heuristique = 0
		self.error = 0

def parser_file(parse, name_file):
        f = open(name_file, "r")
        count = 0
        line = "coucou"
        dim = 0

        # get dim
        while line and count == 0:
                line = f.readline()
                data = line.split(' ')
                if (data[0] == "#" or data[0] == "\n"):
                        sys.stdout.write("COMMENT : " + line)
                elif (count == 0):
                        parse.dim = dim = int(line)
                        sys.stdout.write("DIM : " + line)
                        count += 1

        print ("Get dim " + str(dim))
        # get matrice of dim DIM
        matrice = [[0] * dim for i in range(dim)]
        for i in range(0, dim):
                line = f.readline()
                print(line)
                if (data[0] == "#" or data[0] == "\n"):
                        print "COMMENT"
                else:
                        data = line.split()
                        print(data)
                        for x in range(0, dim):
                                matrice[i][x] = int(data[x])
                print (line)
        f.close()
	parse.matrice = matrice
        return matrice


def main_arg():
	# default : valuer par default
	# choices : restreindre les choix possible
	# nargs : nombre de choix
	# action='store_tue' | no argument after
	# required=True | obligatoire

	parser = argparse.ArgumentParser()
	parser.add_argument('-f', nargs=1, help="input file", required=True)
	parser.add_argument('-e', '--heuristique', nargs=1, choices=['coucou', 'john', 'her'], default="coucou", help='choose an heuristique')
	parser.add_argument('--save', nargs=1, help='save in file data result')
	parser.add_argument('--stats', action='store_true', help="show stats")
	parser.add_argument('--graphics', action='store_true', help="launch graphic mode(tkinter)")
	#parser.add_argument('--foo', nargs=2)#

	# parse argument
	args = parser.parse_args()
	return (args)

#if __name__ == '__main__':
def parsing_bitch():
	parse = Parsing()
	try:
		args = main()
		print args.f[0]
		parser_file(parse, args.f[0])
		print parse.matrice
	except:
		parse.error = 1
	return (parse)
	#print(args)
	#print(args.f)
