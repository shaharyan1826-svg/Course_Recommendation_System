# Course Recommendation System

## Project Overview
The Course Recommendation System recommends suitable courses to students based on their interests, skills, and career goals. It uses content-based filtering, collaborative filtering, and a hybrid recommendation approach.

## Features
- Course dataset containing 15 courses.
- Student profiles and course ratings.
- Content-based course recommendations.
- Collaborative filtering using student rating similarities.
- Hybrid recommendations combining both approaches.
- Recommendation evaluation using Precision@K and Recall@K.
- Simple web interface built with Flask.

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Flask
- HTML and CSS

## Recommendation Methods

### 1. Content-Based Filtering
Uses TF-IDF vectorization and cosine similarity to compare student interests and career goals with course information.

### 2. Collaborative Filtering
Uses similarities between students' course-rating patterns to recommend courses.

### 3. Hybrid Recommendation
Combines content-based and collaborative scores using equal weights (50% each).

## Project Structure

```text
Course_Recommendation_System/
├── app.py
├── recommendation.py
├── collaborative.py
├── hybrid.py
├── evaluation.py
├── data/
│   ├── courses.csv
│   └── ratings.csv
├── templates/
│   └── index.html
└── tests/
    ├── __init__.py
    └── test_recommendation.py
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/Course-Recommendation-System.git
```

2. Open the project folder:

```bash
cd Course-Recommendation-System
```

3. Create and activate a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
python app.py
```

Open this address in your browser:

```text
http://127.0.0.1:5000
```

Enter student interests, career goals, and a student ID to receive course recommendations.

## Testing

Run the automated tests:

```bash
python -m unittest discover -s tests -v
```

## Evaluation

The project uses:
- Precision@K
- Recall@K

The current evaluation uses an illustrative manually selected relevant-course list. It is not a real-world effectiveness benchmark.

## Dataset

The project includes:
- `courses.csv`: 15 sample courses with categories, skills, career goals, and descriptions.
- `ratings.csv`: Sample student-course ratings.

**Note:** The student ratings are synthetic sample data created for this project.

## Limitations
- The dataset is small and uses sample data.
- Collaborative filtering may be less effective for new students with no ratings.
- Evaluation results are illustrative and depend on the manually selected relevant courses.

## Future Improvements
- Add a larger real-world course dataset.
- Collect actual student feedback and ratings.
- Improve recommendation evaluation.
- Add student registration and profile management.
- Deploy the application online.

## Author
Aryan

## License
This project is created for educational and internship purposes.
