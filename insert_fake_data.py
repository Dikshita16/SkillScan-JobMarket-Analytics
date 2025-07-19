import pymysql
from faker import Faker
import random

fake = Faker()
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='Hatte@1604',  # Replace with your MySQL password
    database='skillscan'
)
cursor = connection.cursor()

# Sample skill pool
skills = ['Python', 'SQL', 'Java', 'JavaScript', 'C++', 'HTML', 'CSS', 'Excel', 'Data Analysis', 'Machine Learning']

# Insert skills (ignore duplicates)
for skill in skills:
    try:
        cursor.execute("INSERT IGNORE INTO Skills (skill_name) VALUES (%s)", (skill,))
    except:
        pass

# Insert companies
for _ in range(20):
    name = fake.company()
    industry = fake.job()
    size = random.choice(['Small', 'Medium', 'Large'])
    cursor.execute("INSERT INTO Companies (name, industry, size) VALUES (%s, %s, %s)", (name, industry, size))

# Insert locations
for _ in range(15):
    city = fake.city()
    state = fake.state()
    country = fake.country()
    cursor.execute("INSERT INTO Locations (city, state, country) VALUES (%s, %s, %s)", (city, state, country))

# Get company and location IDs
cursor.execute("SELECT company_id FROM Companies")
company_ids = [row[0] for row in cursor.fetchall()]
cursor.execute("SELECT location_id FROM Locations")
location_ids = [row[0] for row in cursor.fetchall()]
cursor.execute("SELECT skill_id FROM Skills")
skill_ids = [row[0] for row in cursor.fetchall()]

# Insert job postings and assign skills
for _ in range(100):
    company_id = random.choice(company_ids)
    location_id = random.choice(location_ids)
    role_title = fake.job()
    posted_date = fake.date_between(start_date='-6M', end_date='today')
    salary_min = random.randint(30000, 60000)
    salary_max = salary_min + random.randint(10000, 50000)
    
    cursor.execute("""
        INSERT INTO JobPostings (company_id, role_title, location_id, posted_date, salary_min, salary_max)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (company_id, role_title, location_id, posted_date, salary_min, salary_max))
    
    job_id = cursor.lastrowid
    skill_sample = random.sample(skill_ids, k=random.randint(2, 5))
    for sid in skill_sample:
        cursor.execute("INSERT INTO JobSkills (job_id, skill_id) VALUES (%s, %s)", (job_id, sid))

connection.commit()
connection.close()
print("✅ Data insertion completed!")
