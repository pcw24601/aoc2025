from dataclasses import dataclass
from pathlib import Path
from collections import namedtuple, deque
import re

input_file = Path('input.txt')
# input_file = Path('test.txt')


# Load data
with open(input_file, 'r') as f:
    input_lines = [line.strip('\n') for line in f.readlines()]

Machine = namedtuple('Machine', ['target_lights', 'buttons', 'joltages'])
machines = []

for line in input_lines:
    pattern =r'\[([\.#]+)\] (\(.*\)+?) \{([^\}]+)\}'
    groups = re.match(pattern, line)  # group 1: lights, group 2: buttons, group 3: joltages
    target_light_str = groups[1]
    target_lights = [1 if char == '#' else 0 for char in target_light_str]

    button_str = groups[2]
    button_patterns = re.findall(r'\(([\d,]+)\)', button_str)
    buttons = [set(int(num) for num in pattern.split(',')) for pattern in button_patterns]

    joltages_str = groups[3]
    joltages = [int(num) for num in joltages_str.split(',')]

    machines.append(Machine(target_lights, buttons, joltages))


@dataclass
class MachineState:
    light_states: list[int]
    number_presses: int
    next_button_press: set[int]
    target_lights: list[int]

    def is_solved(self) -> bool:
        return self.light_states == self.target_lights

    def press_button(self, button_press_queue: deque, buttons: list[set[int]],
                     light_states_tested: set[tuple[int]]) -> int:
        new_light_states = self.light_states.copy()
        for light_index in self.next_button_press:
            new_light_states[light_index] ^= 1  # Toggle light state
        self.light_states = new_light_states
        self.number_presses += 1

        if self.is_solved():
            return self.number_presses

        # Check if this state has been tested
        light_states_tuple = tuple(self.light_states)
        if light_states_tuple in light_states_tested:
            return -1  # Already tested
        light_states_tested.add(light_states_tuple)

        # Enqueue next possible buttons
        for button in buttons:
            machine_state = MachineState(light_states=self.light_states.copy(),
                                         number_presses=self.number_presses,
                                         next_button_press=button,
                                         target_lights=self.target_lights)
            button_press_queue.append(machine_state)
        return -1  # Not solved yet


button_press_count = 0
for machine_num, machine in enumerate(machines):
    print(f'Solving machine {machine_num + 1} of {len(machines)}')
    button_press_queue = deque()
    light_states_tested = set()
    # Initially populate deque with all buttons
    for switch in machine.buttons:
        machine_state = MachineState(light_states=[0] * len(machine.target_lights),
                                     number_presses=0,
                                     next_button_press=switch,
                                     target_lights=machine.target_lights)
        button_press_queue.append(machine_state)

    # Loop until solved
    while True:
        test_machine = button_press_queue.popleft()
        presses = test_machine.press_button(button_press_queue, machine.buttons,
                                            light_states_tested)
        if presses > 0:
            button_press_count += presses
            break

print(button_press_count)
