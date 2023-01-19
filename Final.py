import os
import pandas as pd
import re
import shutil

main_directory = "//home//rajesh//Desktop//week2//TASK 3.1//sample_dataset"
destination_path = "//home//rajesh//Desktop//week2//TASK 3.1//1//Sample_data_output"

os.makedirs(destination_path)


for subfolder in os.listdir(main_directory):
    subfolder_path = os.path.join(main_directory, subfolder)
    if os.path.isdir(subfolder_path):
        file_names = []
        for filename in os.listdir(subfolder_path):
            name_without_ext, file_extension = os.path.splitext(filename)
            if file_extension != '.csv':
                file_names.append(name_without_ext)
        destination_file = os.path.join(destination_path, subfolder + '.csv')
     
        df = pd.DataFrame(file_names)

        df.to_csv(destination_file,index=False,header=False)
        string = open(destination_file).read()
        new_str1 = re.sub('_',',',string)
        open(destination_file,'w').write(new_str1)       
        df = pd.read_csv(destination_file)
        df.columns = ["Roll no 1", "Roll no 2", "Distance"]
        df.to_csv(destination_file, index=False)


files = os.listdir(destination_path)
for file in files:
    file_name = os.path.splitext(file)[0]
    src = os.path.join(destination_path, file)
    if '1' in file_name: 
        os.makedirs(os.path.join(destination_path, file_name+''), exist_ok=True)
        dst = os.path.join(destination_path, file_name+'', file)
        
    shutil.move(src, dst)