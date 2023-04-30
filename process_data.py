import os
import shutil
import splitfolders


if __name__ == "__main__":


    tag_names = [name for name in os.listdir("dataset") if os.path.isdir(os.path.join("dataset", name))]
    numToChar =  {x:y for x,y in enumerate(tag_names)}
    numToChar = {0: 'aether', 1: 'albedo', 2: 'amber', 3: 'barbara', 4: 'bennett', 5: 'chongyun', 6: 'diluc', 7: 'diona', 8: 'eula',
                  9: 'fischl', 10: 'ganyu', 11: 'gorou', 12: 'hu', 13: 'jean', 14: 'kaedehara', 15: 'kaeya', 16: 'kamisato', 17: 'keqing',
                    18: 'klee', 19: 'kujou', 20: 'lisa', 21: 'lumine', 22: 'mona', 23: 'ningguang', 24: 'noelle', 25: 'paimon', 26: 'qiqi',
                      27: 'raiden', 28: 'razor', 29: 'rosaria', 30: 'sangonomiya', 31: 'sayu', 32: 'sucrose', 33: 'tartaglia', 34: 'thoma',
                        35: 'venti', 36: 'xiangling', 37: 'xiao', 38: 'xingqiu', 39: 'xinyan', 40: 'yae', 41: 'yanfei', 42: 'yoimiya', 
                        43: 'yunjin', 44: 'zhongli'}
    
    charToNum = {v: k for k, v in numToChar.items()}

    def renameFolderstoNumbers(): 
        current_directory = os.getcwd()
        final_directory = os.path.join(current_directory, 'dataset copy')
        for folder in os.listdir(final_directory):
            os.rename(os.path.join(final_directory, folder), os.path.join(final_directory, str(charToNum[folder])))

    #renameFolderstoNumbers()



    def filesplitter():
        splitfolders.ratio('dataset copy', output="./split_dataset", seed=1337, ratio=(.8, 0.1,0.1))

    renameFolderstoNumbers()
    filesplitter()
