from tkinter.filedialog import askopenfilename

file_name = askopenfilename()
file_content = open(file_name,"r")

for line in file_content:
    print(line)
