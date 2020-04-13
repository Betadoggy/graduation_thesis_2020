import os

path = "crawled"
file_list = os.listdir(path)
file_list_txt = [file for file in file_list if file.endswith(".txt")]

print ("file_list_txt: {}".format(file_list))

