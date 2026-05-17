# EV Battery Degradation & Energy Usage Analysis

This project analyzes electric vehicle (EV) battery degradation patterns and energy usage behaviors using data visualization techniques in Python.

The goal is to understand how operational factors such as charging cycles, temperature, driving style, and internal resistance affect battery health (State of Health - SOH).

---

## 📊 Project Objectives

- Analyze battery degradation trends over time
- Identify key factors affecting battery health
- Visualize relationships between operational variables
- Explore vehicle-level differences in performance

---

## 🛠️ Tools & Technologies

- Python
- Pandas
- Matplotlib
- Seaborn

---

## 📁 Dataset Features

The dataset includes information such as:

- Total Charging Cycles
- Internal Resistance
- Average Temperature
- Driving Style
- Battery Type
- Car Model
- State of Health (SOH %)
- Battery Status

---

## 📊 Data Visualizations

### 1. Charging Cycles vs State of Health
Shows how battery health decreases as charging cycles increase.

![Charging Cycles](graphs/1_charging_cycles_vs_soh_advanced.png)

---

### 2. Internal Resistance vs State of Health
Higher internal resistance is generally associated with lower battery health.

![Internal Resistance](graphs/2_internal_resistance_vs_soh.png)

---

### 3. Battery Type Distribution (SOH Density)
Comparison of battery health across different battery types.

![Battery Type](graphs/3_soh_density_by_battery_type.png)

---

### 4. Driving Style vs State of Health
Aggressive driving behavior may contribute to faster degradation.

![Driving Style](graphs/4_driving_style_vs_soh.png)

---

### 5. Car Model vs State of Health
Comparison of battery performance across different EV models.

![Car Model](graphs/5_car_model_vs_soh_sorted.png)

---

### 6. Operational Factors Overview
Combined analysis of multiple operational variables.

![Operational Factors](graphs/6_operational_factors_grid.png)

---

### 7. Correlation Heatmap
Shows relationships between all numerical variables in the dataset.

![Correlation Heatmap](graphs/7_correlation_heatmap_polished.png)

---

## 📌 Key Insights

- Charging cycles have a strong negative correlation with battery health.
- Higher internal resistance indicates battery degradation.
- Temperature and driving behavior also influence SOH.
- Different car models show varying degradation patterns.

---

## 🚀 How to Run

1. Clone the repository:
```bash
git clone https://github.com/your-username/ev-battery-analysis.git
