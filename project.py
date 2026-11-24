def b(a):
  c=0
  for i in range(1,4):
    print(a)
    for j in range(0,4-i):
      if a[j]>a[j+1]:
        a[j], a[j+1]=a[j+1],a[j]
        c+=1
      print(a)
  return c
  def s(a):
    c=0
    for i in range(1,4):
      m=i-1
      for j in range(i,4):
        if a[m]>a[j]:
          m=j
        print(a)
      if m!=i-1:
        a[i-1], a[m] = a[m], a[i-1]
        c+=1
    print(a)
    return c
           
a=[8,4,2,1]
key=int(input("버블정렬은1을 누르시고, 선택정렬은2를 누르세요 : "))
if key==1:
  print("초기 : ", a)
  print()
  c=b(a)
  print(a)
  print("교환횟수 : ", a)
else:
  if key==2:
    print("초기 : ", a)
    print()
    c=s(a)
    print(a)
    print("교환횟수 : ", a)
  else:
    print()
