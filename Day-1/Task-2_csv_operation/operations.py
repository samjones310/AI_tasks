def csvOperations(data):
    datatype=['int16','int32','int64','float16','float32','float64']
    numeric_Data= data.select_dtypes(include=datatype)
    #print(data.dtypes)
    #print(numeric_Data.head())
    mean_data=['Mean']+numeric_Data.mean(axis=0,skipna=True).tolist()
    variance =['Variance']+numeric_Data.var(axis=0,skipna=True).tolist()
    median   =['Median']+numeric_Data.median(axis=0,skipna=True).tolist()
    standarddev=['Standard Deviation']+numeric_Data.std(axis=0) .tolist()
    mode1=numeric_Data.mode(axis=0)
    mode1=mode1.values.tolist()
    mode=['mode']
    for i in mode1[0]:
        mode.append(i)
    colname=['Operations']+list(numeric_Data.columns)
    l=[colname,mean_data,variance,median,standarddev,mode]
    #print((numeric_Data.mean(axis=0,skipna=True).tolist()))
    #print("Mean:\n",numeric_Data.mean(axis=0,skipna=True))
    #print("Variance:\n",numeric_Data.var(axis=0,skipna=True))
    #print("Median:\n",numeric_Data.median(axis=0,skipna=True))  
    #print("Mode:\n",numeric_Data.mode(axis=0),end="")
    #print("Standard Deviation:\n",numeric_Data.std(axis=0))
    return l