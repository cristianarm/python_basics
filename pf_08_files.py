import os
import random
import linecache

DATA_FILE="data.txt"
randfile = open(DATA_FILE, "w" )
NUM_LINES = 4096
NUM_BASE = 9048

for i in range(NUM_LINES):
    line = str(random.uniform(-NUM_BASE, NUM_BASE))  + "\n"
    randfile.write(line)
    #print(line)
randfile.close()

if os.path.exists(DATA_FILE):
    # read expecific lines
    line_numbers = [random.randint(1,NUM_LINES), random.randint(1,NUM_LINES)]
    print(line_numbers)
    lines = []
    for i in line_numbers:
        #x = linecache.getline(DATA_FILE, i).strip()
        lines.append(linecache.getline(DATA_FILE, i).strip())
    print(lines)