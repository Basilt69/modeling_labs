import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from st_aggrid import AgGrid

def main():
    st.markdown("### Lab 1 - Engineering of polynomial interpolation of tabular functions")
    st.markdown("Purpose - Developing of skills in engineering og algorithms for interpolation of tabular functions by "
                "the Newton "
                "and Hermite polynomial")

    x_arr = [0.00, 0.15, 0.30, 0.45, 0.60, 0.75, 0.90, 1.05]
    y_arr = [1.000000, 0.838771, 0.655336, 0.450447, 0.225336, -0.018310, -0.278390, -0.552430]
    y_div_arr = [-1.000000, -1.14944, -1.29552, -1.43497, -1.56464, -1.68164, -1.78333, -1.86742]

    df = pd.DataFrame({
        "x" : x_arr,
        "y" : y_arr,
        "y'" : y_div_arr
    })


    st.subheader("Table of the function with N nodes:")
    grid_return = AgGrid(
        df,
        editable=True,
        height=300,
        reload_data=False,
        theme="bright",
    )
    arr = grid_return["data"].to_numpy()



