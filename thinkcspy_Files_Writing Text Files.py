infile = open("qbdata.txt", "r")
aline = infile.readline()
while aline:
    items = aline.split()
    dataline = items[1] + ',' + items[0]
    print(dataline)
    aline = infile.readline()

infile.close()

