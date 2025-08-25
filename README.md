# **Problem Statement 1**  
### **Filtering the Noise: ML for Trustworthy Location Reviews**  
**Team 3Pandas** *(Tran Ha My, Diane Teo Min Xuan, Ng Yuen Ning)*  

---

## **Problem Statement**  
Design and implement an **ML-based system** to evaluate the **quality** and **relevancy** of Google location reviews. The system should:  

- **Gauge review quality:** Detect spam, advertisements, irrelevant content, and rants from users who have likely never visited the location.  
- **Assess relevancy:** Determine whether the content of a review is genuinely related to the location being reviewed.  
- **Enforce policies:** Automatically flag or filter out reviews that violate the following example policies:  
  - No advertisements or promotional content.  
  - No irrelevant content (e.g., reviews about unrelated topics).  
  - No rants or complaints from users who have not visited the place (can be inferred from content, metadata, or other signals).  

---

## **Motivation & Impact**  
- **For Users:** Increases trust in location-based reviews, leading to better decision-making.  
- **For Businesses:** Ensures fair representation and reduces the impact of malicious or irrelevant reviews.  
- **For Platforms:** Automates moderation, reduces manual workload, and enhances platform credibility.  

---

## **Data Sources**  

| **Data Sources**       | **Details** |
|-------------------------|-------------|
| **Public Datasets**    | - **Google Review Data:** Open datasets containing Google location reviews (e.g., [Google Local Reviews on Kaggle](https://www.kaggle.com/datasets/denizbilginn/google-maps-restaurant-reviews))<br>- **Google Local review data:** [UCSD Public Dataset](https://mcauleylab.ucsd.edu/public_datasets/gdrive/googlelocal/)<br>- **Alternative Sources:** Yelp, TripAdvisor, or other open review datasets for supplementary training. |
| **Student-Crawled Data** | - Students are encouraged to crawl additional reviews from Google Maps (in compliance with Google's terms of service).<br>- **Example:** [Scraping Google Reviews (YouTube)](https://www.youtube.com/watch?v=LYMdZ7W9bWQ) |
