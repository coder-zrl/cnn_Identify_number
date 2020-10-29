# 依赖

* python---->version=3.6
* cv2---->version=4.4.0
* tkinter---->version=系统自带
* torch---->version=1.6.0
* torchvision---->version=0.7.0

<br>

# 模型搭建简介

* 搭建CNN模型
* 使用mnist手写数字数据集进行训练

<br>

# 代码介绍

* mnist：存放下载下来的数据集，为了减少程序上传大小，我已经将数据删除，需要获取请执行model_train.py
* model：存放训练好的模型
* photo：一些自己手写的测试照片
* cnn_model.py：搭建的CNN模型，准确率高达99%
* model_train.py：训练模型的代码
* model_reference.py：调用模型，识别photo中的数字
* tkGUI：搭建的可视化界面

* main.py：程序启动入口

<br>

# 使用介绍

尽量将自己手写字截图为正方形，`存放在没有汉字的目录下`，运行main.py程序

效果如图：

![在这里插入图片描述](https://img-blog.csdnimg.cn/20201030021753513.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzQ2NTIxNzg1,size_16,color_FFFFFF,t_70#pic_center)

