import itertools

from abc import ABC
from typing import List, Dict, Set
from entities.letters import generate_dict
from entities.numbers import Numbers
from entities.operation import Operation


class Grid(ABC):

	""" contains all the Operation """

	numeric_grid: List[Operation]
	operations_list: List[Operation]
	solution: Dict[str, str]

	def __init__(self, operations_list: List[str] = None):
		self.operations_list = [Operation(o) for o in operations_list]

	def get_from_console(self):
		op_1 = Operation(input('insert first operation: '))
		op_2 = Operation(input('insert second operation: '))
		op_3 = Operation(input('insert third operation: '))
		op_4 = Operation(input('insert fourth operation: '))
		op_5 = Operation(input('insert fifth operation: '))
		op_6 = Operation(input('insert sixth operation: '))
		self.operations_list = [op_1, op_2, op_3, op_4, op_5, op_6]

	def print(self):
		for op in self.operations_list:
			op.print()

	def replace_grid(self, my_dict: Dict[str, str]) -> List[Operation]:
		new_grid = []
		for op in self.operations_list:
			op.replace(my_dict)
			new_grid.append(op)
		self.numeric_grid = new_grid

		return new_grid

	def check_grid(self, my_dict: Dict[str, str]) -> bool:
		try_grid = self.replace_grid(my_dict)
		self.print()
		print('----------')
		return all(boh.check() for boh in try_grid)

	def get_unique_values(self) -> Set[str]:
		unique_values = []
		for op in self.operations_list:
			unique_values = unique_values + op.get_unique_values()
		return set(unique_values)

	# def print_solution(self):
	# 	self.operations_list[0].print()
	# 	print(f'  {self.operations_list[3].op}     '
	# 		  f'{self.operations_list[4].op}   {self.operations_list[5].op}')
	# 	self.operations_list[1].print()
	# 	print('---------------')
	# 	self.operations_list[2].print()

	def solve(self) -> int:
		k = len(self.get_unique_values())
		for combo in itertools.permutations(Numbers.numbers, k):
			my_dict = generate_dict(list(self.get_unique_values()),
									list(combo))

			if self.check_grid(my_dict):
				#  self.print_solution()
				self.solution = my_dict
				print(my_dict)
				return 0
		print('Sorry, no solution!')
		return 1




