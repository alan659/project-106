
import plotly.express as px
import csv
import numpy as np

def plotfigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x='marks in percentage',y='days present')
        fig.show()


def getDataSource(data_path):
    marks_in_percentage=[]
    days_present =[]
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            marks_in_percentage.append(float(row["Marks In Percentage"]))
            days_present.append(float(row["Days Present"]))

    return{"x" :marks_in_percentage, "y": days_present }

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation :-  \n-->", correlation[0,1])

def setup():
      #copy relative path of the file
     data_path = "Student Marks vs Days Present.csv"

     datasource = getDataSource(data_path)
     findCorrelation(datasource)
     plotfigure(data_path)

setup()

