import streamlit as st
import pandas as pd
import plotly.express as pl
import matplotlib.pyplot as plt

# first find a average for global sales
st.title('Statistics For Games')
the_df = pd.read_csv('vgsales.csv')
total_games = the_df.shape[0]
global_sales = the_df['Global_Sales'].sum()
eu_sales = round(the_df['EU_Sales'].sum(),2)



col1,col2,col3 = st.columns(3)
col1.metric('Total Games',total_games)
col2.metric('EU Sales',eu_sales)
col3.metric('Global Sales',global_sales)
# top 10 ranked games
st.text(" ")
st.text(" ")
st.text(" ")
st.text(" ")
st.text(" ")

st.subheader('Games Review')



col1,col2 = st.columns(2)


with col1:
    st.header('Top 10 Ranked Games')
    top_ranked = the_df['Name'].value_counts().head(10) # value counts takes the
    st.bar_chart(top_ranked)

with col2:
    st.header('Top 10 Games With The Most Sales')
    top_sales = the_df.groupby('Name')['Global_Sales'].sum().head(10)
    ordering = top_sales.sort_values(ascending=False)
    st.bar_chart(ordering)

# vertical padding
st.text(" ")
st.text(" ")
st.text(" ")
st.text(" ")
st.text(" ")
st.text(" ")

st.subheader('Genres & Publishers')
colon,colona2 = st.columns(2)
colors_sequence = ['#07013d','#054752','#ffd9d0','#282b2b','#170062']
colors_sequence2 = ['#07013d','#054752']

with colon:
    take_most = the_df['Genre'].value_counts().head(5)
    take_most_df = take_most.reset_index()
    take_most_df.columns = ['Genre','Count']
    fig = pl.pie(take_most_df,names='Genre',values='Count',title='Top 5 Genres',color='Genre',color_discrete_sequence=colors_sequence)
    st.plotly_chart(fig)
    st.text("")

with colona2:
    the_df_instead = the_df['Publisher'].value_counts().head(2)
    the_df_instead_indexing = the_df_instead.reset_index() # converts series into data frame
    # and in the previous series in the_df_instead the publishers name was the index
    # so now reseting it the index of the series becomes an column in the data frame
    the_df_instead_indexing.columns = ['Publisher','Count']
    figura = pl.pie(the_df_instead_indexing,names='Publisher',values='Count',title='Top 2 Publishers',color='Publisher',color_discrete_sequence=colors_sequence2)
    st.plotly_chart(figura)

# find the neweest game
st.subheader('Top 5 Latest Games')
kolona1,kolona2 = st.columns(2)

with kolona1:
    newest_game = the_df.sort_values(by='Year', ascending=False)

    the_top_5 = newest_game.drop_duplicates(subset='Year').head(5)

    datat = {
        'Name':[name for name in the_top_5['Name']],
        'Year':[year for year in the_top_5['Year']]
    }

    into_data_frames = pd.DataFrame(datat)
    st.bar_chart(into_data_frames)





