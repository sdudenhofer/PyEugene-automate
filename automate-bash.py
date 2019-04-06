import os

command = os.popen('ls -alh')

print(command.read())