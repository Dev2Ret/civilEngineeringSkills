import streamlit as st
import pandas as pd

class LoadComponent:
    def __init__(self, tup):
        self.load_types_tuple = tup

    def get_options(self):
        """Generate options for the Streamlit multi-select widget."""
        return [f"{full_term}: {abbreviation}" for full_term, abbreviation in self.load_types_tuple]
    
    def get_selected_loads_df(self, selected_options):
        """Create a DataFrame from the selected options."""
        selected_data = [option.split(": ") for option in selected_options]
        return pd.DataFrame(selected_data, columns=['Load Type', 'Acronym'])
    
    def display_form(self, selected_loads, switch=None):
        """Display the form for load pattern definition."""
        with st.form("Load Pattern Definition"):
            header = st.columns([1, 2])
            header[0].subheader('Load type')
            header[1].subheader('The number of according types')
            
            num_dict = {}
            # Update the form with selected load types
            if selected_loads:
                selected_df = self.get_selected_loads_df(selected_loads)
                for index, row in selected_df.iterrows():
                    cols = st.columns([1, 2])
                    cols[0].write(row['Load Type'])
                    if switch:
                        number = cols[1].slider(f"Number for {row['Load Type']}:", 0, 30, key=f"slider_{row['Load Type']}")
                    else:
                        number = cols[1].number_input(f"Number for {row['Load Type']}:", min_value=0, key=f"number_{row['Load Type']}")
                    num_dict[row['Load Type']] = number

            # Submit button for the form
            submitted = st.form_submit_button("Submit")
            if submitted:
                # Create a DataFrame with load types as columns and load names as rows
                max_count = max(num_dict.values())
                data = {load_type: [f"{load_type} {i+1}" for i in range(count)] + [''] * (max_count - count) for load_type, count in num_dict.items()}
                load_names_df = pd.DataFrame(data)

                st.success(f"{sum(num_dict.values())} patterns were generated!")

                # Display the DataFrame
                st.dataframe(load_names_df, height=300)
            # num = []
            # load_types = []
            # # Update the form with selected load types
            # if selected_loads:
            #     selected_df = self.get_selected_loads_df(selected_loads)
            #     for index, row in selected_df.iterrows():
            #         cols = st.columns([1, 2])
            #         cols[0].write(row['Load Type'])
            #         if switch:
            #             number = cols[1].slider(f"Number for {row['Load Type']}:", 0, 30)
            #         else:
            #             # Assuming you want to input a number for each load type
            #             number = cols[1].number_input(f"Number for {row['Load Type']}:", min_value=0, key=row['Load Type'])
            #         num.append(number)
            #         load_types.append(row['Load Type'])

            # # Submit button for the form
            # submitted = st.form_submit_button("Submit")
            # if submitted:
            #     total_patterns = sum(num)
            #     st.success(f"{total_patterns} patterns were generated!")
                
            #     # Create a DataFrame to hold all load names
            #     load_name_data = []
            #     for load_type, count in zip(load_types, num):
            #         for i in range(count):
            #             load_name_data.append([load_type, f"{load_type} {i+1}"])
            #     load_names_df = pd.DataFrame(load_name_data, columns=['Load Type', 'Load Name'])

            #     # Display the DataFrame
            #     st.dataframe(load_names_df.assign(hack='').set_index('hack'), height=300)  # A workaround to show the DataFrame without the index