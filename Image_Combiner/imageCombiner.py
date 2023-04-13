from PIL import Image
import os
os.chdir('{your_path}\Image_Combiner')

#Read the two images

for i in range(101):
    image1 = Image.open('a/'+str(i)+'.png')
    image1.show()
    image2 = Image.open('b/'+str(i)+'.png')
    image2.show()
    #resize, first image
    #image1 = image1.resize((426, 240))
    image1_size = image1.size
    image2_size = image2.size
    new_image = Image.new('RGB',(2*image1_size[0], image1_size[1]), (250,250,250))
    new_image.paste(image1,(0,0))
    new_image.paste(image2,(image1_size[0],0))
    new_image.save("result/"+str(i)+".png","PNG")
    new_image.show()