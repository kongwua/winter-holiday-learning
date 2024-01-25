# pandas库学习

numpy只能处理数值型的数据，当要处理其他数据，要用pandas

## 数据类型

- Series 一维，带标签数组
- DataFrame 二维，Series容器

## Series创建

![image-20240123120931625](https://jiatu315.oss-cn-guangzhou.aliyuncs.com/img1/202401231209838.png)

==index是索引==

**通过字典创建：**

![image-20240123121325364](https://jiatu315.oss-cn-guangzhou.aliyuncs.com/img1/202401231213443.png)

## Series切片和索引

![image-20240123121636981](https://jiatu315.oss-cn-guangzhou.aliyuncs.com/img1/202401231216053.png)

## DateFrame类型

![image-20240123125548670](https://jiatu315.oss-cn-guangzhou.aliyuncs.com/img1/202401231255721.png)

![image-20240123133130404](https://jiatu315.oss-cn-guangzhou.aliyuncs.com/img1/202401231331466.png)

## 取行取列

- 方括号写数组，表示取行，对行进行操作
- 写字符串，表示取列索引，对列进行操作

![image-20240123141852624](https://jiatu315.oss-cn-guangzhou.aliyuncs.com/img1/202401231418698.png)

![image-20240123142429159](https://jiatu315.oss-cn-guangzhou.aliyuncs.com/img1/202401231424216.png)

## bool索引

![image-20240123142635593](https://jiatu315.oss-cn-guangzhou.aliyuncs.com/img1/202401231426663.png)

## 字符串方法

![image-20240123144331465](https://jiatu315.oss-cn-guangzhou.aliyuncs.com/img1/202401231443542.png)

## 常用统计方法

![image-20240123160724491](https://jiatu315.oss-cn-guangzhou.aliyuncs.com/img1/202401231607599.png)

## 读取外部数据

**数据保存在csv文件中，直接使用`pd.read_csv`**

读取数据：使用Pandas的`read_csv()`函数或其他适用的函数加载数据集。

```python
# 例如，读取CSV文件
df = pd.read_csv('your_dataset.csv')
```

## 简单的数据清洗

### 查看数据：使用`head()`函数查看前几行数据，以确保数据被正确加载。

```python
print(df.head())
```

### 处理缺失值：使用`dropna()`或`fillna()`函数处理缺失值。

```python
# 删除包含缺失值的行
df = df.dropna()

# 或者使用特定值填充缺失值
# df = df.fillna(value)
```

### 处理重复值：使用`drop_duplicates()`函数删除重复行。

```python
df = df.drop_duplicates()
```

### 数据类型转换：确保每列具有正确的数据类型，可以使用`astype()`函数进行转换。

```python
# 例如，将某列转换为整数类型
# df['column_name'] = df['column_name'].astype(int)
```

### 列重命名：使用`rename()`函数为列重新命名。

```python
# 例如，将某列重命名为新名称
# df = df.rename(columns={'old_name': 'new_name'})
```

### 过滤数据：使用条件语句过滤数据。

```python
# 例如，选择满足条件的行
# df_filtered = df[df['column_name'] > threshold]
```

### 保存清洗后的数据：使用`to_csv()`函数将清洗后的数据保存到文件。

```python
df.to_csv('cleaned_dataset.csv', index=False)
```