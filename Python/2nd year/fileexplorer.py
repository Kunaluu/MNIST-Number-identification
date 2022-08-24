from tkinter import *
from tkinter import filedialog

def openFile():
    tf = filedialog.askopenfilename(
        initialdir="C:/Users/MainFrame/Desktop/", 
        title="Open Text file", 
        filetypes=(("Text Files", "*.txt"),("All Files","*.*"))
        )                                                                                           
    pathh.insert(END, tf)
    tf = open(tf, 'r')
    data = tf.read()
    txtarea.insert(END, data)
    tf.close()                           

ws = Tk()
ws.title("File explorer in Python!")
ws.geometry("400x450")
ws['bg']='blue'
txtarea = Text(ws, width=70, height=20)
txtarea.pack(pady=20)

pathh = Entry(ws)
pathh.pack(side=LEFT, expand=True, fill=X, padx=20)



Button(
    ws, 
    text="Open File", 
    command=openFile
    ).pack(side=RIGHT, expand=True, fill=X, padx=20)


ws.mainloop()