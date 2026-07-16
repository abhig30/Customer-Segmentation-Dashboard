import streamlit as st
import pandas as pd

# Page Title
st.set_page_config(page_title="Customer Segmentation Dashboard")

st.title("🛍️ Customer Segmentation Dashboard")

# Load Dataset
df = pd.read_csv("Mall_Customers.csv")

# Summary Metrics
st.subheader("📊 Summary")

col1, col2, col3 = st.columns(3)

col1.metric("Total Customers", len(df))
col2.metric("Average Income", round(df["Annual Income (k$)"].mean(), 2))
col3.metric("Average Spending Score", round(df["Spending Score (1-100)"].mean(), 2))

# Dataset
st.subheader("📋 Customer Dataset")
st.dataframe(df)

# Statistics
st.subheader("📈 Dataset Statistics")
st.write(df.describe())

# Customer Segmentation Graph
st.subheader("🎯 Customer Segmentation Graph")

try:
    st.image("clusters.png")
except:
    st.warning("clusters.png not found. Run the clustering code first.")

# Marketing Recommendations
st.subheader("💡 Marketing Recommendations")

st.success("""
Cluster 1: High Income & High Spending

• Premium Membership Plans
• Luxury Product Promotions
• Loyalty Rewards Program
""")

st.info("""
Cluster 2: High Income & Low Spending

• Personalized Discounts
• Targeted Marketing Campaigns
• Special Offers on Premium Products
""")

st.warning("""
Cluster 3: Low Income & High Spending

• Budget-Friendly Bundles
• Seasonal Discounts
• Cashback Offers
""")

st.error("""
Cluster 4: Low Income & Low Spending

• Awareness Campaigns
• Entry-Level Products
• Attractive Introductory Offers
""")

# Footer
st.markdown("---")
st.write("""
This project uses K-Means Clustering to divide mall customers into groups
based on Annual Income and Spending Score. These groups help businesses
create targeted marketing strategies.
""")