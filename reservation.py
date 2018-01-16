from groupy.client import Client
from datetime import datetime

curr_date=datetime.now()
dt_str=str(curr_date.month)+'/'+str(curr_date.day+7)

client=Client.from_token("0FpwvtwlWizeagQa5K4hEgLPEZqhLzDVETYJGs0Q")

for group in client.groups.list():
  # print(group.name)
  if group.name=='PJW Calling Email Method':
    grp=group

msg="PJW Calling for this Sunday: "+dt_str+"\n1. Trophy Room\n2. Rec\n3. Greg"

grp.post(text=msg)

