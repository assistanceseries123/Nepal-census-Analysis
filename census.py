import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
#loading the dataset
df=pd.read_csv('national_population and housing of nepal.csv')
st.set_page_config(layout='wide',page_title='Nepal census Analysis')

st.sidebar.title('Nepal Census Analysis')

def show_overallanalysis():
    #st.subheader('Total Population')
    st.subheader('Top 10 most populated district in Nepal')
    temp_df=df.groupby('District')['Total population'].sum().sort_values(ascending=False).head(10)
    fig=px.bar(temp_df,
    temp_df.index,
    temp_df.values,
    color='Total population')
    st.plotly_chart(fig,use_container_width=False)
    st.subheader('Top 10 most populated district with male population')
    st.text('You can view the full screen by clicking on the arrow cursor')
    temp_df1=df.groupby('District')['Total Male'].sum().sort_values(ascending=False).head(10)
    fig=px.bar(temp_df1,
    temp_df1.index,
    temp_df1.values,
    color='Total Male')
    st.plotly_chart(fig,use_container_width=False)
    st.subheader("Total Family number Districtwise")
    temp_df=df.groupby('District')['Total family number'].sum()
    fig2=px.bar(data_frame=temp_df,
    x=temp_df.index,
    y=temp_df.values,
    animation_frame='Total family number')
    st.plotly_chart(fig2,use_container_width=False)
    col1=st.columns(1)
    
def show_districtwiseanalysis():
    st.subheader("District wise Analysis")
    option1=st.selectbox('Select District',['Rupandehi','Palpa'])
    
    if option1=='Rupandehi':
        
        rupan=df[df['District']=='Rupandehi']
        rupan_=rupan.groupby(['District','Local Level Name'])['Total population'].sum().sort_values(ascending=False).reset_index()
        fig4=px.bar(rupan_,rupan_['Local Level Name'],
        y=rupan_['Total population'],
        color='Local Level Name',
        hover_name='District')
        st.plotly_chart(fig4,use_container_width=False)
        st.subheader("Total male population in the Rupandehi district")
        mpop=rupan['Total Male'].sum()
        st.metric("Male Population",mpop)
        st.subheader("Total Female population in the Rupandehi district")
        fpop=rupan['Total Female'].sum()
        st.metric("Female Population",fpop)
        st.subheader("Sex_Ratio of the rupandehi District")
        Sex_ratio=np.round((rupan['Total Female'].sum()/rupan['Total Male'].sum())*100,2)
        st.metric("Sex_Ratio",Sex_ratio)
    #if option1==Palpa:
    #    palpa=df[df['District']=='Palpa']
    #    palpa_=palpa.groupby(['District','Local Level Name'])['Total population'].sum().sort_values(ascending=False).reset_index()
    #    fig5=px.bar(palpa_,x=palpa_['Local Level Name'],y=palpa_['Total population'],color='Local Level Name',hover_name='District')
    #    st.plotly_chart(fig5,use_container_width=False)

def show_rural_municipalanalysis():
    st.header("Rural Municipality")
    temp_d=df[df['Local Level Name'].str.contains('Rural Municipality')]
    st.subheader("Total male population municipality wise")
    temp_df=temp_d.groupby(['Local Level Name'])['Total Male'].sum().sort_values(ascending=False)
    st.dataframe(temp_df)
    st.subheader("Total Female population municipality wise")
    temp_df=temp_d.groupby(['Local Level Name'])['Total Female'].sum().sort_values(ascending=False)
    st.dataframe(temp_df)
    col1,col2,col3,col4=st.columns(4)
    with col1:
        st.subheader("Top 10 most populated Rural municipality in Nepal")
        temp_df=temp_d.groupby(['Local Level Name'])['Total population'].sum().sort_values(ascending=False).head(10)

        fig1=px.bar(temp_df,
        x=temp_df.index,
        y=temp_df.values,
        hover_name='Total population')
        st.plotly_chart(fig1,use_container_width=False)
    with col2:
        st.subheader("Total male population in the Rural Municipality")
        mpop=temp_d['Total Male'].sum()
        st.metric('Male population',mpop)
    with col3:
        st.subheader("Total Female population in the Rural Municipality")
        fpop=temp_d['Total Female'].sum()
        st.metric("Female population",fpop)
    with col4:
        st.subheader("Total household number in the Rural municipality")
        hno=temp_d['Total household number'].sum()
        st.metric("Total Household number",hno)

def show_metropolitan_city():
    st.subheader("Sub-Metropolitan City polpulation")
    temp1_d=df[df['Local Level Name'].str.contains('Sub-Metropolitian City')]
    temp_=temp1_d.groupby(['District','Local Level Name'])['Total population'].sum().sort_values(ascending=False).reset_index()
    fig3=px.bar(temp_,
           x=temp_['District'],
           y=temp_['Total population'],
           hover_name='Local Level Name',
           color='Local Level Name')
    st.plotly_chart(fig3,use_container_width=False)
    st.subheader("Total household number in the submetropolitan city")
    hno=temp1_d['Total household number'].sum()
    st.metric('Household number',hno)
    st.subheader("Total male ppulation in the submetropoltan city")
    mpop=temp1_d['Total Male'].sum()
    st.metric("Male population",mpop)
    st.subheader("Total Female population in the submetropolitan city")
    fpop=temp1_d['Total Female'].sum()
    st.metric("Female population",fpop)

        
option=st.sidebar.selectbox('Select one',['Overall Analysis','Districtwise','Rural municipality','Metropolitan city'])

if option=='Overall Analysis':
    
    btn0=st.sidebar.button('showoverallanalysis')
    if btn0:
        show_overallanalysis()

if option=='Districtwise':
    #district=st.sidebar.selectbox('District',sorted(df['District'].unique().tolist()))
    btn1=st.sidebar.button("Show districtwise Analysis")
    if btn1:
        show_districtwiseanalysis()


if option=='Rural municipality':
    
    #rural_municipality=st.sidebar.selectbox('Rural municipality',sorted(temp_d['Local Level Name'].unique().tolist()))
    btn2=st.sidebar.button('show-rural-municipal-analysis')
    if btn2:
        show_rural_municipalanalysis()
if option=='Metropolitan city':
    btn3=st.sidebar.button('Show Metropolitan city')
    if btn3:
        show_metropolitan_city()

