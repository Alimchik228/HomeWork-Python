rating = [7, 5, 3, 3, 2]
m = int(input())
if rating[0] < m:
    rating.insert(0, m)
    print(rating)
elif rating[len(rating)-1] > m:
    rating.append(m)
    print(rating)

else:
  i = 0
  while rating[i] != m:
      i+=1
  rating.insert(i, m)
  print(rating)