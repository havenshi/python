# Example1: time
class Time:
    pass

time = Time()
time.hours = 11
time.minutes = 59
time.seconds = 30

def print_time(t):
	print str(t.hours)+':'+str(t.minutes)+':'+str(t.seconds)

def add_time(t1, t2):                     # pure function, not modify any of the objects(t1,t2) passed to it as parameters
    sum = Time()
    sum.hours = t1.hours + t2.hours
    sum.minutes = t1.minutes + t2.minutes
    sum.seconds = t1.seconds + t2.seconds
    return sum
    
current_time = Time()
current_time.hours = 9
current_time.minutes = 14
current_time.seconds =  30
bread_time = Time()
bread_time.hours = 3
bread_time.minutes = 35
bread_time.seconds = 0
done_time = add_time(current_time, bread_time)
print_time(done_time)                      # 12:49:30

def increment(time, seconds):
    time.seconds = time.seconds + seconds

    while time.seconds >= 60:
        time.seconds = time.seconds - 60
        time.minutes = time.minutes + 1

    while time.minutes >= 60:
        time.minutes = time.minutes - 60
        time.hours = time.hours + 1
        

# Example2:phototype and plan
def convert_to_seconds(t):
    minutes = t.hours * 60 + t.minutes
    seconds = minutes * 60 + t.seconds
    return seconds

def make_time(seconds):
    time = Time()
    time.hours = seconds/3600
    seconds = seconds - time.hours * 3600
    time.minutes = seconds/60
    seconds = seconds - time.minutes * 60
    time.seconds = seconds
    return time


def add_time(t1, t2):
    seconds = convert_to_seconds(t1) + convert_to_seconds(t2)
    return make_time(seconds)
    

# 1.follow chronologically
def after(t1, t2):
    return convert_to_seconds(t1) > convert_to_seconds(t2)

# 2.rewrite increment
def increment(time, seconds):                   # modify time
    sum = convert_to_seconds(time) + seconds
    newtime = make_time(sum)
    time.hours = newtime.hours
    time.minutes = newtime.minutes
    time.seconds = newtime.seconds
    
def increment(time, seconds):                   # not modify time, pure function
    sum = convert_to_seconds(time) + seconds
    newtime = make_time(sum)
    return newtime
    
    
print increment(current_time, 180)              # <__main__.Time instance at 0x7fab7dab63f8>
