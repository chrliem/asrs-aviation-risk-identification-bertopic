# Exploring Aviation Safety Risk Factors through BERTopic Modeling of Incident Reports

You can try to put some sample of incident report similar to ASRS here:
**[Aviation Risk Identification](https://aviation-risk-identification-bertopic.streamlit.app/)**

---

## Abstract
The increasing volume of aviation incident narratives presents both an opportunity and a challenge for safety analysis. This study introduces a dynamic topic modeling framework based on BERTopic to automatically identify and trace aviation safety risk factors from 57,292 reports in NASA’s Aviation Safety Reporting System (2013–2023).

The framework integrates transformer-based embeddings, dimensionality reduction (UMAP), and density-based clustering (HDBSCAN) to discover coherent topics without predefined parameters. Topic representations were refined through KeyBERTInspired and Maximal Marginal Relevance (MMR), while labeling was supported by large language models and validated against ICAO taxonomies.

The best-performing model (M5) achieved the highest coherence (c_v = 0.646) and diversity (0.829), generating seventeen distinct and interpretable risk factors encompassing technical, operational, and behavioral dimensions of aviation safety.

---

## Methodology
The topic modeling process followed the BERTopic pipeline with fine-tuning steps for representation refinement.

![Research Methodology](method%20diagram%20600dpi.jpg)

---

## Results
The model generated 17 distinct risk factors.

![Topic Representation](doctopics_600dpi.jpg)
![Topic Distribution](stacked%20topic%20distribution.png)
![Topic Intensity](topic%20intensity.png)

### Identified Risk Factors

| Topic | Final Label after Validation |
| :--- | :--- |
| 0 | System/Component Failure or Malfunction |
| 1 | Hazardous Goods Mishandling |
| 2 | Maintenance Control Failure |
| 3 | Drone Encounter |
| 4 | Disruptive Passenger |
| 5 | Crew Duty/Fatigue Management Failure |
| 6 | Cabin Safety Equipment |
| 7 | Passenger Non-Compliance |
| 8 | Navigation System Interference |
| 9 | Runway Lighting/NOTAM Failure |
| 10 | Pilot Distraction |
| 11 | Window Structural Failure |
| 12 | UAS Airspace Violation |
| 13 | Oxygen System Malfunction |
| 14 | Disease Exposure |
| 15 | Pilot Deviation |
| 16 | Spoiler System Malfunction |

---

## Author
**Christian Darma Setiawan, 2025**

---

*Disclaimer: This tool is for research and demonstration purposes only. It is not an official aviation safety management system and should not be used for operational decision-making.*
