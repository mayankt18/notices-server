from flask import Flask, json
import time
import sys,os
import threading


companies = [{"id": 1, "name": "Company One"}, {"id": 2, "name": "Company Two"}]
baseurl = 'https://nitdgp.ac.in/p/noticesnitd/general-2'
api = Flask(__name__)

@api.route('/notices', methods=['GET'])
def get_companies():
  try:
    f = open('response.json')
    data = json.load(f)
  except:
    data = {}
  return json.dumps(data)

def getNotices():
  while True:
    print('Updating')
    al.AllNotices(baseurl)
    print('Waiting')
    time.sleep(30*60)

if __name__ == '__main__':

  path = os.getcwd()
  sys.path.insert(0,path+"/nitdgp_website_notices_web_sraper")


  from waitress import serve
  from nitdgp_website_notices_web_sraper import AllNotices as al


  thread = threading.Thread(target=getNotices)
  thread.daemon = True
  thread.start()
  port = int(os.environ.get('PORT', 33507))
  serve(api,port=port)
  thread.join()