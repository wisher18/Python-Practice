a = ['bhushan', 'mayur', 'python', 'lilnaz']

try:
    print(a[int(input("type the number which you want see:"))])
except Exception as e:
    print("Exception handled")