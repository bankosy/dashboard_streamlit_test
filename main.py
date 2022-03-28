import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title("Streamlit超入門")



#"""
## 章
### 節
#### 項

#```python
#import streamlit as st
#import numpy as np
#import pandas as pd
#from PIL import Image
#```
#"""

# データ表
#st.write("DataFrame")
#df = pd.DataFrame({
#    '1列目':[1, 2, 3, 4],
#    '2列目':[10, 20, 30, 40]
#})
#st.dataframe(df.style.highlight_max(axis=0))


# データをマッピング
#df = pd.DataFrame(
#    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#    columns=['lat','lon']
#)
#st.map(df)

#st.write("DisplayImage")

# 画像を表示
#img = Image.open('スライド192.PNG')
#st.image(img, caption = 'test', use_column_width = True)

# 画像を表示（チェックボックス）
#if st.checkbox('Show Image'):
#    st.image(img, caption = 'test', use_column_width = True)

# セレクトボックス
#option = st.selectbox(
#    'あなたが好きな数字を教えてください。', list(range(1,11))
#)
#'あなたが好きな数字は、',option,'です。'

# テキスト入力
#text = st.text_input('あなたの趣味を教えて下さい。')
#'あなたの趣味：',text

# スライダー
#condition = st.slider('あなたの今の調子は？', 0, 100, 50)


# interactive widget
#st.sidebar.write('Interactive Widgets')
#text = st.sidebar.text_input('あなたの今の調子は？', 0, 100, 50)
#condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)

# Please replace st.beta_columns with st.columns.
# st.beta_columns will be removed after 2021-11-02.　変わったらしい。
#left_column, right_column = st.columns(2)
#button = left_column.button('右カラムに文字を表示')
#if button:
#    right_column.write('ここは右カラム')

# Please replace st.beta_expander with st.expander.
# st.beta_expander will be removed after 2021-11-02.　変わったらしい。
#expander1 = st.expander('問合せ1')
#expander1.write('問合せ内容をかく1')
#expander2 = st.expander('問合せ2')
#expander2.write('問合せ内容をかく2')
#expander3 = st.expander('問合せ3')
#expander3.write('問合せ内容をかく3')

# プログレスバー
st.write('プログレスバーの表示')
'Start!!!'
latest_iteration = st.empty()
bar = st.progress(0)
#for i in range(1,11):
for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)
'Done!'


