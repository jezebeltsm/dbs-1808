#!/usr/bin/env python
# coding: utf-8

# In[28]:


from flask import Flask, request, render_template


# In[29]:


app = Flask(__name__) # 


# In[30]:


import joblib


# In[31]:


# decorater: any function that you declare below, you must come to this function first (you must run this first before you can run the other fns)
@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        rates = float(request.form.get("rates"))
        print(rates)
        model1 = joblib.load("regression") # rmb to paste regression & tree files into vs code folder
        r1 = model1.predict([[rates]])
        model2 = joblib.load("tree")
        r2 = model2.predict([[rates]])
        return(render_template("index.html", result1 = r1, result2 = r2))
    else:
        return(render_template("index.html", result1 = "waiting", result2 = "waiting"))


# In[ ]:


if __name__ == "__main__": # making sure that this program belongs to you
    app.run()


# In[ ]:





# In[ ]:





# In[ ]:




