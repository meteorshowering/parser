import os
import json
res_floder = 'result'
res_files = os.listdir(res_floder)
for file in res_files:
    print(file)
    file_dir=os.path.join(res_floder,file)
    figure_title_save=os.path.join('extractedimgs',file,'figure_title.txt')
    num=0
    pages=os.listdir(file_dir)
    pages.sort(key=lambda x:int(x.split('_')[1])) #in case all pages are tackled randomly 
    for page in pages:
        page_dir=os.path.join(file_dir,page)  
        txt_dir=os.path.join(page_dir,"res_0.txt")
# txt_dir = "result/qlora/images_2/res_0.txt"
        with open(txt_dir,'r') as file:
            data = file.readlines()
            for block in data:
                singleblockdata = json.loads(block)
                if singleblockdata["type"]=="text":
                    # singlelinedata.sort(key=lambda z: (z.bbox.x1, z.bbox.y1, z.bbox.x2, z.bbox.y2))

                    for slices in singleblockdata['res']:
                        print(slices['text'])  
                elif singleblockdata['type'] == 'figure_caption':   #figure title extract 
                    figure_title = ''
                    for slices in singleblockdata['res']:
                        figure_title += slices['text']
                    with open(figure_title_save,'a') as figurefile:
                        figurefile.writelines(figure_title+'\n')
                    print(figure_title)
def blockedgesmooth(block_datas):
                
        # for data in os.listdir(page_dir):      #第data页下的文件
        #     data_dir=os.path.join(page_dir,data)
        #     txttype=filetype.guess(data_dir)
        #     if txttype==None:
        #         pass
        #     else:
        #         txttype=txttype.extension
        #     if txttype=="txt":