#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data=pd.read_csv('50_Startups.csv')


# In[3]:


x=data.iloc[:,0:-2]
y=data.iloc[:,-1]


# In[5]:


from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.20)


# In[6]:


from sklearn.linear_model import LinearRegression
model=LinearRegression()


# In[7]:


model.fit(xtrain,ytrain)


# In[20]:


from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def gjkkjg():
    return render_template('linear.html')
@app.route('/info',methods=['POST'])
def gkjf():
    if(request.method=='POST'):
        res=int(request.form['r'])
        admin=int(request.form['a'])
        mark=int(request.form['m'])
        amount=model.predict([[res,admin,mark]])
        return render_template('linear.html',profit=amount[0])
if __name__=='__main__':
    app.run()

