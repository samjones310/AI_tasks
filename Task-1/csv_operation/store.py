import pandas as pd
def store_results(data):
    #print(data)
    filename=input('Filename to be save:')
    filename =filename+'.csv'
    df=pd.DataFrame(data)
    df.to_csv(filename,index=False,header=False)
    print('Your File is saves as',filename)