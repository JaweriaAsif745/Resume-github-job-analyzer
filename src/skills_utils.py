from .skills_extractor import preprocess
from fuzzywuzzy import fuzz

def canonicalize(s):
    return (s or "").lower().strip()

def compare_skills(a, b):
    A = set(map(canonicalize, a))
    B = set(map(canonicalize, b))
    return list(A - B), list(B - A)

def skill_match_score(resume_skills, github_skills, job_skills=None):
    rs = set(map(canonicalize, resume_skills))
    gs = set(map(canonicalize, github_skills))
    js = set(map(canonicalize, job_skills or []))

    score = {
        'resume_vs_job_score': None,
        'github_vs_job_score': None,
        'resume_github_overlap': None
    }

    if js:
        score['resume_vs_job_score'] = len(rs & js) / max(1, len(js))
        score['github_vs_job_score'] = len(gs & js) / max(1, len(js))

    union = rs | gs
    if union:
        score['resume_github_overlap'] = len(rs & gs) / len(union)
    else:
        score['resume_github_overlap'] = 0.0

    return score
