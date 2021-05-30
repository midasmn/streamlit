from re import T
from numpy.random import f
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')
st.sidebar.write('DataFrame')

df = pd.DataFrame({
    '1列目':[1, 2, 3, 4],
    '2列目':[10, 20, 30, 40]
})
if st.sidebar.checkbox('データフレーム'):   
    st.write('データフレーム')
    st.dataframe(df.style.highlight_max(axis=0), width=500, height=500) #表

df2 = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)
if st.sidebar.checkbox('チャート'):   
    st.write('チャート')
    st.line_chart(df2) #折れ線グラフ
    st.area_chart(df2) #エリアチャート
    st.bar_chart(df2) #棒グラフ

df3 = pd.DataFrame(
    np.random.rand(100,2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)
if st.sidebar.checkbox('地図'):   
    st.write('地図')
    st.map(df3)


if st.sidebar.checkbox('マークダウン'):   
    st.write('マークダウン')
    """
    # 章
    ## 節
    ### 項

    ``` python
    import streamlit as st
    import numpy as np
    import pandas as pd
    ```
    """
st.sidebar.write('インタラクティブ')
    
if st.sidebar.checkbox('チェツクボックス'):
    st.write('チェツクボックス')
    img = Image.open('img/sample.jpg')
    st.image(img, caption='Sample画像', use_column_width=True)

if st.sidebar.checkbox('セレクトボックス'):
    st.write('セレクトボックス')
    option = st.selectbox(
        'あなたがすきな数字を教えてください',
        list(range(1, 11))
    )
    'あなたの好きな数字は、', option, 'です。'

if st.sidebar.checkbox('テキストインプット'):
    st.write('テキストインプット')
    text = st.text_input('あなたの趣味を教えてください')
    'あなたの趣味は', text, 'です'

if st.sidebar.checkbox('コンディション'):
    st.write('コンディション')
    condition = st.slider('あなたのコンディションは？', 0, 100, 50)
    'コンディション：', condition

if st.sidebar.checkbox('2カラム表示'):
    st.write('2カラム表示')
    left_colum, right_colum = st.beta_columns(2)
    button = left_colum.button('右カラムに文字を表示')
    if button:
        right_colum.write('ここは右カラム')

if st.sidebar.checkbox('エキスパンダー'):
    st.write('エキスパンダー')
    expander1 = st.beta_expander('お問い合わせ1')
    expander1.write('お問い合わせ1の回答')
    expander2 = st.beta_expander('お問い合わせ2')
    expander2.write('お問い合わせ2の回答')
    # 

if st.sidebar.checkbox('プログレスバー'):
    st.write('プログレスバー')

    latest_iteration = st.empty() #プログレスバー用意
    bar = st.progress(0) #バーの値
    for i in range(100):
        latest_iteration.text(f'Iteration {i+1}')
        bar.progress(i+1)
        time.sleep(0.1)
    'Done!!!!!'









