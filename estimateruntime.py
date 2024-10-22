# Write a program to estimate runtime of all the functions you have used so far.

import time as t
curr = t.time()
print(curr)

def outer_function():
  x=30

  def inner_function():
   x=40
   print(x)

  inner_function()
  print(x)

outer_function()
update_time = t.time()
print(update_time)

difference = update_time - curr
print(f"\n Time to execute function is {difference/60} min")