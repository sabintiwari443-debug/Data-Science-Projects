#  Movie Recommender System

A beginner-friendly **Movie Recommender System** built with Python, Scikit-learn, and Streamlit.  
The system recommends movies similar to a selected title using metadata such as **overview, genres, keywords, cast, and crew**.  

---

## Dataset
We used the **TMDB 5000 Movie Dataset** (available on [Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata))  
- `tmdb_5000_movies.csv` → movie metadata (title, overview, genres, keywords, etc.)  
- `tmdb_5000_credits.csv` → cast and crew information  

---

## Steps in the Project

### 1. Data Collection & Exploration
- Loaded datasets with Pandas  
- Explored data using `.head()`, `.info()`, `.isnull().sum()`, `.duplicated().sum()`  
- Checked dataset structure, missing values, duplicates  

### 2. Data Cleaning & Transformation
- Merged **movies** and **credits** datasets on title  
- Dropped missing values and duplicates  
- Converted JSON-like strings (`genres`, `keywords`, `cast`, `crew`) into lists using `ast.literal_eval`  
- Selected top 3 actors and director  
- Created a new feature `tags` (overview + genres + keywords + cast + crew)  

### 3. Exploratory Data Analysis (EDA)
- Plotted **Top 10 genres, keywords, cast, and directors**  
- Analyzed distribution of overview lengths  
- Found common patterns (Drama/Comedy most frequent genres, some actors/directors dominate dataset)  

### 4. Feature Selection
- Selected relevant features: `overview`, `genres`, `keywords`, `cast`, `crew`  
- Combined into a single column `tags` for modeling  

### 5. Model Development 
- **Supervised ML Demo (for learning)**:  
  - Built a classifier (Logistic Regression) to predict if a movie is Action or not  
  - Evaluated with accuracy, precision, recall, and F1-score  

### 6. Model Evaluation & Tuning
- Compared `CountVectorizer` vs `TF-IDF`  
- Used cross-validation & GridSearchCV (on classification demo) to tune hyperparameters  

### 7. Model Deployment (Streamlit App)
- Built a simple **dashboard with Streamlit**  
- User selects a movie → system recommends top 5 similar movies  
- Run locally:  
  ```bash
  streamlit run app.py
