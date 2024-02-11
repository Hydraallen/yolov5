# coding:utf-8
# 划分数据集
import os
import random
import argparse

parser = argparse.ArgumentParser()
# xml文件的地址，根据自己的数据进行修改 xml一般存放在Annotations下
parser.add_argument('--xml_path', default='../DataSets_Mask_Win/annotations', type=str, help='xml path')
# xml文件的地址，根据自己的数据进行修改 xml一般存放在Annotations下
parser.add_argument('--img_path', default='../DataSets_Mask_Win/images', type=str, help='img path')
# 数据集划分后txt文件的存储地址，地址选择自己数据下的ImageSets/Main
parser.add_argument('--txt_path', default='../DataSets_Mask_Win/ImageSets/Main', type=str, help='output txt label path')
opt = parser.parse_args()

trainval_percent = 0.9 # 训练集和验证集的比例
train_percent = 0.9 # 训练集占总数据的比例
imgfilepath = opt.img_path
txtsavepath = opt.txt_path

total_xml = os.listdir(imgfilepath)
if not os.path.exists(txtsavepath):
    os.makedirs(txtsavepath)

num = len(total_xml)
list_index = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
# 训练集+验证集 767
trainval = random.sample(list_index, tv)
# 训练集 690
train = random.sample(trainval, tr)
# 划分生成的文件名称
file_trainval = open(txtsavepath + '/trainval.txt', 'w')
file_test = open(txtsavepath + '/test.txt', 'w')
file_train = open(txtsavepath + '/train.txt', 'w')
file_val = open(txtsavepath + '/val.txt', 'w')

# 遍历range表，将训练集+验证集、训练集、验证集、测试集分别写入相应文件
for i in list_index:
    name = total_xml[i][:-4] + '\n'
    if i in trainval:
        file_trainval.write(name)
        if i in train:
            file_train.write(name)
        else:
            file_val.write(name)
    else:
        file_test.write(name)

file_trainval.close()
file_train.close()
file_val.close()
file_test.close()




