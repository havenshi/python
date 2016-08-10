infile = open("qbdata.txt", "r")
line = infile.readline()
while line:
    values = line.split()
    print('QB ', values[0], values[1], 'had a rating of ', values[10] )
    line = infile.readline()

infile.close()


# In the case of readline this moves the marker to the first character of the next line in the file. In the case of read or readlines the marker is moved to the end of the file.
