import webapp2
import time

class Worker(webapp2.RequestHandler):
  def post(self):
    time.sleep(60)

app = webapp2.WSGIApplication([('/hard-work', Worker)], debug=True)
