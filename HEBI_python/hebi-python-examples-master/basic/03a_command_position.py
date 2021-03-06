#!/usr/bin/env python3

import hebi
from math import pi, sin
from time import sleep, time

lookup = hebi.Lookup()

# Wait 2 seconds for the module list to populate
sleep(2.0)

family_name = "Arm"
module_name = "J5_wrist2"

group = lookup.get_group_from_names([family_name], [module_name])

if group is None:
  print('Group not found: Did you forget to set the module family and name above?')
  exit(1)

group_command  = hebi.GroupCommand(group.size)
group_feedback = hebi.GroupFeedback(group.size)

# Start logging in the background
group.start_log('logs', mkdirs=True)

freq_hz = 0.1                 # [Hz]
freq    = freq_hz * 2.0 * pi  # [rad / sec]
amp     = 0.5           # [rad] (45 degrees)

duration = 4              # [sec]
start = time()
t = time() - start

# while t < duration:
#   # Even though we don't use the feedback, getting feedback conveniently
#   # limits the loop rate to the feedback frequency
#   group.get_next_feedback(reuse_fbk=group_feedback)
#   t = time() - start

#   group_command.position = amp * sin(freq * t)
#   group.send_command(group_command)
group_command.position = pi/2
group.send_command(group_command)

# Stop logging. `log_file` contains the contents of the file
log_file = group.stop_log()
hebi.util.plot_logs(log_file, 'position')
