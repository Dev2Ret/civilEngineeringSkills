import streamlit as st


class Tab3:
    def __init__(self):
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