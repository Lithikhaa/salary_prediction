# save as 1_generate_synthetic_data.py

import pandas as pd
import numpy as np
import random

company_tiers = {
    'google': 1, 'microsoft': 1, 'amazon': 1, 'apple': 1, 'meta': 1,
    'netflix': 1, 'linkedin': 1, 'adobe': 1, 'salesforce': 1, 'uber': 1,
    'ibm': 2, 'accenture': 2, 'oracle': 2, 'sap': 2, 'deloitte': 2,
    'tcs': 3, 'infosys': 3, 'wipro': 3, 'cts': 3, 'hcl': 3,
    'virtusa': 4, 'hexaware': 4, 'zensar': 4,
    'coforge': 5, 'valuelabs': 5, 'happiest-minds': 5,
}

roles = ['Software Developer', 'Senior Developer', 'Tech Lead', 'QA Engineer',
         'Data Scientist', 'DevOps Engineer', 'Cloud Engineer', 'Business Analyst']

locations = ['Bangalore', 'Hyderabad', 'Chennai', 'Mumbai', 'Pune', 'Delhi', 'Gurgaon']
education_levels = ['Bachelor', 'Master', 'PhD']
certifications = ['None', 'AWS', 'PMP', 'Azure', 'GCP', 'Scrum Master']
skills = ['Cloud', 'AI', 'Security', 'Full Stack', 'Data Engineering', 'DevOps']

data_rows = []

for _ in range(3000):  # generate 3000 samples
    current_company = random.choice(list(company_tiers.keys()))
    target_company = random.choice([c for c in company_tiers if c != current_company])
    current_tier = company_tiers[current_company]
    target_tier = company_tiers[target_company]
    current_role = random.choice(roles)
    gender = random.choices(['Male', 'Female', 'Other'], weights=[0.65, 0.33, 0.02])[0]
    location = random.choice(locations)
    education = random.choice(education_levels)
    cert = random.choice(certifications)
    skill = random.choice(skills)
    years_exp = round(random.uniform(1, 15), 1)
    base_salary = random.randint(400000, 3000000)
    current_ctc = int(base_salary + years_exp * 40000 + random.randint(-50000, 50000))
    hike_factor = random.uniform(1.2, 1.6)
    expected_salary = int(current_ctc * hike_factor)

    data_rows.append({
        'current_company': current_company,
        'target_company': target_company,
        'years_of_experience': years_exp,
        'current_salary': current_ctc,
        'expected_salary': expected_salary,
        'gender': gender,
        'location': location,
        'current_role': current_role,
        'sector': 'IT',
        'education': education,
        'certifications': cert,
        'skills': skill,
        'current_company_tier': current_tier,
        'target_company_tier': target_tier
    })

df = pd.DataFrame(data_rows)
df.to_csv('synthetic_salary_data.csv', index=False)
print("✅ Synthetic dataset saved as 'synthetic_salary_data.csv'")
