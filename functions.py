listEnemy = ["e", "r", "t", 20, [20,4,21,10,34,58]]
print(listEnemy[1])
print(len(listEnemy))
print("Длинна массива",len(listEnemy))

print(listEnemy[-1])

print(listEnemy)

listEnemy.append("МАША")

print(listEnemy)

listEnemy.insert(4, "element")
print(listEnemy)

listEnemy.pop()
print("next to pop", listEnemy)

listEnemy.remove("e")
print("next to rermove", listEnemy)

index = listEnemy.index("za")
print("result index", index)

count = listEnemy.count(20)
print("result", count)

listEnemy.reverse()
print("next to reverse", listEnemy)

listEnemy.sort(reverse=True)
print("next to reverse", listEnemy)


#Создать список врагов













   












# import math
# def SumTaxi(km=1):
#     min_sum = 100
#     distanse = km*1000

#     sum = math.ceil(min_sum + distanse/140*25)
#     print(f"Вы должны {sum}")
# SumTaxi(5)
# SumTaxi(10)

# SumTaxi()

