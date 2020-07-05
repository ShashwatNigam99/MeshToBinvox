import os,sys
import numpy as np
import binvox_rw
import scipy.io as sio

MODEL_PATH = sys.argv[1] 
OUTPUT_PATH = MODEL_PATH[:-4]+".binvox"
FILE_NAME = MODEL_PATH.split('/')[-1].split('.')[0]
print(OUTPUT_PATH)
os.system( "./binvox " + MODEL_PATH )

with open(OUTPUT_PATH, 'rb') as f:
    model = binvox_rw.read_as_3d_array(f)

print("MODEL DIMENSIONS: ",model.dims)
data = np.array(model.data)
print(data)

sio.savemat( "./output/" + FILE_NAME + '.mat', {'voxel':data} )
