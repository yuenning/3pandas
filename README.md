# 🐼 3Pandas – Filtering the Noise: ML for Trustworthy Location Reviews  

**Team Members:**  
- Tran Ha My  
- Diane Teo Min Xuan  
- Ng Yuen Ning  

---

## 📌 Problem Statement  

Location-based platforms rely heavily on user reviews. However, many reviews are noisy — containing spam, advertisements, irrelevant content, or rants from users who may not have even visited the location.  

We aim to design and implement an **ML-based system** that can:  

- **Gauge Review Quality:** Detect spam/ads, irrelevant content, and low-quality rants.  
- **Assess Relevancy:** Determine whether a review genuinely relates to the location.  
- **Enforce Policies:** Flag or filter out reviews that violate policies (e.g., ads, irrelevant content, fake reviews).  

---

## 🎯 Motivation & Impact  

- **Users:** More trustworthy reviews → better decision-making.  
- **Businesses:** Fairer representation and protection from malicious reviews.  
- **Platforms:** Automated moderation reduces manual workload and strengthens credibility.  

---

## 📂 Data Sources  

  *   **Kaggle Dataset:** Loads the ["Google Maps Restaurant Reviews"](https://www.kaggle.com/datasets/denizbilginn/google-maps-restaurant-reviews) dataset.
  *   **Apify Dataset:** Downloaded Singapore reviews from a variety of business categories (e.g. retail, tourism, food, fitness) from the Apify platform.
  *   **GoogleLocal Dataset:** Loads a sample of the [McAuley Lab GoogleLocal](https://mcauleylab.ucsd.edu/public_datasets/gdrive/googlelocal/) data (10 states, 1000 reviews per state).
  *   **Yelp Open Dataset:** Loads a sample of 10,000 reviews from the [Yelp Open Dataset](https://business.yelp.com/data/resources/open-dataset/).

---

## 🛠 Methodology  

### 1. **Data Preprocessing**  
- Cleaning: lowercasing, punctuation removal, tokenization  
- Normalizing: handling emojis, non-English reviews, duplicates  
- Labeling: OpenAI API used to generate policy-aligned ground truth for supervised training  

### 2. **Feature Engineering**  
- **Classical ML:** TF-IDF, bag-of-words, review length, sentiment scores  
- **Deep Learning:** Transformer embeddings (Qwen models, Gemma)  

### 3. **Models Evaluated**  
We compared both **classical ML models** and **transformer-based models**:  

| **Model**               | **Description**                                                                 | **Use Case**                                                                 |
|--------------------------|---------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| **Random Forest**        | Baseline ML model using TF-IDF + handcrafted features.                          | Strong baseline, interpretable feature importance.                            |
| **MLP Classifier**       | Multi-layer perceptron on embeddings.                                           | Captures nonlinearities, moderately performant.                               |
| **Gemma-3 1B (finetuned)** | Transformer-based model trained on review labels.                               | Strong semantic understanding, but requires GPU resources.                     |
| **Qwen 0.5B – 0.8B (finetuned)** | Lightweight transformer models tested for efficiency-performance tradeoff. | Achieves better balance between accuracy and compute cost than larger LLMs.   |

---

## 📊 Results (Summary)  

- **Random Forest:** Achieved ~0.58 F1-macro. Good interpretability but limited semantic capture.  
- **MLP:** Slight improvements (~0.55 F1-macro) but struggles with imbalance.  
- **Gemma 2B:** Stronger performance (~0.46 F1-macro) with embeddings, but high GPU demand.  
- **Qwen 0.5B–0.8B:** Balanced efficiency vs. accuracy (~0.33 F1-macro). Lightweight enough for real-world deployment.  

---

## ⚖️ Key Challenges  

- **Class Imbalance:** Ads and rants were rare compared to normal reviews → models struggled.  
- **Thresholding:** MLP & transformer outputs required tuning decision thresholds to avoid over-flagging.  
- **Generalization:** Some irrelevant reviews were subtle and context-dependent (hard even for humans).  

---

## 🚀 Future Work

- Experiment with **ensemble methods** (e.g., RF + Transformer voting).  
- Apply **data augmentation** (synthetic spam/rant generation).  
- Deploy as a **real-time moderation pipeline** for location platforms.  

---
