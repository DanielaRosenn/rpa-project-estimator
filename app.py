"""
RPA Project Estimator - Main Application
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import os
from calculations import RPACalculator
import config

# Page configuration
st.set_page_config(
    page_title="RPA Project Estimator 2026",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize calculator
calc = RPACalculator()

# Initialize session state for data storage
if 'projects' not in st.session_state:
    st.session_state.projects = pd.DataFrame()

if 'project_counter' not in st.session_state:
    st.session_state.project_counter = 1

# Excel file path
EXCEL_FILE = "rpa_projects_database.xlsx"


# Load data from Excel if exists
@st.cache_data
def load_data():
    if os.path.exists(EXCEL_FILE):
        try:
            return pd.read_excel(EXCEL_FILE, sheet_name='projects')
        except:
            return pd.DataFrame()
    return pd.DataFrame()


# Save data to Excel
def save_data(df):
    with pd.ExcelWriter(EXCEL_FILE, engine='xlsxwriter') as writer:
        df.to_excel(writer, sheet_name='projects', index=False)
    return True


# Load existing data
if st.session_state.projects.empty:
    st.session_state.projects = load_data()

# Sidebar navigation
st.sidebar.title("🤖 RPA Estimator 2026")
page = st.sidebar.radio(
    "Navigate to:",
    ["📊 Dashboard", "➕ New Project", "📋 Project List", "🎯 Magic Quadrant", "📈 Reports"]
)

# Dashboard Page
if page == "📊 Dashboard":
    st.title("📊 Executive Dashboard")

    if not st.session_state.projects.empty:
        df = st.session_state.projects

        # Calculate metrics
        total_projects = len(df)
        total_fte_saved = df['fte_saved'].sum() if 'fte_saved' in df.columns else 0
        total_savings = df['annual_savings'].sum() if 'annual_savings' in df.columns else 0
        avg_roi = df['roi_percentage'].mean() if 'roi_percentage' in df.columns else 0

        # Display metrics
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric(
                "Total Projects",
                total_projects,
                delta=f"{total_projects} in pipeline"
            )
        with col2:
            st.metric(
                "Total FTE Saved",
                f"{total_fte_saved:.1f}",
                delta=f"${total_fte_saved * 35 * 2080:,.0f} value"
            )
        with col3:
            st.metric(
                "Annual Savings",
                f"${total_savings:,.0f}",
                delta="Per year"
            )
        with col4:
            st.metric(
                "Average ROI",
                f"{avg_roi:.0f}%",
                delta="Portfolio average"
            )

        # Quick Quadrant Preview
        if 'automation_potential' in df.columns and 'implementation_ease' in df.columns:
            st.subheader("Portfolio Overview")

            fig = px.scatter(df,
                             x='implementation_ease',
                             y='automation_potential',
                             size='annual_savings' if 'annual_savings' in df.columns else None,
                             color='quadrant' if 'quadrant' in df.columns else None,
                             hover_data=['project_name', 'roi_percentage'] if 'project_name' in df.columns else None,
                             title="Magic Quadrant Preview"
                             )

            # Add quadrant lines
            fig.add_hline(y=50, line_dash="dash", line_color="gray", opacity=0.5)
            fig.add_vline(x=50, line_dash="dash", line_color="gray", opacity=0.5)

            fig.update_layout(
                xaxis_title="Implementation Ease →",
                yaxis_title="Automation Potential →",
                xaxis=dict(range=[0, 100]),
                yaxis=dict(range=[0, 100]),
                height=500
            )

            st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No projects yet. Add your first project to see the dashboard!")

# New Project Page
elif page == "➕ New Project":
    st.title("➕ Add New RPA Project")

    with st.form("new_project_form"):
        # Section 1: Basic Information
        st.subheader("1️⃣ Basic Information")
        col1, col2 = st.columns(2)

        with col1:
            project_name = st.text_input("Project Name *", placeholder="e.g., Invoice Processing")
            business_area = st.selectbox("Business Area *",
                                         ["Engineering", "Finance", "HR", "Sales", "Operations", "IT",
                                          "Customer Service"])
            process_owner = st.text_input("Process Owner Email", placeholder="owner@company.com")

        with col2:
            category = st.selectbox("Category",
                                    ["Data Processing", "Report Generation", "System Integration", "Customer Service",
                                     "Compliance"])
            status = st.selectbox("Status",
                                  ["Idea", "Assessment", "In Queue", "Development", "Testing", "Production"])

        description = st.text_area("Description", placeholder="Describe the process to be automated...")

        # Section 2: Process Metrics
        st.subheader("2️⃣ Process Metrics")
        col1, col2, col3 = st.columns(3)

        with col1:
            current_fte = st.number_input("Current FTEs Required", min_value=0.1, value=1.0, step=0.1)
            frequency = st.selectbox("Process Frequency", list(config.FREQUENCY_MULTIPLIERS.keys()))

        with col2:
            volume_per_freq = st.number_input("Volume per Frequency", min_value=1, value=10)
            avg_handle_time = st.number_input("Avg Handle Time (minutes)", min_value=1, value=30)

        with col3:
            app_count = st.number_input("Number of Applications", min_value=1, max_value=10, value=2)
            process_steps = st.number_input("Number of Process Steps", min_value=1, value=10)

        # Section 3: Automation Readiness
        st.subheader("3️⃣ Automation Readiness Assessment")

        col1, col2 = st.columns(2)
        with col1:
            rules_based = st.select_slider(
                "Decisions have straightforward rules",
                options=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"],
                value="Agree"
            )
            digital_data = st.select_slider(
                "Input data is accessed digitally",
                options=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"],
                value="Agree"
            )

        with col2:
            data_formatted = st.select_slider(
                "Data is highly formatted",
                options=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"],
                value="Agree"
            )
            process_stable = st.select_slider(
                "Process is stable (no changes expected)",
                options=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"],
                value="Agree"
            )

        # Section 4: Technical Complexity
        st.subheader("4️⃣ Technical Complexity")

        col1, col2, col3 = st.columns(3)
        with col1:
            data_type = st.selectbox("Data Type", list(config.COMPLEXITY_FACTORS['data'].keys()))

        with col2:
            logic_complexity = st.selectbox("Logic Complexity", list(config.COMPLEXITY_FACTORS['logic'].keys()))

        with col3:
            environment = st.selectbox("Environment", list(config.COMPLEXITY_FACTORS['environment'].keys()))

        # Section 5: AI Components (Optional)
        st.subheader("5️⃣ AI/ML Components (Optional)")

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            use_ocr = st.checkbox("Document Processing (OCR)")
            ocr_pages = st.number_input("Pages/month", value=0) if use_ocr else 0

        with col2:
            use_nlp = st.checkbox("Natural Language (NLP)")
            nlp_tokens = st.number_input("Tokens/month (K)", value=0) if use_nlp else 0

        with col3:
            use_cv = st.checkbox("Computer Vision")
            cv_images = st.number_input("Images/month", value=0) if use_cv else 0

        with col4:
            use_ml = st.checkbox("Custom ML Model")

        # Submit button
        submitted = st.form_submit_button("🧮 Calculate & Save Project", type="primary", use_container_width=True)

    if submitted:
        # Perform calculations
        annual_volume = calc.calculate_annual_volume(frequency, volume_per_freq)
        annual_hours = calc.calculate_annual_hours(annual_volume, avg_handle_time)
        fte_required = calc.calculate_fte_required(annual_hours)

        automation_potential = calc.calculate_automation_potential(
            rules_based, digital_data, data_formatted, process_stable, annual_volume, data_type
        )

        implementation_ease = calc.calculate_implementation_ease(
            app_count, logic_complexity, environment, data_type
        )

        complexity_score = calc.calculate_complexity_score(
            data_type, app_count, logic_complexity, environment
        )

        dev_days, total_days = calc.calculate_effort_days(process_steps, complexity_score)

        # Calculate AI costs
        ai_monthly_cost = (
                (ocr_pages * config.AI_COSTS['ocr_per_page']) +
                (nlp_tokens * config.AI_COSTS['nlp_per_1k_tokens']) +
                (cv_images * config.AI_COSTS['cv_per_image']) +
                (config.AI_COSTS['ml_custom_model'] / 12 if use_ml else 0)
        )

        # Calculate FTE savings (80% efficiency)
        fte_saved = fte_required * config.FTE_CONSTANTS['automation_efficiency']

        # Calculate costs and ROI
        financials = calc.calculate_costs_and_roi(total_days, fte_saved, ai_monthly_cost)

        # Determine quadrant
        quadrant = calc.determine_quadrant(automation_potential, implementation_ease)

        # Calculate priority score
        priority_score = calc.calculate_priority_score(
            automation_potential, financials['roi_percentage'], implementation_ease, fte_saved
        )

        # Display results
        st.success("✅ Project Calculated Successfully!")

        st.subheader("📊 Estimation Results")

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Automation Potential", f"{automation_potential:.1f}%")
            st.metric("Development Days", f"{dev_days:.0f}")
        with col2:
            st.metric("Implementation Ease", f"{implementation_ease:.1f}%")
            st.metric("Total Effort Days", f"{total_days:.0f}")
        with col3:
            st.metric("Annual Savings", f"${financials['annual_savings']:,.0f}")
            st.metric("Implementation Cost", f"${financials['implementation_cost']:,.0f}")
        with col4:
            st.metric("ROI", f"{financials['roi_percentage']:.0f}%")
            st.metric("Payback (months)", f"{financials['payback_months']:.1f}")

        st.info(f"**Quadrant:** {quadrant} | **Priority Score:** {priority_score:.0f}/100")

        # Create project record
        new_project = pd.DataFrame([{
            'project_id': f"P{st.session_state.project_counter:04d}",
            'project_name': project_name,
            'business_area': business_area,
            'category': category,
            'status': status,
            'process_owner': process_owner,
            'description': description,
            'current_fte': current_fte,
            'frequency': frequency,
            'volume_per_freq': volume_per_freq,
            'annual_volume': annual_volume,
            'avg_handle_time': avg_handle_time,
            'annual_hours': annual_hours,
            'fte_required': fte_required,
            'fte_saved': fte_saved,
            'app_count': app_count,
            'process_steps': process_steps,
            'automation_potential': automation_potential,
            'implementation_ease': implementation_ease,
            'complexity_score': complexity_score,
            'dev_days': dev_days,
            'total_days': total_days,
            'implementation_cost': financials['implementation_cost'],
            'annual_savings': financials['annual_savings'],
            'roi_percentage': financials['roi_percentage'],
            'payback_months': financials['payback_months'],
            'quadrant': quadrant,
            'priority_score': priority_score,
            'ai_monthly_cost': ai_monthly_cost,
            'data_type': data_type,
            'logic_complexity': logic_complexity,
            'environment': environment,
            'created_date': datetime.now().strftime('%Y-%m-%d')
        }])

        # Add to session state
        st.session_state.projects = pd.concat([st.session_state.projects, new_project], ignore_index=True)
        st.session_state.project_counter += 1

        # Save to Excel
        if save_data(st.session_state.projects):
            st.success(f"✅ Project '{project_name}' saved to database!")

# Project List Page
elif page == "📋 Project List":
    st.title("📋 Project Pipeline")

    if not st.session_state.projects.empty:
        df = st.session_state.projects

        # Filters
        col1, col2, col3 = st.columns(3)
        with col1:
            filter_area = st.multiselect("Filter by Business Area",
                                         options=df['business_area'].unique() if 'business_area' in df.columns else [])
        with col2:
            filter_status = st.multiselect("Filter by Status",
                                           options=df['status'].unique() if 'status' in df.columns else [])
        with col3:
            filter_quadrant = st.multiselect("Filter by Quadrant",
                                             options=df['quadrant'].unique() if 'quadrant' in df.columns else [])

        # Apply filters
        filtered_df = df.copy()
        if filter_area:
            filtered_df = filtered_df[filtered_df['business_area'].isin(filter_area)]
        if filter_status:
            filtered_df = filtered_df[filtered_df['status'].isin(filter_status)]
        if filter_quadrant:
            filtered_df = filtered_df[filtered_df['quadrant'].isin(filter_quadrant)]

        # Display table
        st.dataframe(
            filtered_df[[
                'project_id', 'project_name', 'business_area', 'status',
                'quadrant', 'fte_saved', 'annual_savings', 'roi_percentage',
                'priority_score'
            ]].style.format({
                'fte_saved': '{:.1f}',
                'annual_savings': '${:,.0f}',
                'roi_percentage': '{:.0f}%',
                'priority_score': '{:.0f}'
            }),
            use_container_width=True
        )

        # Export button
        st.download_button(
            label="📥 Download Project List (Excel)",
            data=open(EXCEL_FILE, 'rb').read() if os.path.exists(EXCEL_FILE) else b'',
            file_name=f"rpa_projects_{datetime.now().strftime('%Y%m%d')}.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    else:
        st.info("No projects yet. Add your first project to see the list!")

# Magic Quadrant Page
elif page == "🎯 Magic Quadrant":
    st.title("🎯 Magic Quadrant Analysis")

    if not st.session_state.projects.empty and 'automation_potential' in st.session_state.projects.columns:
        df = st.session_state.projects

        # Create the quadrant chart
        fig = go.Figure()

        # Add quadrant backgrounds
        fig.add_shape(type="rect", x0=50, y0=50, x1=100, y1=100,
                      fillcolor="lightgreen", opacity=0.2, line_width=0)
        fig.add_shape(type="rect", x0=0, y0=50, x1=50, y1=100,
                      fillcolor="lightblue", opacity=0.2, line_width=0)
        fig.add_shape(type="rect", x0=0, y0=0, x1=50, y1=50,
                      fillcolor="lightgray", opacity=0.2, line_width=0)
        fig.add_shape(type="rect", x0=50, y0=0, x1=100, y1=50,
                      fillcolor="lightyellow", opacity=0.2, line_width=0)

        # Add quadrant lines
        fig.add_hline(y=50, line_dash="dash", line_color="gray", opacity=0.5)
        fig.add_vline(x=50, line_dash="dash", line_color="gray", opacity=0.5)

        # Add project dots
        for quadrant in df['quadrant'].unique():
            quadrant_df = df[df['quadrant'] == quadrant]
            fig.add_trace(go.Scatter(
                x=quadrant_df['implementation_ease'],
                y=quadrant_df['automation_potential'],
                mode='markers+text',
                name=quadrant,
                text=quadrant_df.index + 1,
                textposition="middle center",
                marker=dict(
                    size=quadrant_df['annual_savings'] / 10000 if 'annual_savings' in quadrant_df else 20,
                    sizemin=10
                ),
                hovertemplate="<b>%{hovertext}</b><br>" +
                              "Automation: %{y:.1f}%<br>" +
                              "Ease: %{x:.1f}%<br>" +
                              "Savings: $%{marker.size:,.0f}",
                hovertext=quadrant_df['project_name']
            ))

        # Add quadrant labels
        fig.add_annotation(x=75, y=75, text="🚀 Quick Wins", showarrow=False, font=dict(size=14, color="green"))
        fig.add_annotation(x=25, y=75, text="💎 Strategic", showarrow=False, font=dict(size=14, color="blue"))
        fig.add_annotation(x=25, y=25, text="⏸️ Nice to Have", showarrow=False, font=dict(size=14, color="gray"))
        fig.add_annotation(x=75, y=25, text="🔧 Fill-ins", showarrow=False, font=dict(size=14, color="orange"))

        fig.update_layout(
            title="Portfolio Magic Quadrant",
            xaxis_title="Implementation Ease →",
            yaxis_title="Automation Potential →",
            xaxis=dict(range=[0, 100]),
            yaxis=dict(range=[0, 100]),
            height=700,
            showlegend=True
        )

        st.plotly_chart(fig, use_container_width=True)

        # Quadrant Statistics
        st.subheader("📊 Quadrant Distribution")
        quadrant_stats = df['quadrant'].value_counts()

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("🚀 Quick Wins", quadrant_stats.get("🚀 Quick Win", 0))
        with col2:
            st.metric("💎 Strategic", quadrant_stats.get("💎 Strategic", 0))
        with col3:
            st.metric("🔧 Fill-ins", quadrant_stats.get("🔧 Fill-in", 0))
        with col4:
            st.metric("⏸️ Nice to Have", quadrant_stats.get("⏸️ Nice to Have", 0))
    else:
        st.info("Add projects to see the Magic Quadrant visualization!")

# Reports Page
elif page == "📈 Reports":
    st.title("📈 Reports & Analytics")

    if not st.session_state.projects.empty:
        df = st.session_state.projects

        # Summary metrics
        st.subheader("Portfolio Summary")

        col1, col2 = st.columns(2)

        with col1:
            # ROI Distribution
            fig_roi = px.histogram(df, x='roi_percentage', nbins=20,
                                   title="ROI Distribution",
                                   labels={'roi_percentage': 'ROI (%)', 'count': 'Number of Projects'})
            st.plotly_chart(fig_roi, use_container_width=True)

        with col2:
            # Projects by Business Area
            area_counts = df['business_area'].value_counts()
            fig_area = px.pie(values=area_counts.values, names=area_counts.index,
                              title="Projects by Business Area")
            st.plotly_chart(fig_area, use_container_width=True)

        # Priority Scores
        st.subheader("Top 10 Priority Projects")
        top_projects = df.nlargest(10, 'priority_score')[
            ['project_name', 'priority_score', 'roi_percentage', 'fte_saved', 'quadrant']
        ]
        st.dataframe(top_projects, use_container_width=True)

        # Financial Summary
        st.subheader("Financial Impact")
        total_investment = df['implementation_cost'].sum() if 'implementation_cost' in df.columns else 0
        total_annual_savings = df['annual_savings'].sum() if 'annual_savings' in df.columns else 0
        portfolio_roi = (
                    (total_annual_savings - total_investment) / total_investment * 100) if total_investment > 0 else 0

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Investment Required", f"${total_investment:,.0f}")
        with col2:
            st.metric("Total Annual Savings", f"${total_annual_savings:,.0f}")
        with col3:
            st.metric("Portfolio ROI", f"{portfolio_roi:.0f}%")
    else:
        st.info("No projects yet. Add projects to see reports!")

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("### 📁 Database")
st.sidebar.info(f"Projects are saved to:\n`{EXCEL_FILE}`")
st.sidebar.markdown("### 🚀 Deployment")
st.sidebar.markdown("[Deploy to Streamlit Cloud](https://streamlit.io/cloud)")