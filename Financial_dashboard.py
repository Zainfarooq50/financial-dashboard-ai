import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlsxwriter
from GPT_utils_fin import get_ai_insights


# ---------------- Main Financial Dashboard ----------------
def generate_financial_dashboard(data_file="finance_data.csv", output_folder="outputs"):
    """
    Generates a Financial Dashboard with KPIs, charts, and AI insights.
    """
    os.makedirs(output_folder, exist_ok=True)

    # Load Data
    try:
        df = pd.read_csv(data_file)
    except FileNotFoundError:
        print(f"❌ File '{data_file}' not found.")
        return

    print("✅ Data Loaded:\n", df.head())

    # Key Financial KPIs
    total_revenue = df["Revenue"].sum()
    total_expenses = df["Expenses"].sum()
    total_profit = df["Profit"].sum()

    print(f"\n📊 Total Revenue: {total_revenue:,.2f}")
    print(f"📊 Total Expenses: {total_expenses:,.2f}")
    print(f"📊 Total Profit: {total_profit:,.2f}")

    # ---------------- Visualizations ----------------

    # Revenue by Department (Bar Chart)
    dep_summary = df.groupby("Department")["Revenue"].sum().reset_index()
    plt.figure(figsize=(8, 5))
    plt.bar(dep_summary["Department"], dep_summary["Revenue"], color="skyblue")
    plt.title("Revenue by Department")
    plt.xlabel("Department")
    plt.ylabel("Total Revenue ($)")
    plt.tight_layout()
    plt.savefig(f"{output_folder}/Revenue_by_Department.png")
    plt.close()

    # Profit Contribution by Department (Pie Chart)
    profit_summary = df.groupby("Department")["Profit"].sum().reset_index()
    plt.figure(figsize=(6, 6))
    plt.pie(profit_summary["Profit"], labels=profit_summary["Department"], autopct="%1.1f%%", startangle=140)
    plt.title("Profit Contribution by Department")
    plt.tight_layout()
    plt.savefig(f"{output_folder}/Profit_Contribution.png")
    plt.close()

    # Financial Trends Over Time
    df_sorted = df.sort_values("Date").copy()
    df_sorted["Date"] = pd.to_datetime(df_sorted["Date"])
    plt.figure(figsize=(10, 6))
    plt.plot(df_sorted["Date"], df_sorted["Revenue"], label="Revenue", color="green")
    plt.plot(df_sorted["Date"], df_sorted["Expenses"], label="Expenses", color="red")
    plt.plot(df_sorted["Date"], df_sorted["Profit"], label="Profit", color="blue")
    plt.title("Financial Trends Over Time")
    plt.xlabel("Date")
    plt.ylabel("Amount ($)")
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"{output_folder}/Financial_Trends.png")
    plt.close()

    # High vs Low Profit Months (Pie Chart)
    df_sorted["Performance"] = np.where(df_sorted["Profit"] > df_sorted["Profit"].mean(), "High", "Low")
    perf_counts = df_sorted["Performance"].value_counts()
    plt.figure(figsize=(6, 6))
    plt.pie(perf_counts, labels=perf_counts.index, autopct="%1.1f%%", startangle=140, colors=["gold", "lightcoral"])
    plt.title("High vs Low Profit Months")
    plt.tight_layout()
    plt.savefig(f"{output_folder}/Profit_Performance.png")
    plt.close()

    # ---------------- AI Insights ----------------

    summary_text = (
        f"Total Revenue: {total_revenue:,.2f}\n"
        f"Total Expenses: {total_expenses:,.2f}\n"
        f"Total Profit: {total_profit:,.2f}\n"
        f"Total Departments: {df['Department'].nunique()}\n"
        f"High Profit Months: {perf_counts.get('High', 0)}\n"
        f"Low Profit Months: {perf_counts.get('Low', 0)}\n"
    )

    ai_text = get_ai_insights(summary_text)
    print("\n🤖 AI Generated Insights:\n", ai_text)

    with open(f"{output_folder}/AI_Insights.txt", "w", encoding="utf-8") as f:
        f.write(f"Summary:\n{summary_text}\n\nAI Insights:\n{ai_text}")

    # ---------------- Excel Report ----------------
    excel_path = f"{output_folder}/Full_Financial_Report.xlsx"
    writer = pd.ExcelWriter(excel_path, engine="xlsxwriter")

    df_sorted.to_excel(writer, sheet_name="Raw_Data", index=False)
    dep_summary.to_excel(writer, sheet_name="Revenue_by_Department", index=False)
    profit_summary.to_excel(writer, sheet_name="Profit_by_Department", index=False)

    workbook = writer.book
    ws = writer.sheets["Revenue_by_Department"]

    ws.insert_image("D2", f"{output_folder}/Revenue_by_Department.png")
    ws.insert_image("D20", f"{output_folder}/Profit_Contribution.png")

    ws_trend = workbook.add_worksheet("Trends")
    ws_trend.insert_image("B2", f"{output_folder}/Financial_Trends.png")

    ws_perf = workbook.add_worksheet("Profit_Performance")
    ws_perf.insert_image("B2", f"{output_folder}/Profit_Performance.png")

    ws_ai = workbook.add_worksheet("AI_Insights")
    ws_ai.write("A1", "Summary:")
    ws_ai.write("A2", summary_text)
    ws_ai.write("A7", "AI Insights:")
    ws_ai.write("A8", ai_text)

    writer.close()

    print("\n✅ Charts & AI Insights saved to 'outputs' folder.")
    print(f"✅ Full Financial Report saved to '{excel_path}'")


# ---------------- Script Entry ----------------
if __name__ == "__main__":
    generate_financial_dashboard()
