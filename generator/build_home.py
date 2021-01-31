# -*- coding: utf-8 -*-
from jinja2 import Environment, FileSystemLoader
from product import load_products
import os
import cv2

def gen_image(img_pth,save_pth,size):
    img = cv2.imread(img_pth)
    s_max = max(img.shape[0],img.shape[1])
    scale = size/s_max
    thumnail_img = cv2.resize(img,(0,0),fx=scale,fy=scale)
    cv2.imwrite(save_pth,thumnail_img)

def build():
    products = load_products('docs/products')
    for p in products:
        img_pth = os.path.join(p.fd,p.imgs[0])
        base_name = os.path.basename(p.fd)
        size = 400
        thumnail_name = base_name+'_thumnail'+str(size)+'.jpg'
        save_pth = '../images/'+thumnail_name
        gen_image(img_pth,save_pth,size)
        p.thumnail = 'images/'+thumnail_name
        
        size = 800
        thumnail_name = base_name+'_thumnail'+str(size)+'.jpg'
        save_pth = '../images/'+thumnail_name
        gen_image(img_pth,save_pth,size)
        p.bigimage = 'images/'+thumnail_name
    
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('home.html')
    template.stream(products=products).dump('../index.html')


if __name__ == '__main__':
    build()
    