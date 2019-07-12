# !/usr/bin/python3
# coding: utf8
import os
import json
import tornado.web
import tornado.websocket
import tornado.ioloop
from algo_src.a_star import astar_launch, is_solvable
from algo_src.utils import spiral, random_puzzle
from algo_src.heuristique import check_gaschnig, check_manhattan, check_hamming


uri = os.getenv("WS_HOST", "127.0.0.1")
port = os.getenv("WS_PORT", "8082")
address = "ws://" + uri + ":" + port
root = os.path.dirname(__file__)


def generate_random_puzzle(dim):
		goal = spiral(dim)
		solvable = 0
		while (solvable == 0):
			pzl = random_puzzle(dim)
			solvable = is_solvable(pzl, goal, dim)
		return pzl


class WebSocketHandler(tornado.websocket.WebSocketHandler):
	connections = set()

	def check_origin(self, origin):
		""" Is not important for this local project"""
		return True

	def open(self):
		self.connections.add(self)
		print("New client connected")

	def on_message(self, message):
		print("Transmitting message: %s" % message)

		front_msg = json.loads(message)
		message_send = {}

		print("DEBUG", front_msg)

		if ('algo' in front_msg.keys()):
			puzzle = front_msg['algo']['puzzle']
			if front_msg['algo']['heuristics'] == "manhattan":
				heuristics = check_manhattan
			elif front_msg['algo']['heuristics'] == "gaschnig":
				heuristics = check_gaschnig
			elif front_msg['algo']['heuristics'] == "hamming":
				heuristics = check_hamming
			factor = front_msg['algo']['factor']
			size_puzzle = front_msg['algo']['size_puzzle']
			message_send['algo'] = astar_launch(heuristics, puzzle, size_puzzle, factor)
		elif('random_puzzle' in front_msg.keys()):
			size_puzzle = front_msg['random_puzzle']
			message_send['random_puzzle'] = {}
			message_send['random_puzzle']['puzzle'] = generate_random_puzzle(size_puzzle)
			message_send['random_puzzle']['size_puzzle'] = size_puzzle

		elif('logs' in front_msg.keys()):
			# Print msg send by the front
			print("Client send logs: %s" % front_msg['logs'])
			message_send['logs'] = "back suck your fucking msg"  # TODO faire un truc intelligent

		# Gestion de retours et de logs d'erreur
		# algo result a_star
		# validate_puzzle result is_valid puzzle
		# logs error with the message of errors
		# stats 

		# if message send is empty / so the front_message is invalid
		if bool(message_send) == False:
			message_send['logs'] = "Error Message Socket invalid"

		print("Message send to a client: %s" % str(message_send))
		self.write_message(json.dumps(message_send))

	def on_close(self):
		self.connections.remove(self)
		print("Client disconnected")

print("URI ws://%s:%s is now open for web communication" % (uri, port))
application = tornado.web.Application([
	(r"/", WebSocketHandler)
])
 
if __name__ == "__main__":
	application.listen(8082)
	tornado.ioloop.IOLoop.instance().start()