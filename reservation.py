from groupy.client import Client
import datetime

curr_date=datetime.datetime.now()
next_sunday=curr_date+datetime.timedelta(days=7)
dt_str=str(next_sunday.month)+'/'+str(next_sunday.day)

client=Client.from_token("0FpwvtwlWizeagQa5K4hEgLPEZqhLzDVETYJGs0Q")

for group in client.groups.list():
  # print(group.name)
  if group.name=='PJW Calling Email Method':
    grp=group

msg="PJW Calling for this Sunday: "+dt_str+"\n1. Trophy Room\n2. Rec\n3. Greg"

grp.post(text=msg)

