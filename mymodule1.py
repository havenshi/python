from datetime import datetime
myage=int(raw_input('insert your age:'))
year=datetime.now().year

print "My name is %s" % __name__

if __name__ == '__main__':
    print "This won't run if I'm  imported."
