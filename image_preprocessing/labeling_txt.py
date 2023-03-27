#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import cv2
import csv

os.chdir(main_path)
for i in  os.listdir("ClinicalReadings"):
    os.chdir(label_path)
    with open(i,"rt") as file:
        if i == ".ipynb_checkpoints":
            pass
        
        else:
            a = file.readlines()
            if a[-1] == "normal":
                x = i.split("0.txt")   # dosyadan okunan resimlerin isimlendirmesini yapmak için 0.txt kullanıyorum
                filename = x[0] + "0.png"
                label[filename] = 0
                x.clear()
            
            else:
                x = i.split("1.txt")   
                filename = x[0] + "1.png"
                label[filename] = 1
                x.clear()


def selection():
    os.chdir(main_path)

    for i,j in zip(label.keys(),os.listdir("CXR_png")):
        if i == j:
            os.chdir(image_path)
            a = cv2.imread(i)
            x = i.split(".png")
            new_filename = x[0] + str(label[i]) + ".png"
            os.chdir(target_path)
            cv2.imwrite(new_filename,a)
            


selection()


# In[ ]:


get_ipython().system('jupyter ')

