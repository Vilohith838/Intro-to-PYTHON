
import pandas as pd
import numpy as np

data = {
    'Transaction_ID': [101, 102, 103, 104, 105, 106],
    'Date': ['2023-01-01', '2023-01-02', '2023-01-02', '2023-01-03', '2023-01-03', np.nan],
    'Product': ['Laptop', 'Mouse', 'Monitor', 'Mouse', 'Laptop', 'Monitor'],
    'Price': [1200, 25, np.nan, 25, 1200, 300],
    'Quantity': [1, 2, 1, 3, 1, 1],
    'Store_Location': ['NY', 'CA', 'NY', 'TX', 'CA', 'TX'],
    'Unnecessary_Notes': ['N/A', 'Check', 'None', 'Paid', 'N/A', 'Flag']
}

df = pd.DataFrame(data)