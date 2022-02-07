from django.shortcuts import render
import requests
from django.views import View
from django.http import HttpResponse
import re

class Index(View):
    greeting = "Good Day"

    def get(self, request):
        return render(request, 'index.html')

    def post(self, request, *args, **kwargs):
        User_String = request.POST.get('inputValue')
        if(User_String==''):
            print("Not allowed")
            error_message = 'You need to enter String'
            return render(request, 'index.html', {'error': error_message})
        else:
            Mydata = MyFunction(User_String)
            print(Mydata[1][0]['Total Tokens'])
            #RealString = Mydata[0]["Your String"]
            dict={
                "data":Mydata[0],
                "token": Mydata[1][0]['Total Tokens'],
                "operators": Mydata[1][1]['Total Operators'],
                "symbols": Mydata[1][2]['Total Symbols'],
                "keywords": Mydata[1][3]['Total Keywords'],
                "identifiers": Mydata[1][4]['Total Identifiers'],
                "inidentifiers": Mydata[1][5]['Total Invalid Identifiers'],
                "numbers": Mydata[1][6]['Total Numbers'],
                "inoperatorss": Mydata[1][7]['Total Invalid Operators'],
                "library": Mydata[1][8]['library']

            }
            return render(request, 'result.html', {'dict': dict})
            
 
    #   summary.append({"Total Tokens": len(userString)})
    # summary.append({"Total Operators": len(totaloperators)})
    # summary.append({"Total Symbols": len(totalsymbols)})
    # summary.append({"Total Keywords": len(totalkeywords)})
    # summary.append({"Total Identifiers": len(totalidentifiers)})
    # summary.append({"Total Invalid Identifiers": len(totalinvalididentifiers)})
    # summary.append({"Total Numbers": len(totalnumbers)})
    # summary.append({"Total Invalid Operators": len(totalinvalidoperators)})

def CheckingAlphabits(a):
    pattern = re.compile("[A-Za-z]+")
    if pattern.fullmatch(a) is not None:
        return True
    else:
        return False

def MyFunction(InputString):
    symbols = [',', ';', '>', '<', '=', '(', ')', '{', '}', '[', ']']
    operators = ['+', '-', '*', '/']
    invalidOperatos = ['++','+++','--','---','**','***','//','///']
    keywords = ['if', 'else', 'while', 'do', 'int', 'double', 'float', 'return', 'char', 'case',
                'char', 'sizeof', 'long', 'short', 'typedef', 'switch', 'unsigned', 'void', 'static', 'struct', 'goto']
    data = []
    line = InputString
    userString = line.split()
    totalData=[]
    summary=[]
    totaloperators=[]
    totalsymbols=[]
    totalkeywords=[]
    totalidentifiers=[]
    totalinvalididentifiers=[]
    totalnumbers=[]
    totalinvalidoperators=[]
    totallibray=[]
    library = ["#include<iostream>", "#include<conio.h>"]
 


    for ch in userString:
        if ch in keywords:
            if not ch in totalkeywords:
                data.append({"Valid Keyword":  ch})
                totalkeywords.append(ch)

        elif ch.isalnum() and ch.isdigit():
            if ch not in totalnumbers:
                data.append({"Valid Number":  ch})
                totalnumbers.append(ch)

        elif ch in symbols:
            if ch not in totalsymbols:
                data.append({"Valid Symbol": ch})
                totalsymbols.append(ch)
        elif ch in library:
            if ch not in totallibray:
                data.append({"Libray": ch})
                totallibray.append(ch)


        elif ch in operators:
            if ch not in totaloperators:
                data.append({"Valid Operator": ch})
                totaloperators.append(ch)

        elif ch in invalidOperatos:
            if ch not in totalinvalidoperators:
                data.append({"InValid Operator": ch})
                totalinvalidoperators.append(ch)

        else:
            if CheckingAlphabits(ch) == True:
                if ch not in totalidentifiers:
                    data.append({"Valid Identifier":  ch})
                    totalidentifiers.append(ch)

            else:
                if ch not in totalinvalididentifiers:
                    data.append({"InValid Identifier":  ch})
                    totalinvalididentifiers.append(ch)

    totalTokens = len(totaloperators)+len(totalsymbols) + \
        len(totalkeywords)+len(totalidentifiers) + \
        len(totalinvalididentifiers)+len(totalnumbers)+len(totalinvalidoperators)+len(totallibray)
    summary.append({"Total Tokens": totalTokens})
    summary.append({"Total Operators": len(totaloperators)})
    summary.append({"Total Symbols": len(totalsymbols)})
    summary.append({"Total Keywords": len(totalkeywords)})
    summary.append({"Total Identifiers": len(totalidentifiers)})
    summary.append({"Total Invalid Identifiers": len(totalinvalididentifiers)})
    summary.append({"Total Numbers": len(totalnumbers)})
    summary.append({"Total Invalid Operators": len(totalinvalidoperators)})
    summary.append({"library": len(totallibray)})
    totalData.append(data)
    totalData.append(summary)
    return totalData

   
