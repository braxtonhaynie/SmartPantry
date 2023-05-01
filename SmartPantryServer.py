import time
import cgi
import netifaces as ni
# from http.server import BaseHTTPRequestHandler
import socketserver
from http import server
from urllib.parse import parse_qs
from motor import StepperMotor
import logging
import camera

motor = StepperMotor()
cam = camera.StreamingCamera()
IP = ni.ifaddresses('wlan0')[ni.AF_INET][0]['addr']
PORT = 8765

def Get_HTML_Home():
	output = "<!DOCTYPE HTML><html>"
	output += "<head>"
	output += "<title>Smart Pantry</title>"
	output += "<style>"
	output += "html { font-family: Helvetica; display: inline-block; margin: 0px auto; text-align: center;}"
	output += "body{margin-top: 50px;} h1 {color: #444444;margin: 50px auto 30px;} h3 {color: #444444;margin-bottom: 50px;}"
	output += ".button { border: none; color: gray; height: 50px; width: 100px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer; border-radius: 12px;}"
	output += "p {font-size: 14px;color: #888;margin-bottom: 10px;}"
	output += ".button:hover { background-color: #4CAF50; color: white;}"
	output += ".button:active {background-color: #3e8e41; box-shadow: 0 5px #666; transform: translateY(4px);}"
	output += "</style>"
	output += "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"/>"
	output += "</head>"
	output += "<body>"
	output += "<h1>Smart Pantry</h1>"

	output += '<button id=\"UP\" class=\"button button1\" name="UP" value="UP">UP</button>'
	output += '<script>'
	output += '''var button1 = document.getElementById("UP");
	var intervalId1;
	var xhr1;

	button1.addEventListener("mousedown", function() {
	intervalId1 = setInterval(sendRequest1, 250); // val of 500 sends a request every half-second
	});

	button1.addEventListener("mouseup", function() {
	clearInterval(intervalId1);
	xhr1.abort(); // aborts any ongoing requests
	});

	function sendRequest1() {
	xhr1 = new XMLHttpRequest();
	xhr1.open("POST", "http://''' + IP + ''':''' + str(PORT) + '''/home/up", true);
	xhr1.setRequestHeader('Content-Type', 'application/json');
	xhr1.send();
	}'''
	output += '</script>'
	output += '<br>'

	output += '<button id=\"DOWN\" class=\"button button2\" name="DOWN" value="DOWN">DOWN</button>'
	output += '<script>'
	output += '''var button2 = document.getElementById("DOWN");
	var intervalId2;
	var xhr2;

	button2.addEventListener("mousedown", function() {
	intervalId2 = setInterval(sendRequest2, 250); // val of 500 sends a request every half-second
	});

	button2.addEventListener("mouseup", function() {
	clearInterval(intervalId2);
	xhr2.abort(); // aborts any ongoing requests
	});

	function sendRequest2() {
	xhr2 = new XMLHttpRequest();
	xhr2.open("POST", "http://''' + IP + ''':''' + str(PORT) + '''/home/down", true);
	xhr2.setRequestHeader('Content-Type', 'application/json');
	xhr2.send();
	}'''
	output += '</script>'

	output += '<h1>Pantry Live Stream</h1>'
	output += '<img src="stream.mjpg" width="640" height="480" />'

	output += "</body>"
	output += "</html>"
	return output

class requestHandler(server.BaseHTTPRequestHandler):
	def do_GET(self):
		if self.path.endswith("/home"):
			self.send_response(200)
			self.send_header("content-type", "text/html")
			self.end_headers()
			output = Get_HTML_Home()
			self.wfile.write(output.encode())
		elif self.path == '/stream.mjpg':
			self.send_response(200)
			self.send_header('Age', 0)
			self.send_header('Cache-Control', 'no-cache, private')
			self.send_header('Pragma', 'no-cache')
			self.send_header('Content-Type', 'multipart/x-mixed-replace; boundary=FRAME')
			self.end_headers()
			try:
				while True:
					with cam.output.condition:
						cam.output.condition.wait()
						frame = cam.output.frame
					self.wfile.write(b'--FRAME\r\n')
					self.send_header('Content-Type', 'image/jpeg')
					self.send_header('Content-Length', len(frame))
					self.end_headers()
					self.wfile.write(frame)
					self.wfile.write(b'\r\n')
			except Exception as e:
				logging.warning('Removed streaming client %s: %s',self.client_address, str(e))

	def do_POST(self):
		if self.path.endswith("/up"):
			print('UP')
			motor.DriveMotors(1, 'up')
			self.send_response(301)
			self.send_header("content-type", "text/html")
			self.send_header("Location", "/home")
			self.end_headers()
		
		if self.path.endswith("/down"):
			print('DOWN')
			motor.DriveMotors(1, 'down')
			self.send_response(301)
			self.send_header("content-type", "text/html")
			self.send_header("Location", "/home")
			self.end_headers()

# creates a threaded server
# prevents the camera from locking up the webpage
class StreamingServer(socketserver.ThreadingMixIn, server.HTTPServer):
    allow_reuse_address = True
    daemon_threads = True


def main():
	try:
		server_address = (IP, PORT)
		server = StreamingServer(server_address, requestHandler)
		print("{}:{}/home".format(IP, PORT))
		server.serve_forever()
	except KeyboardInterrupt:
		cam.picam2.stop_recording()
		motor.cleanup()

if __name__ == "__main__":
	main()
