"""
Configuration file for RPA Project Estimator
Contains all constants, multipliers, and base formulas
"""

# Complexity Multipliers
COMPLEXITY_FACTORS = {
    'data': {
        'Structured (Excel, CSV, Database)': 1.0,
        'Semi-structured (PDF forms, Emails)': 2.0,
        'Unstructured (Scanned docs, Free text)': 3.0
    },
    'applications': {
        1: 1.0, 2: 1.3, 3: 1.5, 4: 1.8, 5: 2.0, 6: 2.5
    },
    'logic': {
        'Linear - Straight-through': 1.0,
        'Moderate - Some branching': 1.5,
        'Complex - Many exceptions': 2.5
    },
    'environment': {
        'API - Direct integration': 0.7,
        'Desktop Applications': 1.5,
        'Web Applications': 2.0,
        'Citrix/Virtual Environment': 4.0,
        'Mainframe/Terminal': 3.0
    }
}

# FTE and ROI Calculations
FTE_CONSTANTS = {
    'annual_work_hours': 2080,
    'productive_hours': 1760,
    'shrinkage_factor': 1.28,
    'automation_efficiency': 0.80,
    'hourly_rate_default': 35
}

# Timeline Factors
TIMELINE_FACTORS = {
    'base_days_per_step': 0.5,
    'testing_factor': 0.30,
    'documentation_factor': 0.15,
    'contingency_buffer': 0.30,
    'daily_rate_default': 1000
}

# Frequency Mappings
FREQUENCY_MULTIPLIERS = {
    'Daily': 260,
    'Weekly': 52,
    'Bi-Weekly': 26,
    'Monthly': 12,
    'Quarterly': 4,
    'Yearly': 1,
    'Hourly': 2080
}

# AI Costs
AI_COSTS = {
    'ocr_per_page': 0.30,
    'nlp_per_1k_tokens': 0.002,
    'cv_per_image': 0.005,
    'ml_custom_model': 7500
}
