import pandas as pd
def read_csv():
    filename=input('Enter the Filename:')
    data=pd.read_csv(filename)
    return data