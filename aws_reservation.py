from groupy.client import Client
import datetime
from config import access_token_gordon, access_token_rishabh

def lambda_handler(event,context):
  access_token=access_token_rishabh
  curr_date=datetime.datetime.now()
  weekday=curr_date.weekday()
  next_week=curr_date+datetime.timedelta(days=7)
  dt_str=str(next_week.month)+'/'+str(next_week.day)

# Hardcoded inputs, these need to be changed to suit your needs
  group_name='2017-2018 UT Captains'
  if weekday==7:
    msg="PJW Calling for next Sunday 8-10pm "+dt_str+"\n1. Greg South\n2. Greg North\n3. Trophy Room"
  elif weekday==2:
    msg="PJW Calling for next Tuesday 10-12pm "+dt_str+"\n1. Greg South\n2. Greg North\n3. Trophy Room"
  elif weekday=3:
    msg="PJW Calling for next Wednesday 10-12pm "+dt_str+"\n1. Greg South\n2. Greg North\n3. Trophy Room"

  client=Client.from_token(access_token)

  for group in client.groups.list():
    # print(group.name)
    if group.name==group_name:
      grp=group

  grp.post(text=msg)

