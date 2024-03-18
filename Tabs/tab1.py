import streamlit as st
import pandas as pd
import numpy as np

class Tab1:
    def __init__(self):
        st.header("Parameters")

        st.code("""
        class Pile:
            '''
            All the units in mm, MPa.
            External corrosion can be considered.
            Forces in units of kN, kN-m.
            '''
            def __init__(self, d, t, P=None, M=None, L=None, dep_c=None):
        """)
        st.button("Click", type="primary")
        st.header("Calculated Parameters")
        df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))
        st.dataframe(df)