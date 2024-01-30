import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 默认字体为黑体
plt.rcParams['axes.unicode_minus'] =False

# 导入数据
train = pd.read_csv("./traincsv")

# train.info() # 查看数据集信息

# 生还几率
n = train["Survived"].value_counts()  # n为series对象，含死亡人数和生存人数

# 绘制总体生还几率扇形图
plt.figure(figsize=(5,5))  # 扇形图大小
plt.pie(n, autopct='%.2f%%', labels=['死亡','生存'], pctdistance=0.4, labeldistance=0.6,
        shadow=True, explode=[0, 0.1], textprops=dict(size=15))
plt.title("总体生还率")

# 不同性别生还率
sex_count = train.groupby(by='Sex')['Survived'].value_counts()  # 按性别进行分组，并统计死亡人数和幸存人数

# 将两张图画在同一张纸上
plt.figure(figsize=(2*5, 5))

axes1 = plt.subplot(1, 2, 1)  # 创建一个 1x2 的子图布局
axes1.pie(sex_count.loc['female'][::-1], autopct='%.2f%%', labels=['死亡', '存活'],
          shadow=True, explode=[0, 0.1], textprops=dict(size=15), colors=['#9400D3', '#FFB6C1'], startangle=90)
axes1.set_title("女性生化率")
axes2 = plt.subplot(1, 2, 2)
axes2.pie(sex_count.loc['male'], autopct='%.2f%%', labels=['死亡', '存活'],
          shadow=True, explode=[0, 0.1], textprops=dict(size=15), colors=['#2E8B57', '#AFEEEE'])
axes2.set_title('男性生还率')

# 不同年龄段乘客生还几率
age_range = train['Age']  # 年龄范围

# 各年龄段人数
age_num, _ = np.histogram(age_range, range=[0.0, 80.0], bins=16)

# 各年龄阶段生还人数
age_survived = []
for age in range(5, 81, 5):
        survived_num = train.loc[(age_range >= age-5) & (age_range <= age)]['Survived'].sum()
        age_survived.append(survived_num)

# 绘制条形图
plt.figure(figsize=(10, 6))
plt.bar(np.arange(2, 78, 5)+0.5, age_num, width=5, label='总人数')
plt.bar(np.arange(2, 78, 5)+0.5, age_survived, width=5, label='生还人数')
plt.xticks(range(0, 81, 5))
plt.yticks(range(0, 121, 10))
plt.title("各年龄段人数和生还人数")

# 不同港口乘客生还情况
embarked_count = train.groupby(by='Embarked')['Survived'].value_counts()

plt.figure(figsize=(3*5, 5))

axes1 = plt.subplot(1, 3, 1)
axes1.pie(embarked_count.loc['C'], autopct='%.2f%%', labels=['死亡', '存活'])
axes1.set_title('法国瑟堡市乘客生还率')

axes2 = plt.subplot(1, 3, 2)
axes2.pie(embarked_count.loc['Q'], autopct='%.2f%%', labels=['死亡', '存活'])
axes2.set_title('爱尔兰昆士敦乘客生还率')

axes3 = plt.subplot(1, 3, 3)
axes3.pie(embarked_count.loc['S'], autopct='%.2f%%', labels=['死亡', '存活'])
axes3.set_title('英国南安普敦乘客生还率')

# 不同船舱乘客生还几率
pclss_count = train.groupby(by='Pclass')['Survived'].value_counts()
plt.figure(figsize=(3*5, 5))

axes1 = plt.subplot(1, 3, 1)
axes1.pie(pclss_count.loc[1], autopct='%.2f%%', labels=['死亡', '存活'])
axes1.set_title('一等舱乘客生还率')

axes2 = plt.subplot(1, 3, 2)
axes2.pie(pclss_count.loc[2], autopct='%.2f%%', labels=['死亡', '存活'])
axes2.set_title('二等舱乘客生还率')

axes3 = plt.subplot(1, 3, 3)
axes3.pie(pclss_count.loc[3], autopct='%.2f%%', labels=['死亡', '存活'])
axes3.set_title('三等舱乘客生还率')



plt.show()
