# importing only those functions which are needed
from tkinter import*
from tkinter.ttk import*
from time import strftime

# creating tkinter window
root = Tk()
root.title('Disk Imager')
root.geometry("700x500")

# Creating Menubar
menubar = Menu(root)

# Adding File Menu and commands
file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='File', menu = file)
file.add_command(label ='Add Evidence Item', command = None)
file.add_command(label ='Remove Evidence Item', command = None)
file.add_command(label ='Create Image', command = None)
file.add_command(label ='Clone Device', command = None)
file.add_command(label ='Export Disk Image', command = None)
file.add_command(label ='Capture Memory', command = None)
file.add_separator()
file.add_command(label ='Exit', command = root.destroy)

# Adding View Menu and commands
view = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='View', menu = view)
view.add_command(label ='Tool Bar', command = None)
view.add_command(label ='Status Bar', command = None)
view.add_command(label ='Show Hex Position Values', command = None)
view.add_command(label ='Evidence Tree', command = None)
view.add_command(label ='Details', command = None)


# Adding Help Menu
help_ = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Help', menu = help_)
help_.add_command(label ='Disk Imager Help', command = None)
help_.add_command(label ='Demo', command = None)
help_.add_separator()
help_.add_command(label ='About Disk Imager', command = None)

# display Menu
root.config(menu = menubar)

mainloop()