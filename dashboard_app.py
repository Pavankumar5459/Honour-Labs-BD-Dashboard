
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Honour Labs BD Dashboard", page_icon="📊", layout="wide")

# ---- Premium Theme ----
st.markdown("""
<style>
.main {background-color:#F4F6F8;}
.block-container {padding-top:2rem;}
h1,h2,h3,h4 {color:#003262;}
.bd-card {
 background:#ffffff; padding:1rem 1.25rem; border-radius:12px;
 box-shadow:0 2px 8px rgba(0,0,0,0.07); margin-bottom:1rem;
 border-left:4px solid #DAA520;
}
</style>
""", unsafe_allow_html=True)

# ---- Sidebar Navigation ----
st.sidebar.title("📘 Navigation")
page = st.sidebar.selectbox(
    "Select a Section:",
    [
        "What is a CDMO?",
        "Home",
        "Market Landscape",
        "Prospecting & Leads",
        "Capability Alignment",
        "Financial Opportunity",
        "About Honour Labs"
    ]
)

# ---- Pages ----

if page == "What is a CDMO?":
    st.title("📘 What is a CDMO?")
    st.markdown("<div class='bd-card'>A CDMO provides outsourced development, scale-up, and API manufacturing.</div>", unsafe_allow_html=True)

    st.subheader("Why CDMOs Are Important")
    st.write("""- Reduce cost & time  
- Provide chemistry expertise  
- Support virtual biotech  
- Enable global supply  
""")

    st.subheader("CDMO Market Growth (Illustrative)")
    df = pd.DataFrame({"Year":[2020,2022,2024,2026,2028], "Market ($B)":[80,95,115,135,160]}).set_index("Year")
    st.line_chart(df)

elif page == "Home":
    st.title("🏠 Home – BD Intelligence Dashboard")
    st.markdown("<div class='bd-card'>Welcome to the Honour Labs strategic dashboard.</div>", unsafe_allow_html=True)
    st.write("Use the left sidebar to continue.")

elif page == "Market Landscape":
    st.title("🌎 Market Landscape")
    df = pd.DataFrame({
        "Company":["Honour Labs","Lonza","Catalent","Wuxi","Thermo Fisher"],
        "Breadth":[3,5,5,5,5],
        "Agility":[5,3,3,3,3]
    })
    st.subheader("CDMO Comparison")
    st.dataframe(df)

elif page == "Prospecting & Leads":
    st.title("🎯 Prospecting & Leads")
    df = pd.DataFrame({
        "Company":["BioGenix","OncoThera","CardioNova","NeuroBridge","Immunexa"],
        "Stage":["Phase II","Phase I","Phase III","Preclinical","Phase II"],
        "Fit":[88,80,92,75,85]
    })
    st.dataframe(df)
    st.bar_chart(df["Stage"].value_counts())

elif page == "Capability Alignment":
    st.title("🧪 Capability Alignment")
    df = pd.DataFrame({
        "Capability":["Route Dev","Scale-up","GMP API","Analytical","CMC Docs"],
        "Strength":[5,4,4,4,3],
        "Relevance":[5,4,5,4,4]
    })
    st.dataframe(df)

elif page == "Financial Opportunity":
    st.title("💰 Financial Opportunity")
    df = pd.DataFrame({
        "Company":["BioGenix","OncoThera","CardioNova","Immunexa"],
        "Revenue":[1.8,2.5,3.4,1.2]
    }).set_index("Company")
    st.bar_chart(df)

elif page == "About Honour Labs":
    st.title("🏢 About Honour Labs")
    st.write("""- Founded: 2011  
- HQ: Hyderabad  
- Revenue: ₹2,390 Cr  
- Model: Small-Molecule CDMO  
""")
