from tkinter.filedialog import askopenfilename

##tkinter window should close
file_name = askopenfilename()
file_content = open(file_name,"r")

for line in file_content:
    print(line)
##File shold close after it is read
