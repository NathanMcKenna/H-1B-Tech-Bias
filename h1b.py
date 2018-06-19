import argparse
import numpy as np
import matplotlib.pyplot as plt
from csv import DictReader, DictWriter

import pandas 
import datetime

import warnings
warnings.filterwarnings("ignore")
import seaborn as sns
sns.set(style="white", color_codes=True)


def plot():
    
    #Create plot of wages
    t = data
    t['PREVAILING_WAGE'].value_counts().tolist
    t = t[t['PREVAILING_WAGE']<250000]
    t = t[t['PREVAILING_WAGE']>0]
    ax = sns.distplot(t['PREVAILING_WAGE'],axlabel='Prevailing wages for H-1B applications')
    sns.plt.show(ax)
    
    



if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='H-1B Parser')
    parser.add_argument('--plot', type=int, default=None,
                        help="default")                    
    args = parser.parse_args()
    
   
    data = pandas.read_csv("/home/nathan/Desktop/WRTG3030/h1b_kaggle.csv")
    
    #List of top IT related jobs
    techJobs = ["Computer Systems Analysts", "Computer Programmers",
    "SOFTWARE DEVELOPERS, APPLICATIONS", "COMPUTER SYSTEMS ANALYSTS",
    "Software Developers, Applications","COMPUTER PROGRAMMERS",
    "COMPUTER OCCUPATIONS, ALL OTHER","Computer Occupations, All Other",
    "Software Developers, Systems Software","SOFTWARE DEVELOPERS, SYTEMS SOFTWARE",
    "Computer Software Engineers, Applications","Computer Occupations, All Other*",
    "Database Administrators","NETWORK AND COMPUTER SYSTEMS ADMINISTRATORS",
    "Network and Computer Systems Administrators","COMPUTER SYSTEMS ANALYST",
    "DATABASE ADMINISTRATORS","Computer and Information Systems Managers",
    "Computer Software Engineers, Systems Software", "COMPUTER AND INFORMATION SYSTEMS MANAGERS",
    "WEB DEVELOPERS","Graphic Designers","Network and Computer Systems Administrators*",
    "Software Quality Assurance Engineers and Testers", "Web Developers", "GRAPHIC DESIGNERS",
    "SOFTWARE QUALITY ASSURANCE ENGINEERS AND TESTERS","Information Security Analysts",
    "Computer Hardware Engineers","Computer and Information Research Scientists"]
    
    #Add Tech Job boolean value to data frame
    data["Tech Job"] = ["True" if x in techJobs else "False" for x in data["SOC_NAME"]]
    
    
    
    #Print top 20 employers based on number of petitions
    #print(data['EMPLOYER_NAME'].value_counts().head(20))
    
    
    #Create plot of Number of petitions per year
    years = [2011,2012,2013,2014,2015,2016]
    petitionCount = [358767,415607,442114,519427,618727,647803]
    
    plt.plot(years,petitionCount)
    plt.xlabel("Year")
    plt.ylabel("Number of petitions")
    plt.title("Number of H-1B petitions per year")
    #plt.show()
    
    
   
    grade = float()
    grade = (36+48+26+71+30+50+39+51+34+36+27+40)/(40+55+35+80+35+50+60+55+40+40+47+45)*100
    
    grade =1
    print(grade)
    
    
    #Get top 20 SOC codes
    
    if(args.plot):
        plot()
    

   
