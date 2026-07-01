# AI Support Operations Platform

Portfolio project simulating an AI-powered support ticket automation and analytics platform.

## Project Goal

The goal of this project is to build an end-to-end workflow for support ticket intake, processing, AI-assisted triage, notifications, analytics and monitoring.

## Planned Tech Stack

- Google AppSheet
- Google Forms
- Google Sheets
- Python
- BigQuery
- n8n
- OpenAI / Claude API
- Gmail
- Looker Studio
- GitHub
- Jira

## Planned Architecture

Google AppSheet / Google Forms  
→ Google Sheets  
→ n8n  
→ Python processing  
→ BigQuery  
→ LLM triage  
→ Gmail notifications  
→ Looker Studio dashboard

## Current Status

Week 1: Project setup in progress.

## Project Structure

## Project Structure

```text
ai-support-operations-platform/
│
├── architecture/              # architecture diagrams
├── dashboard/                 # reporting artifacts
├── data/
│   ├── raw/                   # raw exported datasets
│   ├── processed/             # cleaned datasets
│   └── sample_attachments/    # sample ticket attachments
│
├── docs/                      # project documentation
├── n8n/                       # workflow exports
├── prompts/                   # LLM prompts
├── scripts/                   # Python scripts
├── screenshots/               # project screenshots
├── sql/                       # SQL queries and views
│
├── requirements.txt           # Python dependencies
├── README.md
└── .gitignore
```