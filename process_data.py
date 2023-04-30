import os
import shutil
import splitfolders
import json


if __name__ == "__main__":

    def getCharNumMapping():
        tag_names = [name for name in os.listdir("dataset") if os.path.isdir(os.path.join("dataset", name))]
        numToChar =  {x:y for x,y in enumerate(tag_names)}
        charTonum = {y:x for x,y in enumerate(tag_names)}
        json_object = json.dumps(numToChar, indent=4)
        with open("numToChar.json", "w") as outfile:
            outfile.write(json_object)
        return charTonum

    def renameFolderstoNumbers(): 
        current_directory = os.getcwd()
        final_directory = os.path.join(current_directory, 'dataset')
        for folder in os.listdir(final_directory):
            os.rename(os.path.join(final_directory, folder), os.path.join(final_directory, str(charToNum[folder])))

    def filesplitter():
        splitfolders.ratio('dataset', output="./split_dataset", seed=1337, ratio=(.8, 0.1,0.1))

    charToNum = getCharNumMapping()
    renameFolderstoNumbers()
    filesplitter()
