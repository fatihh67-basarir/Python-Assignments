num = int(input("pozitif bir sayı yazın : "))
str_num = str(num)
len_num = len(str_num)
a = 0
for i in str_num:
  a += int(i)** len_num
if num == a :
  print("armstrong sayı girdiniz... ")
else:
  print("armstrong sayı değil... ")
