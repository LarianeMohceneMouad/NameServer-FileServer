from tkinter import *
from tkinter import ttk


class Client(object):
    def __init__(self, name):
        self.name = name

    def call(self, fileserver, req):
        print(f"CLIENT : {self.name} REACHING : {fileserver}")
        self.look(fileserver, req)

    def look(self, machine, request):
        machine.handler(request)

    def treeviewer(self):

        file = None

        root = Tk()
        root.title("FILE OPENER")
        tree = ttk.Treeview(root)



        A = tree.insert("", "end", "A", text="A")
        tree.insert(A, "end", text="F1", tags='F1')
        tree.insert(A, "end", text="F2", tags='F2')

        tree.insert("", "end", "B", text="B")
        tree.insert("B", "end", text="F3", tags='F3')
        tree.insert("B", "end", text="F4", tags='F4')





        def F1click(event):
            nonlocal  file
            file = "F1"

        def F2click(event):
            nonlocal file
            file = "F2"

        def F3click(event):
            nonlocal file
            file = "F3"

        def F4click(event):
            nonlocal file
            file = "F4"

        tree.tag_configure('F1', background='yellow')
        tree.tag_bind('F1', '<1>', F1click)
        tree.tag_configure('F2', background='yellow')
        tree.tag_bind('F2', '<1>', F2click)
        tree.tag_configure('F3', background='yellow')
        tree.tag_bind('F3', '<1>', F3click)
        tree.tag_configure('F4', background='yellow')
        tree.tag_bind('F4', '<1>', F4click)

        tree.pack()
        Button(root, text="DONE", command=root.destroy).pack()

        root.mainloop()

        return file

