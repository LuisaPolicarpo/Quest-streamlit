import pandas as pd
import streamlit as st
import datetime
import matplotlib.pyplot as plt
import numpy as np
import altair as alt
import seaborn as sns

st.title("Quest_Streamlit")
df_cars=pd.read_csv("https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv", sep =",",)
#st.dataframe(data=df_cars)


    
#df_car.groupby('continent')['mpg'].mean()



#st.dataframe(df_car.groupby('year')['continent'].value_counts())


#options = st.multiselect(
    #'What are your favorite colors',
    #['Green', 'Yellow', 'Red', 'Blue'],
    #['Yellow', 'Red'])

#st.write('You selected:', options)

#fig, ax = plt.subplots(figsize=(10, 4))
#ax = sns.regplot(x="hp", y="mpg", data=df_car)
#ax.set_xlabel("hp")
#ax.set_ylabel("mpg")
#ax.set_title("mpgxweightlbs")
#st.pyplot(fig)

#fig, ax= plt.subplots (figsize= (20,5))

#sns.regplot (x=df_car (df_car['continent']== add_selectbox) ["cubicinches"], y= #df_car[df_car['continent']==add_selectbox] ["cylinders"])
#ax.set_title ("Are cubicinches and cylinders related?")
#ax.set_xlaber ("year")
#st.pyplot(fig)
#St.text('The hither the cubicinches, the higher are the cylinders of the car')


add_selectbox = st.sidebar.radio(
    "Continents",
    ("US", "Europe","Japan"))

#if add_selectbox=='US':
    #st.subheader('You selected US')
   # cond_US=df_car[df_car['continent']==' US.']
    #fig, ax1 = plt.subplots(figsize=(10, 4))
    #ax1.bar(df_car["year"], df_car["hp"])
    #ax1.set_title('Relation Year vs HP')
   # ax1.set_ylabel('HP')
    #ax1.set_xlabel('Year')
    #fig.autofmt_xdate()
    #st.pyplot(fig)
  
   # fig2, ax = plt.subplots(figsize=(10, 4))
    #ax = sns.regplot(x="hp", y="mpg", data=df_car)
    #ax.set_xlabel("hp")
    #ax.set_ylabel("mpg")
    #ax.set_title("Relation Mpg and Wightlibs")
    #st.pyplot(fig2)

if add_selectbox == 'US':
    
    st.subheader('You selected US')
    cond_US=df_cars[df_cars['continent']==' US.']
    st.title('''Only analysed the distribution and correlation of the variables that showed some degree of correlation''')
    st.subheader('The analysis of the distribution of variables:')
    

    fig, axes = plt.subplots(2, 4, figsize=(18, 10))

    ax=sns.histplot(data=cond_US, x='mpg', ax=axes[0,0])
    ax.set_xlabel("mpg")
    ax.set_ylabel("count")
    ax.set_title("mpg")

    ax=sns.histplot(data=cond_US, x='cylinders', ax=axes[0,1])
    ax.set_xlabel("cylinders")
    ax.set_ylabel("count")
    ax.set_title("cylinders")
    
    ax=sns.histplot(data=cond_US, x='cubicinches', ax=axes[0,2])
    ax.set_xlabel("cubicinches")
    ax.set_ylabel("count")
    ax.set_title("cubicinches")
    
    ax=sns.histplot(data=cond_US, x='hp', ax=axes[0,3])
    ax.set_xlabel("hp")
    ax.set_ylabel("count")
    ax.set_title("hp")
    
    ax=sns.histplot(data=cond_US, x='weightlbs', ax=axes[1,0])
    ax.set_xlabel("weightlbs")
    ax.set_ylabel("count")
    ax.set_title("weightlbs")
    
    
    st.pyplot(fig)
    
    st.subheader('The analysis of the distribution of variables')

        
    fig, ax = plt.subplots(figsize=(10, 4))
    ax = sns.regplot(x='weightlbs', y="mpg", data=cond_US)
    ax.set_xlabel("weightlbs")
    ax.set_ylabel("mpg")
    ax.set_title("mpg x weightlbs")
    st.pyplot(fig)
    
    fig, ax = plt.subplots(figsize=(10, 4))
    ax = sns.regplot(x='weightlbs', y="cubicinches", data=cond_US)
    ax.set_xlabel("weightlbs")
    ax.set_ylabel("cubicinches")
    ax.set_title("weightlbs x cubicinches")
    st.pyplot(fig)
    
    fig, ax = plt.subplots(figsize=(10, 4))
    ax = sns.regplot(x='weightlbs', y="hp", data=cond_US)
    ax.set_xlabel("weightlbs")
    ax.set_ylabel("hp")
    ax.set_title("weightlbs x hp")
    st.pyplot(fig)
    
    
