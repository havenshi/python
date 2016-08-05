# -*- coding: utf-8 -*-

current_time_str = input("What is the 'current time' (in hours 0-23)?")
wait_time_str = input("How many hours do you want to wait")

current_time_int = int(current_time_str)
wait_time_int = int(wait_time_str)

final_time_int = current_time_int + wait_time_int
print(final_time_int)


a = input(u'wpisz godzine')
x = input(u'wpisz liczbe godzin')
int(x)
int(a)
h = x // 24
s = x % 24
print (h, s)
a = a + s
print ('godzina teraz %s' %a)
