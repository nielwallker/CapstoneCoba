import streamlit as st
from streamlit_option_menu import option_menu

import home, history, about, setting

st.set_page_config(
    page_title="Quality Control", layout="wide"
)
# Customize the sidebar
markdown = """
Web App URL: <https://capstoneproject37.streamlit.app/>
GitHub Repository: <https://github.com/TaufiiquRahman/CapstoneProject37>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/JFyI8Fl.jpeg"
st.sidebar.image(logo)

# Customize page title
st.markdown(
    """
    Quality Control (QC) Casting Production merupakan elemen penting dalam proses manufaktur, memastikan produk yang dihasilkan memenuhi standar kualitas yang ditetapkan. 
    """
)

st.header("Instructions")

markdown = """
1. Masuk halaman home
2. Maka akan ada tampilan drag file or choose file
3. Drag file atau pilih file yang ingin diupload
4. Klik tombol upload file
5. Maka akan muncul tampilan data yang telah diupload

"""
st.markdown(markdown)
st.image(logo)

class MultiApp:

    def _init_(self):
       self.apps = []
    def add_app(self,title, function):
        self.apps.append({
            "title": title,
            "function": function
        })

    def run():

        with st.sidebar:
            app_mode = option_menu(
                menu_title='Manager',
                options=['Home', 'History', 'About', 'Setting', 'Exit'],
                icons=['house', 'clock', 'info-circle', 'gear', 'door-open'],
                menu_icon="cast",
                default_index=1,
                #styles={"container": {"padding": "5!important", "background-color": "gray"},"icon": {"color": "white", "font-size": "25px"}, "nav-link":{"color": "white","font-size":"20px", "text-align":"left", "margin":"0px"},"nav-link-selected": {"background-color": "#02ab21"},}
            )

        if app== 'Home':
            home.app()
        if app== 'History':
            home.app()
        if app== 'About':
            home.app()
        if app== 'Setting':
            home.app()
    run()