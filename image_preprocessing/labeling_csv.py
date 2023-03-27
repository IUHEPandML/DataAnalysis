#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import os
import cv2


data = pd.read_csv("montgomery_metadata.csv")
datam = data.copy()

yeni_dat = datam.drop(["age","gender"],axis=1)

label_set = {}


"""
Burada yaptığım şey data setimdeki sınıflara göre etiketleme işlemi yapmak ve buradaki data setinde 2 tip sınıf olacak şekilde(normal sınıf ve hasta olan sınıf) data setinden ilgili 
kolonlar üzerinden sınıfları saptayan bir for döngüsü oluşturdum. Ardından bu oluşturduğum etiketleme işleminin bir kopyasının olması için bunu bir kütüphane içerisinden image id lere 
hastalık durumu karşılık gelecek şekilde kaydettim.
İkinci for döngüsünden bu etiketlerin işlenmesi durumunu ele aldım ve ıdler üzerinden imagelerin isimlerine bir etiket ekleyerek bu imageleri etiketli görüntü dosyasına kaydettim 
bu kayıt işlemini yapmamım sebebi ana dosyamıza dokunmadan bir kopya oluşturup bunları etiketleme yapmak ve yapılacak işlemleri bunun üzerinden gerçekleştirmek.
"""
for i in range(len(yeni_dat.index)):
    if yeni_dat["findings"][i] == "normal":
        label_set[yeni_dat["study_id"][i]]="normal"
    else:
        label_set[yeni_dat["study_id"][i]]="problem"
        
    
ana_path = "C:\\Users\\90530\\ML DERSLERİ\\Görüntü işleme dersleri(Güray hoca)"
label_path = "C:\\Users\\90530\\ML DERSLERİ\\Görüntü işleme dersleri(Güray hoca)\\label_dosyası"
image_path = "C:\\Users\\90530\\ML DERSLERİ\\Görüntü işleme dersleri(Güray hoca)\\images\\images"

for i in label_set.keys():
    os.chdir(image_path)
    if label_set[i] == "normal":
        img = cv2.imread(i)
        os.chdir(label_path)
        x = i.split(".png")
        filename = x[0] + "0.png"
        cv2.imwrite(filename,img)
        x.clear()
        os.chdir(ana_path)
    
    else:
        img = cv2.imread(i)
        os.chdir(label_path)
        x = i.split(".png")
        filename = x[0] + "1.png"
        cv2.imwrite(filename,img)
        x.clear()
        os.chdir(ana_path)


# In[1]:


get_ipython().system('pip install nbconvert')


# In[14]:


get_ipython().system('pip install ipython')


# In[8]:


nbconvert to script labeling_csv.ipynb


# In[22]:



import nbconvert


# In[23]:


nbconvert labeling_csv.ipynb --to script 


# In[ ]:




