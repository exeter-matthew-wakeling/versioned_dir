import sys
lines = open("README.md", "r").readlines()

for line in lines:
    print(line, end="")

print("\nEverything is OK")
sys.exit(-1)