elif add_selectbox == 'Europe':
    
    st.subheader('You selected Europe')
    cond_US=df_cars[df_cars['continent']==' Europe.']
    st.title('''Only analysed the distribution and correlation of the variables that showed some degree of correlation''')
    st.subheader('The analysis of the distribution of variables:')
    

    fig, axes = plt.subplots(2, 4, figsize=(18, 10))

    ax=sns.histplot(data=cond_US, x='mpg', ax=axes[0,0])
    ax.set_xlabel("mpg")
    ax.set_ylabel("count")
    ax.set_title("mpg")

    ax=sns.histplot(data=cond_US, x='cylinders', ax=axes[0,1])
    ax.set_xlabel("cylinders")
    ax.set_ylabel("count")
    ax.set_title("cylinders")
    
    ax=sns.histplot(data=cond_US, x='cubicinches', ax=axes[0,2])
    ax.set_xlabel("cubicinches")
    ax.set_ylabel("count")
    ax.set_title("cubicinches")
    
    ax=sns.histplot(data=cond_US, x='hp', ax=axes[0,3])
    ax.set_xlabel("hp")
    ax.set_ylabel("count")
    ax.set_title("hp")
    
    ax=sns.histplot(data=cond_US, x='weightlbs', ax=axes[1,0])
    ax.set_xlabel("weightlbs")
    ax.set_ylabel("count")
    ax.set_title("weightlbs")
    
    
    st.pyplot(fig)
    
    st.subheader('The analysis of the distribution of variables')

        
    fig, ax = plt.subplots(figsize=(10, 4))
    ax = sns.regplot(x='weightlbs', y="mpg", data=cond_US)
    ax.set_xlabel("weightlbs")
    ax.set_ylabel("mpg")
    ax.set_title("mpg x weightlbs")
    st.pyplot(fig)
    
    fig, ax = plt.subplots(figsize=(10, 4))
    ax = sns.regplot(x='weightlbs', y="cubicinches", data=cond_US)
    ax.set_xlabel("weightlbs")
    ax.set_ylabel("cubicinches")
    ax.set_title("weightlbs x cubicinches")
    st.pyplot(fig)
    
    fig, ax = plt.subplots(figsize=(10, 4))
    ax = sns.regplot(x='weightlbs', y="hp", data=cond_US)
    ax.set_xlabel("weightlbs")
    ax.set_ylabel("hp")
    ax.set_title("weightlbs x hp")
    st.pyplot(fig)
    
elif add_selectbox == 'Japan':
    
    st.subheader('You selected Japan')
    cond_US=df_cars[df_cars['continent']==' Japan.']
    st.title('''Only analysed the distribution and correlation of the variables that showed some degree of correlation''')
    st.subheader('The analysis of the distribution of variables:')
    

    fig, axes = plt.subplots(2, 4, figsize=(18, 10))

    ax=sns.histplot(data=cond_US, x='mpg', ax=axes[0,0])
    ax.set_xlabel("mpg")
    ax.set_ylabel("count")
    ax.set_title("mpg")

    ax=sns.histplot(data=cond_US, x='cylinders', ax=axes[0,1])
    ax.set_xlabel("cylinders")
    ax.set_ylabel("count")
    ax.set_title("cylinders")
    
    ax=sns.histplot(data=cond_US, x='cubicinches', ax=axes[0,2])
    ax.set_xlabel("cubicinches")
    ax.set_ylabel("count")
    ax.set_title("cubicinches")
    
    ax=sns.histplot(data=cond_US, x='hp', ax=axes[0,3])
    ax.set_xlabel("hp")
    ax.set_ylabel("count")
    ax.set_title("hp")
    
    ax=sns.histplot(data=cond_US, x='weightlbs', ax=axes[1,0])
    ax.set_xlabel("weightlbs")
    ax.set_ylabel("count")
    ax.set_title("weightlbs")
    
    
    st.pyplot(fig)
    
    st.subheader('The analysis of the distribution of variables')

        
    fig, ax = plt.subplots(figsize=(10, 4))
    ax = sns.regplot(x='weightlbs', y="mpg", data=cond_US)
    ax.set_xlabel("weightlbs")
    ax.set_ylabel("mpg")
    ax.set_title("mpg x weightlbs")
    st.pyplot(fig)
    
    fig, ax = plt.subplots(figsize=(10, 4))
    ax = sns.regplot(x='weightlbs', y="cubicinches", data=cond_US)
    ax.set_xlabel("weightlbs")
    ax.set_ylabel("cubicinches")
    ax.set_title("weightlbs x cubicinches")
    st.pyplot(fig)
    
    fig, ax = plt.subplots(figsize=(10, 4))
    ax = sns.regplot(x='weightlbs', y="hp", data=cond_US)
    ax.set_xlabel("weightlbs")
    ax.set_ylabel("hp")
    ax.set_title("weightlbs x hp")
    st.pyplot(fig)