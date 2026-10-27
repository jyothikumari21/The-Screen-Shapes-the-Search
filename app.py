"""Interactive human-centred clickstream story: run with streamlit run app.py."""
import pandas as pd
import plotly.express as px
import streamlit as st
from src.data import load_data
from src.analysis import position_summary, session_clicks

st.set_page_config(page_title='The Screen Shapes the Search',page_icon='🛍️',layout='wide')
st.title('The Screen Shapes the Search')
st.caption('What a shopper experiences, what a clickstream records — and what remains unknown.')

@st.cache_data(show_spinner='Loading the original UCI dataset…')
def get_data():
    return load_data()

try:
    df = get_data()
except Exception as exc:
    st.error(f'Could not load the authentic UCI data: {exc}')
    st.markdown('[Get the original UCI dataset](https://archive.ics.uci.edu/dataset/553/clickstream+data+for+online+shopping)')
    st.stop()

st.markdown('## 1 · Meet Maya')
st.write('Maya is a fictional storytelling character, based on an anonymous six-click session in a historical clothing-store dataset. We know which products were clicked, but cannot know what she thought, saw without clicking, or bought.')
selected_id = st.number_input('Explore session ID', min_value=1, value=18817, step=1)
session = session_clicks(df, selected_id)
if session.empty:
    st.warning('No recorded clicks for this session ID.')
else:
    st.metric('Clicks in this session',len(session))
    st.dataframe(session[['order','page_1_main_category','page_2_clothing_model','colour','position_name','price','page']],hide_index=True,use_container_width=True)
    st.caption('Each row is a recorded click; these are not all the products displayed.')

st.markdown('## 2 · Two views of one interaction')
left,right=st.columns(2)
with left:
    st.subheader('What the shopper encounters')
    st.write('A page of product images, colours and prices. The original interface and all unseen products are not captured in these records.')
with right:
    st.subheader('What the data retains')
    st.write('An anonymous session ID, click order, product and category codes, a six-part screen position, and a recorded price.')

st.markdown('## 3 · Zoom out to all recorded clicks')
months = sorted(df['month'].dropna().astype(int).unique().tolist())
chosen_months = st.multiselect('Month (2008)',months,default=months)
filtered=df[df['month'].isin(chosen_months)]
categories=sorted(filtered['page_1_main_category'].dropna().unique().tolist())
chosen_categories=st.multiselect('Product category code',categories,default=categories)
filtered=filtered[filtered['page_1_main_category'].isin(chosen_categories)]
summary=position_summary(filtered)
a,b=st.columns(2)
with a:
    st.metric('Recorded clicks (filtered)',f'{len(filtered):,}')
    st.metric('Distinct session IDs (filtered)',f'{filtered.session_id.nunique():,}')
with b:
    st.plotly_chart(px.bar(summary,x='position',y='clicks',title='Clicked products by recorded screen position',labels={'clicks':'Recorded clicks','position':'Position'}),use_container_width=True)

st.subheader('Six-position click-share map')
arr=summary['share_pct'].to_numpy().reshape(2,3)
heat=pd.DataFrame(arr,index=['Top','Bottom'],columns=['Left','Middle','Right'])
st.plotly_chart(px.imshow(heat,text_auto='.1f',aspect='auto',labels={'color':'% of clicks'},title='Percentage of recorded clicks, NOT click-through rate'),use_container_width=True)
st.dataframe(summary,use_container_width=True,hide_index=True)

st.markdown('## 4 · Return to the human question')
st.write('If more clicked products appear in certain positions, is it because of placement, inventory, visibility or something else? We cannot distinguish those explanations with click-only data. A follow-up UX study should measure product impressions, page layout and clicks together.')
st.info('Interpretation guardrail: observed click share is not a click-through rate, attention measure, purchase rate, or causal placement effect.')
st.caption('Source: UCI Clickstream Data for Online Shopping (2008 activity; UCI release 2019), DOI: 10.24432/C5QK7X. CC BY 4.0. Story concept: Jyothi Kumari.')
