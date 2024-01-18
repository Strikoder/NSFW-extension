import os 
import shutil
import pandas as pd


data = pd.read_csv("Dataset/SCUT-FBP5500_v2/train_test_files/All_labels.txt", delimiter=" ", header=None,names=['photo','score'])



source_dir ="Dataset/SCUT-FBP5500_v2/Images"
hit_dir="Dataset/SCUT-FBP5500_v2/hit"
miss_dir="Dataset/SCUT-FBP5500_v2/miss"

for _,row in data.iterrows():
    filename = row['photo']
    score = row['score']
    source_file=os.path.join(source_dir,filename)
    if os.path.isfile(source_file): # I deleted male photos
        if score>=4:
            shutil.move(source_file,os.path.join(hit_dir,filename))
        else:
            shutil.move(source_file,os.path.join(miss_dir,filename))

