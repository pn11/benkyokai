import sys
import subprocess
import re

command = "tree -d -L 2".split(" ")

tree = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
 
out = tree.stdout.decode("utf8")

for line in out.split("\n"):
    match = re.search("─ .*", line)
    if match is not None:
        start = match.start()
        dirname = line[start+2:]
        if start == 2:
            parent = dirname
            print(line[0:start] + "─ [{}]({})  ".format(dirname, dirname))
        elif start == 6:           
            print(line[0:start] + "─ [{}]({}/{})  ".format(dirname, parent, dirname))
