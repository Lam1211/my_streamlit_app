import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

st.title('Analyse du dataset de caractéristiques des voitures')

st.header("Présentation du dataset")

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_car = pd.read_csv(link)

df_car

st.header("Corrélation entre les variables")
viz_correlation = sns.heatmap(df_car.corr(), 
								center=0,annot=True, fmt=".1g",
								cmap = sns.color_palette("vlag", as_cmap=True),
                                linewidths=0.5, linecolor= 'black', vmax=1, vmin= -1
								)
st.pyplot(viz_correlation.figure)
st.write('Les variables cyclinder, cubicinches, hp et weightslbs sont positivement corrélées avec mpg.')
st.write('Les variables time-to-60 et hp sont positivement corrélées')
st.write('Les variables hp et weightlbs sont négativement corrélées avec cylinders et cubicinches')

st.header("Distribution des variables")
pays = st.radio('Veuillez choisir un continent pour filtrer', ('US', 'Japan', 'Europe'))
if pays == 'US':
    df_car = df_car[df_car['continent'] == ' US.']
elif pays == 'Japan':
    df_car = df_car[df_car['continent'] == ' Japan.']
else:
    df_car = df_car[df_car['continent'] == ' Europe.']

fig, axs = plt.subplots(3,2)
axs[0,0].hist(df_car['mpg'])
axs[0,0].set_title('Mpg')

axs[0,1].hist(df_car['cylinders'])
axs[0,1].set_title('Cylinders')

axs[1,0].hist(df_car['weightlbs'])
axs[1,0].set_title('weightlbs')

axs[1,1].hist(df_car['cubicinches'])
axs[1,1].set_title('Cubicinches')

axs[2,0].hist(df_car['hp'])
axs[2,0].set_title('Hp')

axs[2,1].hist(df_car['year'])
axs[2,1].set_title('Year')

st.pyplot(fig)

pays = ['US', 'Japan', 'Europe']
x = np.array([162, 51, 48])
fig1, ax1 = plt.subplots()
ax1.pie(x, labels = pays, autopct='%1.1f%%',startangle=0)
plt.title('Répartition des voitures par continent')
st.pyplot(fig1)





