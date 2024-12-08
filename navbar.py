import streamlit as st

# CSS for sticky container
st.markdown(
    """
    <style>
    /* Style for the sticky container */
    .sticky-container {
        position: -webkit-sticky; /* For Safari */
        position: sticky;
        top: 0;
        background-color: #f4f4f4;
        padding: 10px;
        z-index: 1000; /* Ensures it stays on top of other elements */
        margin-bottom: 20px; /* Add space between sticky container and content below */
    }

    /* Make sure the body content doesn't overlap the sticky container */
    body {
        padding-top: 70px;  /* Adjust according to the height of your container */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Create a sticky container
with st.container():
    st.markdown('<div class="sticky-container">', unsafe_allow_html=True)
    st.header("This is a sticky container")
    st.write("This container will stick to the top of the page as you scroll down.")
    st.markdown('</div>', unsafe_allow_html=True)

# Add content below to test the sticky behavior
st.write("Scroll down to see how the container remains at the top.")
st.write("More content...")
for _ in range(50):
    st.write("More content to scroll...")
