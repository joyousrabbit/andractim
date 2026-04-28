# -*- coding: utf-8 -*-
import os
import json

class Product:
    def __init__(self,fd):
        self.fd = fd
        self.title = ''
        self.price = 0.0
        self.imgs = []
        
        self.__load_info()
        self.__load_images()
        
    def __load_info(self):
        with open(os.path.join(self.fd,'info.json')) as f:
            data = json.load(f)
            self.title = data['title']
            self.price = data['price']
        
    def __load_images(self):
        self.imgs = sorted([f for f in os.listdir(os.path.join(self.fd)) if f.endswith('.png') or f.endswith('.jpg')])
        
def load_products(root_fd):
    products = []
    subfolders = sorted([f.name for f in os.scandir(root_fd) if f.is_dir()])
    for subfolder in subfolders:
        p = Product(os.path.join(root_fd,subfolder))
        products.append(p)
    return products