
## Project Structure

```
Data Science/
│
├── Question_1_to_12.ipynb     Main Data Science notebook (EDA -> ML)
├── vgsalesGlobale.csv         Dataset: Video game global sales
├── Mall_Customers.csv         Dataset: Mall customer segmentation
├── model.pkl                  Saved trained ML model
│
├── Question_13/
│   └── main.py                REST API serving Iris flower predictions
│
├── Question_14/
│   ├── Scrape.py            Web scraper: quotes + authors
│   └── quotes.csv           Output: scraped quotes exported to CSV
│
├── Question_15/
│   ├── Selenium.py            Browser automation: login + data extraction
│   └── extracted_data.json    Output: data extracted after login
│
└── .gitignore               Ignores FastAPI cache files
```

---

## Project - Data Science Notebook (`Question_1_to_12.ipynb`)

The main notebook. Covers the full data science workflow from raw CSV to trained ML model.

**Dataset used:** `vgsalesGlobale.csv` — Video game sales across NA, EU, JP and global markets.

### What it covers (step by step):

| Step | Topic | What was done |
|------|-------|---------------|
| 1 | EDA | Loaded CSV, ran `.head()`, `.info()`, `.describe()` |
| 2 | Missing Values | Filled `Year` with median, `Publisher` with "Unknown" |
| 3 | Duplicates | Removed duplicate rows |
| 4 | Encoding | Label Encoding for Platform, Genre, Publisher — One-Hot for Name |
| 5 | Visualizations | Bar chart (genres), Line chart (sales by year), Scatter (NA vs Global sales) |
| 6 | Outlier Treatment | Boxplot + IQR method to remove extreme Global Sales values |
| 7 | Feature Engineering | Created `Total_Sales`, `NA_ratio`, and binary `target` column |
| 8 | Scaling | StandardScaler (mainly used for LR) and MinMaxScaler (mainly used for KMeans) |
| 9 | Train/Test Split | 70/30 split |
| 10 | Logistic Regression | Trained + evaluated with accuracy, confusion matrix, classification report |
| 11 | Decision Tree | Trained + compared with Logistic Regression |
| 12 | K-Means Clustering | Elbow method to find optimal K, clustered Mall customers into 5 groups |

### Key finding:
Decision Tree outperformed Logistic Regression on this dataset — achieving near-perfect accuracy with 0 false positives and 0 false negatives.

### How to run:
```bash
pip install pandas scikit-learn matplotlib seaborn jupyter
jupyter notebook Question_1_to_12.ipynb
```

---

## Project - FastAPI Prediction API (`Question_13/`)

A lightweight REST API that serves Iris flower species predictions.

**File:** `Question_13/main.py`

### How it works:
1. Trains a Random Forest model on the built-in Iris dataset when the server starts
2. Exposes two endpoints - a health check and a prediction route
3. User sends 3 flower measurements - API returns the predicted species

### Endpoints:

| Method | Route | Description |
|--------|-------|-------------|
| GET | `/` | Health check — confirms API is running |
| POST | `/predict` | Send measurements, get species prediction back |

### Example request:
```json
POST /predict
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

### Example response:
```json
{
  "species": "setosa",
  "message": "This flower is most likely a setosa!"
}
```

### How to run:
```bash
pip install fastapi uvicorn scikit-learn
uvicorn main:app --reload
```
Then open: `http://localhost:8000/docs` for the interactive playground.

---

##  Project — Web Scraper (`Question_14/`)

Scrapes quotes, authors, and tags from a practice website and exports them to a CSV file.

**File:** `Question_14/Scrape.py`
**Output:** `Question_14/quotes.csv`

**Practice website used:** `https://quotes.toscrape.com` (built for scraping practice)

### What it scrapes:
- Quote text
- Author name
- Tags (comma-separated)

### How it works:
1. `requests` downloads the page HTML (like a browser fetching a webpage)
2. `BeautifulSoup` reads the HTML and finds all quote blocks
3. Extracts text, author, and tags from each block
4. `pandas` converts the list to a DataFrame
5. Exports to `quotes.csv`

### Sample output (`quotes.csv`):
```
quote, author, tags
"The world as we have created it...", Albert Einstein, "change, thinking, world"
"It is our choices Harry...", J.K. Rowling, "abilities, choices"
```

### How to run:
```bash
pip install requests beautifulsoup4 pandas
python Scrape.py
```

---

##  Project - Browser Automation (`Question_15/`)

Automates a real Chrome browser using Selenium — logs into a website and extracts page data automatically.

**File:** `Question_15/Selenium.py`
**Output:** `Question_15/extracted_data.json`

**Practice website used:** `https://the-internet.herokuapp.com/login` (built for Selenium practice)

### What it does:
1. Opens Chrome browser automatically
2. Navigates to the login page
3. Types username and password into the form
4. Clicks the login button
5. Verifies login success via the flash message
6. Extracts page title, URL, heading, paragraph text
7. Saves everything to `extracted_data.json`
8. Clicks logout and closes the browser

### Login credentials used (public test account):
```
Username: tomsmith
Password: SuperSecretPassword!
```

### How to run:
```bash
pip install selenium webdriver-manager
python Selenium.py
```

> **Tip:** Set `options.headless = False` in the script to watch the browser work in real time — great for understanding what each line does.

---



## Datasets

| File | Description | Rows | Key Columns |
|------|-------------|------|-------------|
| `vgsalesGlobale.csv` | Global video game sales data | ~16,000 | Name, Platform, Year, Genre, NA_Sales, Global_Sales |
| `Mall_Customers.csv` | Mall customer segmentation data | 200 | Age, Annual Income, Spending Score |

---

## Tech Stack

| Tool | Used For |
|------|----------|
| Python | All projects |
| Pandas | Data loading, manipulation, CSV export |
| Scikit-learn | ML models (Logistic Regression, Decision Tree, K-Means, encoders, scalers) |
| Matplotlib + Seaborn | Visualizations |
| FastAPI + Uvicorn | REST API server |
| Selenium | Browser automation |
| Requests + BeautifulSoup | Web scraping |
| Jupyter Notebook | Main data science workflow |

---

## Quick Start (Run Everything)

```bash
# 1. Install all dependencies
pip install pandas scikit-learn matplotlib seaborn jupyter fastapi uvicorn selenium webdriver-manager requests beautifulsoup4

# 2. Run the notebook
jupyter notebook 1.ipynb

# 3. Run the API
cd Question_13 && uvicorn main:app --reload

# 4. Run the browser automation
cd Question_15 && python Selenium.py

# 5. Run the scraper
cd Question_14 && python Scrape.py
```

---

## Notes

- `model.pkl` is the saved trained model from the notebook — can be loaded with `pickle.load()` for reuse without retraining
- `Question_13/__pycache__` is ignored via `.gitignore` — no need to push compiled files
- All practice websites used (`the-internet.herokuapp.com`, `quotes.toscrape.com`) are publicly available and built specifically for learning automation and scraping
