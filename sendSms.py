from ipaddress import IPv4Address
from pyairmore.request import AirmoreSession
from pyairmore.request import AirmoreRequest
from pyairmore.services.device import DeviceService
from pyairmore.services.messaging import MessagingService

ip = IPv4Address("192.168.43.1")  # whatever server's address is
session = AirmoreSession(ip,2333)  # port is default to 2333

service = MessagingService(session)
def send(phone,message):
    try:
        service.send_message(contact_or_phone=phone, content=message)
        return 1
    except:
        return 0

x = send("0781146100","Hello from zuku")
print(x)