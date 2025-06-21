# 💼 In-Hand Salary Calculator (Streamlit App)

**In-Hand Salary Calculator** is a simple and interactive Python web app built using **Streamlit**.  
It helps users estimate their **monthly take-home salary** by calculating standard deductions based on either their **Annual CTC (in LPA)** or **Monthly Gross Salary**.

---

## 🔧 Features

### 📥 Input:
- Choose between:
  - **Annual CTC (LPA)**
  - **Monthly Gross Salary**
- Optional checkbox for:
  - **Health Insurance deduction (₹750/month)**

### 📉 Deductions Applied:
- 🏥 **Provident Fund (PF):** 12% of Basic Salary (Basic = 50% of Gross)
- 🏛️ **Professional Tax:** ₹200/month
- 🩺 **Health Insurance:** ₹750/month (optional)

### 📊 Output:
- Monthly **Gross Salary**
- **Basic Salary**
- Total **Deductions**
- Final **In-Hand Salary**

---

## 🖥️ User Interface

Built using **Streamlit**, the UI is:
- Clean and intuitive
- Uses:
  - 📌 **Numeric Input** for salary
  - 🔘 **Radio Buttons** to choose salary type
  - ☑️ **Checkbox** to include/exclude health insurance

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/in-hand-salary-calculator.git
cd in-hand-salary-calculator

## Install Dependencies
pip install streamlit

### Run the App
streamlit run app.py
