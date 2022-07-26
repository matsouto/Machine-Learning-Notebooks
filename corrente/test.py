import h5py
import numpy as np
filepath = 'V.mat'
arrays = {}
f = h5py.File(filepath)
for k, v in f.items():
    arrays[k] = np.array(v)
print(arrays)
