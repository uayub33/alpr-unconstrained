import os, os.path
import vehicleDetection as VD
import licensePlateDetection as LP
import licensePlateOcr as OCR
#import genOutputs as Gen
import result_maker as RM

path = '/home/umar/Desktop/Video_Surveillance_Lab/Car_Theft/Experiments/Datasets/'

#r=root, d=directories, f = files
All_input_dir = []
for r, d, f in os.walk(path):
	for dirs in d:
		All_input_dir.append(os.path.join(r,dirs))

#All_input_dir.append(path+"baza_slika/040603")#Remove this line and uncomment the above for all files
All_output_dir = list(map(lambda a: a.replace("Datasets", "Results_Exp"), All_input_dir))

num_of_dirs = len(All_input_dir)

lp_model="data/lp-detector/wpod-net_update1.h5"#these weights are used in Licenceplate detection

for i in range(num_of_dirs):
	input_dir=All_input_dir[i]
	output_dir=All_output_dir[i]
	csv_file = os.path.join(output_dir,"results.csv")

	# Detect vehicles
	#VD.main(input_dir, output_dir)
	
	# Detect license plates
	#LP.main(output_dir,lp_model)

	# OCR
	#OCR.main(output_dir)

	# Draw output and generate list
	#Gen.main(input_dir, output_dir)

	RM.main(input_dir,output_dir)

# files = []
# txtFiles = [".txt"]
# for f in os.listdir(output_dir):
#     ext = os.path.splitext(f)[1]
#     if ext.lower() in txtFiles:
# 	    os.remove(os.path.join(output_dir,f))
