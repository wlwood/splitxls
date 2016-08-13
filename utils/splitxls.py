#!/usr/bin/env python
# encoding:utf-8

import time
import os
import xlrd
import csv
import sys

from name2name import find_cate

reload(sys)
sys.setdefaultencoding("utf-8")


class GetContent(object):
    def __init__(self,file_name):
        self.file_name = file_name
        self.tb_temp_name = "Template"
        self.tb_data = self.readdesc()
        self.header = self.get_header()
        self.content = self.get_content()


    def read_excel(self,file_name):
        try:
            data = xlrd.open_workbook(file_name)
        except Exception,e:
            print "open workbook Error!,%s"%e
            return {'status':False, 'message':"打开文件错误,转成xls格式试下吧,%s"%e}
        #sheets = data.sheet_by_name('Template')
        sheets = data.sheets()
        _value_list = [{'name':sheet.name,'values':sheet._cell_values,'nrows':len(sheet._cell_values)} for sheet in sheets]
        #print _value_list
        return {'status':True,'info':_value_list}

    def readdesc(self):
        print "read file ..."
        file_info = self.read_excel(self.file_name)
        if not file_info['status']:
            return {'status':False, "message":file_info['message']}
        tb_data = {}
        for tmp_data in file_info['info']:
            if tmp_data.get("name") == self.tb_temp_name:
                tb_data = tmp_data
        if not tb_data:
            return {"status":False, "message":"not found Template table "}
        return tb_data
    
    def get_header(self):
        header = []
        try:
            header = self.tb_data.get('values',[])[2]
        except Exception,e :
            print "not found header ..."
        return header
    
    def get_content(self):
        content = {}
        try:
            content = self.tb_data.get('values', [])[3:]
        except Exception ,e :
            print "not found content .."
        return content

    
    def mytest(self):
        print self.header
        print self.content
        

    def write_images_csv(self, image_csv_name):
        need_index_name = ['sku','main_image_url', 'other_image_url8']
        name_i_dict = {}
        for name in need_index_name:
            try:
                name_i_dict[name] = self.header.index(name)
            except Exception, e:
                print "not found %s index in header ..." % (name)
                return {"status":False, "message":"没有找到字段: %s " % (name)}
        try:
            img_file = open(image_csv_name,"wb")
        except Exception, e:
            print "open file error,%s"%e
            return {"status":False, "message":"打开文件错误: %s" % e}
        writer = csv.writer(img_file)
        image_csv_header = ['store', 'websites', 'sku', 'images']
        writer.writerow(image_csv_header)
        for line in self.content:
            sku = line[name_i_dict.get('sku')]
            if not sku:
                continue
            images = "|".join(filter(lambda x:x.endswith(".jpg") or x.endswith(".png"),
                                     line[name_i_dict.get("main_image_url"): name_i_dict.get("other_image_url8")]))
            writer.writerow(['admin', 'base', sku, images])
        img_file.close()
        print "write image_csv over ..."
        return {"status":True}
        
                        
    def write_configure_product(self, configure_filename):
        need_index_name = ['parent_child','sku', 'item_name', u'单价', 'product_description', u'毛重','department_name', 'item_type']
        not_index_name = ['color_name', 'size_name']
        name_i_dict = {}
        for name in need_index_name:
            try:
                name_i_dict[name] = self.header.index(name)
            except Exception, e:
                print "not found %s index in header ..." %(name)
                return {"status":False, "message": u"没有找到 %s 字段" % (name)}
        for name in not_index_name:
            try:
                name_i_dict[name] = self.header.index(name)
            except Exception,e :
                print "not found %s index in header ..."%(name)
        try:
            configure_filename_csv = open(configure_filename, "wb")
        except Exception, e:
            print "open file Error, %s" % e
            return {"status":False, "message": "open file Error, %s" %e}
        writer = csv.writer(configure_filename_csv)
        configure_header = ['store', 'websites', 'attribute_set', 'categories', 'type', 'sku', 'name', 'price',
                            'used_attribute','super_attibute_value', 'child_products_sku', 'description', 'weight',
                            'is_in_stock', 'qty', 'status', 'options_container', 'tax_class_id','visibility',
                            'color', 'size']
        writer.writerow(configure_header)
        
        tmp_super_attribute_value = ""
        tmp_child_products_sku = ""
        tmp_used_attribute = []
        current_product_parent = False
        parent_line = ""
        parent_price = 0
        for line in self.content:
            current_n = self.content.index(line)
            if line == self.content[-1]:
                lastline = True
            else:
                lastline = False
            if line[name_i_dict.get("parent_child")].lower() == "parent":
                parent_line = line
                current_product_parent = True
                if current_product_parent:
                    continue
            
            if current_product_parent:
                tmp_child_products_sku += line[name_i_dict.get("sku")] + ","
                if line[name_i_dict.get("department_name")] == "mens":
                    if name_i_dict.get("color_name") and  name_i_dict.get("color_name")!="None":
                        if "man_color" not in tmp_used_attribute:
                            tmp_used_attribute.append("man_color")
                    if name_i_dict.get("size_name") and  name_i_dict.get("size_name"):
                        if "man_size" not in tmp_used_attribute:
                            tmp_used_attribute.append("man_size")
                elif line[name_i_dict.get("department_name")] == "womens":
                    if name_i_dict.get("color_name") and name_i_dict.get("color_name") != "None":
                        if "wom_color" not in tmp_used_attribute:
                            tmp_used_attribute.append("wom_color")
                    if name_i_dict.get("size_name") and   name_i_dict.get("size_name") != "None":
                        if "wom_size" not in tmp_used_attribute:
                            tmp_used_attribute.append("wom_size")
                else:
                    tmp_used_attribute = []
                
                parent_price += float(line[name_i_dict.get(u"单价", 0)])
                if name_i_dict.get("color_name") and  name_i_dict.get("color_name") != "None":
                    tmp_super_attribute_value += str(line[name_i_dict.get("color_name")]) + ":0:0|"
                if name_i_dict.get("size_name") and  name_i_dict.get("size_name") != "None" :
                    tmp_super_attribute_value += str(line[name_i_dict.get("size_name")]) + ":0:0|"
            if lastline:
                current_product_parent = False
            if not lastline and  self.content[current_n + 1][name_i_dict.get("parent_child")].lower() == "parent":
                current_product_parent = False                        
            write_lst = self.get_line_list(line, name_i_dict)
            writer.writerow(write_lst)
            #print tmp_child_products_sku, current_product_parent
            if lastline or not current_product_parent:
                if not parent_line: parent_line = line
                parent_line[name_i_dict.get("sku")] = tmp_child_products_sku.split(",")[0] + "_main"
                parent_line[name_i_dict.get(u"单价")] = parent_price
                parent_line[name_i_dict.get("item_name")] = "configurable"
                tmp_super_attribute_value = "|".join(tmp_super_attribute_value.split("|")[0:-1])
                tmp_used_attribute = ",".join(tmp_used_attribute)
                tmp_child_products_sku = ",".join(tmp_child_products_sku.split(",")[0:-1])
                write_lst = self.get_line_list(parent_line,name_i_dict,
                                               tmp_used_attribute=tmp_used_attribute ,
                                               tmp_child_products_sku=tmp_child_products_sku,
                                               tmp_super_attribute_value=tmp_super_attribute_value)
                writer.writerow(write_lst)
                parent_line = ""
                tmp_super_attribute_value = ""
                tmp_child_products_sku = ""
                tmp_used_attribute = []
                parent_price = 0
        print "write configure product over ..."
        return {"status":True}
                

    def get_line_list(self, line, name_i_dict, tmp_used_attribute=None,tmp_child_products_sku=None, tmp_super_attribute_value=None):
        store = "admin"
        websites = "base"
        categories = find_cate(line[name_i_dict.get("department_name")].lower(), line[name_i_dict.get("item_type")])
        if line[name_i_dict.get("department_name")].lower() == "mens":
            attribute_set = "Men_"+ str(categories).split("/")[-1]
        elif line[name_i_dict.get("department_name")].lower() == "womens":
            attribute_set = "Womens_"+str(categories).split("/")[-1]
        else:
            attribute_set = ""
        type_txt = "simple" if line[name_i_dict.get("parent_child")] == "Child" else "configurable"
        sku = line[name_i_dict.get('sku')]
        name = line[name_i_dict.get("item_name")]
        price = line[name_i_dict.get(u"单价")]
        if tmp_used_attribute:
            used_attribute = tmp_used_attribute
        else:
            used_attribute = ""
        
        if  tmp_super_attribute_value:
            super_attibute_value = tmp_super_attribute_value
        else:
            super_attibute_value = ""
                
        if not tmp_child_products_sku:
            child_products_sku = ""
        else:
            child_products_sku = tmp_child_products_sku
            
        description = line[name_i_dict.get("product_description")]
        weight = line[name_i_dict.get(u"毛重")]
        is_in_stock = "1"
        qty = "100"
        status = "Enabled"
        options_container = "Block after Info Column"
        tax_class_id = "None"

        if line[name_i_dict.get("parent_child")] == "Child":
            visibility = "Not Visible Individually"
        else:
            visibility = "Catalog,Search"
        if line[name_i_dict.get("parent_child")] == "Child":
            man_color = line[name_i_dict.get("color_name")]
        else:
            man_color = ""
                
        if line[name_i_dict.get("parent_child")] == "Child":
            man_size = line[name_i_dict.get("size_name")]
        else:
            man_size = ""

        return [store, websites, attribute_set, categories, type_txt, sku, name, price,
                used_attribute, super_attibute_value, child_products_sku, description,
                weight, is_in_stock, qty, status, options_container, tax_class_id, visibility,
                man_color, man_size]
        
    
