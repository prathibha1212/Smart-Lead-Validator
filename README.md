# Smart Lead Data Validator

**Caprae Challenge Submission – Developer Intern**

A Python tool to enhance the quality of lead generation data.  
It validates emails and phone numbers, removes duplicates, assigns a lead score, and allows filtering and exporting of clean, actionable leads — improving the efficiency of raw scraped lead data.

---

## 📌 Problem Statement

Lead scraping tools like SaaSquatch Leads collect large volumes of potential leads.  
However, these datasets often contain:

- Invalid email addresses  
- Incorrect or incomplete phone numbers  
- Duplicate entries  
- Missing company or role information  

This reduces the efficiency of sales outreach and increases manual effort.  
This project provides a **quality-first approach** to ensure leads are validated, scored, and ready for use.

---

## ⚙️ Features

- **Email Validation:** Checks for proper email format using regex.  
- **Phone Validation:** Ensures phone numbers are numeric and have a minimum length.  
- **Duplicate Removal:** Removes duplicate entries based on email.  
- **Lead Scoring:** Assigns a score from 0–100 based on data completeness and validity.  
- **Interactive Filtering:** Filter leads based on minimum lead score.  
- **Export Clean Data:** Download filtered leads as CSV for CRM or ML pipelines.  

---


## 🛠️ Installation & Setup

1. **Clone the repository**
```bash
git clone https://github.com/prathibha1212/Smart-Lead-Validator.git
cd Smart-Lead-Validator
2.**install dependencies**
  pip install -r requirements.txt
3.**Run the Streamlit app **
  streamlit run app.py



