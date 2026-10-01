# Dataset Schema & Data Dictionary

This directory contains the anonymized datasets used in the study:
**"Temporal Representation Learning of Teaching Styles and Its Impact on Lecturer Performance in Higher Education LMS"**

All personal identifiers (lecturer names, NIP/NIDN, student names, course titles, and exact calendar dates) have been fully stripped or anonymized in compliance with institutional data governance and research ethics standards.

---

## 📁 Files Summary

| File Name | Description | Rows | Format |
|---|---|---|---|
| `temporal_events_anonymized.csv` | Full corpus of primary pedagogical interaction events | 22,240 | CSV |
| `sample_events.csv` | Sample slice of events for quick testing and validation | 100 | CSV |
| `lecturer_performance_anonymized.csv` | Institutional ground-truth performance evaluation target scores | 386 | CSV |

---

## 📊 Data Dictionary

### 1. `temporal_events_anonymized.csv` & `sample_events.csv`

| Column | Type | Description | Example Values |
|---|---|---|---|
| `event_id` | String | Unique synthetic identifier for each log event | `EVT_000001` |
| `lecturer_id` | String | Anonymized lecturer identifier (linked across datasets) | `LEC_001` |
| `course_id` | String | Anonymized course/class identifier | `CRS_105` |
| `week_offset` | Integer | Semester week index (1 to 16) | `1`, `8`, `16` |
| `day_offset` | Integer | Day of week index (1 = Monday, 7 = Sunday) | `1`, `5` |
| `token_type` | String | Pedagogical action category | `Material Creation`, `Assignment Posting` |
| `token_code` | String | Discrete sequence token representation used in models | `MAT`, `ASN`, `QZ`, `FRM`, `GRD`, `ANC` |
| `duration_minutes` | Float | Session duration in minutes | `45.0`, `12.5` |

#### Token Categories (`token_code`)
- **`MAT` (Material Creation)**: Uploading slides, syllabus, reading materials.
- **`ASN` (Assignment Posting)**: Creating coursework, task prompts, guidelines.
- **`QZ` (Quiz Creation)**: Building online quizzes, exams, or assessments.
- **`FRM` (Interactive Forum)**: Initiating discussion threads, replying to student queries.
- **`GRD` (Grading Activity)**: Grading submissions, giving feedback, recording marks.
- **`ANC` (Announcement)**: Class broad notifications and updates.

---

### 2. `lecturer_performance_anonymized.csv`

| Column | Type | Description | Example Values |
|---|---|---|---|
| `lecturer_id` | String | Anonymized lecturer identifier | `LEC_001` |
| `num_classes` | Integer | Number of active classes taught during the semester | `7`, `12` |
| `lesson_planning_score` | Float | Lesson Planning component score (max 30.0%) | `30.0`, `25.5` |
| `learning_process_score` | Float | Learning Process component score (max 40.0%) | `39.4`, `32.0` |
| `learning_assessment_score` | Float | Learning Assessment component score (max 30.0%) | `30.0`, `22.4` |
| `total_lps` | Float | Aggregate Lecturer Performance Score (LPS, max 100.0%) | `99.4`, `79.9` |

---

## 🔒 Ethics & Anonymization Protocol
- **PII Stripping**: All real names, ID numbers, and course codes were removed.
- **Timestamp Relative Shift**: Exact timestamps were converted to relative semester offsets (`week_offset`, `day_offset`) to prevent reverse-engineering of timetables.
- **Access & License**: Released under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license.
