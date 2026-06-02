# Expense Tracker CLI

A lightweight Command Line Interface (CLI) application developed in Python. This system allows users to track personal financial streams by recording daily expenses, categorizing transactions, calculating total investments, and persisting data to a local JSON file.

---

## 🛠️ Key Features

### 1. Structured CRUD Operations
* **Create**: Add transaction records with input validation (including blank checks, type safety, and boundary validation).
* **Read**: Display the stored transaction history in a clear, tabular layout.
* **Delete**: Remove specific records using their assigned sequential ID keys.

### 2. Live Analytics Dashboard
* Calculates real-time total expenses dynamically across the JSON data array.
* Groups transactions by category to show individual sub-total metrics.

### 3. Data Integrity & Resilience
* Automatic verification of database structures (creates the storage file and folder if missing at launch).
* Error-handling boundaries prevent application crashes during invalid terminal input or JSON parsing errors.

### 4. Sequential Re-indexing
* To keep indices intuitive, removing a record triggers an automated sequential re-indexing process, reorganizing all remaining IDs starting from `1` to `N`.

---

## 📂 Project Structure

The project follows a modular structure, keeping core runtime files separate from persistent database stores:

```text
expense-tracker/
├── .gitignore               # Excludes Python cache files and system configurations
├── README.md                # System manual and developer documentation
├── data/
│   └── expenses.json        # Persistent JSON storage file
└── src/
    └── expense_tracker.py   # Main core system runtime application engine
```

---

## ⚙️ Development Setup

### Prerequisites

* **Python 3.8** or higher installed on your machine.
* A configured **Git** environment.

### Installation & Execution

1. **Clone the repository**:
   ```bash
   git clone https://github.com/vivekjoshi2006/Expense-Tracker.git
   cd expense-tracker
   ```

2. **Verify repository status**:
   ```bash
   git status
   ```

3. **Run the application**:
   ```bash
   python src/expense_tracker.py
   ```

---

## 💡 How It Works

### Storage Lifecycle
When you launch the program, the script inspects its environment. If the `/data` directory or `expenses.json` do not exist, they are generated dynamically as an empty JSON array.

```json
[
  {
    "id": 1,
    "amount": 25.50,
    "category": "Food",
    "description": "Lunch at cafe",
    "date": "2026-06-02"
  }
]
```

All interactions use standard UTF-8 stream writing, organizing entries with standard 4-space indentation layouts for readable local inspection.

---

## 📝 Git Workflow Log

This project was developed incrementally using structured commit phases:

```bash
# Phase 1: Environment Definition
git add .gitignore README.md
git commit -m "Initial project setup"

# Phase 2: Engine Integration
git add src/expense_tracker.py
git commit -m "Add expense + file save"

# Phase 3: Analytics Deployment
git commit --allow-empty -m "Add view, delete, total"
```

---

## 🛡️ License & Code Standards

* Developed in compliance with standard **PEP 8** style guidelines to encourage clean structure, coherent naming conventions, and consistent formatting.
* Licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute this codebase.
