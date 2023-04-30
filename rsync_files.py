import sys
import os
import glob
import argparse
import shutil
from generate_file_list import handler

if __name__ == "__main__":
    
    def mergefolders(name):
        current_directory = os.getcwd()
        final_directory = os.path.join(current_directory, name + '_merged')
        if not os.path.exists(final_directory):
            os.makedirs(final_directory)
        
        for folder in os.listdir(os.path.join(current_directory, name)):
            for file in os.listdir(os.path.join(current_directory, name, folder)):
                for file2 in os.listdir(os.path.join(current_directory, name, folder, file)):
                    os.rename(os.path.join(current_directory, name, folder, file, file2), os.path.join(final_directory, f'{file2}'))
        shutil.rmtree(os.path.join(current_directory, name))
        os.rename(os.path.join(current_directory, name + '_merged'), os.path.join(current_directory, name))



    parser = argparse.ArgumentParser(description='Download Danbooru2019 images')
    parser.add_argument("-o","--original",help="Download from original dataset. Default behavior is to use the 512px dataset", action="store_true")
    parser.add_argument("-s","--skip-file-list",help="Don't create the file list before calling rsync. Will assume that file list(s) exist in tmp directory in current path", action="store_true")
    parser.add_argument("-c","--config-path",help="Path to config.json file. Defaults to current directory",default="")
    args = parser.parse_args()
    ftype = "original" if args.original else "512px"
    if not args.skip_file_list:
        print("Making file list(s)...")
        handler(args.config_path+"config.json")

    files = glob.glob('tmp/*.txt')
    if len(files) > 1:
        
        for file in files:
            path = "".join(file[:-4].split('_')[2])
            file = file[:3] + '/' + file[3:]
            print(file)
            print(path)
            os.makedirs(path, exist_ok=True)
            os.system(f'rsync -P --recursive --verbose  --include="*/" --include-from={file} --exclude="*" --ignore-existing --relative rsync://176.9.41.242:873/danbooru2021/{ftype}/ ./{path}/') 
            mergefolders(path)

    else:
        print(files)
        path = "dataset"
        file = files[0]
        file = file[:3] + '/' + file[3:]
        os.makedirs(path, exist_ok=True)
        os.system(f'rsync -P --recursive --verbose  --include="*/" --include-from={file} --exclude="*" --ignore-existing --relative rsync://176.9.41.242:873/danbooru2021/{ftype}/ ./{path}/') 
        os.system(f'find {path}/{ftype}/ -mindepth 2 -type f -print -exec mv {{}} {path} \\;')
        os.system(f'find {path}/{ftype}/ -empty -type d -delete')






