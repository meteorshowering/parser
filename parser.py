import cv2
import os
import layoutparser as lp
from paddleocr import PPStructure,draw_structure_result,save_structure_res
from paddleocr.ppstructure.recovery.recovery_to_doc import sorted_layout_boxes, convert_info_docx
from PIL import Image
import json

table_engine = PPStructure(show_log=True)
save_folder = './result/CLIP'
figure_folder = './figures/CLIP'
img_dir = './imgs'

files = os.listdir(img_dir)  
# for fi in files:
#     # 找到文件对应子目录
#     # print(fi)
#     fi_d = os.path.join(img_dir,fi)  
#     # print(fi_d)  
# fi_d="imgs\qlora"
# for img in os.listdir(fi_d):
#     img_path = os.path.join(fi_d,img)    #pdf to imgs
figure_count = 0
img_path = "imgs\CLIP\images_39.img"
page_num =img_path.split('_')[1]

img = cv2.imread(img_path)
result = table_engine(img)    #get layout
# save_structure_res(result, os.path.join(save_folder,"qlora"),os.path.basename(img_path).split('.')[0])
# 保存在每张图片对应的子目录下
h, w, _ = img.shape
res = sorted_layout_boxes(result, w)   #这个函数是左右分栏的处理函数，厉害，效果很好
#print(type(res))   sort之后的结果是list

#以下代码用来把table作为图片存下来
figure_per_page = 0
res_useful =[]
figures_info=[]
for region in res:
    useful_info={}
    useful_info['type'] = region['type']
    useful_info['bbox'] = region['bbox']
    useful_info['text'] = ''
    if (type(region['res']).__name__=='list'):
        for i in range(len(region['res'])):
            useful_info['text'] += region['res'][i]['text']
    print(useful_info['text'])
    res_useful.append(useful_info)
# with open('test.json','a') as file: 
#             json.dump(res_useful,file,indent=2)
where_fig = 0
for i in range(len(useful_info)):
    if useful_info[i]['type'] == 'table' or useful_info[i]['type'] == 'figure':
        figure_info = {}
        figure_count += 1
        figure_per_page += 1
        figure_img = img[useful_info[i]['bbox'][0]:useful_info[i]['bbox'][2],useful_info[i]['bbox'][1]:useful_info[i]['bbox'][3]]
        figure_addr = os.path.join(figure_folder,str(figure_count),)
        figure_info['figure_per_eassy'] = figure_count
        figure_info['page'] = page_num
        figure_info['figure_per_page'] = figure_per_page
        
    if region['type']=='table':
        table_img = img[region['bbox'][0]:region['bbox'][2],region['bbox'][1]:region['bbox'][3]]
        table_addr = os.path.join(figure_folder,)
        cv2.imwrite('test.jpg',table_img)
# print(figure_context)        
        
        

#以下代码用来在图片上画region框框，以及ocr的结果
# font_path = 'doc/fonts/simfang.ttf' # PaddleOCR下提供字体包
# im_show = draw_structure_result(img, result,font_path=font_path)
# im_show = Image.fromarray(im_show)
# im_show.save('result.jpg')

# convert_info_doc(img, res, save_folder, os.path.basename(img_path).split('.')[0])



# image = cv2.imread('imgs/CLIP/images_3.img')
# image = image[..., ::-1]

# # 加载模型
# model = lp.PaddleDetectionLayoutModel(config_path="lp://PubLayNet/ppyolov2_r50vd_dcn_365e_publaynet/config",
#                                 threshold=0.5,
#                                 label_map={0: "Text", 1: "Title", 2: "List", 3:"Table", 4:"Figure"},
#                                 enforce_cpu=False ,
#                                 enable_mkldnn=True)
# # 检测
# layout = model.detect(image)

# # 显示结果
# show_img = lp.draw_box(image, layout, box_width=3, show_element_type=True)


