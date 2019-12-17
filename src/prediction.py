import pickle
import numpy as np
import cv2

def loadTrainedModel():
    filepath='./output/models/rfc_model_acu81.sav'
    loaded_model = pickle.load(open(filepath, 'rb'))
    return loaded_model

def resizeImages(img_path,size=(50,50)):
    """resize images to 50x50 and format to prediction"""
    image = cv2.imread(img_path)
    resized = cv2.resize(image, size, interpolation=cv2.INTER_CUBIC)
    img=np.array([resized.flatten()])
    #print('resized image')
    return img

def predictNewImage(loaded_model,path):
    im = resizeImages(path)
    pred_nueva=loaded_model.predict(im)
    #print(pred_nueva)
    if pred_nueva == 0:
        diagnosis={'Diagnóstico':'Tumor benigno'}
    else:
        diagnosis={'Diagnóstico':'Tumor maligno'}
    
    return diagnosis 

def prediction(filepath):
    loaded_model= loadTrainedModel()
    prediction=predictNewImage(loaded_model,filepath)
    return prediction