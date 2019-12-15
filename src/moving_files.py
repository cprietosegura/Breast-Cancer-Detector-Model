import os 
from shutil import copyfile

#en este script creo un nuevo directorio para clasificar las imágenes en negativo (0)
#o positivo (1) y muevo automáticamente los ficheros que pertenecen a cada categoría

dirpath = os.getcwd()
print("current directory is : " + dirpath)
foldername = os.path.basename(dirpath)
print("Directory name is : " + foldername)

dst_folder = 'images'  

os.mkdir(os.path.join(dst_folder, '0')) 
os.mkdir(os.path.join(dst_folder, '1'))  

src_folder = './breast-histopathology-images' 

folders = os.listdir(src_folder) 

for f in folders:
    f_path = os.path.join(src_folder, f)
    for cl in os.listdir(f_path):
        cl_path = os.path.join(f_path, cl)
        for img in os.listdir(cl_path):
            copyfile(os.path.join(cl_path, img), os.path.join(dst_folder, cl, img))