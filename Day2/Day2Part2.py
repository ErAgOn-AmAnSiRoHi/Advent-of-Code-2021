with open("inputday2.txt", "r") as f:
    lines = f.readlines()

actions = []

for l in lines:
    split = l.split(" ")
    actions.append([split[0], int(split[1].strip())])


class State:
    def __init__(self, depth, horizontal_position, aim):
        self.depth, self.horizontal_position, self.aim = depth, horizontal_position, aim


def up(state, x):
    return State(state.depth, state.horizontal_position, state.aim - x)


def down(state, x):
    return State(state.depth, state.horizontal_position, state.aim + x)


def forward(state, x):
    return State(state.depth + x * state.aim, state.horizontal_position + x, state.aim)


action_appliers = {
    "up": up,
    "down": down,
    "forward": forward
}

state = State(0, 0, 0)
for action, amount in actions:
    state = action_appliers[action](state, amount)

print(state.depth * state.horizontal_position)
