import os
import csv
from glob                    import glob
import pandas as pd

def get_accuracy(gt_file, result_file):
    
    #Name of Folder
    t_gt_file  = gt_file
    t_gt_file = t_gt_file.split('/Datasets/')[1]
    print("gt dir", t_gt_file)
    
    #Name of Folder
    t_result_file  = result_file
    t_result_file = t_result_file.split('/Results_Exp/')[1]
    print("result dir", t_result_file)

    #GT of folder
    curr_gt = pd.read_csv(gt_file) 
    # print("gt_file: ", gt_file)
    # print("contents: ")
    # print(curr_gt)

    #Results of folder
    curr_res = pd.read_csv(result_file) 
    # print("result_file: ", result_file)
    # print("contents: ")
    # print(curr_res)

    success = 0
    offset = 0
    i = 0

    while i < len(curr_gt):        
        j=i-offset #sometimes a LP is not detected, in this case we have an offset of compairing files
        
        #print("curr_gt.ix[i]: ", curr_gt.ix[i])
        
        #print("curr_gt.ix[i]: ",curr_gt.ix[i])
        #print("curr_res.ix[i]: ",curr_res.ix[i])
        if curr_gt.ix[i][0] == curr_res.ix[j][0]:
            if curr_gt.ix[i][1] == curr_res.ix[j][1]:
                #print("Matched: ", curr_gt.ix[i][1]," == ",curr_res.ix[i][1])
                success = success + 1
            else:
                #print("Not Matched: ", curr_gt.ix[i][1]," == ",curr_res.ix[j][1])
                pass               
        else:
            offset = offset + 1#Offset changed to match rows
            #print("<<<<<<<<<<<<<Results & GT Mismatch at index: ", i,">>>>>>>>>>>>>>>>")
            #print("Not Matched: ", curr_gt.ix[i][0]," == ",curr_res.ix[j][0])
            #print("i",i,"j",j)
        i = i+1

    print("accuracy: ", (float(success*100)/ len(curr_gt)))          
    print("\n\n\n")  

def main(input_dir, output_dir):
    gt_files = glob('%s/*GT.csv' % input_dir)
    result_files = glob('%s/*results.csv' % output_dir)

    for file in range(len(gt_files)):
        get_accuracy(gt_files[file],result_files[file])