import time
import datetime

import webapp2
from google.appengine.api import taskqueue

class MainHandler(webapp2.RequestHandler):
  def get(self):
    eta_5mins = datetime.datetime.fromtimestamp(time.time() + 300)
    for _ in xrange(20):
      taskqueue.add(queue_name='worker', url='/hard-work', eta=eta_5mins)
    self.response.out.write('New tasks queued')

app = webapp2.WSGIApplication([('/start', MainHandler)],
                               debug=True)
