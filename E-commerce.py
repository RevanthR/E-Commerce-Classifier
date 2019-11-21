from math import sqrt,pi,exp
from csv import reader

#Function to load the dataset
def load_csv(filename):
    dataset=list()
    with open(filename,'r') as file:
        csv_reader=reader(file)
        for row in csv_reader:
            if not row:
                continue
            dataset.append(row)
    return dataset
#Function to convert string column to float
def str_column_to_float(dataset,column):
    for row in dataset:
        row[column] = float(row[column].strip())
#function to separate the dataset by class
def separate_by_class(dataset):
    sep=dict() #dictionary where the tuples are stored
    for i in range(len(dataset)):
        vector=dataset[i]
        class_value = vector[-1]
        if class_value not in sep:
            sep[class_value] =list()
        sep[class_value].append(vector)
    return sep
def mean(numbers): #function to find the mean of the values
    return sum(numbers)/float(len(numbers))
def stdev(numbers): #function to find the stadard deviation of the values
    avg=mean(numbers)
    variance= sum([(x-avg)**2 for x in numbers]) / float(len(numbers)-1)
    return sqrt(variance)

def summarize_data(dataset):
    summaries = [(mean(column), stdev(column), len(column)) for column in zip(*dataset)]
    del(summaries[-1])
    return summaries

def summarize_data_class(dataset):
    separated= separate_by_class(dataset)
    summaries= dict()
    for class_value, rows in separated.items():
        summaries[class_value]= summarize_data(rows)
    return summaries

# Calculate the Gaussian probability distribution function for x
def calculate_probability(x, mean, stdev):
	exponent = exp(-((x-mean)**2 / (2 * stdev**2 )))
	return (1 / (sqrt(2 * pi) * stdev)) * exponent
sume=summarize_data_class(data)
def calculate_class_probability(summaries,row):
    total_rows = sum([summaries[label][0][2] for label in summaries])
    probabilities = dict()
    for class_value, class_summaries in summaries.items():
        probabilities[class_value] = summaries[class_value][0][2]/float(total_rows)
        for i in range(len(class_summaries)):
            mean, stdev, _ = class_summaries[i]
            probabilities[class_value] *= calculate_probability(row[i], mean, stdev)
    return probabilities

