import statistics
import pandas as pd 

df = pd.read_csv("StudentsPerformance.csv")
dataList = df["math score"].tolist()

mean = statistics.mean(dataList)
print('Mean:',mean)
mode = statistics.mode(dataList)
print('Mode:',mode)
median = statistics.median(dataList)
print('Median:',median)
standardDev = statistics.stdev(dataList)
print('Standard Deviation:',standardDev)

st_dev1_start,st_dev1_end = mean - standardDev, mean + standardDev
st_dev2_start,st_dev2_end = mean - 2*standardDev, mean + 2*standardDev
st_dev3_start,st_dev3_end = mean - 3*standardDev, mean + 3*standardDev

lenData1 = [result for result in dataList if result > st_dev1_start and result < st_dev1_end]
lenData2 = [result for result in dataList if result > st_dev2_start and result < st_dev2_end]
lenData3 = [result for result in dataList if result > st_dev3_start and result < st_dev3_end]

print("{}% of data lies within 1 standard deviation.".format(len(lenData1)*100.0/len(dataList)))
print("{}% of data lies within 2 standard deviations.".format(len(lenData2)*100.0/len(dataList)))
print("{}% of data lies within 3 standard deviations.".format(len(lenData3)*100.0/len(dataList)))


