# Expense Tracker CLI

A lightweight, robust command-line interface (CLI) application built in Python for monitoring personal expenses. This system utilizes structural JSON file handling for persistent database storage, ensuring your ledger records are saved securely even after closing the terminal.

## 🚀 Features Implemented

- **1. Add Expense**: Securely captures item descriptions, custom categories, and numeric amount values.
- **2. View Expenses**: Displays all running transactions inside a clean, perfectly aligned tabular ledger grid.
- **3. Delete Expense**: Purges selected tracking rows using their unique ID with automated sequential re-indexing.
- **4. Total Spending Calculations**: Computes aggregate spending profiles and breaks down metrics category-wise.
- **5. Persistent Storage**: Auto-generates and updates a JSON database layer to prevent data loss.

## 📂 Project Directory Structure

Your project should be organized according to the following industry standard layout:

```text
expense-tracker/
├── .gitignore               # Excludes cache and environmental garbage
├── README.md                # Project documentation layout manifest
├── data/
│   └── expenses.json        # Auto-generated persistent JSON database
└── src/
    └── expense_tracker.py   # Main core application source code file
