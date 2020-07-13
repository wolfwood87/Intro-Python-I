# Print "Hello, world!" to your terminal

num = 123
name = "Derek"
print("Hello, world!")

lst = [1, 4, 10, "cat", 23]
lst.append(3.5)
lst.append([10, 100, 200, 300])
lst.insert(2, "hello")
print(lst)
print(lst[0])

for elm in lst:
    print(elm)

for i in range(6):
    print(lst[i])

dic={"foo": 12, "bar": 34}
print(dic)
val = dic["foo"]
print(val)
print(f'Hello, my name is {name}')