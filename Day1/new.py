students = [int(input()), int(input()), int(input()), int(input()), int(input())]
def all(students):
  count_even = 0
  count_odd = 0
  r = sum(students)
  avg = r/len(students)
  for x in students:
    if x%2==0:
      count_even = count_even+1
    else:
      count_odd = count_odd+1
    
  print("Sum is ",r, "Average is ",avg ,"Odd numbers are ", count_odd,"Even numbers are", count_even)
  
all(students)
  