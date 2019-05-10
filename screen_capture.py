from grabscreen import grab_screen
from getkeys import key_check
from directkeys import PressKey, ReleaseKey, W,S,A,D
import random
import time
from PIL import Image
import utils
import numpy as np
if __name__ == "__main__":
    '''
    #input()
    while(True):
        PressKey(W)
        time.sleep(1)
        ReleaseKey(W)
    '''
    start = False
    p = utils.ParallelWriterHDF5('temp.hdf5')
    t = time.time()

    while(True):
        if not start:
            if "X" in key_check("X"):
                start=True
            continue
        image = grab_screen(window_title='Grand Theft Auto V',region=(1,41,1067,640))
        #image = grab_screen(region=(1,31,1067,630))
        keys_t = key_check("WSADY")
        if "Y" in keys_t:
            break
        assert image.dtype <= 'uint8'
        image = Image.fromarray(image)
        img = Image.Image.resize(image, (640, 360))
        img.save('output.png')
        keys = [0, 0]
        if 'W' in keys_t:
            keys[0] = 0
        else:
            keys[0] = 1
        if 'D' in keys_t:
            keys[1] = 0
        elif 'A' in keys_t:
            keys[1] = 1
        else:
            keys[1] = 2

        p.append((image, np.array(keys)))
        #pickle.dump((image,keys),open('{}.pickle'.format(t),'wb'))
        #data.append((image,keys))
        t_new = time.time()
        print(1/(t_new-t))
        t = t_new
