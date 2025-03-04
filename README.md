# Character Classifier
Adapted from danbooru dataset maker + image classifer

Dataset from Danbooru2021 (https://www.gwern.net/Danbooru2021). 

## Usage

In config.json, set "metadata path" to null. 

Run generate_file_list.py. 

Combine the years into a single folder. Delete years that are irrelevant (selected characters did not exist by then).

Set that file location to metadata path

Run `rsync_files.py`

The arguments to `rsync_files.py` are:
```
  -o, --original        Download from original dataset. Default behavior is to
                        use the 512px dataset
  -s, --skip-file-list  Don't create the file list before calling rsync. Will
                        assume that file list(s) exist in tmp directory in
                        current path
  -c CONFIG_PATH, --config-path CONFIG_PATH
                        Path to config.json file. Defaults to current
                        directory

```

Run `process_data.py` 
Note: includes splitfolders library

Install dependencies: torch, pandas, matplotlib, seaborn 
Run all cells of classifier.ipynb. 


## Config
The config file allows you to specify tags of images that you want to include or exclude. There are 4 lists of tags that can be provided for controlling the images that end up in the final file list. These lists filter images successively in the order mentioned below. Any image that passes through all filters will end up in the final file list. Any of these lists can be left `null`, in which case all images that passed through the previous filter will also pass through this filter.
```
  include_and: If all of the tags in this list are present in an image, it will be selected
  exclude_or: If any one of the tags in this list are present in an image, it will be rejected
  exclude_and: If all of the tags in this list are present in an image, it will be rejected
  include_or: If any one of the tags in this list are present in an image, it will be selected
```
There are a few more options defined in the config file.

  **classification**: This option lets one switch between making a labelled classification dataset or an unlabelled dataset. If left true, separate file lists will be made for every tag in the include_or list. Images will be separately downloaded for every file list(using multiple calls to `rsync`) and stored in separate directories. Note that if an image has multiple tags it will be downloaded in all possible directories. So the datasets are not mutually exclusive. If left false, a single file list will be made for all tags and all images will be downloaded in a single `rsync` call. This option is *much* faster.
  
  **ratings**: This option takes a list with contents 's','q' and 'e'. They control whether the downloaded images are SFW or NSFW. The 512px version of the dataset only has SFW images so, if using 'q' or 'e' use the `-o` option with `rsync_files.py`.
  
The example config file provided creates a classification dataset for genshin impact characters images that necessarily have the `solo` tag.
