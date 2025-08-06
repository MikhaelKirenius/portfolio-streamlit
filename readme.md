# Customer Segmentation with K-Means Clustering

This project implements **Customer Segmentation using K-Means clustering** to group customers based on their purchasing behavior and demographics.  
The insights from these clusters can help businesses create targeted marketing strategies and improve customer engagement.

---

## 📦 Dataset Information

- **Name:** [Customer Segmentation: Clustering](https://www.kaggle.com/datasets/vishakhdapat/customer-segmentation-clustering)  
- **Author:** Vishakh Patel  
- **License:** **Apache 2.0** – You are free to use, modify, and share the dataset, provided that you **give attribution to the original source** and retain the license when redistributing.  
- **Description:** The dataset contains customer data such as income, age, number of children, purchase history, and tenure with the company.  
- **Approx. Size:** ~8,000 customer records  

---

## ⚙️ Project Workflow

1. **Data Download**  
   Download the dataset automatically from Kaggle using `kagglehub`.

2. **Preprocessing**  
   - Handle missing values  
   - Convert date fields  
   - Feature engineering (Age, Customer Tenure, Total Spent)  

3. **Outlier Removal**  
   - Remove extreme values using **IQR method**  

4. **Feature Scaling**  
   - Apply `StandardScaler` for normalization  

5. **Model Training**  
   - Apply **K-Means clustering**  
   - Determine optimal clusters using **Elbow Method** and **Silhouette Score**  

6. **Cluster Profiling**  
   - Analyze cluster characteristics and generate insights  

7. **Streamlit Dashboard**  
   - **Overview Page:** Project details and dataset info  
   - **Performance Page:** Evaluation metrics (Elbow & Silhouette)  
   - **Results Page:** Cluster profiles, correlation heatmap, and business insights  
   - **Prediction Page:** Predict cluster for new customers  

---

## ▶️ How to Run the Project

### **1. Clone the Repository**

```bash
git clone https://github.com/MikhaelKirenius/portfolio-streamlit.git
cd portfolio-streamlit
```

### **2. Install Dependencies**

```bash
pip install -r requirements.txt
```

### **3. Download Dataset**

```bash
python download_dataset.py
```

### **4. Train the Model**

```bash
python main.py
```
This will:

- Preprocess the dataset

- Train the K-Means model

- Save the model and scaler into models/ folder

- Export processed data for visualization

### **5. Run the Dashboard**

```bash
streamlit run app.py
```

---

