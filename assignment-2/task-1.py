import pandas as pd

def read_csv_file(file_path):
    """Reads data from a given CSV file and returns a DataFrame."""
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error reading the CSV file: {e}")
        return None

   
data = read_csv_file('data1.csv')
print(2) 
if data is not None:
    print(data)
else:
    print("No data to display.")


if data is not None:
        numeric = data.select_dtypes(include='number')
        if numeric.empty:
            print("No numeric columns to compute statistics.")
        else:
            stats = numeric.agg(['mean', 'min', 'max']).transpose()
            for col, row in stats.iterrows():
                print(f"Column: {col}")
                print(f"  mean: {row['mean']}")
                print(f"  min:  {row['min']}")
                print(f"  max:  {row['max']}")
else:
    print("No data to compute statistics.")