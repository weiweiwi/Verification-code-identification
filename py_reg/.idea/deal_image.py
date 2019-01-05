import os
import image

pic_url = 'C:/Users/dell/Desktop/Verification-code-identification/pic/inOrder'
def read_image():
    image_array=[]
    image_label=[]
    file_list=os.listdir(pic_url)
    for file in file_list:
        image=Image.open(path+'/'+file)
        file_name=file.split(".")[0]
        image_array.append(image)
        image_label.append(file_name)

    return image_array,image_label


if __name__=="__main__":
    read_image()


