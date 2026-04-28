import pandas as pd

COLUMNS = ['Edge ID', 'Start Node ID', 'End Node ID', 'L2 Distance']

def parse_csv(file_path):
    """
    Parses the edge list file and returns a pandas DataFrame with columns:
    Edge ID, Start Node ID, End Node ID, L2 Distance.
    """
    try:
        data = pd.read_csv(
            file_path,
            sep=r'\s+',         # whitespace-separated
            header=None,        # no header row in file
            names=COLUMNS,      # assign our column names
        )
        return data
    #if it cant parse
    except Exception as e:
        print(f"Error parsing CSV file: {e}")
        return None