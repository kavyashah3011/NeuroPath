import pandas as pd
import os

DATA_PATH = os.path.join("data", "job_skill.csv")

def load_skills():

    df = pd.read_csv(DATA_PATH)

    possible_columns = ["skill", "skills", "Skill", "Skills"]

    skill_column = None
    for col in df.columns:
        if col.lower() in [c.lower() for c in possible_columns]:
            skill_column = col
            break

    if not skill_column:
        skill_column = df.columns[1]

    skills = df[skill_column].dropna().astype(str).str.lower().unique().tolist()

    return skills

MASTER_SKILLS = load_skills()

def extract_skills(text):
    text = text.lower()
    found = []

    for skill in MASTER_SKILLS:
        if skill in text:
            found.append(skill)

    return list(set(found))