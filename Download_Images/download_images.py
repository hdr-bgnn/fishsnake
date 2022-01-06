# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 16:29:01 2021

@author: tabarin
"""

import os
import sys
import pandas as pd
from urllib import request


def download_images(csv_list):
    '''
    Download images from a subset of the Images_metadata
    https://bgnn.tulane.edu/hdrweb/hdr/user/latesttestmetadata/

    Parameters
    ----------
    csv_list : csv file format
        This file should be a subset of this metadata file
        https://bgnn.tulane.edu/hdrweb/hdr/user/latesttestmetadata/
    Returns
    Create a folder "Images" and download the images from the list in the folder
    -------
    None.

    '''
    
    # Create a folder 'Images' to download the image at the same level than csvlsit
    main_folder, list_name = os.path.split(csv_list)
    list_name  = os.path.splitext(list_name)[0]
    Images_folder = os.path.join(main_folder, 'Images') 
    if not os.path.exists(Images_folder):
        
        os.mkdir(Images_folder)
    
    
    df_list = pd.read_csv(csv_list)
    path_list = df_list['path'].tolist()
    
    for file_path in path_list:
        
        
        file_name = os.path.split(file_path)[-1]
        file_local_path = os.path.join(Images_folder,file_name) 
        
        request.urlretrieve(file_path, file_local_path)
    

if __name__ == '__main__':
    
    download_images(sys.argv[1])
