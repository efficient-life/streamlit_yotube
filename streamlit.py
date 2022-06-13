import imp
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title("streamlit テスト")

st.write('ブログレスバーの表示')

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.01)


expander1 = st.beta_expander('問い合わせ1')
expander1.write('問い合わせ1の回答')
expander2 = st.beta_expander('問い合わせ2')
expander2.write('問い合わせ2の回答')




letf_column, right_column = st.beta_columns(2)
button = letf_column.button('右カラムに文字を表示')
if button:
    right_column.write('右カラムです')


conditon = st.slider('あなたの今の調子は',0,100,50)
'コンディション:',conditon


option2 = st.text_input('あなたの趣味を教えてください')
'あなたの趣味は',option2,'です'

if st.checkbox('Show Image'):
    st.write('display image')
    img = Image.open('kyouto.JPG')
    st.image(img, caption='smart phone', use_column_width=True)

option = st.selectbox(
    'あなたが好きな数字を教えて下さい',
    list(range(1,11))
)
'あなたの好きな数字は',option,'です'







st.write('DateFrame')



df = pd.DataFrame(
    np.random.rand(100, 2)/[50,50]+[35.69,139.70],
    columns=['lat','lon']
)

# st.line_chart(df)
# st.area_chart(df)
# st.bar_chart(df)

st.map(df)

st.write(df)

st.table(df.style.highlight_max(axis=0))

"""
#章
##節
"""