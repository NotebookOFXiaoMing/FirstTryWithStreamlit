import streamlit as st
import pandas as pd
from PIL import Image




st.write('''
# MingYan
### *Resume*
''')

col1, col2, col3 = st.columns([1,6,1])

with col1:
    st.write("")

with col2:
    image = Image.open('img/MingYan.jpg')
    st.image(image,width=400)

with col3:
    st.write("")

st.markdown('## Summary')
st.info('''
- enthusiast of data visualization using R package ggplot2
''')

st.markdown('''
# Education
''')

col1,col2 = st.columns([4,1])

with col1:
    st.markdown('**Phd candidate** (Pomology), *Nanjing Forestry University*, China')
with col2:
    st.markdown('2016.09---present')

st.markdown('''
- Research thesis entitled `ABC`
''')

col1,col2 = st.columns([4,1])

with col1:
    st.markdown('**Bachelor of Science in Forestry**, *Northwest A&F University*, Shanxi, China')
with col2:
    st.markdown('2012.09---2016.06')

st.markdown('''
- GPA 3
''')

st.markdown('''
# Publication
''')

image2019 = Image.open("img/publication/yan2019complete.html.png")
st.image(image2019,width=800)
