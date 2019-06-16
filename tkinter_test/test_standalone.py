from Tkinter import *
import ast #for parsing

root = Tk()

text_turn = Label(text="turn yhea")
text_turn.pack()

# text
obj = Label(text="zone de text")
obj.config(text="bibitch", state=DISABLED) # griser la zone
obj.config(text="grosse pute", state=NORMAL)
obj.pack()

bouton = Button(text="john the button")
bouton.pack()

bt_img = Button()
#imm = PhotoImage(file="~/Images/aa.png")
#bt_img.config(image=imm)
bt_img.pack()

# zone de saisie
saisie = Entry()
saisie.insert(0, "content")
saisie.pack()

# combo box need ttk
#b = Combobox(root, values=["hamming", "h2", "h3"])
#b.pack()

# canva creation

w = 600
h = 600

pos = [0, 0]

graph = Canvas()

graph.config(width = w, height = h)

color  = "red"

turn = 0
matrice = "[[[7, 5, 0], [2, 3, 8], [4, 6, 1]], [[7, 0, 5], [2, 3, 8], [4, 6, 1]], [[7, 3, 5], [2, 0, 8], [4, 6, 1]], [[7, 3, 5], [2, 8, 0], [4, 6, 1]], [[7, 3, 0], [2, 8, 5], [4, 6, 1]], [[7, 0, 3], [2, 8, 5], [4, 6, 1]], [[0, 7, 3], [2, 8, 5], [4, 6, 1]], [[2, 7, 3], [0, 8, 5], [4, 6, 1]], [[2, 7, 3], [8, 0, 5], [4, 6, 1]], [[2, 7, 3], [8, 6, 5], [4, 0, 1]], [[2, 7, 3], [8, 6, 5], [4, 1, 0]], [[2, 7, 3], [8, 6, 0], [4, 1, 5]], [[2, 7, 3], [8, 0, 6], [4, 1, 5]], [[2, 0, 3], [8, 7, 6], [4, 1, 5]], [[0, 2, 3], [8, 7, 6], [4, 1, 5]], [[8, 2, 3], [0, 7, 6], [4, 1, 5]], [[8, 2, 3], [7, 0, 6], [4, 1, 5]], [[8, 2, 3], [7, 1, 6], [4, 0, 5]], [[8, 2, 3], [7, 1, 6], [0, 4, 5]], [[8, 2, 3], [0, 1, 6], [7, 4, 5]], [[8, 2, 3], [1, 0, 6], [7, 4, 5]], [[8, 2, 3], [1, 4, 6], [7, 0, 5]], [[8, 2, 3], [1, 4, 6], [7, 5, 0]], [[8, 2, 3], [1, 4, 0], [7, 5, 6]], [[8, 2, 3], [1, 0, 4], [7, 5, 6]], [[8, 2, 3], [1, 5, 4], [7, 0, 6]], [[8, 2, 3], [1, 5, 4], [0, 7, 6]], [[8, 2, 3], [0, 5, 4], [1, 7, 6]], [[8, 2, 3], [5, 0, 4], [1, 7, 6]], [[8, 2, 3], [5, 7, 4], [1, 0, 6]], [[8, 2, 3], [5, 7, 4], [0, 1, 6]], [[8, 2, 3], [0, 7, 4], [5, 1, 6]], [[8, 2, 3], [7, 0, 4], [5, 1, 6]], [[8, 2, 3], [7, 1, 4], [5, 0, 6]], [[8, 2, 3], [7, 1, 4], [5, 6, 0]], [[8, 2, 3], [7, 1, 0], [5, 6, 4]], [[8, 2, 3], [7, 0, 1], [5, 6, 4]], [[8, 2, 3], [7, 6, 1], [5, 0, 4]], [[8, 2, 3], [7, 6, 1], [0, 5, 4]], [[8, 2, 3], [0, 6, 1], [7, 5, 4]], [[8, 2, 3], [6, 0, 1], [7, 5, 4]], [[8, 2, 3], [6, 1, 0], [7, 5, 4]], [[8, 2, 3], [6, 1, 4], [7, 5, 0]], [[8, 2, 3], [6, 1, 4], [7, 0, 5]], [[8, 2, 3], [6, 1, 4], [0, 7, 5]], [[8, 2, 3], [0, 1, 4], [6, 7, 5]], [[8, 2, 3], [1, 0, 4], [6, 7, 5]], [[8, 0, 3], [1, 2, 4], [6, 7, 5]], [[0, 8, 3], [1, 2, 4], [6, 7, 5]], [[1, 8, 3], [0, 2, 4], [6, 7, 5]], [[1, 8, 3], [6, 2, 4], [0, 7, 5]], [[1, 8, 3], [6, 2, 4], [7, 0, 5]], [[1, 8, 3], [6, 0, 4], [7, 2, 5]], [[1, 0, 3], [6, 8, 4], [7, 2, 5]], [[0, 1, 3], [6, 8, 4], [7, 2, 5]], [[6, 1, 3], [0, 8, 4], [7, 2, 5]], [[6, 1, 3], [8, 0, 4], [7, 2, 5]], [[6, 1, 3], [8, 2, 4], [7, 0, 5]], [[6, 1, 3], [8, 2, 4], [0, 7, 5]], [[6, 1, 3], [0, 2, 4], [8, 7, 5]], [[0, 1, 3], [6, 2, 4], [8, 7, 5]], [[1, 0, 3], [6, 2, 4], [8, 7, 5]], [[1, 2, 3], [6, 0, 4], [8, 7, 5]], [[1, 2, 3], [0, 6, 4], [8, 7, 5]], [[1, 2, 3], [8, 6, 4], [0, 7, 5]], [[1, 2, 3], [8, 6, 4], [7, 0, 5]], [[1, 2, 3], [8, 0, 4], [7, 6, 5]]]"
print matrice
matrice = list(ast.literal_eval(matrice))
print matrice
max_turn = len(matrice)
dim = len(matrice[0])

