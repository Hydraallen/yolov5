import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join
import shutil

# VOC生成txt的文件

sets = ['train', 'val', 'test']  # 数据集，最后会生成以这三个数据集命名的txt文件

classes = ['with_mask', 'without_mask', 'mask_weared_incorrect']  # 标签名，注意一定不要出错


def convert(size, box):
    # yolo x,y,w,h
    #   x：中心点x值/图片宽度，
    #   y:中心点y值/图片高度，
    #   w：目标框的宽度/图片宽度，
    #   h：目标框的高度/图片高度。
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)


def convert_annotation(image_id):
    in_file = open('./DataSets/annotations/%s.xml' % (image_id), 'r', encoding="UTF-8")
    out_file = open('./DataSets/labels/%s.txt' % (image_id), 'w')
    tree = ET.parse(in_file)
    root = tree.getroot()
    # 获取图片大小，为后续坐标转换做准备
    # <annotation>
    #     <folder>images</folder>
    #     <filename>maksssksksss603.png</filename>
    #     <size>
    #         <width>400</width>
    #         <height>278</height>
    #         <depth>3</depth>
    #     </size>
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        # 获取标注框的标签和位置，并进行转换
        #     <object>
        #         <name>with_mask</name>
        #         <pose>Unspecified</pose>
        #         <truncated>0</truncated>
        #         <occluded>0</occluded>
        #         <difficult>0</difficult>
        #         <bndbox>
        #             <xmin>49</xmin>
        #             <ymin>11</ymin>
        #             <xmax>55</xmax>
        #             <ymax>17</ymax>
        #         </bndbox>
        #     </object>
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        box = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text),
                float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w, h), box)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')


if not os.path.exists('./DataSets/labels/'):  # 创建label文件夹
    os.makedirs('./DataSets/labels/')

for image_set in sets:
    image_ids = open('./DataSets/ImageSets/Main/%s.txt' % (image_set)).read().strip().split()
    list_file = open('./DataSets/%s.txt' % (image_set), 'w')
    for image_id in image_ids:
        list_file.write('./images/%s.png\n' % (image_id))  # 这里最好用全局路径
        convert_annotation(image_id)
    list_file.close()



