from datetime import datetime
import requests
from cv2 import cv2
import base64

sess = requests.Session()

modelarts_server = 'https://10212e1dcf5b4388a9a4b7f3e1feb1d1.apig.cn-north-4.huaweicloudapis.com/v1/infers/11a1d0cf-bcf4-4a3d-ab37-dfee85252002'
modelarts_auth = 'https://iam.cn-north-4.myhuaweicloud.com/v3/auth/tokens'

with open('auth.json', 'r') as f:
	auth = f.read()
	res = sess.post(modelarts_auth, data= auth)
	token = res.headers['X-Subject-Token']
	string_time = res.json()['token']['expires_at']
	expires = datetime.strptime(string_time[:10] + string_time[11:-1], '%Y-%m-%d%H:%M:%S.%f').timestamp()
	print(token)
	print(len(token))

frame = cv2.imread('dummy.jpg')
ret, buffer = cv2.imencode('.jpg', frame)
buffer = base64.b64encode(buffer).decode('ascii')
result = sess.post(modelarts_server, 
                        headers={'X-Auth-Token': token},
                        json={'image_base64': buffer})
print(result.json())
