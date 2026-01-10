# 2024 CAC Analysis – Data Story and Optimization Plan

**Author / Contact:** 23f3000686@ds.study.iitm.ac.in  

This repository contains a small analysis of **Customer Acquisition Cost (CAC)** for 2024, compared against an **industry target CAC of 150**.  
The goal is to understand the current performance and propose specific, actionable recommendations to reach the target.

---

## 1. Dataset

Quarterly CAC values for 2024:

| Quarter | CAC    | Industry Target |
|---------|--------|-----------------|
| Q1      | 228.83 | 150             |
| Q2      | 230.45 | 150             |
| Q3      | 230.07 | 150             |
| Q4      | 231.14 | 150             |

**Average CAC for 2024:** **230.12**  
(independently computed in `analysis_cac_2024.py` using the raw numbers)

---

## 2. How to run the analysis

```bash
# (optional) create and activate a virtual environment
# python -m venv venv
# source venv/bin/activate  # on Windows: venv\Scripts\activate

pip install -r requirements.txt

python analysis_cac_2024.py

Note: This branch is used to create the CAC 2024 analysis pull request.
