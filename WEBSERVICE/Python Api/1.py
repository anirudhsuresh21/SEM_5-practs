from zeep import Client
from requests import Session
from zeep.transports import Transport

session = Session()
session.verify = False  # Disable SSL certificate verification for testing

# Use the session in the zeep transport
transport = Transport(session=session)

url = "https://localhost:44344/WebService1.asmx?wsdl"
client = Client(wsdl=url, transport=transport)
print("Math Operation")
opr1 = int(input("Enter operand 1: "))
result = client.service.CheckEvenOdd(opr1)
print("Output:",result)
