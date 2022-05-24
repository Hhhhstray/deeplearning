#读取文件
with open('note.txt', encoding='utf-8') as file:
    contents = file.readlines()
    print(contents)
newlist = []
for content in contents:
    newcontent = content.replace('\n','')
    money = newcontent.split('：')[-1]
    newlist.append(int(money))
print(newlist)
import numpy as np
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5, 6]
y = newlist
plt.xlabel('month')
plt.ylabel('money')
plt.savefig('xiaoshoue.png')

plt.show()

average2 = sum(newlist) / len(newlist)
print('averages2:',average2)

