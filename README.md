# Scheduler-schule
A smart and efficient University timetable scheduling system designed to automatically generate optimized class schedules while minimizing conflicts between classes, teachers, and time slots.

---

## Overview

Scheduler Schulea is a project focused on solving one of the most complex problems in educational institutions — **timetable generation**.

Creating schedules manually is time-consuming and error-prone. This system automates the process using algorithms to ensure:
- No overlapping classes
- Efficient time slot allocation
- Balanced distribution of subjects

---

##  Tech Stack

- **Language:** Python  
- **Concepts Used:**
  - Graph Coloring Algorithm
  - Data Structures (Dictionaries, Lists)
  - Scheduling Optimization Techniques

---

## Project Structure
```bash
Scheduler-schulea/
  │── main.py
  │── README.md
  │── src/
      │── fetchData.py
      │── greedySolver.py
      │── graphEngine.py
      │── backtracker.py
      │── optimizer.py
  │── data/
      │── class_group.json
      │── constraint.json
      │── prof_availablity.json
      │── rooms.json
      │── std_grouping.json
      │── timeslot.json
      


## ▶️ Installation & Setup

1. Clone the repository:
```bash
git clone https://github.com/tusharrbhardwaj/Scheduler-schulea.git
cd Scheduler-schulea
```

Future Improvements
Web-based UI (React / Vue)
Database integration (MongoDB / MySQL)
Teacher & room allocation optimization
AI-based smart scheduling
Export schedules to PDF/Excel
