# matplotlib库学习

使数据可视化，更直观地呈现

## 基本要点

![image-20240125105427413](https://jiatu315.oss-cn-guangzhou.aliyuncs.com/img1/202401251054538.png)

## 设置图片大小

![image-20240125111829429](https://jiatu315.oss-cn-guangzhou.aliyuncs.com/img1/202401251118530.png)

## 调整x轴和y轴上的刻度

![image-20240125191016663](https://jiatu315.oss-cn-guangzhou.aliyuncs.com/img1/202401251910758.png)

## 添加描述信息

```
plt.xlabel
plt.ylabel
```

## 风格

![](https://jiatu315.oss-cn-guangzhou.aliyuncs.com/img1/202401251930763.png)

![image-20240125193217755](https://jiatu315.oss-cn-guangzhou.aliyuncs.com/img1/202401251932800.png)

## 散点图

```
plt.scatter(x,y)
```

## 条形图

```
plt.bar(x,y,width,color) # 竖向直方图
plt.barh() # 横向直方图
```

![image-20240125200541097](https://jiatu315.oss-cn-guangzhou.aliyuncs.com/img1/202401252005148.png)



## **直方图(Histogram)**：

```python
import matplotlib.pyplot as plt
import numpy as np

# 生成随机数据
data = np.random.randn(1000)

# 绘制直方图
plt.hist(data, bins=30)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.grid(True)
plt.show()
```

## **箱线图(Box Plot)**：

```python
import matplotlib.pyplot as plt
import numpy as np

# 生成随机数据
data = np.random.randn(100)

# 绘制箱线图
plt.boxplot(data)
plt.ylabel('Value')
plt.title('Box Plot')
plt.grid(True)
plt.show()
```

## 扇形图

```python
import matplotlib.pyplot as plt

# 准备数据
labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0, 0.1, 0, 0)  # 突出显示第二个扇形块

# 绘制扇形图
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')  # 确保扇形图是正圆的
plt.title('Pie Chart')
plt.show()
```

在这个示例中，`labels`是每个扇形块的标签，`sizes`是每个扇形块的大小，`colors`是每个扇形块的颜色，`explode`用于指定是否要突出显示某个扇形块。然后使用`pie()`函数将这些数据绘制成扇形图，并通过参数设置来控制扇形图的样式。

## 其他工具

- echart
- plotly
