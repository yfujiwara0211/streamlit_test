"""- 楽天トラベルのデータ
    - 取得したデータをPandasで読み込む
- グラフ化
    - Plotlyで読む
- ダッシュボード化
    - フロントに出して、インタラクティブにする
    - 変数がさわれるようにする
- 簡単なデプロイ？
    - Streamlit cloudにデプロイ"""

import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Step2-課題')
st.write('Interactive Widgets') # ウィジェットの表示

df = pd.read_csv('machine_learning.csv', encoding='cp932')

st.write(df)
st.line_chart(df['reviewCount']) # 折れ線グラフの表示

text = st.sidebar.text_input('あなたの好きな本を教えてください。') # テキスト入力
'あなたの好きな本は', text, 'です。' # テキスト表示

condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50) # スライダー
'コンディション：', condition # テキスト表示