def splitFile(filename, upload_path):
    file_start = filename.split(".")[0]
    image_csv_filename = file_start + "_images_csv_" + str(time.time()).replace(".","") + ".csv"
    #image_csv_filename = os.path.join(upload_path, image_csv_filename_start)
    print "image_csv_filename:",image_csv_filename
    configure_filename = file_start + "_configure_filename_" + str(time.time()).replace(".", "") + ".csv"
    #configure_filename = os.path.join(upload_path, configure_filename_start)
    print "configure_filename:", configure_filename
    myget = GetContent(filename)
    img_status =  myget.write_images_csv(image_csv_filename)
    image_csv_name = image_csv_filename.split("/")[-1] if img_status else ""
    print "img_status: ", img_status
    configure_status = myget.write_configure_product(configure_filename)
    configure_name = configure_filename.split("/")[-1] if configure_status else ""
    print "configure_status: ", configure_status
    if img_status.get("status") != False  and configure_status.get("status") != False: 
        return {"image_csv_filename":image_csv_filename,
                "image_csv_name": image_csv_name,
                "configure_filename":configure_filename,
                "configure_name": configure_name
            }    
    else:
        if not img_status.get("status") and configure_status.get("status"):
            return {"status":False, "message": img_status.get("message")}
        elif  img_status.get("status") and not configure_status.get("status"):
            return {"status":False, "message": configure_status.get("message")}
        else:
            return {"status":False,
                    "message": "img:"+str(img_status.get("message","")) +",\t\n" +
                    "configure:"+ str(configure_status.get("message"))}
        
        

if __name__ == "__main__":
    if len(sys.argv)>1:
        filename = sys.argv[1]
    else:
        print "not found xls or xlsx file ..."
        sys.exit()
    print filename
    image_csv_filename = "images_csv.csv"
    configure_filename = "configure_product.csv"
    
    myget = GetContent(filename)
    myget.write_images_csv(image_csv_filename)
    myget.write_configure_product(configure_filename)
    
            
