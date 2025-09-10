# organ-donation-neo4j
# Organ Donation and Transplantation Management (Neo4j Aura)

This project demonstrates how to use **Neo4j Aura** to model and query an **organ donation and transplantation system**.  
It helps represent relationships between **donors, recipients, hospitals, and organs**, making it easier to track compatibility and availability.

## 📌 Features
- Add **donors** and **recipients** as graph nodes.
- Link **donors → organs → recipients** relationships.
- Query for **compatible donors**.
- Query for **organs available at a hospital**.

## 🗂 Data Model
- **Donor** (name, blood group, age, location)
- **Recipient** (name, blood group, condition, location)
- **Organ** (type, status)
- **Hospital** (name, city)

## 🚀 How to Run
1. Create a free Neo4j Aura instance from [Neo4j Aura Console](https://console.neo4j.io).
2. Replace the credentials in `src/connect.py` with your Aura database connection details.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
