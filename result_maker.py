import os
import csv
from glob                    import glob
import pandas as pd

def main(output_dir):
    files = glob('%s/*car_lp_str.txt' % output_dir)
    results = []
    temp = ""

    for file in files:
        f = open(file, "r")
        temp = file.split('/')[-1]
        temp = temp.replace("car_lp_str.txt","")
        results.append([temp,(f.read()).strip()])            
        f.close()
    df = pd.DataFrame(results)
    print(len(files))
    df.to_csv(output_dir+'results.csv')

    # with open(output_dir+'results.csv', 'wb') as myfile:
    #     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    #     wr.writerow(results)

main('/home/umar/Desktop/Video_Surveillance_Lab/Car_Theft/Experiments/Results_Exp/baza_slika/040603/')
