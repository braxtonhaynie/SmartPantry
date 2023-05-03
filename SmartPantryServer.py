import time
import cgi
import netifaces as ni
# from http.server import BaseHTTPRequestHandler
import socketserver
from http import server
# from urllib.parse import parse_qs
from motor import StepperMotor
import logging
import camera
from HTML import Get_html

motor = StepperMotor()
cam = camera.StreamingCamera()
IP = ni.ifaddresses('wlan0')[ni.AF_INET][0]['addr']
PORT = 8765

class requestHandler(server.BaseHTTPRequestHandler):
	def do_GET(self):
		if self.path.endswith("/home"):
			self.send_response(200)
			self.send_header("content-type", "text/html")
			self.end_headers()
			# output = Get_HTML_Home()
			output = Get_html(IP, PORT)
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
