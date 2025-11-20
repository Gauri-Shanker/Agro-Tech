# 🌾 Crop Recommendation System (India)

A **Streamlit-based web application** that recommends the **best crops for Indian districts** based on historical agricultural production data.

The system analyzes crop productivity using:

```
Production_by_Area = Production (Tonnes) / Area (Hectares)
```

It helps **farmers, researchers, students, and planners** understand which crops perform best for a specific **State → District → Season** combination.

---

## 🚀 Features

- Interactive **State → District → Season** filtering  
- Crop productivity (Tonnes per Hectare) calculation  
- **Top 10 crop recommendations**  
- Clean, modern, responsive UI (Streamlit)  
- Fast and lightweight  
- Real dataset from **Indian agricultural statistics**

---

## 📦 Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```

**Included Libraries**

- streamlit  
- pandas  
- numpy  
- plotly  
- matplotlib  
- seaborn  

---

## ▶️ How to Run

Run the Streamlit app:

```bash
streamlit run app.py
```

Your browser will open automatically at:

http://localhost:8501

---

## 📊 Dataset Details

| Column          | Description                                 |
|-----------------|---------------------------------------------|
| State_Name      | State of India                              |
| District_Name   | District within the state                   |
| Crop_Year       | Year of production                          |
| Season          | Kharif, Rabi, Summer, Winter, Whole Year    |
| Crop            | Name of the crop                            |
| Area            | Cultivated area (Hectares)                  |
| Production      | Output (Metric Tonnes)                      |

### Yield Formula

```
Tonnes per Hectare (t/ha)
```

Calculated using:

```python
productivity = Production / Area
```

---

## 📙 Project Structure

```
📦 crop-recommendation
│── app.py                 # Streamlit application
│── crop_production.csv    # Dataset
│── requirements.txt       # Dependencies
└── README.md              # Documentation
```

---

## 🌐 Deployment

This project can be deployed for **free** on:

- Streamlit Cloud  
- HuggingFace Spaces  
- Render  

Just upload the repository and set **app.py** as the entry point.

---

## 📄 License

This project is **open-source**.  
You may use, modify, and distribute it freely.