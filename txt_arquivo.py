number = int(input("valor: "))

list_value = []
for i in range(1,11):
    calc =  number * 1
    value =  f"{number} x {i} = {calc}"
    list_value.append(value)

with open("amigos.txt","w") as file:
    file.write("\n".join(list_value))