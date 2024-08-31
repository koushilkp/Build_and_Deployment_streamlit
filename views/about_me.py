import streamlit as st
from form.contact import contact_form

@st.experimental_dialog("Contact_me")
def show_contact_form():
    contact_form()
    

# Hero Selection
col1,col2=st.columns(2,gap='small',vertical_alignment='center')
with col1:
    st.image(r'E:\Project\Build and Deploy streamlit\1692449950391-modified.png',width=230)

with col2:
    st.title('Koushil Prajapati',anchor=False)
    st.write('Data Scientist | Machine Learning Engineer | Gen-AI Engineer')

    if st.button('📧 Connect Me'):
        show_contact_form()

# --Experience and Qualification
st.write("\n")
st.subheader('Experience and Qualification',anchor=False)
st.write(
    """
    -Luthra Group LLP | Data Scientist, Surat \n
    -1 Years | July 2023 to Present Date \n
    -Project 1: Provide Dashboard for financial & Cost sheet from SAP HANA \n
    -Descriptions: Due to strategic moves from other competitors and ineffective- making in management. The Grand are losing its market share and revenue in business hotel Category. they wanted to incorporate” Business and Data intelligence” to region their market share and revenue. \n
    Responsibility: \n
    -Create the metric for the YoY client Consistency in Venn Diagram \n
    -Power BI Dashboard according to the mockup provided by shareholder \n
    -Taking the Budget KPI of the plant wise and input Active/Inactive Client Compare Budget year to Actual Year Qty rate \n
    -SAP HANA Data Integration and Store in SQL data base using Store Procedure Run Daily Data ETL Weekly Monthly and YTD and Production and breakdown, become easy to monitor and set the benchmark and budget too \n
    -This, we also have the Cost Sheet bifurcation, and creating KPI and Metric thought this help the management take req Action and also it helps to actionable Plan with PM, PP, FICO. All this Plan was integrated in Power BI and SQL Database \n
    """
)

# --skill--
st.write("\n")
st.subheader('Project skill',anchor=False)
st.write(
        """
    -Python Packages-NumPy, Pandas, SciPy, Scikit-learn, Seaborn, OCR, Matplotlib \n
    -Machine learning- Linear Regression, Logistic Regression, K-Nearest Neighbour’s Classifier, Support Vector Machine, Decision Tree, Random Forest, Ada-Boost, XGBoost, K-means Clustering, Features Engineering, Features Selection, Hypothesis Test \n
    -NLP  Tokenization, Data cleaning, Count Vectorization, TF-IDF, RAKE, YAKE \n
    Word cloud, N-gram, Vector Embedding ,Cosine Similarity , RAG \n
    """
    )
