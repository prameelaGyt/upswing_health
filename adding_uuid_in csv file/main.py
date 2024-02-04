import pandas as pd
import uuid

# Read the CSV file
file_path = 'S3_STREAMING_URLS.csv' 
data = pd.read_csv(file_path)

# Remove the 'video link' column
data.drop('video_link', axis=1, inplace=True)  

# Generate UUIDs for the 'reference' column
data['reference'] = [str(uuid.uuid4()) for _ in range(len(data))]

# Save the modified data to a new CSV file
output_file_path = r"C:\Users\PrameelaSathivada\Downloads\modified_s3_streaming.csv"
 # Replace 'modified_file.csv' with your desired output file path
data.to_csv(output_file_path, index=False)

print(f"CSV file has been modified and saved to '{output_file_path}'")
