#!usr/bin/python2.7
import sys
import csv # python csv module is used to manipulate csv files
from collections import OrderedDict, namedtuple  # OrderedDict to traverse the dict in the same order they are created or elements are inserted                                                 #pass values in namedtuple and it will itself assign the values to names as per order of values

#file_path='/home/learnomatics/python_codes/share.csv'
csv_file='/home/learnomatics/python_codes/share.csv'







def getMaxPriceByCompany():
    try:
        share_doc=open(csv_file,'r')  #open the csv file in read mode
        print share_doc
    except IOError as e:
        print e
        sys.exit()
    doc=csv.reader(share_doc)        #csv.reader
    labels=namedtuple('max_price', 'price year month')     # create a namedtuple with price year and month fields
    company_names=next(doc)[2:]                         #next method is used to read a line from csv.reader object. 
    data_dic=OrderedDict()                              # an order dict return the data in the manner it is created
    for name in company_names:                          
        data_dic[name]=labels(0,0,0)                    #data_dic['company_name]=(year,month,price)
    for line in doc:                                    #to read the lines from the csv.reader object
        year=line[0]                                    #get year as we know year is on 0 index
        month=line[1]                                   #get month as we know month is on 1 index
        for name, price in zip(company_names, map(int, line[2:])):     # zip method is used to create tuples by getting elements from all provided                                                                    touples or lists like li=[1,2,3] and names=['a','b','c',d] zip function will                                                                     convert it in ((1,a),(2,b),(3,c)) and will leave out the d from names
            if data_dic[name].price<price:                           #compare the price of data_dic[company_name] with the price of iterating row
                data_dic[name]=labels(price,year,month)              #change the year, month and price if condition is trie


    output={}
    for key , val in data_dic.items():
        print key , ":" , data_dic[key]
                  # print the max share prices with the company name, month and year
        output[key]={'price':data_dic[key][0],'year':data_dic[key][1],'month':data_dic[key][2]} #converting ordereddict to a simple dict for making test cases simple

    return output
    

if __name__== '__main__':
    getMaxPriceByCompany()











