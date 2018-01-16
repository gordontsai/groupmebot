from groupy.client import Client
import datetime
from config import access_token

curr_date=datetime.datetime.now()
next_sunday=curr_date+datetime.timedelta(days=7)
dt_str=str(next_sunday.month)+'/'+str(next_sunday.day)

#Hardcoded inputs, these need to be changed to suit your needs
group_name='PJW Calling Email Method'
msg="PJW Calling for this Sunday: "+dt_str+"\n1. Trophy Room\n2. Rec\n3. Greg"

client=Client.from_token(access_token)

for group in client.groups.list():
  # print(group.name)
  if group.name==group_name:
    grp=group

grp.post(text=msg)

