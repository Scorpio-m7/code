from PIL import Image#导入Image模块
img1=Image.open('img1.jpg')#打开图片
img1.show()#显示图片
print('图片的格式',img1.format,'\n大小',img1.size,'\n宽度',img1.width,'高度',img1.height,'\n获取(100,100)处RGB值',img1.getpixel((100,100)))#查看图片信息
#=======================================================================================
img2=Image.new('RGB',img1.size,'blue')#创建RGB模式蓝色图片,大小和img1一样
Image.blend(img1,img2,alpha=0.5).show()#透明度混合
img3=Image.open('img3.jpg').resize(img1.size)#重设img3大小,和img1一样
r,g,b=img3.split()#按RGB三个通道切割
Image.composite(img1,img3,b).show()#使用b通道对img1遮罩
#=======================================================================================
Image.eval(img1,lambda x:x*2).show()#每个像素扩大2倍,使用匿名函数,将img1中每个像素传给x,x*2返回
img4=img1.copy()#复制图像
img4.thumbnail((920,200))#按尺寸进行缩放
img4.show()
img3_crop=img3.crop((50,50,200,200))#剪切矩形区域
img4.paste(img3_crop,(30,30))#粘贴到指定位置
img4.show()
#=======================================================================================
img1.rotate(30).show()#旋转图像
img1.transpose(Image.FLIP_LEFT_RIGHT).show()#左右镜像反转
img1.transpose(Image.ROTATE_90).show()#90°旋转
img1.transpose(Image.TRANSPOSE).show()#转置
r1,g1,b1=img2.split()#按照RGB通道分离图像
r2,g2,b2=img3.split()
Image.merge('RGB',[r1,g2,b2]).show()#按照RGB通道合并图像
