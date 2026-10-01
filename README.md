# Temporal Representation Learning of Teaching Styles & Lecturer Performance in LMS

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

Official repository and anonymized dataset for the paper:
**"Temporal Representation Learning of Teaching Styles and Its Impact on Lecturer Performance in Higher Education LMS"**

---

## 📌 Overview

This repository provides the anonymized dataset, feature extraction pipelines, and Deep Sequential Learning models (LSTM & Transformer Encoder) for modeling temporal pedagogical patterns from Learning Management System (LMS) interaction logs.

---

## 📂 Repository Structure

```text
lms-teaching-performance/
├── data/
│   ├── README.md                          # Data dictionary and anonymization protocol
│   ├── temporal_events_anonymized.csv      # Full dataset (22,240 events)
│   ├── sample_events.csv                  # Quick demo sample (100 events)
│   └── lecturer_performance_anonymized.csv# Target ground-truth LPS scores
├── src/
│   ├── data_loader.py                     # Sequence builder & tokenizer
│   └── models.py                          # LSTM & Transformer Encoder implementation
├── requirements.txt                       # Python dependencies
└── README.md                              # Main documentation
```

---

## 🚀 Quick Start

### 1. Installation
Clone the repository and install requirements:
```bash
git clone https://github.com/your-username/lms-teaching-performance.git
cd lms-teaching-performance
pip install -r requirements.txt
```

### 2. Run Data Tokenization & Sequence Generation
```python
from src.data_loader import load_and_tokenize_sequences

sequences, targets = load_and_tokenize_sequences('data/temporal_events_anonymized.csv', 'data/lecturer_performance_anonymized.csv')
print(f"Loaded {len(sequences)} sequence trajectories.")
```

---

## 🛡️ Data Governance & Privacy

All datasets included in this repository have undergone strict **pseudonymization and timestamp relative transformation**. No Personally Identifiable Information (PII) of instructors, students, or institutional courses is stored or exposed.

---


## 📜 License
This project and dataset are licensed under the [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).
