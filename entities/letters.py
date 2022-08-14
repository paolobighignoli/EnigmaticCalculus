from enum import Enum
from typing import Dict, List


class Letters(Enum):
	A = 'A'
	B = 'B'
	C = 'C'
	D = 'D'
	E = 'E'
	F = 'F'
	G = 'G'
	H = 'H'
	I = 'I'
	L = 'L'


def generate_dict(letters: List[str], numbers: List[str]) -> Dict[str, str]:

	my_dict = dict(zip(letters, numbers))

	return my_dict

