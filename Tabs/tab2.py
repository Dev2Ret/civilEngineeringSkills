import streamlit as st
from responseSpectrum import ResponseSpectrum
from custom import CustomPlot

class Tab2:
    def __init__(self):
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