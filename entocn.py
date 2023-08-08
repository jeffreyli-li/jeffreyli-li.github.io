import requests,tkinter,pygame
from bs4 import BeautifulSoup
from tkinter.messagebox import showinfo,showerror,askquestion

pygame.mixer.init()
def search():
    global listb, e1
    word = e1.get()
    #在13行补充代码，拼接get获取到的待翻译词语到url中
    url = "http://www.iciba.com/word?w=" + word
    response = requests.get(url)
    soup = BeautifulSoup(response.text,"lxml")
    data1 = soup.find(name="ul", class_="Mean_part__1RA2V")
    try:
        for i in data1:
            data=i.find_all(name="span")
    except:
        pass
    #在18行补充清除列表框内容的语句，要求从首行到末行全部清除
    listb.delete(0,tkinter.END)
    try:
        for n in data:
            listb.insert(0, n.text)
    except:
        listb.insert(0,'未找到该词语！')
root = tkinter.Tk()
root.title('词语翻译器')
def clrred():
    e1.configure(fg='red')
    button1.configure(fg='red')
    listb.configure(fg='red')
def clrblue():
    e1.configure(fg='blue')
    button1.configure(fg='blue')
    listb.configure(fg='blue')
def clrpurple():
    e1.configure(fg='purple')
    button1.configure(fg='purple')
    listb.configure(fg='purple')
def clrblack():
    e1.configure(fg='black')
    button1.configure(fg='black')
    listb.configure(fg='black')
def clrwhite():
    e1.configure(fg='white')
    button1.configure(fg='white')
    listb.configure(fg='white')
def clrgreen():
    e1.configure(fg='green')
    button1.configure(fg='green')
    listb.configure(fg='green')
def bgclrred():
    e1.configure(bg='red')
    button1.configure(bg='red')
    listb.configure(bg='red')
    root.configure(background="red")
def bgclrblue():
    e1.configure(bg='blue')
    button1.configure(bg='blue')
    listb.configure(bg='blue')
    root.configure(background="blue")
def bgclrpurple():
    e1.configure(bg='purple')
    button1.configure(bg='purple')
    listb.configure(bg='purple')
    root.configure(background="purple")
def bgclrblack():
    e1.configure(bg='black')
    button1.configure(bg='black')
    listb.configure(bg='black')
    root.configure(background="black")
def bgclrwhite():
    e1.configure(bg='white')
    button1.configure(bg='white')
    listb.configure(bg='white')
    root.configure(background="white")
def bgclrgreen():
    e1.configure(bg='green')
    button1.configure(bg='green')
    listb.configure(bg='green')
    root.configure(background="green")
def quit():
    ask=askquestion('确认？','确认要关闭窗口吗？')
    if ask=='yes':
        root.destroy()
        #print(ask)
    else:
        showinfo('成功','好的')
        #print(ask)
def nbgm():
    pygame.mixer.music.pause()
def bgm1():
    pygame.mixer.music.load("Hero's Theme.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)
root.protocol("WM_DELETE_WINDOW",quit)
menu1 = tkinter.Menu(root, tearoff=0) #1的话多了一个虚线，如果点击的话就会发现，这个菜单框可以独立出来显示
menu1.add_command(label="蓝色",command=clrblue)
menu1.add_command(label="红色",command=clrred)
menu1.add_command(label="紫色",command=clrpurple)
menu1.add_command(label="黑色",command=clrblack)
menu1.add_command(label="白色",command=clrwhite)
menu1.add_command(label="绿色",command=clrgreen)
menu2 = tkinter.Menu(root, tearoff=0) #1的话多了一个虚线，如果点击的话就会发现，这个菜单框可以独立出来显示
menu2.add_command(label="蓝色",command=bgclrblue)
menu2.add_command(label="红色",command=bgclrred)
menu2.add_command(label="紫色",command=bgclrpurple)
menu2.add_command(label="黑色",command=bgclrblack)
menu2.add_command(label="白色",command=bgclrwhite)
menu2.add_command(label="绿色",command=bgclrgreen)
menu3 = tkinter.Menu(root, tearoff=0) #1的话多了一个虚线，如果点击的话就会发现，这个菜单框可以独立出来显示
menu3.add_command(label="Hero's Theme",command=bgm1)
menu3.add_command(label="关掉背景音乐",command=nbgm)
mebubar = tkinter.Menu(root)
mebubar.add_cascade(label="前景颜色", menu=menu1) #原理：先在主菜单中添加一个菜单，与之前创建的菜单进行绑定。
mebubar.add_cascade(label="背景颜色", menu=menu2)
mebubar.add_cascade(label="背景音乐", menu=menu3)
mebubar.add_command(label="退出", command=quit)
root.config(menu=mebubar)
#可以在23行修改主窗口的颜色
root.configure(background="white")
#利用Entry定义输入控件e1，要求输入框的粗细为5
e1 = tkinter.Entry(root,bd=3,fg='red')
e1.pack()
button1 = tkinter.Button(root, text="查询",fg='red',command=search)
button1.pack()
#自定义列表框的宽width、高height、背景颜色bg、字体颜色fg（不要丢掉重要的第一个参数主窗口名哦！）
listb = tkinter.Listbox(root,width=50,height=20,bg='white',fg='red')
listb.pack()
root.mainloop()
