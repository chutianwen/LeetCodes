from collections import defaultdict
from enum import Enum
import sys

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
		:param active_install:  if this software is installed independently for system or installed as hidden dependency
		'''
		self.name = name
		self.active_install = active_install

class SystemDependencyControl:
	def __init__(self):
		self.parent_to_child = defaultdict(set)
		self.child_to_parent = defaultdict(set)
		self.installed_softwares = defaultdict(Software)
		self.parsing_splitter = " "

	def execute(self, cmd):
		print(cmd)
		try:
			parsed_cmd = cmd.split(self.parsing_splitter)
		except Exception as _:
			raise Exception("Illegal cmd")

		# filter out empty terms
		parsed_items_trim = list(filter(lambda term: term, parsed_cmd))
		operator = parsed_items_trim[0]

		if operator == SysOperator.DEPEND.value:
			assert len(parsed_items_trim) >= 3, "depend operation must have at least 3 terms"
			self.__depend(parsed_items_trim[1], *parsed_items_trim[2:])
		elif operator == SysOperator.INSTALL.value:
			assert len(parsed_items_trim) == 2, "depend operation must have 2 terms"
			self.__install(parsed_items_trim[1])
		elif operator == SysOperator.REMOVE.value:
			assert len(parsed_items_trim) == 2, "remove operation must have 2 terms"
			self.__remove(parsed_items_trim[1])
		elif operator == SysOperator.LIST.value:
			assert len(parsed_items_trim) == 1, "list operation must have 1 terms"
			self.__list()
		elif operator == SysOperator.END.value:
			print("-"*10 + "DONE" + "-"*10)
		else:
			raise Exception("Illegal operator")

	def __depend(self, child, *parents):

		for parent in parents:
			if child in self.child_to_parent[parent]:
				print("{} depends on {}, ignoring command".format(parent, child))
				return

		for parent in parents:
			self.child_to_parent[child].add(parent)
			self.parent_to_child[parent].add(child)

	def __list(self):
		for installed_software in self.installed_softwares:
			print("\t{}".format(installed_software))

	def __install(self, software_name, target_software=True):

		if software_name in self.installed_softwares:
			if target_software:
				print("\t{} is already installed".format(software_name))
			return

		for parent in self.child_to_parent[software_name]:
			self.__install(parent, False)

		print("\tInstalling {}".format(software_name))
		software = Software(software_name)
		if target_software:
			software.active_install = True
		self.installed_softwares[software_name] = software

	def __remove(self, software_name, target_software=True):

		if software_name not in self.installed_softwares:
			print("\t{} is not installed".format(software_name))
			return

		# case software has no sub-dependencies
		if not self.parent_to_child[software_name]:
			print("\tRemoving {}".format(software_name))
			self.installed_softwares.pop(software_name)

			self.parent_to_child.pop(software_name)
			# delete it from all its parents' children set
			for parent in self.child_to_parent[software_name]:
				self.parent_to_child[parent].remove(software_name)
				# if parent software is not actively installed
				if not self.installed_softwares[parent].active_install:
					self.__remove(parent, False)

			# delete from child to parent graph
			self.child_to_parent.pop(software_name)

		else:
			if target_software:
				print("\t{} is still needed".format(software_name))


import unittest


class SystemDependencyControlTest(unittest.TestCase):
	def setUp(self):
		self.input = '''
				DEPEND TELNET TCPIP NETCARD
				DEPEND TCPIP NETCARD
				DEPEND NETCARD TCPIP
				DEPEND DNS TCPIP NETCARD
				DEPEND BROWSER TCPIP HTML
				INSTALL NETCARD
				INSTALL TELNET
				INSTALL foo
				REMOVE NETCARD
				INSTALL BROWSER
				INSTALL DNS
				LIST
				REMOVE TELNET
				REMOVE NETCARD
				REMOVE DNS
				REMOVE NETCARD
				INSTALL NETCARD
				REMOVE TCPIP
				REMOVE BROWSER
				REMOVE TCPIP
				LIST
				END
				'''

	def test_example(self):
		systemDependencyControl = SystemDependencyControl()
		for line in self.input.split("\n"):
			line = line.replace("\t", "")
			if line:
				systemDependencyControl.execute(line)


if __name__ == '__main__':
	unittest.main()
