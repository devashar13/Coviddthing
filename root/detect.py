
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import os
from PIL import Image



class Predict:
    def __init__(self):
        pass

    def GetResult(self,x_ray_img):
        classifier = load_model('model_adv.h')
        test_image=image.load_img(os.path.abspath(x_ray_img),target_size = (224, 224))
        test_image=image.img_to_array(test_image)
        test_image=np.expand_dims(test_image, axis = 0)
        result=classifier.predict(test_image)
        return result
# if result >= 0.5:
#     prediction='COVID NEGATIVE'
# else:
#     prediction='COVID POSITIVE'
    
# print(prediction)
