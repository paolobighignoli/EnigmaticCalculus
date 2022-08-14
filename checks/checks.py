from abc import ABC, abstractmethod


class Check(ABC):

	def __init__(self, first: int, second: int, result: int):
		self.first = first
		self.second = second
		self.result = result

	@abstractmethod
	def check(self) -> bool:
		pass


class CheckSum(Check):

	def check(self) -> bool:
		return self.first + self.second == self.result


class CheckSubtraction(Check):

	def check(self) -> bool:
		return self.first - self.second == self.result


class CheckProduct(Check):

	def check(self) -> bool:
		return self.first * self.second == self.result


class CheckDivision(Check):

	def check(self) -> bool:
		return self.first / self.second == self.result


class CheckGrid:
	pass
