import streamlit as st

# Set page config
st.set_page_config(page_title="Take-Home Salary Calculator", layout="centered")

# Title and description
st.title("Take-Home Salary Calculator")
st.markdown("Enter your salary to calculate your in-hand pay after deductions.")

# Input section
input_type = st.radio("Select Salary Type", ["Annual CTC (LPA)", "Monthly Gross Salary"])
salary = st.number_input(
    "Enter Salary Amount",
    min_value=0.0,
    step=0.1,
    format="%.2f",
    help="Enter Annual CTC in LPA (e.g., 5.0 for 5 LPA) or Monthly Gross Salary in ₹"
)
health_insurance = st.checkbox("Include Health Insurance (₹750/month)", value=False)

# Calculation function
def calculate_take_home_salary(salary, input_type, health_insurance):
    # Convert salary to monthly gross
    if input_type == "Annual CTC (LPA)":
        monthly_gross = (salary * 100000) / 12
    else:
        monthly_gross = salary

    # Assumptions
    basic_salary = monthly_gross * 0.5  # Basic is 50% of gross
    pf = basic_salary * 0.12  # 12% of Basic
    professional_tax = 200  # Fixed ₹200/month
    health_insurance_cost = 750 if health_insurance else 0  # ₹750/month if selected

    # Total deductions
    total_deductions = pf + professional_tax + health_insurance_cost

    # In-hand salary
    in_hand_salary = monthly_gross - total_deductions

    return {
        "monthly_gross": monthly_gross,
        "basic_salary": basic_salary,
        "pf": pf,
        "professional_tax": professional_tax,
        "health_insurance": health_insurance_cost,
        "total_deductions": total_deductions,
        "in_hand_salary": in_hand_salary
    }

# Calculate and display results
if salary > 0:
    results = calculate_take_home_salary(salary, input_type, health_insurance)
    
    # Display results
    st.subheader("Salary Breakdown (Monthly)")
    st.write(f"**Gross Salary**: ₹{results['monthly_gross']:,.2f}")
    st.write(f"**Basic Salary**: ₹{results['basic_salary']:,.2f}")
    st.write(f"**Provident Fund (PF)**: ₹{results['pf']:,.2f}")
    st.write(f"**Professional Tax**: ₹{results['professional_tax']:,.2f}")
    if health_insurance:
        st.write(f"**Health Insurance**: ₹{results['health_insurance']:,.2f}")
    st.write(f"**Total Deductions**: ₹{results['total_deductions']:,.2f}")
    st.markdown(f"**In-Hand Salary**: ₹{results['in_hand_salary']:,.2f}")
else:
    st.info("Please enter a salary amount to see the breakdown.")

# Footer
st.markdown("---")
st.markdown("Built by Karthick Raja | Assumptions: Basic = 50% of Gross, PF = 12% of Basic, Professional Tax = ₹200/month")