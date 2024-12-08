# import streamlit as st

# options = ["North", "East", "South", "West"]
# st.markdown("### Directions")

# # Create a list of checkboxes for each option
# selection = [option for option in options if st.checkbox(option)]

# st.markdown(f"Your selected options: {', '.join(selection) if selection else 'None'}.")


# import streamlit as st

# options = ["North", "East", "South", "West"]
# selection = st.pills("Directions", options, selection_mode="multi")
# st.markdown(f"Your selected options: {selection}.")


import streamlit as st

# Define a unique key for the button to track state
if "checkbox_selected" not in st.session_state:
    st.session_state.checkbox_selected = False

# Custom CSS for the styled "checkbox"
st.markdown("""
    <style>
    .custom-checkbox {
        width: 100px;
        height: 50px;
        display: flex;
        align-items: center;
        justify-content: center;
        border: 2px solid #ddd;
        border-radius: 10px;
        background-color: #f0f0f0;
        color: #333;
        cursor: pointer;
        font-weight: bold;
        transition: background-color 0.3s ease, color 0.3s ease;
    }
    .custom-checkbox.selected {
        background-color: #4CAF50; /* Green color when selected */
        color: white;
    }
    </style>
    """)

# Create a custom checkbox
is_selected = st.session_state.checkbox_selected

button_class = "custom-checkbox selected" if is_selected else "custom-checkbox"
if st.button(f'<div class="{button_class}">{"Selected" if is_selected else "Click Me"}</div>'):
    # Toggle selection state
    st.session_state.checkbox_selected = not st.session_state.checkbox_selected

# Example usage of the checkbox state
if st.session_state.checkbox_selected:
    st.info("Checkbox is selected!")
else:
    st.text("Checkbox is not selected.")
