import streamlit as st
from Source.loadDefElement import LoadComponent
from Source.loadType import LoadType
from Source import sapInit, sapLoadPattern, sapLoadCombination
import pandas as pd

st.header("Load Pattern Definition")
st.subheader("No excel sheets to import into SAP2000?")

# Instantiate the LoadTypeManager
load_manager = LoadComponent(LoadType().load_types_tuple)

# Display the full DataFrame
df = pd.DataFrame(load_manager.load_types_tuple, columns=['Load Type', 'Acronyms'])
st.dataframe(df)

# Generate and display the multi-select widget
options = load_manager.get_options()

# Define the default selection indices
default_indices = [0, 1, 2, 4, 5, 7, 9, 13]

selected_loads = st.multiselect(
    label="Select your load types:",
    options=options,
    default=[options[i] for i in default_indices]  # Set the default selection, if needed
)


slider_switch = st.toggle('Number slider')

load_manager.display_form(selected_loads, slider_switch)

button = st.button("SAP2000 Launch")

if button:
    Model = sapInit.SapInit(path='C:\CSiAPIexample', fileName='Example2',
                existing_file=False)


st.subheader("Want to start with SAP2000 load template?")

st.header("Load Case Definition")

