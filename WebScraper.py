
from bs4 import BeautifulSoup
from urllib.request import urlopen
import sqlite3

page = urlopen('index.html');
soup = BeautifulSoup(page.read(),'html.parser')
soup.prettify()

def getTableData():
    saveddata = "";
    for record in soup.findAll('tr'):
        newdata = ""
        for data in record.findAll('td'):
            newdata += ", "+data.get_text()
        saveddata += "\n" + newdata[1:]
    print(saveddata)

def getParaData():
    listparas = soup.findAll('p')
    i = 1;
    for element in listparas:
        print("Paragraph " + str(i) +". ")
        print(element.get_text())
        i += 1
def getHeaderData():
    listheaders = soup.findAll('head')
    i = 1;
    for element in listheaders:
        print("Header " + str(i)+ ". ")
        print(element.get_text())
        i += 1;
def getTitle():
    title = soup.find('title')
    print(title.get_text())

def main():
    print("Welcome to Devansh's WebScraping App");
    a = int(input("How many times would you like to run the code? "))
    for i in range(a):
        ch = int(input("Enter choice: "))
        if(ch==1):
            getTableData()
            print()
            print()
        if(ch == 2):
            getParaData()
            print()
            print()
        if(ch==3):
            getHeaderData()
            print()
            print()
        if(ch==4):
            getTitle()
            print()
            print()
    print("Thank you for using the Program!")

if __name__ == "__main__":
    main()




