import streamlit as st
import pandas as pd
import re

# --- Helper Functions ---
def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool(re.match(pattern, str(email).strip()))

def validate_phone(phone):
    phone = re.sub(r'\D', '', str(phone))
    return len(phone) >= 10

def score_lead(row):
    score = 0
    if row['Valid Email']: score += 40
    if row['Valid Phone']: score += 30
    if pd.notna(row.get('Company')) and row.get('Company') != '': score += 10
    if pd.notna(row.get('Role')) and row.get('Role') != '': score += 10
    if row['Valid Email'] and row['Valid Phone']: score += 10
    return min(score, 100)

# --- Streamlit UI ---
st.set_page_config(page_title="Smart Lead Quality Validator", layout="centered")
st.title("🧠 Smart Lead Data Validator")
st.write("Upload your raw lead CSV file to clean, validate, and score lead quality.")

uploaded_file = st.file_uploader("📂 Upload CSV File", type=["csv"])

if uploaded_file:
    # Read CSV safely
    df = pd.read_csv(uploaded_file)
    
    # Ensure all required columns exist
    required_cols = ['Name', 'Email', 'Phone', 'Company', 'Role']
    for col in required_cols:
        if col not in df.columns:
            st.error(f"Column '{col}' is missing in the CSV.")
            st.stop()

    # --- Clean & Validate ---
    df['Valid Email'] = df['Email'].apply(is_valid_email)
    df['Valid Phone'] = df['Phone'].apply(validate_phone)
    df['Lead Score'] = df.apply(score_lead, axis=1)
    
    # Mark invalid emails/phones for easy visibility
    df['Email Status'] = df['Valid Email'].apply(lambda x: "✅ Valid" if x else "❌ Invalid")
    df['Phone Status'] = df['Valid Phone'].apply(lambda x: "✅ Valid" if x else "❌ Invalid")

    # Remove duplicate emails and reset index
    df.drop_duplicates(subset=['Email'], inplace=True)
    df.reset_index(drop=True, inplace=True)

    # --- Stats ---
    valid_emails = df['Valid Email'].sum()
    valid_phones = df['Valid Phone'].sum()
    avg_score = round(df['Lead Score'].mean(), 2)

    st.write("### 📊 Lead Quality Summary")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Leads", len(df))
    col2.metric("Valid Emails", valid_emails)
    col3.metric("Average Lead Score", avg_score)

    # --- Filters ---
    score_filter = st.slider("Minimum Lead Score to Display", 0, 100, 50)
    filtered = df[df['Lead Score'] >= score_filter].reset_index(drop=True)

    st.write(f"### 🎯 Leads with Score ≥ {score_filter}")
    filtered_display = filtered.copy()
    filtered_display.index = filtered_display.index + 1  # start index at 1
    st.dataframe(filtered_display)
    

    # --- Download ---
    csv = filtered.to_csv(index=False).encode('utf-8')
    st.download_button(
        "⬇️ Download Cleaned Leads",
        csv,
        "cleaned_leads.csv",
        "text/csv"
    )

else:
    st.info("Please upload a CSV file to get started.")

