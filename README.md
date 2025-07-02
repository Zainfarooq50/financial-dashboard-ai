# AI-Powered Financial Dashboard with Visuals & Insights

This Python tool generates a complete financial dashboard from raw business data. It includes interactive charts, performance breakdowns, and AI-generated financial insights using OpenAI's GPT model. Perfect for finance teams, analysts, and business decision-makers.

---

## ⚡ Features
✅ Loads and analyzes financial data from CSV files  
✅ Calculates KPIs: Revenue, Expenses, Profit, Department performance  
✅ Auto-generates visual charts:  
- Revenue by Department (Bar Chart)  
- Profit Contribution by Department (Pie Chart)  
- Financial Trends Over Time (Line Chart)  
- High vs Low Profit Months (Pie Chart)  
✅ AI-generated business insights using GPT  
✅ Saves outputs as PNG images and a structured Excel report  

---

## 🛠️ Requirements
- Python 3.x  
- `pandas`, `numpy`, `matplotlib`, `xlsxwriter`  
- `GPT_utils_fin.py` for AI integration (requires OpenAI API key)  

---

## 🚀 How to Use
1. Paste your OPENAI key in .env file.  
2. Prepare your financial CSV file with columns:  
   `Date`, `Department`, `Revenue`, `Expenses`, `Profit`  
3. Run the script:  
   ```bash
   python Financial_dashboard.py
All charts, insights, and the Excel report will be saved in the outputs folder

📁 Example Output Structure
Copy
Edit
outputs/
├── Revenue_by_Department.png
├── Profit_Contribution.png
├── Financial_Trends.png
├── Profit_Performance.png
├── AI_Insights.txt
├── Full_Financial_Report.xlsx
🤖 AI Integration
Model: GPT-3.5-Turbo

Provides automated, business-focused financial insights

Insights embedded directly into the report files

💼 Ideal Use Cases
✔ Financial dashboards for businesses or startups
✔ Automated performance reporting
✔ AI-powered finance summaries for management
✔ Visual tools for data-driven decision making
