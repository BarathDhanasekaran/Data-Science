class Univariate():
    
    def quanqual(dataset):
        quan=[]
        qual=[]
        for columnName in dataset.columns:
            #print(columnName)
            if(dataset[columnName].dtype=='O'):
                #print("qual")
                qual.append(columnName)
            else:
                #print("quan")
                quan.append(columnName)
        return quan,qual
        
    def freqtable(columnName,dataset):
        freqtable=pd.DataFrame(columns=["Unique_Values","Frequency","Relative Frequency","Cumsum"])
        freqtable["Unique_Values"]=dataset[columnName].value_counts().index
        freqtable["Frequency"]=dataset[columnName].value_counts().values
        freqtable["Relative Frequency"]=(freqtable["Frequency"]/103)
        freqtable["Cumsum"]=freqtable["Relative Frequency"].cumsum()
        return freqtable

    def univariate(quan,dataset):
    descriptive=pd.DataFrame(index=["mean","median","mode","Q1:25%","Q2:50%","Q3:75%","Q4:100%","IQR","1.5rule","Lesser","Greater","Min","Max","kurtosis","skew","var","std"],columns=quan)
    
    for columnName in quan:
            descriptive[columnName]["mean"]= dataset[columnName].mean()
            descriptive[columnName]["median"]= dataset[columnName].median()
            descriptive[columnName]["mode"]= dataset[columnName].mode()[0]
            descriptive[columnName]["Q1:25%"]=dataset.describe()[columnName]["25%"]
            descriptive[columnName]["Q2:50%"]=dataset.describe()[columnName]["50%"]
            descriptive[columnName]["Q3:75%"]=dataset.describe()[columnName]["75%"]
            descriptive[columnName]["Q4:100%"]=dataset.describe()[columnName]["max"]
            descriptive[columnName]["IQR"]=descriptive[columnName]["Q3:75%"]-descriptive[columnName]["Q1:25%"]
            descriptive[columnName]["1.5rule"]=1.5*descriptive[columnName]["IQR"]
            descriptive[columnName]["Lesser"]=descriptive[columnName]["Q1:25%"]-descriptive[columnName]["1.5rule"]
            descriptive[columnName]["Greater"]=descriptive[columnName]["Q3:75%"]+descriptive[columnName]["1.5rule"]
            descriptive[columnName]["Min"]= dataset[columnName].min()
            descriptive[columnName]["Max"]= dataset[columnName].max()
            descriptive[columnName]["kurtosis"]=dataset[columnName].kurtosis()
            descriptive[columnName]["skew"]=dataset[columnName].skew()
            descriptive[columnName]["var"]=dataset[columnName].var()
            descriptive[columnName]["std"]=dataset[columnName].std()
    return descriptive


    def outlier(columnName,quan):
        lesser=[]
        greater=[]
        
        for columnName in quan:
            if(descriptive[columnName]["Min"]<descriptive[columnName]["Lesser"]):
                lesser.append(columnName)
            if(descriptive[columnName]["Max"]<descriptive[columnName]["Q4:100%"]):
                greater.append(columnName)


