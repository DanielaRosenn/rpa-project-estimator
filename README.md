# 🤖 RPA Project Estimator 2026 - Complete Documentation

## Table of Contents
1. [Overview](#overview)
2. [How Calculations Work](#how-calculations-work)
3. [System Sections Explained](#system-sections-explained)
4. [Customizing Categories](#customizing-categories)
5. [Understanding the Magic Quadrant](#understanding-the-magic-quadrant)
6. [Excel Database Structure](#excel-database-structure)
7. [Deployment Guide](#deployment-guide)

---

## Overview

The RPA Project Estimator is a comprehensive tool for evaluating, prioritizing, and tracking RPA (Robotic Process Automation) projects. It calculates ROI, estimates implementation effort, and helps you build a strategic automation roadmap for 2026.

### Key Features:
- **Automatic ROI Calculation** - Based on FTE savings and implementation costs
- **Magic Quadrant Visualization** - Projects plotted by automation potential vs implementation ease
- **Priority Scoring** - Weighted algorithm to rank projects
- **AI Cost Estimation** - Includes OCR, NLP, Computer Vision costs
- **Excel Database** - All data stored in easily editable Excel file

---

## How Calculations Work

### 1. Volume & FTE Calculations

#### Annual Volume
```
Annual Volume = Volume per Frequency × Frequency Multiplier

Frequency Multipliers:
- Daily: 260 (business days/year)
- Weekly: 52
- Monthly: 12
- Quarterly: 4
- Yearly: 1
- Hourly: 2080 (business hours/year)
```

#### Annual Hours Required
```
Annual Hours = (Annual Volume × Average Handle Time in Minutes) ÷ 60
```

#### FTE Required
```
FTE Required = (Annual Hours × Shrinkage Factor) ÷ Productive Hours per Year

Where:
- Shrinkage Factor = 1.28 (accounts for breaks, vacation, training)
- Productive Hours = 1,760 per year (after vacation/sick leave)
```

#### FTE Saved
```
FTE Saved = FTE Required × Automation Efficiency

Where:
- Automation Efficiency = 80% (typical RPA efficiency)
```

---

### 2. Automation Potential Score (0-100%)

The automation potential represents how much of the process can be successfully automated.

#### Scoring Components:
| Factor | Weight | Scoring |
|--------|--------|---------|
| **Straightforward Rules** | 30% | Agree/Strongly Agree: 30 points, Neutral: 15, Disagree: 0 |
| **Digital Data Access** | 25% | Agree/Strongly Agree: 25 points, Neutral: 12.5, Disagree: 0 |
| **Formatted Data** | 20% | Agree/Strongly Agree: 20 points, Neutral: 10, Disagree: 0 |
| **Process Stability** | 15% | Agree/Strongly Agree: 15 points, Neutral: 7.5, Disagree: 0 |
| **Volume Bonus** | 10% | >10,000: 10 pts, >5,000: 7 pts, >1,000: 5 pts, <1,000: 2 pts |

#### Data Type Penalties:
- **Structured Data**: No penalty (×1.0)
- **Semi-structured**: 20% reduction (×0.8)
- **Unstructured**: 40% reduction (×0.6)

**Maximum Score**: Capped at 95% (nothing is 100% automatable)

---

### 3. Implementation Ease Score (0-100%)

Represents how easy/difficult it is to implement the automation.

Starting with 100 points, deductions are made for complexity:

#### Deductions:
| Factor | Penalty |
|--------|---------|
| **Applications** | 2 apps: -10, 3 apps: -20, 4+ apps: -30, 6+ apps: -40 |
| **Logic Complexity** | Moderate: -15, Complex: -30 |
| **Environment** | Desktop: -10, Web: -20, Mainframe: -35, Citrix: -40 |
| **Data Type** | Semi-structured: -10, Unstructured: -25 |
| **API Bonus** | API available: +10 points |

---

### 4. Complexity Score Calculation

Used to estimate development effort:

```
Complexity Score = Data Multiplier × Application Multiplier × Logic Multiplier × Environment Multiplier

Multipliers:
- Data: Structured(1.0), Semi(2.0), Unstructured(3.0)
- Applications: 1(1.0), 2(1.3), 3(1.5), 4(1.8), 5(2.0), 6+(2.5)
- Logic: Linear(1.0), Moderate(1.5), Complex(2.5)
- Environment: API(0.7), Desktop(1.5), Web(2.0), Mainframe(3.0), Citrix(4.0)
```

---

### 5. Effort Estimation

#### Development Days
```
Base Days = Number of Process Steps × 0.5
Development Days = Base Days × Complexity Score
```

#### Total Effort Days
```
Total Days = Development Days × (1 + Testing Factor) × (1 + Contingency Factor)

Where:
- Testing Factor = 30% (0.30)
- Contingency Factor = 30% (0.30)
- Combined multiplier = 1.69
```

---

### 6. Financial Calculations

#### Implementation Cost
```
Implementation Cost = Total Effort Days × Daily Rate

Where:
- Default Daily Rate = $1,000
```

#### Annual Savings
```
Annual Savings = FTE Saved × Hourly Rate × Annual Work Hours

Where:
- Default Hourly Rate = $35
- Annual Work Hours = 2,080
```

#### ROI Calculation
```
ROI % = ((Annual Savings - Implementation Cost) ÷ Implementation Cost) × 100
```

#### Payback Period
```
Payback Months = (Implementation Cost ÷ Annual Savings) × 12
```

---

### 7. AI/ML Cost Calculations

Optional AI components add to the monthly/annual costs:

| Component | Cost |
|-----------|------|
| **OCR (Document Processing)** | $0.30 per page |
| **NLP (Natural Language)** | $0.002 per 1,000 tokens |
| **Computer Vision** | $0.005 per image |
| **Custom ML Model** | $7,500 one-time + hosting |

```
Monthly AI Cost = (OCR Pages × 0.30) + (NLP Tokens × 0.002) + (CV Images × 0.005) + (ML Model ÷ 12)
Annual AI Cost = Monthly AI Cost × 12
```

---

### 8. Priority Score (0-100)

Weighted scoring to rank projects:

```
Priority Score = (Automation Potential × 30%) + 
                 (ROI Normalized × 30%) + 
                 (Implementation Ease × 20%) + 
                 (FTE Saved Normalized × 20%)

Where:
- ROI Normalized = MIN(ROI ÷ 500, 1) × 100
- FTE Normalized = MIN(FTE Saved ÷ 10, 1) × 100
```

---

## System Sections Explained

### 📊 Dashboard
**Purpose**: Executive overview of entire RPA portfolio

**Displays**:
- **Total Projects**: Count of all projects in pipeline
- **Total FTE Saved**: Sum of all FTE savings across projects
- **Annual Savings**: Total yearly financial benefit
- **Average ROI**: Portfolio-wide return on investment

**Magic Quadrant Preview**: Mini visualization of all projects

---

### ➕ New Project
**Purpose**: Add and calculate new RPA opportunities

**Sections**:
1. **Basic Information**: Project identification and ownership
2. **Process Metrics**: Volume, frequency, and time measurements
3. **Automation Readiness**: Likert scale assessment (Strongly Disagree to Strongly Agree)
4. **Technical Complexity**: Technology stack assessment
5. **AI Components**: Optional AI/ML cost factors

**Process Flow**:
1. Enter all project data
2. Click "Calculate & Save"
3. System runs all calculations
4. Displays results instantly
5. Saves to Excel database

---

### 📋 Project List
**Purpose**: Manage and filter project pipeline

**Features**:
- **Filterable Table**: Sort by business area, status, or quadrant
- **Key Metrics Display**: FTE saved, savings, ROI for each project
- **Export Function**: Download complete Excel database

---

### 🎯 Magic Quadrant
**Purpose**: Strategic visualization for prioritization

**Quadrants**:
- **🚀 Quick Wins** (Top Right): High potential + Easy implementation → Do first!
- **💎 Strategic** (Top Left): High potential + Difficult → Worth the effort
- **🔧 Fill-ins** (Bottom Right): Low potential + Easy → Good for learning
- **⏸️ Nice to Have** (Bottom Left): Low potential + Difficult → Reconsider

**Bubble Size**: Represents annual savings (larger = more savings)

---

### 📈 Reports
**Purpose**: Analytics and insights

**Includes**:
- ROI distribution histogram
- Projects by business area pie chart
- Top 10 priority projects
- Total portfolio financial impact

---

## Customizing Categories

### Easy Customization in `config.py`

You can easily modify all dropdown categories by editing the `config.py` file:

#### 1. Business Areas and Categories
Add these to your `config.py`:
```python
BUSINESS_AREAS = [
    "Engineering", 
    "Finance", 
    "HR", 
    "Sales", 
    "Operations", 
    "IT", 
    "Customer Service",
    "Marketing",  # Add your own
    "Legal"       # Add more as needed
]

PROJECT_CATEGORIES = [
    "Data Processing",
    "Report Generation", 
    "System Integration",
    "Customer Service",
    "Compliance",
    "Your New Category"  # Add custom categories
]

PROJECT_STATUSES = [
    "Idea",
    "Assessment",
    "In Queue",
    "Design",        # Add more statuses
    "Development",
    "Testing",
    "UAT",
    "Production",
    "On Hold"
]
```

#### 2. Update `app.py` to Use Config Categories
Replace the hardcoded lists with:
```python
# In the New Project form section:
business_area = st.selectbox("Business Area *", config.BUSINESS_AREAS)
category = st.selectbox("Category", config.PROJECT_CATEGORIES)
status = st.selectbox("Status", config.PROJECT_STATUSES)
```

#### 3. Modifying Calculation Parameters
In `config.py`, adjust these values:

```python
FTE_CONSTANTS = {
    'hourly_rate_default': 35  # Change to your local rate
}

TIMELINE_FACTORS = {
    'daily_rate_default': 1000  # Change to your contractor rate
}
```

#### 4. Adding New Frequencies
```python
FREQUENCY_MULTIPLIERS = {
    'Daily': 260,
    'Weekly': 52,
    'Bi-Weekly': 26,
    'Monthly': 12,
    'Quarterly': 4,
    'Yearly': 1,
    'Hourly': 2080,
    'Every 10 minutes': 12480  # Add custom frequencies
}
```

---

## Understanding the Magic Quadrant

### Axes Explanation
- **X-Axis (Horizontal)**: Implementation Ease (0-100%)
  - Further right = Easier to implement
  - Further left = More difficult

- **Y-Axis (Vertical)**: Automation Potential (0-100%)
  - Higher = More of the process can be automated
  - Lower = Less automation possible

### Strategic Interpretation
1. **Start with Quick Wins** to build momentum and prove ROI
2. **Plan Strategic projects** for maximum long-term value
3. **Use Fill-ins** when you have extra capacity
4. **Reconsider Nice to Have** projects - maybe manual is better

---

## Excel Database Structure

The system creates `rpa_projects_database.xlsx` with these columns:

| Column | Description |
|--------|-------------|
| project_id | Unique identifier (P0001, P0002, etc.) |
| project_name | Name of the automation project |
| business_area | Department/division |
| current_fte | Current manual FTEs required |
| annual_volume | Calculated yearly transactions |
| automation_potential | 0-100% score |
| implementation_ease | 0-100% score |
| complexity_score | Multiplier for effort |
| dev_days | Pure development days |
| total_days | Including testing & contingency |
| implementation_cost | One-time cost |
| annual_savings | Yearly benefit |
| roi_percentage | Return on investment |
| payback_months | Time to break even |
| quadrant | Strategic classification |
| priority_score | 0-100 ranking score |

---

## Deployment Guide

### Local Testing
```bash
# With UV (recommended)
uv run streamlit run app.py

# Or with standard pip
streamlit run app.py
```

### Deploying to Streamlit Cloud (Free Hosting)

1. **Create GitHub Repository**
   - Upload all files (app.py, config.py, calculations.py, requirements.txt)
   - Don't upload the Excel file (it's created automatically)

2. **Sign up at [streamlit.io/cloud](https://streamlit.io/cloud)**
   - Use your GitHub account

3. **Deploy Your App**
   - Click "New app"
   - Select your repository
   - Choose `app.py` as main file
   - Click "Deploy"

4. **Share Your App**
   - You'll get a URL like: `https://your-app-name.streamlit.app`
   - Share with anyone!

### Requirements File
Already created, but ensure it contains:
```
streamlit
pandas
openpyxl
plotly
xlsxwriter
python-dateutil
```

---

## Tips for Success

### 1. Project Selection
- Focus on **high-volume, repetitive** processes
- Prioritize processes with **structured data**
- Start with processes having **clear rules**

### 2. Accurate Estimation
- Be realistic about handle times
- Include all applications involved
- Consider peak periods

### 3. Portfolio Management
- Maintain a mix of Quick Wins and Strategic projects
- Quick Wins: 40% of portfolio
- Strategic: 40% of portfolio  
- Fill-ins: 15% of portfolio
- Nice to Have: 5% of portfolio

### 4. Regular Reviews
- Update project statuses weekly
- Recalculate ROI with actual data
- Track realized vs estimated benefits

---

## Troubleshooting

### Excel File Issues
- File is created automatically on first save
- Located in same folder as `app.py`
- Can be edited manually - app reads on restart

### Calculation Questions
- All formulas in `calculations.py`
- Constants in `config.py`
- Modify multipliers to match your organization

### Deployment Issues
- Ensure all files are in repository
- Check requirements.txt is complete
- Streamlit Cloud has free tier limits

---

## Future Enhancements Ideas

1. **Monte Carlo Simulation** - Risk analysis for estimates
2. **Process Mining Integration** - Auto-discover processes
3. **Benefits Tracking** - Actual vs estimated
4. **Multi-user Support** - Team collaboration
5. **API Integration** - Connect to UiPath Orchestrator
6. **Advanced Analytics** - ML-based predictions

---

## Support & Maintenance

### Regular Maintenance
- Export Excel backup weekly
- Review and update multipliers quarterly
- Archive completed projects annually

### Customization Support
All configuration is in two files:
- `config.py` - All constants and categories
- `calculations.py` - All formulas

No need to modify `app.py` unless adding new features!

---

## License & Credits

Created for RPA Portfolio Management - 2026 Planning
Built with Streamlit, Pandas, and Plotly
Excel integration via OpenPyXL

---

*Last Updated: January 2025*