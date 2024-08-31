import streamlit as st

# --page setup--
about_page = st.Page(
    page="views/about_me.py",
    title="About me",
    icon="🧑‍💻",
    default=True
)

project_1_page = st.Page(
    page="views/salesdashboard.py",
    title="Sales Dashboard",
    icon="📊"
)

project_2_page = st.Page(
    page="views/chat_bot.py",
    title="chat bot",
    icon="🤖"
)

project_image = st.Page(
    page="views/img_to_text.py",
    title="Img_to_text",
    icon="🧐"
)

# Navigation steup
pg = st.navigation(
    {
        "info"      :[about_page],
        "Project"   :[project_1_page, project_2_page,project_image]
    }
)
# run Navigation
pg.run()