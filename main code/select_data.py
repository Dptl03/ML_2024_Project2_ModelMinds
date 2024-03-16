import pandas as pd
import numpy as np
import csv


with open('object_info_all2.csv', 'w', newline='') as csvfile:
    
    csv_writer = csv.writer(csvfile)

    # Load the original csv
    df = pd.read_csv('object_info_all.csv')

    # Determine the number of batches
    num_batches = len(df) // 10

    # Initialize an empty list to store selected rows
    selected_rows_list = pd.DataFrame()
    
    for i in range(num_batches):
        # Select a random row index from the batch and append to the list
        random_index = np.random.randint(i * 10, (i + 1) * 10)
        
        print(list(df.iloc[random_index]))
        csv_writer.writerow(list(df.iloc[random_index]))
    