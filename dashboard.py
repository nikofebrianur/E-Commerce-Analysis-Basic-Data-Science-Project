import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

def products_by_review_df(data):
    # Group the data by product_id and calculate statistics
    product_stats = data.groupby('product_category_name').agg({
        'review_score': ['count', 'mean']
    }).reset_index()

    # Rename the columns for clarity
    product_stats.columns = ['product_category_name', 'review_count', 'average_review_score']

    # Sort the products by review count and average review score
    product_stats = product_stats.sort_values(by=['review_count', 'average_review_score'], ascending=False)

    return product_stats

def top_payment_df(data):
    # Group the data by payment_type and calculate statistics
    payment_stats = data.groupby('payment_type').agg({
        'order_id': 'count',
        'price': 'sum'
    }).reset_index()

    # Rename the columns for clarity
    payment_stats.columns = ['payment_type', 'order_count', 'total_amount_paid']

    # Sort the payment types by order count and total amount paid
    payment_stats = payment_stats.sort_values(by=['order_count', 'total_amount_paid'], ascending=False)

    return payment_stats

all_df = pd.read_csv("all_data.csv")

datetime_columns = ["order_purchase_timestamp", "order_estimated_delivery_date"]
all_df.sort_values(by="order_purchase_timestamp", inplace=True)
all_df.reset_index(inplace=True)
 
for column in datetime_columns:
    all_df[column] = pd.to_datetime(all_df[column])

min_date = all_df["order_purchase_timestamp"].min()
max_date = all_df["order_purchase_timestamp"].max()
 
with st.sidebar:
    # Logo
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")
    
    # Get start_date & end_date from date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

main_df = all_df[(all_df["order_purchase_timestamp"] >= str(start_date)) & 
                (all_df["order_purchase_timestamp"] <= str(end_date))]

by_review_df = products_by_review_df(main_df)
by_payment_type_df = top_payment_df(main_df)

# Create a Streamlit web app
st.title("Product Review Analysis")

# Display the top products by review count
st.subheader("Top Products by Review Count")
top_products_by_review_count = by_review_df.head(10)  # Adjust the number of products to display
st.table(top_products_by_review_count)

# Create a bar plot for top products by review count
plt.figure(figsize=(10, 6))
sns.barplot(x='review_count', y='product_category_name', data=top_products_by_review_count, orient='h')
plt.xlabel('Review Count')
plt.ylabel('Product ID')
plt.title('Top Products by Review Count')
st.pyplot(plt)

# Display the top products by average review score
st.subheader("Top Products by Average Review Score")
top_products_by_avg_score = by_review_df.sort_values(by='average_review_score', ascending=False).head(10)  # Adjust the number of products to display
st.table(top_products_by_avg_score)

# Create a bar plot for top products by average review score
plt.figure(figsize=(10, 6))
sns.barplot(x='average_review_score', y='product_category_name', data=top_products_by_avg_score, orient='h')
plt.xlabel('Average Review Score')
plt.ylabel('Product ID')
plt.title('Top Products by Average Review Score')
st.pyplot(plt)

# Create a Streamlit web app
st.title("Product Review and Payment Analysis")

# Display the top products by review count
st.subheader("Top Products by Review Count")
top_products_by_review_count = by_review_df.head(10)  # Adjust the number of products to display
st.table(top_products_by_review_count)

# Create a bar plot for top products by review count
plt.figure(figsize=(10, 6))
sns.barplot(x='review_count', y='product_category_name', data=top_products_by_review_count, orient='h')
plt.xlabel('Review Count')
plt.ylabel('Product Category Name')
plt.title('Top Products by Review Count')
st.pyplot(plt)

# Display the top products by average review score
st.subheader("Top Products by Average Review Score")
top_products_by_avg_score = by_review_df.sort_values(by='average_review_score', ascending=False).head(10)  # Adjust the number of products to display
st.table(top_products_by_avg_score)

# Create a bar plot for top products by average review score
plt.figure(figsize=(10, 6))
sns.barplot(x='average_review_score', y='product_category_name', data=top_products_by_avg_score, orient='h')
plt.xlabel('Average Review Score')
plt.ylabel('Product Category Name')
plt.title('Top Products by Average Review Score')
st.pyplot(plt)

