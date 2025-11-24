# 🎯 Resume + GitHub + Job Analyzer

An intelligent Streamlit-based web application that **analyzes your Resume**, **GitHub profile**, and an optional **Job Description** — all in one place.

It extracts skills from all three sources, compares them, identifies gaps, calculates match scores, and gives clear recommendations to improve your chances of being shortlisted.

---

## 🚀 Features

### **📄 Resume Analysis**
- Upload any **PDF resume**
- Extracts text and identifies important skills
- Detects programming languages, frameworks, ML skills, DevOps tools, etc.

### **🐙 GitHub Integration**
- Enter a GitHub username
- Fetches:
  - Public profile data
  - All public repositories
  - Programming languages usage
  - Topics, descriptions, and extracted skills
  - Activity (stars, forks, last updated)
- Works with or without `GITHUB_TOKEN`

### **💼 Job Description Matching**
- Upload PDF/TXT job description
- Extracts required skills
- Compares JD skills with resume and GitHub
- Shows what’s missing

### **📊 Skill Comparison Dashboard**
- Resume skills
- GitHub skills
- Job description skills
- Missing skills on Resume
- Missing skills on GitHub
- Job → Resume skill gap
- Job → GitHub skill gap

### **📈 Match Score Generation**
- Resume → Job match %
- GitHub → Job match %
- Resume ↔ GitHub overlap %

### **🖼️ Result Images Folder**
Your repository includes a folder named **`RESULT IMAGES/`** which contains:
- Output screenshots
- Skill comparison examples
- GitHub profile view
- Language charts

---

## 🗂 Project Structure

```

Resume-github-job-analyzer/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── RESULT IMAGES/        # 📸 Screenshots of results
│
└── assets/
│       └── skills_list.txt
├── src/
|   ├── __init__.py
│   ├── resume_parser.py
│   ├── github_api.py
│   ├── skills_extractor.py
│   └── skills_utils.py
│   
│
└── .env (optional)

````

---

## ⚙️ Installation

### **1️⃣ Clone the repository**
```bash
https://github.com/JaweriaAsif745/Resume-github-job-analyzer
cd Resume-github-job-analyzer
````

### **2️⃣ Install dependencies**

```bash
pip install -r requirements.txt
```

### **3️⃣ (Optional) Add GitHub token**

Create `.env` file:

```env
GITHUB_TOKEN=your_token_here
```

This increases API rate limits.

### **4️⃣ Run the App**

```bash
streamlit run app.py
```

---

## 🧠 How it Works

### **1. Resume Parsing**

* Extracts text using **PyPDF2**
* Cleans and processes text
* Detects skills using keyword matching

### **2. GitHub Analysis**

* Fetches repositories using GitHub REST API
* Aggregates languages
* Extracts skills from:

  * Repo descriptions
  * Repo topics
  * Languages

### **3. Job Description Parsing**

* Extracts text from PDF or TXT
* Detects job-required skills

### **4. Skill Matching Engine**

The system calculates three scores:

* **Resume → Job Match %**
* **GitHub → Job Match %**
* **Resume ↔ GitHub Overlap %**

---

## 📝 Output Examples (in repository)

The **RESULT IMAGES/** folder contains:

* Resume extraction preview
* GitHub profile preview
* Language bar-chart
* Skill comparison table
* Match score meters
---
## Full Result Image

<img width="1920" height="7594" alt="Full Page result" src="https://github.com/user-attachments/assets/3ecd1389-4c92-4419-91a7-30f80837d022" />

---

## 🤝 Contributing

Want to improve this tool?
Pull requests are welcome!

---

## 📄 License

This project is open-source and available under the **MIT License**.

````
markdown
# Resume Analyzer + GitHub Integration

A Streamlit app that analyzes a PDF resume, fetches a GitHub user's public repositories and languages, extracts skills from both sources, compares them with a job description and provides actionable recommendations.

## Features
- Upload a resume (PDF) and parse text
- Enter GitHub username to fetch profile, repos, languages
- Upload a job description (text or PDF)
- Extract skills from resume, GitHub and job description
- Compare skills and show missing / extra skills
- Simple activity stats (stars, forks, recent commits)

## Requirements
See `requirements.txt`.

## Quick start
1. Create a virtualenv
2. `pip install -r requirements.txt`
3. Set optional environment variable `GITHUB_TOKEN` to increase rate limits
4. Run:

```bash
streamlit run app.py
````

## Notes

* The app uses unauthenticated GitHub requests by default; supplying a token via `GITHUB_TOKEN` is recommended.
* Resume parsing is basic (text extraction) and may not perfectly preserve formatting.
  
```

## Usage notes & next steps

1. **Improve skill extraction**: Replace the simple keyword approach with an ML model, or a curated taxonomy.
2. **Authentication**: Add OAuth flow to analyze private repos (requires more GitHub App setup).
3. **UI polish**: Add charts, repo thumbnails, and links to top repos.
4. **Tests**: Add unit tests for parsing and skill extraction.

