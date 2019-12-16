import pandas as pd
import glob
import cv2
import os
import pickle
import numpy as np
from scipy.fftpack import fft

#en este script están las funciones para crear un dataframe a partir 
# de las imagenes y exportarlo

def readImages(path1,path0):
    #el primero crea dataframe con 200 de una clase y 200 de otra
    #el segubndo crea dataframe con los 1000 de una clase y 1000 de otra
    images=[]
    labels=[]
    paths=[]
    
    #path_0 = './images/0/*'
    #path_1 = './images/1/*'
    
    for file in glob.glob(path1)[:15000]:
        images.append(cv2.imread(file))
        paths.append(os.path.relpath(file))
        labels.append(1)
            
    for file in glob.glob(path0)[:15000]:
        images.append(cv2.imread(file))
        paths.append(os.path.relpath(file))
        labels.append(0)
    
    return images,labels,paths


def fftransform(lst):
    '''fft to all the array images in a list'''
    tff=[]
    for im in lst:
        tff.append(np.abs(fft(im,512)))
    return tff

def createDf(labels, images, paths):
    df = pd.DataFrame(list(zip(labels, images, paths)), columns =['label', 'image', 'path']) 
    return df

def resizeImages(img_path,size=(50,50)):
    "resize all images to 50x50"
    image = cv2.imread(img_path)
    resized = cv2.resize(image, size, interpolation=cv2.INTER_CUBIC)
    #print('resized image')
    return resized

def reziseDF(df):
    size=(50,50,3)
    df['image'] = df['path'].apply(lambda x: resizeImages(x) if df['image'].shape != size else x)
    return df

def exportDF(df,file_name):
    return df.to_pickle("./output/{}.pkl".format(file_name))

def importDfPickle(path):
    with open(path, 'rb') as f:
        df = pickle.load(f)
    return df