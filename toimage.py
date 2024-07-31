import datetime#引入依赖
import os
import fitz  # fitz就是pip install PyMuPDF
import cv2
import shutil
from paddleocr import PPStructure,draw_structure_result,save_structure_res
def pyMuPDF_fitz(pdfPath, imagePath):#pdf转图片
    startTime_pdf2img = datetime.datetime.now()  # 开始时间

    print("imagePath=" + imagePath)
    pdfDoc = fitz.open(pdfPath)
    for pg in range(pdfDoc.page_count):
        page = pdfDoc[pg]
        rotate = int(0)
        # 每个尺寸的缩放系数为4，这将为我们生成分辨率提高4的图像。
        # 此处若是不做设置，默认图片大小为：792X612, dpi=96
        zoom_x = 4  # (1.33333333-->1056x816)   (2-->1584x1224)
        zoom_y = 4
        mat = fitz.Matrix(zoom_x, zoom_y).prerotate(rotate)
        pix = page.get_pixmap(matrix=mat, alpha=False)

        if not os.path.exists(imagePath):  # 判断存放图片的文件夹是否存在
            os.makedirs(imagePath)  # 若图片文件夹不存在就创建

        pix._writeIMG(imagePath + '/' + 'images_%s.img' % pg,1,'img')  # 将图片写入指定的文件夹内

    endTime_pdf2img = datetime.datetime.now()  # 结束时间
    print('pdf转图片时间=', (endTime_pdf2img - startTime_pdf2img).seconds)

def gci(filepath):
#遍历filepath下所有文件  
    files = os.listdir(filepath)  
    for fi in files:
        # 将转换的图片保存到对应imgs的对应子目录下     
        pyMuPDF_fitz(os.path.join(filepath,fi), os.path.join('imgs',fi[:-4]))
 
fi="./pdf/qlora.pdf"
pyMuPDF_fitz(fi,os.path.join('imgs',fi[:-4]))