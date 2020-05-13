#!/usr/bin/env python
# coding: utf-8

# In[5]:


from keras.preprocessing import image
import numpy as np
from tensorflow.keras.models import load_model


# In[283]:


classifies = load_model('model/final.pb')


# In[275]:

path = input("Enter the path of the image file(jpg/jpeg/png) :")
img = image.load_img(path,target_size=(64,64))


# In[276]:


test_img = image.img_to_array(img)


# In[277]:


test_img = np.expand_dims(test_img,axis=0)


# In[278]:


test_img


# In[284]:


result = classifies.predict(test_img)


# In[285]:


if result[0][0] == 1 or result[0][0]==0.9999:
    prediction = 'Adho Mukha Svanasana' 
elif result[0][1] == 1 or result[0][1]==0.9999:
    prediction = 'Ashtanga Namaskara'
elif result[0][2] == 1 or result[0][2]==0.9999:
    prediction = 'Ashwa Sanchalanasana'
elif result[0][3] == 1 or result[0][2]==0.9999:
    prediction = 'Bhujangasana'
elif result[0][4] == 1 or result[0][3]==0.9999:
    prediction = 'Dandasana'
elif result[0][5] == 1 or result[0][4]==0.9999:
    prediction = 'Hastapadasana'
elif result[0][6] == 1 or result[0][5]==0.9999:
    prediction = 'Hastauttanasana'
elif result[0][7] == 1 or result[0][6]==0.9999:
    prediction = 'pranamasana'
elif result[0][8] == 1 or result[0][7]==0.9999:
    prediction = 'Tadasana'


# In[286]:


print(result)


# In[287]:


print(prediction)


# In[ ]:




