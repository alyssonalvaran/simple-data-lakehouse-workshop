---
# Slidev config and frontmatter
theme: nord
layout: center
transition: slide-up
class: text-center
---

# Data-Engineered Analytics
Building Schema-Driven Event Pipelines in Python

<div class="pt-12">
  <span class="text-xl">by Alysson Alvaran</span>
</div>

---
layout: center
transition: slide-up
class: text-center
---

# Goal

To build a simple, local data lakehouse in Python that transforms messy, unstructured JSON event streams into highly compressed Parquet files, enabling fast SQL analytics and real-time visualization.

---
layout: center
transition: slide-up
---

# Workshop Outline

<v-clicks>

- **Introduction:** Concepts & Architecture
- **Module 0:** Project Setup
- **Module 1:** The Problem with Unstructured JSON
- **Module 2:** Schema Enforcement with Pydantic
- **Module 3:** Building the Local Pipeline
- **Module 4:** Exporting and Analytics with DuckDB
- **Module 5:** Visualization with Streamlit

</v-clicks>

---
layout: center
transition: slide-up
class: text-center
---

# Introduction
Concepts & Architecture

---
layout: center
transition: slide-up
---

# JSON Event Logs

<v-clicks>

- The universal language of application events
- **The Good:** Highly flexible for software engineers
- **The Bad:** Unpredictable schemas break analytics pipelines

</v-clicks>

---
layout: center
transition: slide-up
---

# Data Lakehouses

<v-clicks>

- **Data Lakes:** Dump raw files. Cheap, but terrible for querying.
- **Data Warehouses:** Rigid SQL databases. Fast, but expensive and inflexible.
- **Data Lakehouses:** Open file formats (Parquet) + High-speed SQL.

</v-clicks>

---
layout: center
transition: slide-up
class: text-center
---

# Module 0
Project Setup

---
layout: center
transition: slide-up
---

# Initialize Environment

```bash
mkdir simple-data-lakehouse
cd simple-data-lakehouse

python -m venv venv

# On Mac/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate
```

---
layout: center
transition: slide-up
class: text-center
---

# Module 1
The Problem with Unstructured JSON

---
layout: center
transition: slide-up
---

# Event Log Anatomy

```json
{
  "event_id": "123e4567-e89b-12d3-a456-426614174000",
  "event_name": "user.signup",
  "timestamp": "2023-10-25T14:30:00Z",
  "user_id": 49201,
  "plan_type": "pro",
  "referral_source": "https://google.com"
}
```

---
layout: center
transition: slide-up
---

# Create Generator Script

```bash
pip install faker click
```

---
layout: center
transition: slide-up
class: text-center
---

# Module 2
Schema Enforcement with Pydantic

---
layout: center
transition: slide-up
class: text-center
---

# Data Contracts

---
layout: center
transition: slide-up
---

# Define Data Models

```bash
pip install pydantic
```

---
layout: center
transition: slide-up
class: text-center
---

# Modules 3 & 4
Building the Pipeline & Exporting to Parquet

---
layout: center
transition: slide-up
class: text-center
---

# JSON vs. Parquet

---
layout: center
transition: slide-up
---

# Create Pipeline Script

```bash
pip install pandas duckdb
```

---
layout: center
transition: slide-up
class: text-center
---

# Module 5
Visualization with Streamlit

---
layout: center
transition: slide-up
class: text-center
---

# Streamlit

---
layout: center
transition: slide-up
---

# Create Dashboard Script

```bash
pip install streamlit
```

---
layout: center
transition: slide-up
---

# Thank you!

<v-clicks>

- Workshop materials: [github.com/alyssonalvaran/simple-data-lakehouse-workshop](https://github.com/alyssonalvaran/simple-data-lakehouse-workshop)
- LinkedIn: [linkedin.com/in/alyssonalvaran](https://www.linkedin.com/in/alyssonalvaran/)
- Email: alvaran.alysson@gmail.com

</v-clicks>