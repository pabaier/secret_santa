from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from twilio.rest import Client
from members.models import Pairings, User_By_Group as userGroups
from create_group.models import myGroups
import os, json, sys

def sendText(userName, pairingName, groupName, userPhoneNumber):
  with open(os.path.join(sys.path[0], 'secret_santa/config.json'), 'r') as f:
      config = json.load(f)
  tConfig = config['twilio']

  client = Client(tConfig['account_sid'], tConfig['auth_token'])
  txt = f'Hello {userName}!\nYour Secret Santa pairing for group {groupName} is {pairingName}!'

  try:
    message = client.messages.create(
      to    = f'{userPhoneNumber}',
      from_ = tConfig['number'],
      body  = txt
    )
    result = {'success': {'userName': userName}}
  except Exception as err:
    message = err.__dict__['msg']
    result = {'failure': {'userName': userName}}

  return {'result': result}

def sendEmail(userName, pairingName, groupName, userEmail):
  subject =  f'Secret Santa Pairing For Group {groupName}'
  message = f'Hello {userName}!\nYour Secret Santa pairing for group {groupName} is {pairingName}!'
  toEmail = [userEmail]
  try:
    send_mail(subject, message, settings.EMAIL_HOST_USER, toEmail, fail_silently=False,)
    result = {'success': {'userName': userName}}
  except Exception as err:
    message = err.__dict__['msg']
    result = {'failure': {'userName': userName, 'error': message}}
  return result

def sendGroup(request, groupId):
  if (not userGroups.objects.filter(member_1ID=request.user.id, group_ID=groupId).exists()):
    return JsonResponse({'failure': [{'message': 'You are not part of the requested group'}]})
  # pairings = Pairings.objects.filter(groupID=groupId)
  # groupName = myGroups.objects.filter(id=groupId)[0].group_name
  # results = {'success': [], 'failure': []}
  # for pairs in pairings:
  #   user = pairs.member_1ID
  #   pair = pairs.member_2ID
  #   if(user.phone and user.phone != ''):
  #     result = sendText(user.username, pair.username, groupName, user.phone)
  #   else:
  #     result = sendEmail(user.username, pair.username, groupName, user.email)
  # if 'success' in result:
  #   results['success'].append(result['success'])
  # else:
  #   results['failture'].append(result['failure'])
  results = {
    'success': [{'message': 'user1'}, {'message': 'user3'}], 
    'failure': [{'message': 'user2'}, {'message': 'user4'}]
  }
  results = {
    'success': [{'message': 'user1'}, {'message': 'user3'}], 
    'failure': []
  }
  output = {k:v for (k,v) in results.items() if len(results[k]) > 0}
  return JsonResponse(output)

def testGroupSend(request):
  return render(request, 'comms/testGroupPairs.html')
