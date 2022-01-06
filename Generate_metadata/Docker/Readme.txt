Read.me
# 

# Use of Docker image for metadata generator
# Steps to setup and use metadata_generator docker

#Clone github directory drexel_metadata
git clone https://github.com/hdr-bgnn/drexel_metadata.git
# make sure there is a folder name output containing model_final.pth

#TODO# The model weights model_final.pth is available ???
#TODO# Create a download from somewhere this could be integrated in the dockerfile

# Build the docker image
cd location/of/drexel_metadata

sudo docker build -t metadata_generator -f Docker/Dockerfile .

# Usage to analysis Images
# Create a folder Data and a list of the image_path to analysis 
# Image_path are available in Image_MetaData_GLIN (available here https://bgnn.tulane.edu/hdrweb/hdr/user/latesttestmetadata/)
# List_images should look like this :
http://www.tubri.org/HDR/INHS/INHS_FISH_29592.jpg
http://www.tubri.org/HDR/INHS/INHS_FISH_27116.jpg
http://www.tubri.org/HDR/INHS/INHS_FISH_28597.jpg

mkdir Data
cd Data
cat > List_images
http://www.tubri.org/HDR/INHS/INHS_FISH_29592.jpg
http://www.tubri.org/HDR/INHS/INHS_FISH_27116.jpg
http://www.tubri.org/HDR/INHS/INHS_FISH_28597.jpg
ctrl d

./script_dowload_image.sh List_images $(pwd) 

# Run the docker
cd location/of/Data
sudo docker run -v $(pwd):/app/Data -it metadata_generator bash
#Docker_cmd_line$ python gen_metadata.py /app/Data/Images
#Docker_cmd_line$ mv metadata.json Data/



 
