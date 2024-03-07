from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import pandas as pd
import numpy as np
from responseSpectrum import ResponseSpectrum
import plotly.express as px
import plotly.graph_objects as go
from custom import CustomPlot
from io import BytesIO
from googletrans import Translator, LANGUAGES

st.title("Skills")

tab1, tab2, tab3, tab4 = st.tabs(["Pile Buckling", "Response Spectrum", "Section Design", "Extract tables from Pdf"])
with tab1:
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

with tab2:
    option = st.selectbox("Which code are you referring?",
                          ("Eurocode3", "California Building Code"),
                          index=0,
                          placeholder="Select the reference code...",
                          )
    st.write("You selected:", option)
    st.write("What's the soil type?")
    option2 = st.selectbox("Soil type?",
                          ("A", "B", "C", "D", "E"),
                          index=0,
                          placeholder="Select the soil type...",
                          )

    st.header("Response Spectrum")

    from Tables import BS_EN_1998_1
    # Either in table format or HTML 
    st.table(BS_EN_1998_1.Tables().type1)
    # st.write(BS_EN_1998_1.Tables().type1.to_html(), unsafe_allow_html=True)

    
    rs = ResponseSpectrum(code=option, soilType=option2, ag=0.25, step=0.01)

    fig = CustomPlot.FormatPlot("Elastic Spectral",
               'Period T (s)',
               'Acceleration (g)')
    fig.add_scatter(x=rs.T, y=rs.Sa, name="Acceleration")
    fig.add_scatter(x=rs.T, y=rs.Sv, name="Velocity")
    fig.add_scatter(x=rs.T, y=rs.Sd, name="Displacement")

    fig2 = CustomPlot.FormatPlot("Displacement vs. Acceleration",
               'Displacement, Sd',
               'Acceleration, Sa')
    fig2.add_scatter(x=rs.Sd, y=rs.Sa, name="Disp-Acc")

    if option or option2 is None:
        st.plotly_chart(fig, use_container_width=True)
        st.plotly_chart(fig2, use_container_width=True)
    # fig2 = go.Figure(
    #     data = [go.Scatter(x=rs.T, y=rs.Sd)],
    #     layout=go.Layout(
    #         title=go.layout.Title(text="Elastic Spectra - Displacement")
    #         )
    # )
    # if option or option2 is None:
    #     st.warning('Both code and soil information should be selected.')
    # else:
    # st.plotly_chart(fig2, use_container_width=True)
    #from responseSpectrum import ResponseSpectrum

with tab3:
    st.header("Configurations")
    from tab3 import sections

    option = st.selectbox("Define Sections",
                          ("Rectangular", "Pipe", "H Beam", "Angled"),
                          index=0,
                          placeholder="Select the section...",
                          )
    if option == "Rectangular":
        section = sections.Rectangle(B=200, d=100, tw=10, tf=10)
    elif option == "Pipe":
        section = sections.Pipe(d=5, t=0.3)
    elif option == "H Beam":
        section = sections.Hbeam(d=300, B=150, tw=10, tf=20, R=0, h=260, b=130, n=0, Lmajor=5000, Lminor=3000, Kmajor=1.0, Kminor=1.0)
    else:
        section = sections.Angled(b=4, d=4, t=0.5)
    st.plotly_chart(section.fig, use_container_width=True)

    st.header("Stress Calculations")

    st.subheader("Bending")
    st.table()

    st.subheader("Compression")
    st.table()

    st.subheader("Tension")
    st.table()

    st.subheader("Shear")
    st.table()

    st.subheader("Combined - Bending & Axial Forces")
    st.table()

    
with tab4:
    st.header("PDF File Upload")
    file_upload = st.file_uploader(label="Choose a PDF file")