# Display the top payment methods by order count
st.subheader("Top Payment Methods by Order Count")
top_payment_by_order_count = by_payment_type_df.head(10)  # Adjust the number of payment methods to display
st.table(top_payment_by_order_count)

# Create a bar plot for top payment methods by order count
plt.figure(figsize=(10, 6))
sns.barplot(x='order_count', y='payment_type', data=top_payment_by_order_count, orient='h')
plt.xlabel('Order Count')
plt.ylabel('Payment Type')
plt.title('Top Payment Methods by Order Count')
st.pyplot(plt)

# Display the top payment methods by total amount paid
st.subheader("Top Payment Methods by Total Amount Paid")
top_payment_by_total_amount = by_payment_type_df.sort_values(by='total_amount_paid', ascending=False).head(10)  # Adjust the number of payment methods to display
st.table(top_payment_by_total_amount)

# Create a bar plot for top payment methods by total amount paid
plt.figure(figsize=(10, 6))
sns.barplot(x='total_amount_paid', y='payment_type', data=top_payment_by_total_amount, orient='h')
plt.xlabel('Total Amount Paid')
plt.ylabel('Payment Type')
plt.title('Top Payment Methods by Total Amount Paid')
st.pyplot(plt)

# Create a Streamlit web app
st.title("Product Review and Payment Analysis")

# Display the top products by review count
st.subheader("Top Products by Review Count")
top_products_by_review_count = by_review_df.head(10)  # Adjust the number of products to display
st.table(top_products_by_review_count)

# Create a bar plot for top products by review count
plt.figure(figsize=(10, 6))
sns.barplot(x='review_count', y='product_category_name', data=top_products_by_review_count, orient='h')
plt.xlabel('Review Count')
plt.ylabel('Product Category Name')
plt.title('Top Products by Review Count')
st.pyplot(plt)

# Display the top products by average review score
st.subheader("Top Products by Average Review Score")
top_products_by_avg_score = by_review_df.sort_values(by='average_review_score', ascending=False).head(10)  # Adjust the number of products to display
st.table(top_products_by_avg_score)

# Create a bar plot for top products by average review score
plt.figure(figsize=(10, 6))
sns.barplot(x='average_review_score', y='product_category_name', data=top_products_by_avg_score, orient='h')
plt.xlabel('Average Review Score')
plt.ylabel('Product Category Name')
plt.title('Top Products by Average Review Score')
st.pyplot(plt)

# Display the top payment methods by order count
st.subheader("Top Payment Methods by Order Count")
top_payment_by_order_count = by_payment_type_df.head(10)  # Adjust the number of payment methods to display
st.table(top_payment_by_order_count)

# Create a bar plot for top payment methods by order count
plt.figure(figsize=(10, 6))
sns.barplot(x='order_count', y='payment_type', data=top_payment_by_order_count, orient='h')
plt.xlabel('Order Count')
plt.ylabel('Payment Type')
plt.title('Top Payment Methods by Order Count')
st.pyplot(plt)

# Display the top payment methods by total amount paid
st.subheader("Top Payment Methods by Total Amount Paid")
top_payment_by_total_amount = by_payment_type_df.sort_values(by='total_amount_paid', ascending=False).head(10)  # Adjust the number of payment methods to display
st.table(top_payment_by_total_amount)

# Create a bar plot for top payment methods by total amount paid
plt.figure(figsize=(10, 6))
sns.barplot(x='total_amount_paid', y='payment_type', data=top_payment_by_total_amount, orient='h')
plt.xlabel('Total Amount Paid')
plt.ylabel('Payment Type')
plt.title('Top Payment Methods by Total Amount Paid')
st.pyplot(plt)

# Create a pie chart to visualize the sum of payment types
st.subheader("Sum of Payment Types")
fig, ax = plt.subplots()
ax.pie(by_payment_type_df['order_count'], labels=by_payment_type_df['payment_type'], autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
st.pyplot(fig)
