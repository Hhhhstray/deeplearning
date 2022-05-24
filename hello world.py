import matplotlib.pyplot as plt
import numpy as np

# 定义x、y散点坐标
x = [10, 20, 30, 40, 50, 60, 70, 80]
y = [174, 216, 255, 290, 325, 341, 350, 352]

x = np.array(x)
y = np.array(y)

plot = plt.plot(x, y, 'b-')
fit = np.polyfit(x, y, 2)
print(fit)

# import matplotlib.pyplot as pl

