# Writing to a file

fout = open('output.txt', 'w')
lines = [
    "This is the first line\n",
    "This is the second line\n",
    "This is the third and final line to be written\n"
]

for line in lines:
    fout.write(line)

fout.close()
