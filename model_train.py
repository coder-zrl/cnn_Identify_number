import torch
import torch.nn as nn
from cnn_module import CNN
import torch.utils.data as Data
import torchvision
import os

torch.manual_seed(1)    # reproducible

# Hyper Parameters
EPOCH = 1           # 训练整批数据多少次, 为了节约时间, 我们只训练一次
BATCH_SIZE = 50
LR = 0.001          # 学习率


# Mnist 手写数字
train_data = torchvision.datasets.MNIST(
    root='./mnist/',    # 保存或者提取位置
    train=True,  # this is training data
    transform=torchvision.transforms.ToTensor(),    # 转换 PIL.Image or numpy.ndarray 成
                                                    # torch.FloatTensor (C x H x W), 训练的时候 normalize 成 [0.0, 1.0] 区间
    download=True,# 没下载就下载, 下载了就不会再下了
)

test_data = torchvision.datasets.MNIST(root='./mnist/', train=False)

# 批训练 50samples, 1 channel, 28x28 (50, 1, 28, 28)
train_loader = Data.DataLoader(dataset=train_data, batch_size=BATCH_SIZE, shuffle=True)
# 为了节约时间, 我们测试时只测试前2000个
test_x = torch.unsqueeze(test_data.test_data, dim=1).type(torch.FloatTensor)[:2000]/255.   # shape from (2000, 28, 28) to (2000, 1, 28, 28), value in range(0,1)
test_y = test_data.test_labels[:2000]

cnn = CNN()
optimizer = torch.optim.Adam(cnn.parameters(), lr=LR)   # optimize all cnn parameters
loss_func = nn.CrossEntropyLoss()   # CrossEntropyLoss自带Softmax分类

# training and testing
for epoch in range(EPOCH):
    for step, (b_x, b_y) in enumerate(train_loader):   # 分配 batch data, normalize x when iterate train_loader
        output = cnn(b_x)               # cnn output
        loss = loss_func(output, b_y)   # cross entropy loss
        optimizer.zero_grad()           # clear gradients for this training step
        loss.backward()                 # backpropagation, compute gradients
        optimizer.step()                # apply gradients

        # 每50次就用模型做做测试
        if step%50 ==0:
            test_out = cnn(test_x)
            pred_y = torch.max(test_out,1)[1].data.squeeze()
            accuracy = torch.div(sum(pred_y == test_y).type(torch.FloatTensor), float(test_y.size(0)))
            print('Epoch:',epoch,'| train loss:%.4f'%loss.item(),'| test accuracy:%.4f',accuracy.item())
if 'model' not in os.listdir('./'):
    os.mkdir('model')
torch.save(cnn,'model/手写数字识别模型.pkl')