# 💼 SkillScan: Job Market Analytics

SkillScan is a data-driven analytics project that uncovers job market trends by identifying in-demand skills, top-paying job roles, and industry-specific talent needs. Built using SQL and Power BI, it provides actionable insights for job seekers, HR professionals, and market analysts.

---

## 📌 Project Highlights

- 📂 **End-to-End Data Pipeline** using MySQL
- 📊 **Interactive Power BI Dashboard** showcasing trends in skill demand, job location density, salary ranges, and hiring patterns
- 🧠 Realistic simulated job data, designed to mimic real-world job boards (e.g., LinkedIn, Naukri)
- 💡 Business-oriented insights for HR teams and career planning

---

## 🛠 Tech Stack

- **Database**: MySQL
- **Visualization**: Power BI
- **(Optional)**: Python (for data simulation using Faker)

---

## 📁 Features

- 🔍 Track the most demanded tech/non-tech skills across job roles
- 🏙️ Identify top hiring cities and job density by region
- 💰 Analyze salary trends across industries and roles
- 🧩 Understand how industries align with specific skill sets
- 📅 Monthly hiring trend analysis

---

## 🧱 Data Schema (Simplified)

- `Companies`: Company details like name, size, industry  
- `Locations`: City, state, country  
- `JobPostings`: Job roles, salaries, posting dates  
- `Skills`: All unique skills  
- `JobSkills`: Mapping table for many-to-many relationship between jobs and skills  

---



---

## 🚀 Getting Started

1. Clone this repo
2. Set up MySQL and run schema scripts from `/sql-scripts/`
3. Import the Power BI dashboard file (`.pbix`) and connect to your local MySQL database
4. Explore, filter, and interact with live job market insights

---

## 🌱 Future Improvements

- Integrate real-world job data from APIs (LinkedIn, Glassdoor)
- Use NLP to extract skills from job descriptions
- Web-hosted dashboard using Streamlit or Flask

---

## 🙋‍♀️ About the Author

**Dikshita Hate**  
Aspiring data analyst | SQL developer | Passionate about building real-world data solutions

---




