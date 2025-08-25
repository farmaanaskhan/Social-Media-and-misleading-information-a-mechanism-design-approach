Social Media and Misleading Information in Democracy – A Mechanism Design Approach
📌 Overview

This project addresses the critical issue of misinformation on social media and its impact on democratic processes. By combining Machine Learning (ML) with Mechanism Design principles, the system detects misleading content in social media posts and proposes a framework for incentivizing platforms to filter misinformation responsibly.

The project was developed as part of the Bachelor of Technology (B.Tech) – CSE (Data Science) program at JNTU Hyderabad (SVIT, Secunderabad campus).

✨ Features

🔹 Fake News Detection: Classifies social media posts as factual or misleading.

🔹 ML Models: Decision Tree, Logistic Regression, and Random Forest.

🔹 Text Processing: Includes cleaning, tokenization, stemming/lemmatization, and TF-IDF vectorization.

🔹 User Roles:

Remote User – Register, log in, and test news for misinformation.

Admin – Upload datasets, train/test models, monitor accuracy, and manage users.

🔹 Visualization: Accuracy comparison charts, pie charts, and prediction summaries.

🔹 Mechanism Design Approach: Models the interaction between governments and social media platforms to encourage truth-preserving behavior.

🛠️ Tech Stack

Frontend: HTML, CSS, JavaScript

Backend: Python (Django Framework)

Database: MySQL (WAMP Server)

ML Libraries: scikit-learn, NumPy, pandas

📂 Project Structure
├── Remote_User/          # Remote user module
├── Service_Provider/     # Admin/Service provider module
├── social_mediaand_misleading_information/ # Core Django project
├── Template/             # HTML, CSS, JS, and media files
└── manage.py             # Django project manager

⚙️ Installation & Setup

Clone the Repository

git clone https://github.com/yourusername/social-media-misinformation.git
cd social-media-misinformation


Set up Virtual Environment

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate


Install Dependencies

pip install -r requirements.txt


Configure Database (MySQL)

Create a database social_mediaand_misleading_information

Update credentials in settings.py

Run Migrations

python manage.py migrate


Start Server

python manage.py runserver


Open in browser:

http://127.0.0.1:8000/

📊 Example Outputs

Accuracy results from multiple ML models

Comparative training charts (Bar Chart, Pie Chart)

User prediction results

🚀 Future Enhancements

Integration of Deep Learning models (RNN, LSTM, BERT)

Real-time detection of misinformation on live social media feeds

Multi-lingual and cross-platform datasets

Addition of sentiment analysis

Development of a dashboard with advanced analytics

📖 References

The project is based on academic research, including works by Allcott & Gentzkow (2017), Vosoughi et al. (2018), and others on misinformation and mechanism design.

👨‍💻 Author

Mohammed Farmaan Khan
B.Tech (CSE - Data Science) | JNTU Hyderabad
