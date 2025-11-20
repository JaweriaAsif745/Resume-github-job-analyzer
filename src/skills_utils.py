from .skills_extractor import preprocess
from fuzzywuzzy import fuzz

def cannonicalize(s):
    return (s or "").lower().strip()

def compare_skills(a,b):
    A = set(map(cannonicalize, a))
    B = set(map(cannonicalize, b))
    return list(A - B), list(B - A)

# ____Checking its working____
# a = ["python", "ml", "sql"]
# b = ["python", "ml", "docker"]
# c = "Python   "
# print(compare_skills(a,b))
# print(cannonicalize(c))

# inersection 
# a = {'sql', 'ml'}
# b = {'ml', 'dl'}
# print(len(a & b)/ max(1, len(a)))

# __Matching skills
def skill_match_score(resume_skills, github_skills, job_skills=None):
    rs = set(map(cannonicalize, resume_skills))
    gs = set(map(cannonicalize, github_skills))
    js = set(map(cannonicalize, job_skills))

    score = {
        'resume_vs_job_score': None,
        'github_vs_job_score': None,
        'resume_github_overlap': None
    }

    if js:
        score['resume_vs_job_score'] = len(rs & js) / max(1, len(js)) # Number of matching skills divided by total job skills
        score['github_vs_job_score'] = len(gs & js) / max(1, len(js))

    union = rs | gs

    if union:
        score['resume_github_overlap'] = len(rs & gs) / len(union)
    else:
        score['resume_github_overlap'] = 0.0

    return score