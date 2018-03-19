from groupy.client import Client
import datetime
from config import access_token_gordon, access_token_rishabh

def lambda_handler(event,context):
  # test=1
  if test == 1:
    access_token=access_token_gordon
    group_name='PJW Calling Email Method'
  else:
    group_name='2017-2018 UT Captains'
    access_token=access_token_rishabh
  curr_date=datetime.datetime.now()
  weekday=curr_date.weekday()
  next_week=curr_date+datetime.timedelta(days=7)
  dt_str=str(next_week.month)+'/'+str(next_week.day)

# Hardcoded inputs, these need to be changed to suit your needs
  if weekday==7 or weekday == 2 or weekday == 3:
    if weekday==7:
      msg="PJW Calling for next Sunday 8-10pm "+dt_str+"\n1. Greg South\n2. Greg North\n3. Trophy Room"
    elif weekday==2:
      msg="PJW Calling for next Tuesday 10-12pm "+dt_str+"\n1. Greg South\n2. Greg North\n3. Trophy Room"
    elif weekday==3:
      msg="PJW Calling for next Wednesday 10-12pm "+dt_str+"\n1. Greg South\n2. Greg North\n3. Trophy Room"

    client=Client.from_token(access_token)

    for group in client.groups.list_all():
      if group.name==group_name:
        group.post(text=msg)


# if __name__=='__main__':
  # lambda_handler('random','random2')


