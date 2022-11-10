# -*- coding: utf-8 -*-


import pandas as pd
import matplotlib.pyplot as plt

#Read input file
df = pd.read_csv("C:/Users/HP/OneDrive - University of Hertfordshire/ADS1 Assignment 1/avg_rainfalltemp in UK - Sheet1.csv")

#Processing the dataframe to remove unwanted rows
df = df[~df["Period"].isin(["Winter", "Spring", "Summer", "Autumn", "Annual"])]

#Creating a new column that combines year and month
df["Time"] = df["Year"].astype(str) + df["Period"]


def lineplot(x, y):
    """Creating lineplots using x and y axes values. Multiple graphs can be made 
    using different arguments"""
    plt.figure()
    plt.plot(df[x], df[y])
    plt.ylabel(y)
    plt.xlabel(x)
    plt.xticks(df[x][::10], rotation=70)
    filename = y + ".png"
    plt.savefig(filename)
    plt.show()

#calling the lineplot function 2 times with different set of values to create two graphs
lineplot("Time", "Avg rainfall(in mm)")
lineplot("Time", "Avg temp(in centigrade)")

def hist(x1, x2, label1, label2):
    """ Creates histogram of two columns """
    
    plt.figure()
    plt.hist(df[x1], density = True, alpha = 0.7, label = label1)
    plt.hist(df[x2], density = True, alpha = 0.7, label = label2)
    plt.legend()
    plt.savefig("hist.png")
    plt.show()
    
#Calls the histogram function
hist("Avg rainfall(in mm)", "Avg temp(in centigrade)", "Rainfall",  "Temperature")


def box(x1, x2, label1, label2, ylabel):
    """ Creates two box plot with two sets of values"""
    plt.figure()
    data = [df[x1], df[x2]]
    dlabel = [label1, label2]
    for i in range(4):
        plt.boxplot(data, labels = dlabel)
       
        plt.ylabel(ylabel)
    plt.savefig("box.png")
    plt.show()

#Calls the boxplot function
box("Avg rainfall(in mm)", "Avg temp(in centigrade)", "Rainfall", "Temperature", "Value")

