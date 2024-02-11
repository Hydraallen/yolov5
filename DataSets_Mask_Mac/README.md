# README

[配置参考](https://www.modb.pro/db/605993)

## Usage

`train.py` 

weights：权重文件路径

cfg：存储模型结构的配置文件

data：存储训练、测试数据的文件

epochs：指的就是训练过程中整个数据集将被迭代（训练）了多少次，轮数，默认300，需要指定；说明一下基本上epochs小于100时训练出来的模型没有任何参考意义。

batch-size：单次吞吐的数据多少，基本上就是电脑的运存，建议为80%左右电脑内存（16g运存就分配个12g那样）

resume： 重新训练默认是false，但是当你的训练因为一些因素被迫暂停了，可以将其置为True来检查断点（checkpoint）继续训练；

img-size：输入图片宽高；

device：cuda device, i.e. 0 or 0,1,2,3 or cpu。选择使用GPU还是CPU

workers：线程数。默认是8。现在大家的电脑CPU普遍是8核心起步，所以CPU训练时候不会报错，但是当你选择GPU训练时，显卡一般都是流处理器，所以我们要将其设为1，或者是0，否则会爆出内存不够的BUG。

`models` 存放已有模型参数

`runs`存放模型训练结果

`DataSets`存放训练集

`DataSets_apart.py` 拆分数据集

`DataSets_tranXML.py`生成`.txt`文件

## Test

**注意修改`./data/mask.yaml`中的路径！**

```bash
python DataSets_apart.py
python DataSets_tranXML.py
python DataSetsTrain.py
```



