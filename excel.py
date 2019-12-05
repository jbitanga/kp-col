# Column Remover
# Created by Jared Bitanga
# Last edited 12/15/19

import pandas
import pandas as pd


# This function asks the user what row he would like to remove
def userDrop(df):

    userCol = raw_input('Enter the col you would like to remove: ')

    # df = DataFrame, calls a function called drop from pandas, axis is setting it to column
    df.drop(userCol, axis=1, inplace=True)
    print df
    
    # This checks if the user would like to delete another column, if not the system saves the file and exits
    userChoice = raw_input('Would you like to delete another column? ')
    while userChoice == "y" or userChoice == "Y":
        userDrop(df)
    if userChoice == "n" or userChoice == "N":
       df.to_csv('C:/Users/jared/employee.csv', index = None, header=True) 
       SystemExit


def loadFile():
    userString = raw_input('Enter where the CSV file is located: ')

    df = pandas.read_csv(userString)
    print(df)
    userDrop(df)


def main():
    loadFile()


main()

