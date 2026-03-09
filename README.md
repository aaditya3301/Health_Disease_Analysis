# Heart Disease Analysis - Flask Web Application

A Flask web application that embeds **Tableau Dashboards and Stories** for interactive heart disease data analysis. The app provides real-time access to visualizations covering gender, race, diabetes, smoking, alcohol impact, and more.

---

## Project Overview

Heart disease remains one of the leading causes of mortality worldwide. This project uses **Tableau** as a data visualization tool to analyze heart disease data and presents the results through a modern **Flask web application**.

### Key Visualizations
- **Gender vs Heart Disease** — Compare disease count between male and female patients
- **Diabetic vs Stroke** — Correlation between diabetes, stroke, and heart disease
- **Race-wise Heart Disease** — Distribution across racial demographics
- **Impact of Smoking & Alcohol** — How lifestyle choices affect heart disease risk

### Story Scenes
1. Gender Suffering from Heart Disease
2. Effect of Physical Activity on Heart Disease
3. Diabetes Affecting Heart Disease
4. Impact of Smoking and Alcohol on Stroke
5. Ethnicity-wise Heart Disease Count
6. People Suffering from Diabetes by Age Category

---

## Tech Stack

| Technology | Purpose |
|---|---|
| **Python / Flask** | Web framework for serving pages |
| **Tableau Public** | Interactive dashboards and stories |
| **HTML5 / CSS3** | Frontend UI |
| **Font Awesome** | Icons |
| **Google Fonts (Inter)** | Typography |

---

## Project Structure

```
Heart-Disease-Analysis/
├── app.py                    # Flask application (main entry point)
├── requirements.txt          # Python dependencies
├── README.md                 # This file
├── templates/
│   ├── base.html             # Base template with navbar & footer
│   ├── home.html             # Home page with hero & features
│   ├── about.html            # About page with project details
│   ├── dashboard.html        # Embedded Tableau Dashboard
│   ├── story.html            # Embedded Tableau Story
│   └── contact.html          # Contact form
└── static/
    ├── css/
    │   └── style.css         # All styles
    └── images/
        └── hero-illustration.svg
```

---

## Setup & Installation

### Prerequisites
- Python 3.8+
- pip

### Steps

1. **Clone / navigate to the project folder**
   ```bash
   cd Heart-Disease-Analysis
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   venv\Scripts\activate        # Windows
   # source venv/bin/activate   # Mac/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Tableau URLs**

   Open `app.py` and replace the placeholder URLs with your actual Tableau Public embed URLs:
   ```python
   TABLEAU_DASHBOARD_URL = "https://public.tableau.com/views/YourWorkbook/Dashboard"
   TABLEAU_STORY_URL = "https://public.tableau.com/views/YourWorkbook/Story"
   ```

   > **How to get Tableau embed URLs:**
   > 1. Open your workbook on [Tableau Public](https://public.tableau.com/)
   > 2. Click the **Share** button on the viz
   > 3. Copy the URL (it looks like `https://public.tableau.com/views/WorkbookName/SheetName`)

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Open in browser**
   ```
   http://localhost:5000
   ```

---

## Pages

| Page | Route | Description |
|---|---|---|
| Home | `/` | Hero section, features, scenarios, CTA |
| About | `/about` | Project overview, team, skills |
| Dashboard | `/dashboard` | Embedded Tableau Dashboard |
| Story | `/story` | Embedded Tableau Story |
| Contact | `/contact` | Contact form |

---

## Real-World Scenarios

- **Dr. Sharma (Cardiologist)** — Uses dashboards to identify high-risk patient groups by age, gender, BMI, and smoking habits
- **Ramesh (Health Policy Maker)** — Studies regional trends to recommend fitness programs and tobacco regulations
- **Anita (Individual)** — Monitors personal risk factors against healthy benchmarks

---

## Team Members

| Name | Role |
|---|---|
| Aaditya Singhal | Team Lead |
| Aalap Raj | Member |
| Aashi Chaudhary | Member |
| Aastha Sheoran | Member |

---

## Skills Used

- Data Analysis
- Data Visualization
- Flask (Web Framework)
- Dashboard Design
- Tableau (Business Intelligence)
- SQL

---

## Publishing to Tableau Public

1. In Tableau Desktop → **File > Save to Tableau Public**
2. Sign in with your Tableau Public credentials
3. Name your workbook and click **Save**
4. Copy the published URL and paste it into `app.py`

---

## License

This project is for educational purposes as part of the Heart Disease Analysis group project.
