import os
import shutil
if __name__ == "__main__":
    def mergefolders(name):
        current_directory = os.getcwd()
        final_directory = os.path.join(current_directory, name + '_merged')
        if not os.path.exists(final_directory):
            os.makedirs(final_directory)
        
        for folder in os.listdir(os.path.join(current_directory, name)):
            for file in os.listdir(os.path.join(current_directory, name, folder)):
                os.rename(os.path.join(current_directory, name, folder, file), os.path.join(final_directory, f'{file}'))
        
        shutil.rmtree(os.path.join(current_directory, name))

    