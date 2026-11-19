# 💸 Expensa

A simple expense tracker built with Python and pandas. I made this project to practice what I've learned and to build something real instead of just watching tutorials.

## Features

- Add expenses with a date, category, amount, and description
- View all your expenses in a table
- Data is saved so it's still there next time you run the app
- Basic summary of spending (total, by category)



## Tech Stack

- **Language:** Python 3
- **Data handling:** pandas
- **Storage:** CSV file

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/Expensa.git
   cd Expensa
   ```

2. (Optional) Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate      # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Run the app

```bash
python main.py
```


## Usage

```
1. Add expense
2. View expenses
3. View summary
4. Exit
```

Example entry:

| Date       | Category | Amount | Description |
|------------|----------|--------|-------------|
| 2026-11-19 | Food     | 150    | Lunch       |

## Project Structure

```
Expensa/
├── main.py            # Main application
├── expenses.csv       # Saved expense data
├── requirements.txt   # Dependencies
└── README.md
```

## What I Learned

- Working with pandas DataFrames (including `pd.concat()` since `append()` was removed in pandas 2.0)
- Reading and writing data with CSV files
- Structuring a small project from scratch
- Debugging real errors and reading documentation

## Future Improvements

- [ ] Edit and delete expenses
- [ ] Monthly reports and charts
- [ ] Budget limits with alerts
- [ ] Simple web interface (Flask or Streamlit)
- [ ] Export reports

## Contributing

This is a learning project, but suggestions and feedback are welcome. Feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

---

Made with ☕ while learning to code.
