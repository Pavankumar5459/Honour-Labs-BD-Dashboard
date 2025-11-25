import streamlit as st
import pandas as pd

# ---------------------- APP CONFIG ----------------------
st.set_page_config(
    page_title="Honour Labs BD Intelligence Dashboard",
    page_icon="📊",
    layout="wide"
)

# ---------------------- PREMIUM THEME (CSS) ----------------------
st.markdown(
    """
    <style>
    .main {
        background-color: #F4F6F8;
    }
    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
    }
    h1, h2, h3, h4 {
        color: #003262;
    }
    .bd-card {
        background: #ffffff;
        border-radius: 12px;
        padding: 1rem 1.25rem;
        margin-bottom: 1rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.07);
        border-left: 4px solid #DAA520;
    }
    .bd-tag {
        display: inline-block;
        background: #003262;
        color: #ffffff;
        border-radius: 999px;
        font-size: 0.75rem;
        padding: 0.2rem 0.75rem;
        margin-bottom: 0.4rem;
    }
    .small-text {
        font-size: 0.85rem;
        color: #555555;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------- SIDEBAR NAVIGATION ----------------------
st.sidebar.title("📘 Navigation")

page = st.sidebar.selectbox(
    "Select a section:",
    [
        "What is a CDMO?",
        "Home",
        "Market Landscape",
        "Prospecting & Leads",
        "Capability Alignment",
        "Financial Opportunity",
        "About Honour Labs",
    ],
)


# ==========================================================
# 1️⃣ WHAT IS A CDMO?
# ==========================================================
if page == "What is a CDMO?":
    st.title("📘 What is a CDMO?")

    st.markdown(
        """
        <div class='bd-card'>
            <span class='bd-tag'>Definition</span>
            <p class='small-text'>
            A <b>CDMO (Contract Development & Manufacturing Organization)</b> is a partner that supports
            pharmaceutical and biotech companies by providing <b>drug substance development</b>,
            <b>process optimization</b>, <b>scale-up</b>, and <b>GMP manufacturing</b> of APIs and intermediates.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.subheader("Why CDMOs Exist")
    st.markdown(
        """
        - Most innovation now comes from **small and mid-size biotech** companies that often lack internal manufacturing infrastructure.  
        - Regulatory expectations around **quality, data integrity, and safety** keep increasing.  
        - CDMOs bring **specialized chemistry know-how, qualified plants, and flexible capacity**.  
        - Sponsors can focus on discovery and clinical strategy while CDMOs handle **R&D, scale-up, and supply**.  
        """
    )

    st.subheader("Importance in the United States")
    st.markdown(
        """
        - A large share of new drug approvals in the US originate from smaller biotech startups.  
        - These companies rarely own plants and rely heavily on **external CDMOs** for tox, clinical, and commercial API supply.  
        - US sponsors prioritize partners with:
            - Strong **regulatory track record**
            - Reliable **on-time delivery**
            - Ability to handle **complex, high-value molecules**.  
        """
    )

    st.subheader("Importance in India")
    st.markdown(
        """
        - India has a very strong base in **small-molecule synthetic chemistry** and **cost-efficient manufacturing**.  
        - Many Indian CDMOs support global pharma with:
            - APIs and advanced intermediates  
            - Route scouting and process optimization  
            - Long-term commercial supply at competitive cost.  
        - As global supply chains diversify, India remains a key hub for **volume + complexity + value**.  
        """
    )

    st.subheader("CDMO Market Growth (Illustrative)")
    market_df = pd.DataFrame(
        {
            "Year": [2020, 2022, 2024, 2026, 2028],
            "Global CDMO Market ($B, est.)": [80, 95, 115, 135, 160],
        }
    ).set_index("Year")
    st.line_chart(market_df)

    st.markdown(
        """
        <div class='bd-card'>
        <span class='bd-tag'>Key Takeaway</span>
        <p class='small-text'>
        CDMOs are no longer just "outsourcing vendors" – they are <b>strategic partners</b>
        that enable small biotechs and big pharma alike to bring complex molecules
        to market faster, more reliably, and at a sustainable cost.
        </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ==========================================================
# 2️⃣ HOME
# ==========================================================
elif page == "Home":
    st.title("🏠 Honour Labs – BD Intelligence Dashboard")

    st.markdown(
        """
        <div class='bd-card'>
            <span class='bd-tag'>Overview</span>
            <p class='small-text'>
            This dashboard is designed as a <b>business development decision-support tool</b> for Honour Labs – 
            providing a structured view of the CDMO market, target biotech companies, capability alignment, 
            financial opportunity, and Honour's long-term positioning.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        ### How to Use This Dashboard

        - Start with **“What is a CDMO?”** to set the context.  
        - Use **Market Landscape** to understand Honour’s place in the ecosystem.  
        - Explore **Prospecting & Leads** for potential target biotechs.  
        - Use **Capability Alignment** to tell a story of technical fit.  
        - Support ROI discussions via **Financial Opportunity**.  
        - End with **About Honour Labs** for a deep, integrated CDMO profile.
        """
    )

    st.markdown(
        """
        <div class='bd-card'>
        <span class='bd-tag'>Intended Use</span>
        <p class='small-text'>
        This is an illustrative, strategic view – not a live CRM. It can be extended later to pull real
        opportunity, revenue, and pipeline data from Honour’s internal systems or spreadsheets.
        </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ==========================================================
# 3️⃣ MARKET LANDSCAPE
# ==========================================================
elif page == "Market Landscape":
    st.title("🌎 Market Landscape")

    st.markdown(
        """
        <div class='bd-card'>
        This view positions Honour Labs relative to large global CDMOs and highlights
        US East Coast biotech clusters as a key BD region.
        </div>
        """,
        unsafe_allow_html=True,
    )

    # CDMO comparison (illustrative)
    comp_df = pd.DataFrame(
        {
            "Company": [
                "Honour Labs",
                "Lonza",
                "Catalent",
                "WuXi AppTec",
                "Thermo Fisher",
            ],
            "Service Breadth (1–5)": [3, 5, 5, 5, 5],
            "Small-Molecule Chemistry Depth (1–5)": [4, 4, 4, 4, 4],
            "Biologics Capability (1–5)": [1, 5, 5, 5, 5],
            "Cost Competitiveness (1–5)": [5, 3, 3, 3, 3],
            "Agility / Flexibility (1–5)": [5, 3, 3, 3, 3],
        }
    )

    st.subheader("CDMO Comparison Snapshot (Illustrative)")
    st.dataframe(comp_df, use_container_width=True)

    # US East Coast Biotech Hotspots
    hotspots_df = pd.DataFrame(
        {
            "Region": [
                "Boston / Cambridge, MA",
                "Philadelphia, PA",
                "New York / New Jersey",
                "Maryland (BioHealth)",
                "North Carolina (RTP)",
            ],
            "Biotech Companies (est.)": [480, 230, 320, 190, 150],
        }
    ).set_index("Region")

    st.subheader("US East Coast Biotech Hotspots (Illustrative)")
    st.bar_chart(hotspots_df)

    st.markdown(
        """
        <div class='bd-card'>
        <span class='bd-tag'>Opportunity Insight</span>
        <p class='small-text'>
        Honour’s small-molecule and HPAPI focus is very relevant to oncology, rare disease, and specialty
        programs emerging from these East Coast clusters. A focused BD effort here can generate
        high-value, long-term programs even with a lean front-end team.
        </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ==========================================================
# 4️⃣ PROSPECTING & LEADS
# ==========================================================
elif page == "Prospecting & Leads":
    st.title("🎯 Prospecting & Leads")

    st.markdown(
        """
        <div class='bd-card'>
        Illustrative biotech targets aligned with Honour Labs’ strengths in small-molecule APIs,
        HPAPI-like safety needs, and peptide/complex chemistry.
        </div>
        """,
        unsafe_allow_html=True,
    )

    leads_df = pd.DataFrame(
        {
            "Company": [
                "BioGenix Therapeutics",
                "OncoThera Bio",
                "CardioNova Pharma",
                "NeuroBridge Labs",
                "Immunexa Biotech",
            ],
            "Location": ["Boston", "Philadelphia", "New York", "New Jersey", "Maryland"],
            "Therapeutic Area": [
                "Oncology",
                "Immunology",
                "Cardiology",
                "Neurology",
                "Rare Disease",
            ],
            "Pipeline Stage": ["Phase II", "Phase I", "Phase III", "Pre-clinical", "Phase II"],
            "Likely Need": [
                "HPAPI-capable API supply",
                "Route scouting & tox supply",
                "Late-stage validation & commercial",
                "Non-GMP SAR & scale-up",
                "Complex API / intermediates",
            ],
            "Fit Score (0–100)": [88, 80, 92, 75, 85],
        }
    )

    st.subheader("High-Priority Targets (Illustrative)")
    st.dataframe(leads_df, use_container_width=True)

    st.subheader("Targets by Clinical Stage (Count)")
    stage_counts = leads_df["Pipeline Stage"].value_counts()
    st.bar_chart(stage_counts)

    st.markdown(
        """
        <div class='bd-card'>
        <span class='bd-tag'>How to Use This</span>
        <p class='small-text'>
        In a real deployment, this table can be linked to Honour's BD/CRM pipeline, including 
        contact status, proposals, and probability of win – turning this into a live BD cockpit.
        </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ==========================================================
# 5️⃣ CAPABILITY ALIGNMENT
# ==========================================================
elif page == "Capability Alignment":
    st.title("🧪 Capability Alignment")

    st.markdown(
        """
        <div class='bd-card'>
        This view shows how Honour Labs’ key capabilities map to the typical needs
        of emerging biotech programs.
        </div>
        """,
        unsafe_allow_html=True,
    )

    companies = [
        "BioGenix Therapeutics",
        "OncoThera Bio",
        "CardioNova Pharma",
        "NeuroBridge Labs",
        "Immunexa Biotech",
    ]
    selected_company = st.selectbox("Select a target company (illustrative):", companies)

    profiles = {
        "BioGenix Therapeutics": "Oncology · 2 assets in Phase II · HPAPI-like safety and complex synthesis needs.",
        "OncoThera Bio": "Immunology · 1 asset in Phase I · Emphasis on early route optimization and tox supply.",
        "CardioNova Pharma": "Cardiology · 1 asset in Phase III · Late-stage process validation and commercial readiness.",
        "NeuroBridge Labs": "Neurology · Pre-clinical · Rapid SAR support and flexible non-GMP supply.",
        "Immunexa Biotech": "Rare Disease · 1 asset in Phase II · Small volumes but very high value molecules.",
    }

    st.subheader("Target Profile (Illustrative)")
    st.write(profiles[selected_company])

    matrix_df = pd.DataFrame(
        {
            "Capability": [
                "Route Scouting / Process Development",
                "Kilo Lab (100 L) & Scale-Up",
                "GMP API Manufacturing (4–10 KL)",
                "HPAPI-Style Handling (OSD safe)",
                "Peptide / Complex Chemistry Support",
                "Analytical Method Dev & Validation",
                "CMC / Regulatory Documentation Support",
            ],
            "Honour Strength (1–5)": [5, 4, 4, 4, 3, 4, 3],
            "Relevance to Selected Client (1–5)": [5, 4, 5, 4, 3, 4, 4],
        }
    )

    st.subheader("Honour Capability Fit (Illustrative Scores)")
    st.dataframe(matrix_df, use_container_width=True)

    st.markdown(
        """
        <div class='bd-card'>
        <span class='bd-tag'>Capability Story</span>
        <p class='small-text'>
        This type of matrix can be used in discussions with clients to show that Honour has the
        right technical backbone – from <b>route scouting</b> and <b>kilo-lab</b> through to
        <b>commercial reactors (4–10 KL)</b> and <b>strong analytical support</b>.
        </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ==========================================================
# 6️⃣ FINANCIAL OPPORTUNITY
# ==========================================================
elif page == "Financial Opportunity":
    st.title("💰 Financial Opportunity")

    st.markdown(
        """
        <div class='bd-card'>
        Illustrative revenue opportunities and a high-level BD funnel for a focused East Coast effort.
        </div>
        """,
        unsafe_allow_html=True,
    )

    rev_df = pd.DataFrame(
        {
            "Company": [
                "BioGenix Therapeutics",
                "OncoThera Bio",
                "CardioNova Pharma",
                "Immunexa Biotech",
            ],
            "Estimated Annual Revenue ($M)": [1.8, 2.5, 3.4, 1.2],
            "Probability of Win (%)": [45, 35, 55, 40],
        }
    ).set_index("Company")

    st.subheader("Revenue Potential by Client (Illustrative)")
    st.bar_chart(rev_df["Estimated Annual Revenue ($M)"])

    st.subheader("Illustrative BD Funnel")
    funnel_df = pd.DataFrame(
        {
            "Stage": ["Identified", "Contacted", "In Discussion", "Proposal Sent", "Won"],
            "Count": [50, 22, 10, 5, 1],
        }
    )
    st.dataframe(funnel_df, use_container_width=True)

    st.markdown(
        """
        <div class='bd-card'>
        <span class='bd-tag'>Next Step</span>
        <p class='small-text'>
        With real data, this page can show pipeline value by stage, expected conversion, and
        capacity impact – helping Honour prioritize which programs and regions to pursue.
        </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ==========================================================
# 7️⃣ ABOUT HONOUR LABS – DEEP PROFILE
# ==========================================================
elif page == "About Honour Labs":
    st.title("🏢 About Honour Labs – CDMO Profile")

    st.markdown(
        """
        <div class='bd-card'>
        <span class='bd-tag'>Company Snapshot</span>
        <p class='small-text'>
        Honour Labs is an integrated <b>small-molecule CDMO</b> based in India, specializing in 
        APIs, advanced intermediates, and complex small molecules. The company supports
        partners across <b>process R&amp;D, scale-up, analytical, and commercial manufacturing</b>.
        </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Founded", "2011")
        st.metric("Headquarters", "Hyderabad, India")
    with col2:
        st.metric("Revenue (FY24)", "₹2,390 Cr (approx.)")
        st.metric("Employees", "1,300+")
    with col3:
        st.metric("CDMO Focus", "Small-Molecule APIs & Intermediates")
        st.metric("Scale", "100 L → 1 KL → 4–10 KL")

    st.subheader("R&D and Process Development")

    rd_df = pd.DataFrame(
        {
            "Area": [
                "Route Scouting & Evaluation",
                "Process Optimization",
                "Kilo Lab (up to ~100 L)",
                "Scale-Up Studies (1 KL reactors)",
            ],
            "Description": [
                "Alternative, cost-effective, IP-sensitive routes to APIs and key intermediates.",
                "Improving yield, impurity profile, safety, and scalability.",
                "Bridging lab chemistry into pilot-scale with robust control strategies.",
                "Translating lab/kilo processes into plant-feasible procedures.",
            ],
        }
    )
    st.dataframe(rd_df, use_container_width=True)

    st.subheader("Analytical & Quality")

    qa_df = pd.DataFrame(
        {
            "Capability": [
                "Method Development & Validation",
                "Stability Studies",
                "Impurity & Genotoxic Impurity Profiling",
                "In-Process and Release Testing",
            ],
            "Comment": [
                "HPLC, UPLC, GC, and related methods tailored to complex molecules.",
                "Support for registration stability and ongoing commercial programs.",
                "Deep impurity investigation to support regulatory filings.",
                "Robust QC systems aligned with international expectations.",
            ],
        }
    )
    st.dataframe(qa_df, use_container_width=True)

    st.subheader("Technology & Chemistry Platforms")

    tech_df = pd.DataFrame(
        {
            "Platform / Technology": [
                "Hydrogenation",
                "High-Pressure Reactions",
                "Cryogenic Chemistry",
                "Flow / Continuous Processing (where applicable)",
                "Chiral Chemistry & Resolution",
                "Peptide / Peptidomimetic Chemistry",
                "HPAPI-Style Handling (OSD-Safe)",
                "Advanced Purification (Chromatography)",
            ],
            "Application": [
                "Catalytic hydrogenations for key intermediates & APIs.",
                "Reactions requiring elevated pressure for efficiency.",
                "Low-temperature control for sensitive transformations.",
                "Improved safety and selectivity for certain steps.",
                "High enantiopurity for chiral APIs.",
                "Support for small peptides and complex scaffolds.",
                "Handling potent compounds in a controlled manner.",
                "Purification of complex mixtures and impurity removal.",
            ],
        }
    )
    st.dataframe(tech_df, use_container_width=True)

    st.subheader("Manufacturing Scale & Infrastructure")

    st.markdown(
        """
        - **R&D / Kilo Lab:** multiple glass-lined and SS reactors up to ~100 L.  
        - **Pilot Scale:** 1 KL multi-purpose reactors for scale-up and validation.  
        - **Commercial Scale:** 4–10 KL reactors for multi-ton API and intermediate campaigns.  
        - Appropriate utilities and controls to support complex, multi-step processes.  
        """
    )

    st.subheader("Competitive Positioning (Simplified)")

    comp2_df = pd.DataFrame(
        {
            "Dimension": [
                "Small-Molecule Chemistry Depth",
                "Cost Competitiveness",
                "Agility / Speed",
                "HPAPI / Potent Handling",
                "Peptide / Complex Molecules",
                "Biologics & Large Molecules",
                "Global Commercial Presence (US/EU Front-end)",
            ],
            "Honour Labs": [
                "Strong",
                "Strong",
                "Strong",
                "Emerging / Selective",
                "Developing",
                "Limited (focus on small molecules)",
                "Developing (room to add US/EU footprint)",
            ],
            "Top Global CDMOs (Lonza / Catalent / WuXi)": [
                "Strong",
                "Moderate–High",
                "Moderate",
                "Very Strong",
                "Very Strong (select players)",
                "Very Strong",
                "Very Strong",
            ],
        }
    )
    st.dataframe(comp2_df, use_container_width=True)

    st.subheader("Strategic Roadmap – Path to a Stronger Global CDMO")

    roadmap_df = pd.DataFrame(
        {
            "Focus Area": [
                "Regulatory & Quality",
                "US/EU BD & Key Account Management",
                "Technology Deepening (HPAPI, Peptides)",
                "Partnerships & Modalities",
            ],
            "Indicative Actions": [
                "Strengthen USFDA/EMA/MHRA approvals, enhance DMF filings and audit readiness.",
                "Build a structured BD engine with local presence, regular travel, and strategic targeting.",
                "Invest in more dedicated HPAPI and peptide capabilities with upgraded containment.",
                "Explore collaborations or alliances for biologics / other modalities while staying strong in small molecules.",
            ],
        }
    )
    st.dataframe(roadmap_df, use_container_width=True)

    st.markdown(
        """
        <div class='bd-card'>
        <span class='bd-tag'>How This Page Helps</span>
        <p class='small-text'>
        This profile can be used directly in BD meetings or investor discussions to clearly explain:
        who Honour Labs is, what it does best, where it stands vs. large global CDMOs, and how it plans to grow.
        </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
