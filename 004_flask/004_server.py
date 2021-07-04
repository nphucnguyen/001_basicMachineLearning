import cv2
import numpy as np
from flask import Flask
from flask_cors import CORS, cross_origin
from flask import request
import tensorflow as tf
import numpy as np
import cv2
import base64

# # load keras model
# sess = tf.Session()
# graph = tf.get_default_graph()
# with sess.as_default():
#     with graph.as_default():
#         face_model = load_model("facenet.h5")


# create Flask Server backend
app = Flask(__name__)

# Apply Flask CORS
CORS(app)
app.config['COR_HEADERS'] = 'Content-Type'

@app.route('/add', methods=['POST','GET'])
@cross_origin(origin='*')
def add_process():
    a = int(request.args.get('sothunhat'))
    b = int(request.args.get('sothuhai'))
    return 'Ket qua la' + str(a+b)

@app.route('/nhandienkhuonmat', methods=['POST'])
@cross_origin(origin='*')

def photo_base64_to_opencv(anh_base64):
    try:
        staff_pix = np.fromstring(base64.b64decode(anh_base64), dtype=np.uint8)
        staff_pix = cv2.imdecode(staff_pix, cv2.IMREAD_ANYCOLOR)
    except:
        return None
    return staff_pix

def count_faces(face):

    # khoi tao bo nhan dien khuon mat
    face_cascade = cv2.CascadeClassifier('haarcascade-frontalface_default.xml')
    # chuyen ve gray
    gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
    # phat hien khuon mat trong anh
    faces = face_cascade.detectMultiScale(gray,1.2,10)
    face_numbers = len(faces)
    return face_numbers

def face_rec_process():
    face_numbers = 0

    # read photo from client
    facebase64 = request.form.get('facebase64')

    #convert base64 to OpenCV format
    face = photo_base64_to_opencv(facebase64)


    #count the number of face regconition
    face_numbers = count_faces(face)

    return f'So mat la: {str(face_numbers)}'



# start backend
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='9999')
