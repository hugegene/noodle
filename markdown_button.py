import streamlit as st

# Embedding HTML with JavaScript
html_code = """
    <html>
    <body>
        <a href="#" id="clickLink">Click me to trigger event</a>
        <script>
            document.getElementById("clickLink").addEventListener("click", function(event) {
                event.preventDefault();
                alert('Link clicked!');
            });
        </script>
    </body>
    </html>
"""

st.markdown(html_code, unsafe_allow_html=True)