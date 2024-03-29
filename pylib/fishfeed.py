import logging
import time
import os
import requests

logger = logging.getLogger('fishfeed')

COLLECTOR_URL='http://127.0.0.1:8081'

class FishTank(object):

    def __init__(self, tank_id):
        self.tank_id = tank_id
        self.recent_values = []
    
    def monitor(self):
        """Starts monitoring the fish tank"""
        while True:
            value = self.get_sample()
            self.record_value(value)
    
    def get_sample(self):
        f = open('/dev/random', 'r+')
        value = f.read(1)
        return value


    def record_value(self, value):
        """Adds a sample to the list of things to send to the server"""
        self.recent_values.append((time.time(), value))
        
        #is it time to send to the server?
        if (self.recent_values) >= 100:
            self.send_values()
    

    def send_values(self):
        """Send a batch of values to the server"""
        pid = os.fork()
        if pid:
            self.recent_values = []
            return
        try:
            url = '{collector_url}/api/value'.format(collector_url=COLLECTOR_URL)
            data = {'tank_id': self.tank_id, 'values': {}}
            for sample_time, value in self.recent_values:
                data['values'][str(sample_time)] = value
                
            response = requests.post(url, data)
            logger.info(response.text)

        except Exception, e:
            logger.exception(e)
        finally:
            os._exit(0)
        

