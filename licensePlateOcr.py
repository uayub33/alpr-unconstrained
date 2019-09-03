import sys
import cv2
import numpy as np
import traceback
import csv


import darknet.python.darknet as dn

from os.path                 import splitext, basename
from glob                    import glob
from darknet.python.darknet import detect
from src.label                import dknet_label_conversion
from src.utils                 import nms


def add_to_results(output_dir,bname,lp_str):
    with open('%s/results.csv' % (output_dir),'a+') as f:
        f.write(bname + ',' + lp_str + '\n')

def main(output_dir) :

    try:
        print("---------------------IN OCR---------------------")
        ocr_threshold = .4

        ocr_weights = 'data/ocr/ocr-net.weights'
        ocr_netcfg  = 'data/ocr/ocr-net.cfg'
        ocr_dataset = 'data/ocr/ocr-net.data'

        ocr_net  = dn.load_net(ocr_netcfg, ocr_weights, 0)
        ocr_meta = dn.load_meta(ocr_dataset)

        imgs_paths = sorted(glob('%s/*lp.png' % output_dir))

        print 'Performing OCR...'

        #Create File and make header
        with open('%s/results.csv' % (output_dir),'a+') as f:
            f.write("FileName,LP" + "\n")



        for i,img_path in enumerate(imgs_paths):

            print '\tScanning %s' % img_path

            bname = basename(splitext(img_path)[0]) #basename of image file 
            lp_str = 'No Chars Found' #Dummy LP 

            R,(width,height) = detect(ocr_net, ocr_meta, img_path ,thresh=ocr_threshold, nms=None)

            if len(R):
                L = dknet_label_conversion(R,width,height)
                L = nms(L,.45)

                L.sort(key=lambda x: x.tl()[0])
                lp_str = ''.join([chr(l.cl()) for l in L])
                
              #  with open('%s/%s_str.txt' % (output_dir,bname),'w') as f:
              #      f.write(lp_str + '\n')
            
            #bname = bname.replace("car_lp_str.txt","")

            if int((bname.split('_')[1].replace("car",""))) > 0: #to remove multiple LPs 
                print("IGNORED: ImgName: ", bname , ' LP: ' , lp_str , '\n')#to remove multiple LPs 
        
            else:
                bname = bname.split('_')[0]

                print("ImgName: ", bname , ' LP: ' , lp_str , '\n')
                add_to_results(output_dir, bname, lp_str)

        print("---------------------OUT OCR---------------------")


    except:
        traceback.print_exc()
        sys.exit(1)

    #sys.exit(0)
