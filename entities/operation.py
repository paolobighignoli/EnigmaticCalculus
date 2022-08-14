from abc import ABC
from enum import Enum
from typing import List, Dict, Type

from checks.checks import CheckSum, CheckSubtraction, CheckProduct, \
	CheckDivision, Check


class Operations(Enum):
	SUM = '+'
	SUB = '-'
	MULTIPLICATION = '*'
	DIVISION = '/'


class Operation(ABC):

	operation_string: str
	numeric_string: str
	op: str
	first: int
	second: int
	result: int

	def print(self):
		print(self.numeric_string)

	def __init__(self, operation_string: str):

		self.operation_string = operation_string
		self.op = operation_string.split(' ')[1]

	def replace(self, number_dict: Dict[str, str]):

		""" given a dict replace the letters in operation_string"""

		self.numeric_string = self.operation_string
		for key in number_dict.keys():
			self.numeric_string = self.numeric_string.replace(key,
															  number_dict[key])

	def get_unique_values(self) -> List[str]:

		""" returns the unique values of the string """

		unique_values = list(self.operation_string)

		unique_values = [i for i in unique_values if i not in ['+', '-',
															   '*', '/',
															   '=', ' ']]
		return unique_values

	def get_numeric_arguments(self, numeric_string: str) -> List[int]:

		""" given the numeric string returns first, second and result"""

		self.first = int(numeric_string.split(' ')[0])
		self.second = int(numeric_string.split(' ')[2])
		self.result = int(numeric_string.split(' ')[4])

		return [self.first, self.second, self.result]

	@staticmethod
	def check_factory(op: str) -> Type[Check]:

		"""
		given the value of op returns the correct Check from checks.py
		"""

		if op == Operations.SUM.value:
			return CheckSum
		elif op == Operations.SUB.value:
			return CheckSubtraction
		elif op == Operations.MULTIPLICATION.value:
			return CheckProduct
		elif op == Operations.DIVISION.value:
			return CheckDivision

	def check(self) -> bool:

		arguments = self.get_numeric_arguments(self.numeric_string)
		check_type = Operation.check_factory(self.op)

		return check_type(arguments[0], arguments[1], arguments[2]).check()


