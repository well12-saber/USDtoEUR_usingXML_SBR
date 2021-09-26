import xml.etree.ElementTree as ET
import urllib.request

url="https://cbr.ru/scripts/XML_daily.asp"

webFile=urllib.request.urlopen(url)
data=webFile.read()

UrlSplit=url.split("/")[-1]

ExtSplit=UrlSplit.split(".")[-1]
FileName=UrlSplit.replace(ExtSplit,"xml")

with open(FileName,"wb") as localFile:
    localFile.write(data)

webFile.close()

root = ET.parse(FileName).getroot()

USD=root.findall(".//*[@ID='R01235']/Value")
print(USD[0].text)
USDcurr=USD[0].text.replace(",",".")

EUR=root.findall(".//*[@ID='R01239']/Value")
print(EUR[0].text)
EURcurr=EUR[0].text.replace(",",".")

dollarHave=float(input("\nHow many USD you have?\n"))
euroGot=dollarHave*(float(USDcurr))/(float(EURcurr))
print("You got "+ str(euroGot) + " euro.")

input("Transaction complete")
