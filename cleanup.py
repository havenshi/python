#
# cleanup.py
#

import os
import sys


def getroot():
    if len(sys.argv) == 1:
        path = ''
    else:
        path = sys.argv[1]

    if os.path.isabs(path):
        tree_root = path
    else:
        tree_root = os.path.join(os.getcwd(), path)

    return tree_root


def getdirlist(path):
    dirlist = os.listdir(path)
    dirlist = [name for name in dirlist if name[0] != '.']
    dirlist.sort()
    return dirlist


def traverse(path, t = 0):
    dirlist = getdirlist(path)

    for num, file in enumerate(dirlist):
        dirsize = len(dirlist)
        path2file = os.path.join(path, file)
        
        if file == 'trash.txt':
            t += 1
            os.remove(path2file)
            
        elif os.path.isdir(path2file):
            t += traverse(path2file)

    return t


if __name__ == '__main__':
    root =  getroot()
    trashed = traverse(root)

    if trashed == 1:
        filestring = 'file'
    else:
        filestring = 'files'

    print '%d trash.txt %s deleted' % (trashed, filestring)
