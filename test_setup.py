"""
Test script to verify everything is working
"""

import streamlit as st
from calculations import RPACalculator
import config

st.title("🧪 Testing RPA Setup")

# Test 1: Configuration loaded
st.header("1️⃣ Configuration Test")
st.write("Frequency multipliers loaded:", config.FREQUENCY_MULTIPLIERS)
st.success("✅ Config loaded successfully!")

# Test 2: Calculator working
st.header("2️⃣ Calculator Test")
calc = RPACalculator()

# Test with sample data
test_volume = calc.calculate_annual_volume('Daily', 10)
test_hours = calc.calculate_annual_hours(test_volume, 30)
test_fte = calc.calculate_fte_required(test_hours)

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Annual Volume", f"{test_volume:,.0f}")
with col2:
    st.metric("Annual Hours", f"{test_hours:,.0f}")
with col3:
    st.metric("FTE Required", f"{test_fte:.2f}")

st.success("✅ Calculator working!")

# Test 3: Interactive calculation
st.header("3️⃣ Interactive Test")

frequency = st.selectbox("Frequency", list(config.FREQUENCY_MULTIPLIERS.keys()))
volume = st.number_input("Volume per frequency", value=10, min_value=1)
handle_time = st.slider("Handle time (minutes)", 5, 120, 30)

if st.button("Calculate"):
    annual_vol = calc.calculate_annual_volume(frequency, volume)
    annual_hrs = calc.calculate_annual_hours(annual_vol, handle_time)
    fte = calc.calculate_fte_required(annual_hrs)

    # Calculate automation potential
    potential = calc.calculate_automation_potential(
        'Agree', 'Agree', 'Agree', 'Agree', annual_vol, 'Structured (Excel, CSV, Database)'
    )

    ease = calc.calculate_implementation_ease(
        2, 'Linear - Straight-through', 'Desktop Applications', 'Structured (Excel, CSV, Database)'
    )

    st.write("### Results:")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Automation Potential", f"{potential:.1f}%")
        st.metric("FTE Savings", f"{fte * 0.8:.2f}")  # 80% efficiency
    with col2:
        st.metric("Implementation Ease", f"{ease:.1f}%")
        quadrant = calc.determine_quadrant(potential, ease)
        st.metric("Quadrant", quadrant)

st.header("4️⃣ All Systems Check")
st.balloons()
st.success("🎉 Everything is working! Ready to build the full app!")