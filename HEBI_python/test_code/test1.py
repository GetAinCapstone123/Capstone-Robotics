import hebi
from time import sleep
import numpy as np

lookup = hebi.Lookup()

sleep(2)

print('Modules foound on network:')
for entry in lookup.entrylist:
    print(f'{entry.family} | {entry.name}')



group = lookup.get_group_from_names(['Arm'], ['J3_elbow'])

# group.command_lifetime = 100.0
group_command = hebi.GroupCommand(group.size)

# group_command.position = 2
t = 0
duration = 3

while True:
    group_command.position = 2
    group.send_command(group_command)
    sleep(0.05)
    t += 0.1


# group = lookup.get_group_from_names(['Arm'], ['J5_wrist2'])

# group_command = hebi.GroupCommand(group.size)

# while True:
#     group_command.position = 2
#     group.send_command(group_command)
