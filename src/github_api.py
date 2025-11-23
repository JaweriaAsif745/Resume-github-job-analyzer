import os
import requests
from time import sleep

BASE = "https://api.github.com"

def _headers(token=None):
    h = {"Accept": "application/vnd.github.v3+json"}
    if token:
        h['Authorization'] = f"token {token}"
    return h

def fetch_user_profile(username, token=None):
    url = f"{BASE}/users/{username}"
    r = requests.get(url, headers=_headers(token))
    return r.json()

def fetch_user_repos(username, token=None):
    repos = []
    page = 1
    while True:
        url = f"{BASE}/users/{username}/repos?per_page=100&page={page}"
        r = requests.get(url, headers=_headers(token))
        if r.status_code != 200:
            return {"message": "error", "status": r.status_code, "details": r.text}
        data = r.json()
        if not data:
            break
        repos.extend(data)
        page += 1
        sleep(0.1)
    return repos

def fetch_repo_languages(repos, token=None):
    languages = {}
    for repo in repos:
        lang_url = repo.get('languages_url')
        if not lang_url:
            continue
        r = requests.get(lang_url, headers=_headers(token))
        if r.status_code != 200:
            continue
        data = r.json()
        for lang, count in data.items():
            languages[lang] = languages.get(lang, 0) + count
    return languages

def fetch_repo_recent_activity(repos, token=None):
    out = []
    for repo in repos:
        out.append({
            'name': repo.get('name'),
            'stars': repo.get('stargazers_count'),
            'forks': repo.get('forks_count'),
            'updated_at': repo.get('updated_at'),
            'html_url': repo.get('html_url')
        })
    return sorted(out, key=lambda r: r['updated_at'] or '', reverse=True)[:20]
