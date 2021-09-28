# 哈希 in python 
## 声明
本文摘录自 知乎作者： 寒冰
文章地址：[哈希 in python](https://zhuanlan.zhihu.com/p/58600070)


## 哈希
本节内容从介绍哈希的基本概念 。主要包含数论基础，哈希表的介绍及实现，双哈希，混沌机，以及摘要算法。

## 知识点
- 哈希的概念
- 数论基础
- 哈希表的实现和介绍
- 双哈希
- 混沌机
- 摘要算法

## 哈希的概念
### 什么是哈希

哈希(Hash)，一般翻译做散列、杂凑，或音译为哈希，
是把任意长度的输入（又叫做预映射 pre-image）通过散列算法变换成固定长度的输出，该输出就是散列值。
这种转换是一种压缩映射，也就是，散列值的空间通常远小于输入的空间，不同的输入可能会散列成相同的输出，所以不可能从散列值来确定唯一的输入值。
**简单的说就是一种将任意长度的消息压缩到某一固定长度的消息摘要的函数**。


### 概念介绍
若结构中存在和关键字 K 相等的记录，则必定在 f(K)的存储位置上。由此，不需比较便可直接取得所查记录。称这个对应关系 f 为**散列函数(Hash function)**，按这个事先建立的表为散列表.

对不同的关键字可能得到同一散列地址，即 `key1≠key2`，而 `f(key1)=f(key2)`，这种现象称**碰撞**。具有相同函数值的关键字对该散列函数来说称做**同义词**。综上所述，根据散列函数 `H(key)`和处理冲突的方法将一组关键字映象到一个有限的连续的地址集（区间）上，并以关键字在地址集中的“象” 作为记录在表中的存储位置，这种表便称为**散列表**，这一映象过程称为散列造表或散列，所得的存储位置称**散列地址**。

若对于关键字集合中的任一个关键字，经散列函数映象到地址集合中任何一个地址的概率是相等的，则称此类散列函数为**均匀散列函数(Uniform Hash function)**，这就是使关键字经过散列函数得到一个“随机的地址”，从而减少冲突。


## 数论基础
素数，也称质数，只包含两个因数，且一个因数为 1，一个因数为它本身。

素数有以下性质：

- 素数 p 的因子有且只有两个：1 和 p
- 素数一定是奇数
- 任意一个大于 1 的正整数 N，一定可以质因式分解为它的有限个质因子之积
- 素数的个数是无限的
- 所有大于 10 的素数中，其个位数只能是 1,3,7,9 其中之一
- 一个充分大的偶数一定可以写成：一个素数加上一个最多由 2 个质因子所组成的合成数


## 判断素数

筛选法
1. 将n个数字全部放进数组 ，并将其置为肯定状态
2. 将数组中下标为偶数的数字置为否定状态
3. 依次遍历数组长度的平方根个苏子
4. 如果当前数字处于肯定状态，将其倍数置为否定状态

```
def find_prime_2(num):
    primes_bool=[False,False]+[True]*(num-1) # 1，2都不为素数
    for i in range(3,len(primes_bool)): # 从3开始遍历数组，第一次将偶数全部放置否定
        if i&1==0:
            prims_bool[i]=False
    for i in range(3,int(math.sqrt(num))+1):  # 第二次 ，将倍数置否
        if prims_bool[i] is True:
            for j in range(i+j,num+1,i):
                prims_bool[j]=False
    prims=[]
    [prims.append(i) for i,v in enumerate(prims_bool) if v is True]
    return prims
```


## 哈希表

哈希表（Hash table，也叫散列表），是根据关键码值`(Key value)`而直接进行访问的数据结构。也就是说，它通过把关键码值映射到表中一个位置来访问记录，以加快查找的速度。这个映射函数叫做`散列函数`，存放记录的数组叫做`散列表`。

给定表 `M`，存在函数 `f(key)`，对任意给定的关键字值 `key`，代入函数后若能得到包含该关键字的记录在表中的地址，则称表 `M `为`哈希(Hash）表`，函数 `f(key)`为哈希(Hash) 函数。

在平均情况下，在哈希表中查找一个元素的期望时间是 O(1) ,因此效率极高。Python 中的字典就是采用了哈希表的结构。

注：定义来自百度百科

### 哈希表的特点

哈希表具有以下特点：

- 若关键字为 k，则其值存放在 f(k)的存储位置上。由此，不需比较便可直接取得所查记录。称这个对应关系 f 为散列函数，按这个思想建立的表为散列表。
- 对不同的关键字可能得到同一散列地址，即 `k1≠k2`，而 `f(k1)=f(k2)`，这种现象称为冲突。具有相同函数值的关键字对该散列函数来说称做同义词。综上所述，根据散列函数 `f(k)`和处理冲突的方法将一组关键字映射到一个有限的连续的地址集（区间）上，并以关键字在地址集中的“像”作为记录在表中的存储位置，这种表便称为散列表，这一映射过程称为散列造表或散列，所得的存储位置称散列地址。
- 若对于关键字集合中的任一个关键字，经散列函数映象到地址集合中任何一个地址的概率是相等的，则称此类散列函数为`均匀散列函数（Uniform Hash function）`，这就是使关键字经过散列函数得到一个“随机的地址”，从而减少冲突。


### 哈希表的实现

#### 线性哈希实现

哈希表为一个具有映射关系的表，通过映射关系及`key` 找到对应的`vlaue`

```
class hashtable(object):
    def __init__(self):
        self.items=[]
    def put(self,k,v):
        self.items.append((k,v)) #添加对应关系
    def get(self,k):
        for key,value in self.items:
            if(k==key):
                return value #返回正确匹配出的结果

```
上述的实现方法的 查找复杂度为线性 $\mathcal{o}(n)$
改进以下： 找到一个映射函数

```
class hash_table(object):
    def __init__(self):
    self.items = [None]*100

    def hash(self,a):
        # 定义线性的映射函数
        return a*1+1
    
    def put(self,k,v):
        # 使用hash函数，计算映射地址，添加该映射关系
        self.items[self.hash(k)]=v 

    def get(self, k):
        hashcode = self.hash(k) # 根据hash函数，计算其映射的值，从哈希表中取出相对应的结果
        return self.items(hashcode)


```

“这 hash 函数有点简单啊” 是的，它是简单，但简单不妨碍它成为一个哈希函数，事实上，它叫直接定址法，是一个线性函数： hash(k)= a*k+b

直接定址法的优点很明显，就是它不会产生重复的 hash 值。但由于它与键值本身有关系，所以当键值分布很散的时候，会浪费大量的存储空间。所以一般是不会用到直接定址法的。

#### 冲突处理
处理冲突假如某个 `hash` 函数产生了一堆哈希值，而这些哈希值产生了冲突怎么办（实际生产环境中经常发生）？在各种哈希表的实现里，处理冲突是必需的一步。 比如你定义了一个 `hash 函数`： `hash(k)=k mod 10` 假设 `key` 序列为：`[15,1,24,32,55,64,42,93,82,76]`，一趟下来，冲突的元素有四个，下面有几个办法解决冲突。

1. 开放地址法
   
   $$hash_i=(hash(key)+d_i) mod m, i= 1,2,3,...,k(k<= m-1) $$

   di 为增量序列；H(key)为散列函数，m为散列表长

2. 再散列法

再散列法：Hi=RHi(key),i=1,2,...，k RHi 均是不同的散列函数，即在同义词产生地址冲突时计算另一个散列函数地址，直到冲突不再发生，这种方法不易产生“聚集”，但增加了计算时间



开放地址法(线性探测 )

```
class hashtable(object):
    def __init__(self):
        self.hash_table=[[None,None] for i in range(10)]
    def hash(self,k,i):
        h_value=(k+i)%10
        if self.hash_table[h_value][0]==k:
            return h_value
        if self.hash_table[h_value][0]!=None:
            i=i+1
            h_value=self.hash(k,i)
        return h_value
    def put(self,k,v):
        hash_v=self.hash(k,0)
        self.hash_table[hash_v][0]=k
        self.hash_table[hash_v][1]=v
    def get(self,k):
        hash_v=self.hash(k,0)
        return self.hash_table[hash_v][1]
table=hashtable()
for i in range(9):
    table.put(i,i)
print(table.get(3))
print(table.hash_table)
```

上述方法的思路简述为： 当遇到冲突时，线性探索，找到一个空槽放进去


载荷因子 load factor ，定义为：$\alpha = 已有的元素/表的长度$，$\alpha$越大表示表中已有的元素越多，产生冲突的可能性就越大

实际上，散列表的平均查找长度是载荷因子 α的函数，只是不同处理冲突的方法有不同的函数。所以当到达一定程度，表的长度是要变的，即 resize，载荷因子被设计为 0.75；超过 0.8，cpu 的 cache missing 会急剧上升。具体扩容多少，一般选择扩到已插入元素数量的两倍.

```
class hashtable(object):
    def __init__(self):
        self.capacity=10
        self.hash_table=[[None,None]for i in range(self.capacity)]
        self.num=0
        self.load_factor=0.75
    def hash(self,k,i):
        h_value=(k+i)%self.capacity
        if self.hash_table[h_value][0]==k:
            return h_value
        if self.hash_table[h_value][0]!=None:
            i=i+1
            h_value=self.hash(k,i)
        return h_value
    def resize(self):
        self.capacity=self.num*2 #扩容到原有元素数量的两倍
        temp=self.hash_table[:]
        self.hash_table=[[None,None]for i in range(self.capacity)]
        for i in temp:
            if(i[0]!=None):  #把原来已有的元素存入
                hash_v=self.hash(i[0],0)
                self.hash_table[hash_v][0]=i[0]
                self.hash_table[hash_v][1]=i[1]
    def put(self,k,v):
        hash_v=self.hash(k,0)
        self.hash_table[hash_v][0]=k
        self.hash_table[hash_v][1]=v
        self.num=self.num+1                 #暂不考虑key重复的情况，具体自己可以优化
        if(self.num/len(self.hash_table)>self.load_factor):# 如果比例大于载荷因子
            self.resize()
    def get(self,k):
        hash_v=self.hash(k,0)
        return self.hash_table[hash_v][1]
table=hashtable()
for i in range(15):
    table.put(i,i)
print(table.get(3))
print(table.hash_table)
```


#### 双重哈希

双重哈希，也叫一致性哈希，属于开放地址哈希中的一种解决冲突方案，也就是说如果一次哈希不能解决问题的时候，要再次哈希，与再哈希方法不同的是，第二次使用的哈希函数与第一次是不同的：(hash1(key) + i * hash2(key)) % TABLE_SIZE

一般来讲，

- hash1(key) = key % TABLE_SIZE
- hash2(key) = PRIME – (key % PRIME)
其中 PRIME 一般选一个比 TABLE_SIZE 小的一个质数就可以了，例如如果 TABLE_SIZE=16，那么 PRIME=13。

注意：第二个哈希函数结果不能为 0，而且第二个哈希函数要覆盖表的每一个单元。

至于 i 就从 1 开始尝试就是了，如果有冲突，则再尝试 i++。
