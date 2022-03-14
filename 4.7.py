def fact(n):

    count = 0
    factorial = 1
    while count < n-1:
      count += 1
      factorial = factorial * (count + 1)
      yield factorial



my_gen = fact(4)

for el in my_gen:
    print(el)
