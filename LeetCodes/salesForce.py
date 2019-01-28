# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
from enum import Enum

class SysOperator(Enum):
	DEPEND = "DEPEND"
	INSTALL = "INSTALL"
	REMOVE = "REMOVE"
	LIST = "LIST"
	END = "END"

class Software:
	def __init__(self, name, active_install=False):
		'''
		Software node
		:param name:            name of software
		:param active_install   if this software is installed independently for system usage, rather than installed for other lib.
		'''
		self.name = name
		self.active_install = active_install

class SystemDependencyController:
	def __init__(self, parsing_spliiter=" ", cmd_length_limit=80, item_length_limit=10):
		# configuration
		self.parsing_splitter = parsing_spliiter
		self.cmd_length_limit = cmd_length_limit
		self.item_length_limit = item_length_limit
		self.print_prefix = ""

		# graph structure
		self.parent_to_child = defaultdict(list)
		self.child_to_parent = defaultdict(list)
		self.installed_softwares = defaultdict(Software)

	def execute(self, cmd):
		# if the line is only number
		print(cmd)

		assert len(cmd) <= self.cmd_length_limit, "length of whole command line is at most 80 characters"
		parsed_items = cmd.split(self.parsing_splitter)
		# trim out some emtpy items due to splitter
		parsed_items_trim = [item for item in parsed_items if item]

		# if no items found in the cmd line
		if not parsed_items_trim:
			return
		assert len(list(filter(lambda item: len(item) > self.item_length_limit, parsed_items_trim))) == 0, "Item length must all be shorter than {}".format(self.item_length_limit)

		operator = parsed_items_trim[0]

		# logic case matching
		if operator == SysOperator.DEPEND.value:
			assert len(parsed_items_trim) >= 3, "depend operation must have at least 3 items"
			self.__depend(parsed_items_trim[1], *parsed_items_trim[2:])
		elif operator == SysOperator.INSTALL.value:
			assert len(parsed_items_trim) == 2, "install operation must have 2 items"
			self.__install(parsed_items_trim[1])
		elif operator == SysOperator.REMOVE.value:
			assert len(parsed_items_trim) == 2, "remove operation must have 2 items"
			self.__remove(parsed_items_trim[1])
		elif operator == SysOperator.LIST.value:
			assert len(parsed_items_trim) == 1, "list operation must have 1 item"
			self.__list()
		elif operator == SysOperator.END.value:
			return
		else:
			raise Exception("Illegal operator")

	def __depend(self, child, *parents):

		# check if depend command is legal, child cannot be dependency for any of current parents
		for parent in parents:
			if child in self.child_to_parent[parent]:
				print("{} depends on {}, ignoring command".format(parent, child))
				return

		for parent in parents:
			self.child_to_parent[child].append(parent)
			self.parent_to_child[parent].append(child)

	def __list(self):
		for installed_software in self.installed_softwares:
			print(self.print_prefix + "{}".format(installed_software))

	def __install(self, software_name, target_software=True):
		if software_name in self.installed_softwares:
			if target_software:
				print(self.print_prefix + "{} is already installed".format(software_name))
			return

		for parent in self.child_to_parent[software_name]:
			self.__install(parent, False)

		print(self.print_prefix + "Installing {}".format(software_name))
		software = Software(software_name)
		if target_software:
			software.active_install = True
		self.installed_softwares[software_name] = software

	def __remove(self, software_name, target_software=True):

		if software_name not in self.installed_softwares:
			print(self.print_prefix + "{} is not installed".format(software_name))
			return

		# case software has no child softwares, we can delete it
		if not self.parent_to_child[software_name]:
			print(self.print_prefix + "Removing {}".format(software_name))
			self.installed_softwares.pop(software_name)
			self.parent_to_child.pop(software_name)

			# delete it from all its parents' children set
			for parent in self.child_to_parent[software_name]:
				self.parent_to_child[parent].remove(software_name)

				# if parent software is not independently installed for system, try to see if we can delete them
				if not self.installed_softwares[parent].active_install:
					self.__remove(parent, False)

			# delete from node in child_to_parent
			self.child_to_parent.pop(software_name)
		else:
			if target_software:
				print(self.print_prefix + "{} is still needed".format(software_name))


import unittest

class SystemDependencyControllerTest(unittest.TestCase):

	def setUp(self):
		self.systemDependencyController = SystemDependencyController()

	def test_example(self):
		n = int(input())
		for _ in range(n):
			cmd = input()
			self.systemDependencyController.execute(cmd)

if __name__ == "__main__":
	unittest.main()