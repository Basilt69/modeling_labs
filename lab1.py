import streamlit as st
import pandas as pd
import numpy as np

# Cache dataframe so it's only loaded once
@st.experimental_memo
def load_data():
    return pd.DataFrame(
        {
            "x" : [0.00, 0.15, 0.30, 0.45, 0.60, 0.75, 0.90, 1.05],
            "y" : [1.000000, 0.838771, 0.655336, 0.450447, 0.225336, -0.018310, -0.278390, -0.552430],
            "y'" : [-1.000000, -1.14944, -1.29552, -1.43497, -1.56464, -1.68164, -1.78333, -1.86742]
        }
    )

# Boolean to resize the dataframe, stired as a session state variable
st.checkbox("Use container width", value=False, key="use_container_width")

df = load_data()

# Display the datdframe and allow the user to stretch the dataframe
#