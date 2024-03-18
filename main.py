import streamlit as st
import pandas as pd
import numpy as np

import plotly.express as px
import plotly.graph_objects as go

from io import BytesIO

# ------------------ Page config ---------------------------
st.set_page_config(page_title="Civil engineering skills stacked", page_icon=":Hamburger:")

st.title("Skills")

with st.sidebar:
    st.image("maritime logo.webp")
    st.write("""Structure design with advanced skills in Rhinoceros3D, Grasshopper, and coding in Python, JavaScript, C#, VBA, 
             fostering innovative, sustainable maritime solutions through continuous learning and technology adoption.
             """)
    


    
tab_list = ["Pile Buckling", "Response Spectrum", "Section Design", "Extract tables from Pdf", "SAP2000 Modeling Automation"]

tab1, tab2, tab3, tab4, tab5 = st.tabs(tab_list)

with tab1:
    from Tabs.tab1 import Tab1

    Tab1()

with tab2:
    from Tabs.tab2 import Tab2

    Tab2()

with tab3:
    from Tabs.tab3 import Tab3

    Tab3()
    
with tab4:
    from Tabs.tab4 import Tab4

    Tab4()

with tab5:
    from Tabs.tab5 import Tab5

    Tab5()
    
