"""
import pandas as pd

# Step 1: Load the CSV file
df = pd.read_csv('sales_data.csv')

# Step 2: Display the first 10 rows
print("First 10 rows:")
print(df.head(10))

# Step 3: Display the last 5 rows
print("\nLast 5 rows:")
print(df.tail())

# Step 4: Get a concise summary
print("\nData Info:")
print(df.info())

# Step 5: Generate descriptive statistics
print("\nDescriptive Stats:")
print(df.describe())


import pandas as pd

# Load the data
df = pd.read_csv('sales_data.csv')

# Step 1: Filter the data
filtered_df = df[(df['Region'] == 'North') & (df['Sales'] > 1000)]

# Step 2: Group by 'Product' and calculate total sales
product_sales = filtered_df.groupby('Product')['Sales'].sum().reset_index()

# Step 3: Sort by total sales descending
sorted_sales = product_sales.sort_values(by='Sales', ascending=False)
print(sorted_sales)

"""
import cv2

# Open the default webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # Mirror effect
    frame = cv2.flip(frame, 1)

    # Draw "Hand Control" text
    cv2.putText(frame, 'Hand Control',
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2)

    cv2.imshow('Camera', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up
cap.release()
cv2.destroyAllWindows()