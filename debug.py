from entities.letters import Letters
from entities.grid import Grid

op_1 = 'ABC - BC = AFF'
op_2 = 'DF * B = AFF'
# op_3 = 'EE / AA = E'
# op_4 = 'BB + CC = DD'
# op_5 = 'F + F = F'
# op_6 = 'F + F = F'

grid = Grid(
	[op_1, op_2]  # op_3, op_4, op_5, op_6]
)

# grid.get_from_console()

grid.solve()
