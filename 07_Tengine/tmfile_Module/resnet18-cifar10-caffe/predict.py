import caffe
import numpy as np
import cv2 as cv
def inference(prototxt, caffemodel, image):
    # img = caffe.io.load_image(image, color=True)*255
    img = cv.imread(image)
    img = img.transpose(2,0,1)
    # img = img[np.newaxis, :, : ,:   ]
    net = caffe.Net(prototxt,
                caffemodel,
                caffe.TEST)
    out = net.forward_all(data=np.asarray([img]))

    caffe.set_mode_cpu()
    return out
prototxt_path = 'deploy.prototxt'
caffemodel_path = 'resnet-18.caffemodel'
img_path = 'Image/175_4.jpg'
prediction = inference(prototxt_path, caffemodel_path, img_path)
print(prediction['softmax'][0])
print(int(prediction['softmax'][0].argmax(axis=0)))
