# 数据下载
下载地址：
[TLC Trip Record Data](https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page)

纽约市 出租车轨迹数据集：

## 简介：
![20210912202819](https://xd-imgsubmit.oss-cn-beijing.aliyuncs.com/images/20210912202819.png)
主要有黄绿出租车 和FHV(for-hire vehicles) 还有其他的注册车辆的行程轨迹数据（一般都有具体的上下车地点和时间，及其他辅助数据），TLC 的说明文档地址：[TLC trip records ueser guide](https://www1.nyc.gov/assets/tlc/downloads/pdf/trip_record_user_guide.pdf)

## FHV数据
本次使用的主要为 FHV数据集，时间为2018年全年(与[论文](https://www.researchgate.net/journal/IEEE-Transactions-on-Intelligent-Transportation-Systems-1524-9050)时间段一致)。
下面介绍该数据集：

![20210912203642](https://xd-imgsubmit.oss-cn-beijing.aliyuncs.com/images/20210912203642.png)
数据的字段主要为：
- Dispatching_base_num: TLC基地许可证号。这个字段也不知道是干嘛的，似乎是区分不同的公司，这个数据集的数据主要来源为Uber,Lyft等公司
- Pickup_datetime：上车时间
- DropOff_datetime：下车时间
- PULocationID： 订单开始的地区的ID ，理解为上车地点
- DOLocationID： 订单结束所在的地区，下车地点
- SR_Flag: 
  文档的描述：
  `Indicates if the trip was a part of a shared ride chain offered by a High Volume FHV company (e.g. Uber Pool, Lyft Line). For shared trips, the value is 1. For non-shared rides, this field is null.`
  用于区分 该订单是否为共享模式的行程订单：如果是，则该表示为1；否则为0。上文提到的论文的主要研究问题为共享模式下的需求研究，所以用该 表示筛选数据。
  此外，文档还提到了Lyft的数据与存在多计数的情况，在这里不过多的考虑这种情况。
## FHV 案例说明
![20210912204512](https://xd-imgsubmit.oss-cn-beijing.aliyuncs.com/images/20210912204512.png)
原始数据按月下载，每个月的数据总量大概在2000万条

![20210912204616](https://xd-imgsubmit.oss-cn-beijing.aliyuncs.com/images/20210912204616.png)

![20210912205403](https://xd-imgsubmit.oss-cn-beijing.aliyuncs.com/images/20210912205403.png)
上面为一月的一条轨迹数据实例，可以看到SR_Flag的值为`nan`，表明该条数据不为共享模式下的出行数据，在之后的的数据清洗过程中，应筛选出去。
此外， 数据中，还存在上车地点或者下车地点的值`nan`的情况，也将其视为无效的数据。
## NYC zones 
该部分主要说明纽约地区的地图信息，为我们之后的数据筛选提供指导。
![20210912205959](https://xd-imgsubmit.oss-cn-beijing.aliyuncs.com/images/20210912205959.png)
- 文件`NYC Taxi Zones`为该地区的一些地理信息文件，文件的数据读取 处理和保存将在下面geopandas初步学习的模块讲解。
![20210912210138](https://xd-imgsubmit.oss-cn-beijing.aliyuncs.com/images/20210912210138.png)
主要我也搞不懂 每一个文件夹里面存放的都是那些具体的值，为甚么有四个打开看起来差不多的文件。
但是，此类文件 都为`shapefile`文件的一部分，提供地理位置信息，包括很多矢量数据和坐标数据。
- 图片文件
  ![taxi_zone_map_manhattan](https://xd-imgsubmit.oss-cn-beijing.aliyuncs.com/images/taxi_zone_map_manhattan.jpg)
  上图为Manhattan地区的出租车分区，订单数据中的`PUlocationId`及`DOlocationId`均依此划分。
- zone_lookup文件
  ![20210912210644](https://xd-imgsubmit.oss-cn-beijing.aliyuncs.com/images/20210912210644.png)
  主要存放的为 `LocationId`及其所属的行政区

# 清洗及过滤

由于整个数据集的 条数 太多，如果先聚合在一起的话再去做处理，会把电脑卡死（--）
所以，按月处理数据。
筛选的条件主要有：
- 去掉 `PULocationID`和`DOLocationID`为空的乘车记录
- 筛选出`SR_Flag`为1,即为共享模式下的乘车记录
- 筛选出 上车和下车都在Manhattan区的数据
- 缺失填充

下面简单介绍处理过程
## 读取数据

首先按月读取数据 pandas
数据类型为dataFrame
接下来主要使用drop函数，及不同的行列定位方法，得到要删除的行的索引

## 去掉 `PULocationID`和`DOLocationID`为空的乘车记录

`np.isnan` 判断是都为 空值

`fhv_data_1.drop(fhv_data_1[np.isnan(fhv_data_1['PUlocationID'])].index,inplace=True)
`
删除 上车地点为空值的 数据

同理 删除 删除 `DOLoctionID`为空的数据

## 过滤 共享模式的数据

`fhv_data_1_shared=fhv_data_1[fhv_data_1['SR_Flag'] == 1.0]`

## 过滤出Manhattan地区数据

根据 taxi_zone的shapefile文件。得到， 曼哈顿地区的 服务区的id ，然后根据id将其筛选出来
`fhv_data_1_shared_manhattan = fhv_data_1_shared.loc[(fhv_data_1_shared['DOlocationID'].isin(Manhattan_id_set))&(fhv_data_1_shared['PUlocationID'].isin(Manhattan_id_set))]
`
## 处理每一个月的数据

```python
for i in range(1,12):
    print('正在处理第%d个月的数据'%i)
    filename = filenames[i]
    fhv_data_tmp = pd.read_csv(path+filename)
    fhv_data_tmp.drop(fhv_data_tmp[np.isnan(fhv_data_tmp['PUlocationID'])].index,inplace=True)
    fhv_data_tmp.drop(fhv_data_tmp[np.isnan(fhv_data_tmp['DOlocationID'])].index,inplace=True)
    fhv_data_tmp= fhv_data_tmp[fhv_data_tmp['SR_Flag'] == 1.0]
    fhv_data_tmp = fhv_data_tmp.loc[(fhv_data_tmp['DOlocationID'].isin(Manhattan_id_set))&(fhv_data_tmp['PUlocationID'].isin(Manhattan_id_set))]
    fhv_data_tmp.to_csv(path_processed+filename[:21]+'_Manhattan_shared.csv')
```
## 聚合所有月的数据
```python
# 存放2018年所有得fhv数据
filenames_manhattan = []
pri_name = 'fhv_tripdata_2018-'
last_name = '_Manhattan_shared.csv'
months = ['01','02','03','04','05','06', '07','08','09','10','11','12']
for month in months:
    filename = pri_name+month+last_name
    filenames_manhattan.append(filename)

fhv_data_manhattan_shared = []
path = '../data/raw_data/2018/processed/'
for filename in filenames_manhattan:
    fhv_data_month = pd.read_csv(path+filename)
    fhv_data_manhattan_shared.append(fhv_data_month)
```

# 建立特征
inflow 和 outflow计数

按照 地点 对数据进行重采样， 将时间index 均匀的划分为 24*365个时间段，按照inflow 和outflow 分别计数
## 按照 index 升序排列数据

`fhv_data_manhattan_shared_all = fhv_data_manhattan_shared_all.sort_values(by='Pickup_DateTime')
`
## 按地点处理数据

示例： 筛选出 id为4的数据
```python

tmp_loc_id = '4'

fhv_data_manhattan_4 = fhv_data_manhattan_shared_all.loc[(fhv_data_manhattan_shared_all['PUlocationID'] == 4) | (fhv_data_manhattan_shared_all['DOlocationID']==4)]
```

将 上车时间和下车时间 更改数据格式为 DateTime

```python
fhv_data_manhattan_4['DropOff_datetime'] = pd.to_datetime(fhv_data_manhattan_4['DropOff_datetime'])
fhv_data_manhattan_4['Pickup_DateTime'] = pd.to_datetime(fhv_data_manhattan_4['Pickup_DateTime'])

```
按照 时间索引 resample 数据

```python
# 遍历 id 列表 ，读取该地区所有id的数据，产生相对应的inflow 和out flow 文件
# 每一个series的长度应该为8760

for i in range(1, len(Manhattan_id_list)-1):
    # 正在读取第几个站点的数据
    print('正在读取第%d个站点的名字'%i)
    location_id = Manhattan_id_list[i] # 地点的名字
    fhv_data_manhattan_id_inflow=fhv_data_manhattan_data_all.loc[fhv_data_manhattan_data_all['DOlocationID'] == location_id]
    fhv_data_manhattan_id_outflow=fhv_data_manhattan_data_all.loc[fhv_data_manhattan_data_all['PUlocationID'] == location_id]
    fhv_data_manhattan_id_inflow['DropOff_datetime'] = pd.to_datetime(fhv_data_manhattan_id_inflow['DropOff_datetime']) # 转换成datetime格式
    fhv_data_manhattan_id_outflow['Pickup_DateTime']=pd.to_datetime(fhv_data_manhattan_id_outflow['Pickup_DateTime'])
    # 设置对应的索引
    fhv_data_manhattan_id_inflow = fhv_data_manhattan_id_inflow.set_index('DropOff_datetime', drop = True)
    fhv_data_manhattan_id_outflow = fhv_data_manhattan_id_outflow.set_index('Pickup_DateTime', drop=True)
    # resample
    fhv_data_manhattan_id_inflow = fhv_data_manhattan_id_inflow.resample('H').SR_Flag.sum()
    # 生成一个series ，判断其长度 将其补全或者删除
    while len(fhv_data_manhattan_id_inflow) > 8760:
        print('数据太长了，需要删除一些行')
        fhv_data_manhattan_id_inflow.drop(fhv_data_manhattan_id_inflow.index[-1],inplace = True)
    fhv_data_manhattan_id_outflow = fhv_data_manhattan_id_outflow.resample('H').SR_Flag.sum()
    while len(fhv_data_manhattan_id_inflow) > 8760:
        print('数据太长了，需要删除一些行')
        fhv_data_manhattan_id_inflow.drop(fhv_data_manhattan_id_inflow.index[-1],inplace = True)
    fhv_data_manhattan_id_processed = pd.concat([fhv_data_manhattan_id_inflow, fhv_data_manhattan_id_outflow], axis=1)
    fhv_data_manhattan_id_processed.columns = ['inflow', 'outflow']
    fhv_data_manhattan_id_processed.to_csv(path+'node_values/fhv_tripdata_2018_Manhattan_'+str(location_id)+'_processed.csv')

```

## 0值填充

`nyc_fhv_tripdata[np.isnan(nyc_fhv_tripdata)] = 0
`


# geopandas

ArcGIS： shapefile 文件， 为GIS中的重要数据类型； 
点 线 多边形： point, polyline, polygon;
矢量格式文件

`geopandas`库允许对几何类型进行空间操作，其DataFrame结构相当于GIS数据中的一张属性表，使得可以直接操作矢量数据属性表，使得在python中操作地理数据更方便。用Python脚本中对Shapefile文件(.shp，.shx，.dbf等格式)进行读写操作。

## 安装 geopandas库

`anaconda`安装 库：

`conda install -c conda-forge geopandas`

导入   `geopandas`

## 曼哈顿区id

## 删除某一列中出现nan行

```
df[np.isnan(df['open'])].index# 这样即可定位到所在行的index，然后对该index进行drop操作即可
```

```
df.drop(df[np.isnan(df['open'])].index, inplace=True)# 直接drop对应indx即可删除该行
```

### 曼哈顿区域

删除 12 103 104 105 202 194 

### pandas bug

- 1. `pandas 解决 A value is trying to be set on a copy of a slice from a DataFrame的问题`

使用 .loc[行名，列名] 进行复制

- 2. .iloc
  
  通过行列号对 dataframe进行数据选择
  `df.iloc[1,1]`第2行第2列的数据

- 3. ndarray nan值填充



# 预测模型选择

## astgcn

![ASTGCN](https://xd-imgsubmit.oss-cn-beijing.aliyuncs.com/images/ASTGCN.png)

## mstgcn

去掉 spatial attention

改进gcn:

具体改进方式如下：
参考论文 ：[STSGCN](https://aaai.org/ojs/index.php/AAAI/article/view/5438)
- gcn 操作公式如下：
![20210913205855](https://xd-imgsubmit.oss-cn-beijing.aliyuncs.com/images/20210913205855.png)
- gcn 堆叠
  方式类似于下图
  ![20210913205933](https://xd-imgsubmit.oss-cn-beijing.aliyuncs.com/images/20210913205933.png)

  ![20210913210103](https://xd-imgsubmit.oss-cn-beijing.aliyuncs.com/images/20210913210103.png)


初步的运算结果：
![20210913210638](https://xd-imgsubmit.oss-cn-beijing.aliyuncs.com/images/20210913210638.png)