w_case = dim
h_case = dim

w_incr = w / w_case
h_incr = h / h_case

graph.config(width = w, height = h)

def update_turn():
	global text_turn
	stringg = "Turn : " + str(turn) + "/" + str(max_turn - 1)
	text_turn.config(text=stringg)

def update_screen():
	global matrice
	for y in range(0, h_case):
       		for x in range(0, w_case):
                	data = str(matrice[turn][y][x])
                	graph.create_rectangle(x * w_incr, y * h_incr, (x + 1) * w_incr, (y + 1) * h_incr, fill="blue")
                	graph.create_text(x * w_incr + w_incr / 2, y * h_incr + h_incr / 2, text=data, fill="black", font=("arial", 18))

def incr_turn():
	global turn
	turn = (turn + 1)
	if (turn >= max_turn):
		turn = max_turn - 1
	update_screen()
	update_turn()

def decr_turn():
	global turn
	turn -= 1
	if (turn < 0):
		turn = 0
	update_screen()
	update_turn()

def last_turn():
	global turn
        turn = max_turn - 1
        update_screen()
	update_turn()

def first_turn():
	global turn
        turn = 0
        update_screen()
	update_turn()

#graph.create_rectangle(100,100,200,200, fill="blue", width=2)
'''
for y in range(0, h_case):
	for x in range(0, w_case):
		data = "{x : " + str(x) + " | y : " + str(y) + "}"
		graph.create_rectangle(x * w_incr, y * h_incr, (x + 1) * w_incr, (y + 1) * h_incr, fill="blue")
		graph.create_text(x * w_incr + w_incr / 2, y * h_incr + h_incr / 2, text=data, fill="black", font=("arial", 18))
'''

update_screen()

graph.pack()

b = Button(text="incr",   command=incr_turn)
b.pack()
b = Button(text="decr", command=decr_turn)
b.pack()
b = Button(text="begin turn", command=first_turn)
b.pack()
b = Button(text="last turn", command=last_turn)
b.pack()


root.mainloop()