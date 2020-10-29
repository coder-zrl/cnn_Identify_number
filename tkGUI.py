from model_reference import Identifier
from cnn_model import CNN
import tkinter as tk
import tkinter.messagebox
from tkinter.filedialog import askopenfilename

class Frame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.filename = None
        self.title("手写数字识别器")
        self.geometry("370x200")
        self.identifier = Identifier()
        self.init()
    def init(self):
        # 文件路径
        self.e1 = tk.Entry(self)
        self.e1.place(x=80,y=30)
        self.e2 = tk.Entry(self)
        self.e2.place(x=100,y=110)
        # 创建按钮
        self.b1 = tk.Button(self, text="选择文件", command=self.getpath)
        self.b1.place(x=230,y=25)
        self.b2 = tk.Button(self, text="开始识别", command=self.do_identify)
        self.b2.place(x=140,y=70)
    def getpath(self):
        self.filename = askopenfilename()
        print(self.filename)
        self.e1.delete(0, tk.END)
        self.e1.insert(0, self.filename)
    def do_identify(self):
        try:
            print(self.e1.get())
            result = str(self.identifier.identify_number(self.e1.get()))
            print(result)
            self.e2.delete(0, tk.END)
            self.e2.insert(0, '识别结果：'+result)
        except Exception as e:
            print(e)
            tkinter.messagebox.showwarning(title='识别失败', message='文件目录请不要含有中文！')





if __name__ == '__main__':
    win = Frame()
    win.mainloop()
