import numpy as np
import pandas as pd
import plotly.express as px
import plotly.io as pio
import streamlit as st

st.text("Hello World!")

code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')

df = pd.DataFrame(np.random.randn(50, 20), columns=('col %d' % i for i in range(20)))

st.dataframe(df)
