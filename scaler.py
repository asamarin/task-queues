import webapp2
from google.appengine.api import modules
from google.appengine.api import taskqueue

class Autoscaler(webapp2.RequestHandler):
  def get(self):
    queue = taskqueue.Queue('worker')
    n_tasks = queue.fetch_statistics().tasks
    if n_tasks > 10:
        modules.set_num_instances(4, module='worker')
    elif n_tasks < 5:
        modules.set_num_instances(1, module='worker')

app = webapp2.WSGIApplication([('/autoscaler', Autoscaler)],
                               debug=True)
