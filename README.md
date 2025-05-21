# 🩺 Diabetes Prediction using Logistic Regression

This is an end-to-end machine learning project that predicts whether a person is diabetic or not using logistic regression. The project includes a clean user interface built with Flask, and the model is trained using the Pima Indians Diabetes dataset.

## 🚀 Features

- Logistic Regression for binary classification
- Web form for input using Flask
- Scikit-learn model saved with `joblib`
- Scaler for consistent prediction
- Clean, beginner-friendly project structure
- Ready for deployment (Elastic Beanstalk compatible)

---

## 📁 Project Structure

```
diabetes_project/
│
├── application.py          # Flask app (rename to app.py for local use)
├── diabetes.csv            # Dataset used
├── model.pkl               # Trained logistic regression model
├── scaler.pkl              # StandardScaler used during preprocessing
├── requirements.txt        # Python dependencies
├── templates/
│   └── index.html          # Web form for user input
└── .ebextensions/
    └── python.config       # Beanstalk configuration (optional)
```

---

## 📊 Dataset

- **Source**: Pima Indians Diabetes Dataset
- **Features**:
  - Pregnancies
  - Glucose
  - Blood Pressure
  - Skin Thickness
  - Insulin
  - BMI
  - Diabetes Pedigree Function
  - Age
- **Target**: Outcome (0 = Non-diabetic, 1 = Diabetic)

---

## 🧪 How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/diabetes-logistic-regression.git
   cd diabetes-logistic-regression
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask app:
   ```bash
   python application.py
   ```

5. Open in browser:
   ```
   http://127.0.0.1:5000/
   ```

---

## 🌐 Deployment (Optional)

To deploy this app on AWS Elastic Beanstalk:

- Rename `app.py` to `application.py`
- Add the `.ebextensions/python.config` file
- Use the EB CLI: `eb init`, `eb create`, `eb deploy`

---

## 📷 Screenshot

> _Include a screenshot of your running app here if you'd like!_

---

## 🤝 Contributing

Feel free to fork this repo and improve it! Pull requests are welcome.

---

## 📜 License

This project is licensed under the MIT License.
