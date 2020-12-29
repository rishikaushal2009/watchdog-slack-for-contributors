from pygithub3 import Github    
import polling
import logging
logging.basicConfig(filename= "E:\mylog.log" , level = logging.DEBUG)
log = logging.getLogger("my-logger")
#log.info("Hello, world")

def abc() :
  gh = Github()
  s = gh.repos.list_contributors(user='confluentinc',repo='cp-helm-charts')
  #print(s.all())
  log.info(s.all())

polling.poll(

    lambda: abc(),
    step=10,
    poll_forever=True
)


