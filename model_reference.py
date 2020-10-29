import torch
from PIL import Image
import torchvision
import cv2 as cv
from cnn_model import CNN
import os

class Identifier():
    def __init__(self):
        # loader使用torchvision中自带的transforms函数
        self.loader = torchvision.transforms.ToTensor()
        self.cnn = torch.load('model/手写数字识别模型——99%成功率.pkl')

    def identify_number(self,filepath):
        src = cv.imread(filepath)
        gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
        ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
        # cv.imwrite(filepath, binary)
        img = Image.fromarray(binary).convert('L').resize((28,28))
        img = self.loader(img).resize(1,1,28,28)

        test_output = self.cnn(img)
        pred_y = torch.max(test_output, 1)[1].data.numpy().squeeze()
        return pred_y

if __name__ == '__main__':
    photo_ls = os.listdir('./my_photo')
    identifier=Identifier()
    # for photo in photo_ls:
    #     real_path = os.path.join('./my_photo',photo)
    #     # print(real_path)
    #     pred = identifier.identify_number(real_path)
    #     print(pred)
    print(identifier.identify_number('C:/Users/Administrator/Desktop/5.jpg'))