import os
import glob
import time
from datetime import timedelta
import re
import uuid
import logging
import sys
from py2neo import Graph, Node, Relationship, NodeMatcher

class ConfigClass:
	"""Config2Path is a class that provide global configurations for 2Path"""

	HEADER = '\033[95m'
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

	INPUT_ARROW = BLUE + ">--> " + ENDC
	INPUT_INVALID_MSG = WARNING + "Invalid input!" + ENDC

	PATH = os.path.abspath(os.path.dirname(__file__))
	INPUT_PATH = os.path.join(PATH, "/sources")
	OUTPUT_PATH = os.path.join(PATH, "/outs")
	BLASTDB_PATH = os.path.join(PATH, "/blast")

	HEAD = HEADER + "\n\n.---. .---.       .-. .-.    \n"
	HEAD += "`--. :: .; :     .' `.: :    \n"
	HEAD += "  ,',':  _.'.--. `. .': `-.  \n"
	HEAD += ".'.'_ : :  ' .; ; : : : .. : \n"
	HEAD += ":____;:_;  `.__,_;:_; :_;:_; \n\n" + ENDC

	TREE = WARNING + "       _-_\n"
	TREE += "    /~~   ~~\\\n"
	TREE += " /~~         ~~\\\n"
	TREE += "{   ~~   ~~     }  "  + GREEN + ".---. .---.       .-. .-.     \n"
	TREE += " \  _-     -_  /   " + GREEN + "`--. :: .; :     .' `.: :     \n"
	TREE += BLUE+"       \\ //        " + GREEN + "  ,',':  _.'.--. `. .': `-.     \n"
	TREE += BLUE+"       | |         " + GREEN + ".'.'_ : :  ' .; ; : : : .. :  \n"
	TREE += BLUE+"       | |        " + GREEN + " :____;:_;  `.__,_;:_; :_;:_;  \n" + GREEN
	TREE += BLUE+"      // \\\\        " +BLUE+"  FOR PLANT SESQUITERPENES      \n"+ ENDC


	def getDatabaseConnection(self):
		try:
			# opening a connection
			g = Graph(user="neo4j", password="researcher")  # if using user/pass
			return g
		except Exception:
			print(self.FAIL + "\nERROR: It was not possible to connect to Neo4J." + self.ENDC)
			print(self.WARNING + "\nPOSSIBLE CAUSE: The database is not running or user/password is wrong." + self.ENDC)
			sys.exit(0)
