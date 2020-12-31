from pygithub3 import Github    
import polling
import logging
import requests
import json
'''
from slackclient import SlackClient
def slack_message(message, channel):
    token = 'T6GLYQPA8/B01HPD5P8NR/Nr0XrY7eE0aB5isNvwcGrCCs'
    sc = SlackClient(token)
    sc.api_call('chat.postMessage', channel=channel, 
                text=message, username='rishi.kaushal',
                icon_emoji=':robot_face:')
'''
#web_url='https://hooks.slack.com/services/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'


logging.basicConfig(filename= "E:\mylog.log" , level = logging.DEBUG)
log = logging.getLogger("my-logger")
#log.info("Hello, world")

k = 0

def abc(user,repo,web_url) :
  global k
  gh = Github()
  slack_msg={'text':'new contribution'}
  #s = gh.repos.list_contributors(user='confluentinc',repo='cp-helm-charts')
  s = gh.repos.list_contributors(user,repo)
  #print(type(s.all()))
  #log.info(s.all())  # will comment this here 
  
  if len(s.all())>k :
      k=len(s.all())
      log.info(k)
      requests.post(web_url,data=json.dumps(slack_msg))
      #slack_message("new contributor", "general")
  
user = raw_input("please provide github username : ")
repo = raw_input("please provide github repo name : ")
web_url = raw_input("please provide url token: ") 
poll_in = raw_input("please provide polling interval : " )


polling.poll(

    lambda: abc(user,repo,web_url),
    step=int(poll_in),
    poll_forever=True
)


