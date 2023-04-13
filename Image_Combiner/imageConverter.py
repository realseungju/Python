from PIL import Image
import os
os.chdir('{your_path}\\Image_Combiner')

for i in range(101):
    image1 = Image.open('a/'+str(i)+'.png').convert('RGB')
    image1.save('convert_result/a/'+str(i)+'.jpg', 'jpeg')
    image2 = Image.open('b/'+str(i)+'.png').convert('RGB')
    image2.save('convert_result/b/'+str(i)+'.jpg', 'jpeg')