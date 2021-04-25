from PIL import Image#导入Image模块
img=Image.open('img1.jpg')#打开图片
img.show()#显示图片
print('图片的格式',img.format,'\n大小',img.size,'\n宽度',img.width,'高度',img.height,'\n获取(100,100)处RGB值',img.getpixel((100,100)))#查看图片信息