# Justpy Tutorial demo browser_location_test 
# Getting the browser location with java_script       
#      
# generated by write_as_demo  at 2023-01-08T10:03:03.328667+00:00 
# 
# see https://justpy.io/reference/webpage#getting-the-browser-location-with-java_script
# see https://github.com/justpy-org/justpy/blob/master/docs/reference/webpage.md

import justpy as jp


javascript_string = """
var options = {
  enableHighAccuracy: true,
  timeout: 5000,
  maximumAge: 0
};

function success(pos) {
  var crd = pos.coords;

  console.log('Your current position is:');
  console.log(`Latitude : ${crd.latitude}`);
  console.log(`Longitude: ${crd.longitude}`);
  console.log(`More or less ${crd.accuracy} meters.`);
  e.result = {latitude: crd.latitude, longitude: crd.longitude, accuracy: crd.accuracy};
  send_to_server(e, 'page_event', false);
}

function error(err) {
  console.warn(`ERROR(${err.code}): ${err.message}`);
  e.result = 'Error';
  send_to_server(e, 'page_event', false);
}

navigator.geolocation.getCurrentPosition(success, error, options);
"""

async def result_ready(self, msg):
    if msg.request_id == 'geo_location':
        msg.page.add(jp.Div(text=f'longitude: {msg.result.longitude} Latitude: {msg.result.latitude} Accuracy: {msg.result.accuracy}',
                        classes='m-2 p-2 text-lg border'))


async def page_ready(self, msg):
    jp.run_task(self.run_javascript(javascript_string, request_id='geo_location', send=False))


def browser_location_test():
    wp = jp.WebPage()
    wp.on('page_ready', page_ready)
    wp.on('result_ready', result_ready)
    # Some arbitrary content
    wp.d = jp.Div(classes='flex flex-wrap', a=wp)
    for i in range(1, 31):
        jp.Div(text=f'Div {i}', a=wp.d, classes='border m-2 p-2 text-xs')
    return wp


# initialize the demo
from examples.basedemo import Demo
Demo("browser_location_test", browser_location_test)