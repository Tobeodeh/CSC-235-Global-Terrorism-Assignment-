#importimg required field
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#reading the file
data = pd.read_csv("terrorist.txt",sep="\t", header = None, names = ["SN","Feature","Sum", "SimilarityID"]).fillna(0)
print(data)


#this code splits the feature column of the data and then converts to integer
data.Feature1= data.Feature.astype(str).str.split(",")
values = pd.DataFrame(data.Feature1.to_list()).fillna(0).add_prefix('Feature_')
values = values.astype(int)


#Sums the values of the feature across the row, then create a variable for the sun column
values["sum_tab"] = values.sum(axis =1)
sum_feature = values["sum_tab"]


#adds the sum value gotten from the above data to the main data table
data["Sum"] = sum_feature
print(data)


#this groups the data based on the feature and sum column of data
Duplicate = data.groupby(["Feature","Sum"]).count()


#creating a table to record the number of times a faeture and sum that are equal
repeat = data.pivot_table(index = ['Feature','Sum'],aggfunc='size')
repeat1  = pd.DataFrame(repeat).reset_index()
repeat1.insert(loc = 0, column = "SN",value = np.arange(len(repeat1)))
repeat1.rename (columns = {0 :"Ocurrence"},inplace = True)
repeat1


#drawing the graph
repeat1['Ocurrence'].plot.bar()
plt.xlabel('SN')
plt.ylabel('Ocurrence')
plt.title('NUmber of feature Occurence')

