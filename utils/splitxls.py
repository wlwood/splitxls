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
            if tmp_data.get("name", "").lower() == "template" or tmp_data.get("name","").lower() == "sheet1":
                tb_data = tmp_data
        if not tb_data:
            return {"status":False, "message":u"请把sheet的名称改成sheet1或者Template"}
        return {"status":True, "tb_data":tb_data }
    
    def get_header(self):
        header = []
        try:
            header = self.tb_data.get("tb_data").get('values',[])[2]
        except Exception,e :
            print "not found header ..."
        return header
    
    def get_content(self):
        content = {}
        try:
            content = self.tb_data.get("tb_data").get('values', [])[3:]
        except Exception ,e :
            print "not found content .."
        return content

    
    def mytest(self):
        print self.header
        print self.content

    def myjudge(self):
        try:
            parent_child_i = self.header.index("parent_child")
        except Exception, e:
            parent_child_i = 0
            return {"status":False, "message":"没有找到parent_child字段"}
        #print parent_child_i
        parent_child_list = map(lambda x:x[parent_child_i].lower(), self.content)
        parent_child_in = "parent" in parent_child_list
        return parent_child_in
        pass


    def jewel_write_images_csv(self, image_csv_name):
        if not self.tb_data.get("status"):
            return {"status": False, "message":self.tb_data.get("message")}
        need_index_name = ['sku','main_image_url', 'other_image_url8', 'parent_child']
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
        #print "name_i_dict: ", name_i_dict
        writer = csv.writer(img_file)
        image_csv_header = ['store', 'websites', 'sku', 'images' ]
        writer.writerow(image_csv_header)
        for line in self.content:
            sku = line[name_i_dict.get("sku")]
            images = "|".join(filter(lambda x:x.endswith(".jpg") or x.endswith(".png"),
                                     line[name_i_dict.get("main_image_url"): name_i_dict.get("other_image_url8")]))
            writer.writerow(['admin', 'base', sku, images[0:-1]])
            #images_all = ""            
        img_file.close()
        print "write image_csv over ..."
        return {"status":True}            
        pass

    def jewel_write_configure_csv(self, configure_filename):
        if not self.tb_data.get("status"):
            return {"status":False, "message": self.tb_data.get("message")}
        need_index_name = ['parent_child','sku', 'item_name', u'单价', 'product_description', u'毛重','department_name', 'item_type']
        not_index_name = ['color_name', 'size_name']
        name_i_dict = {}
        #print self.header
        for name in need_index_name:
            try:
                name_i_dict[name] = self.header.index(name)
            except Exception, e:
                print "not found %s index in header ..." %(name)
                return {"status":False, "message": u"没有找到 %s 字段" % (name)}
        for name in not_index_name:
            try:
                name_i_dict[name] = self.header.index(name)
                #print name_i_dict[name]
            except Exception,e :
                print "not found %s index in header ..."%(name)
        try:
            configure_filename_csv = open(configure_filename, "wb")
        except Exception, e:
            print "open file Error, %s" % e
            return {"status":False, "message": "open file Error, %s" %e}
        typename = "jewels"
        configure_header = self.judge_header(self.content[1], typename, name_i_dict)
        writer = csv.writer(configure_filename_csv)
        writer.writerow(configure_header)
        for line in self.content:
            current_n = self.content.index(line)
            write_lst = []
            #write_lst = self.get_line_list(line, name_i_dict)
            store = "admin"
            websites = "base"
            categories = find_cate("jewels", line[name_i_dict.get("item_type")])
            attribute_set = "Jewels_" + str(categories).split("/")[-1]
            type_txt = "configurable"
            sku = line[name_i_dict.get("sku")] + "_main"
            name = line[name_i_dict.get("item_name")]
            price = line[name_i_dict.get(u"单价")]
            if name_i_dict.get("color_name") and name_i_dict.get("size_name"):
                if line[name_i_dict.get("color_name")] !="" and line[name_i_dict.get("size_name")] != "":
                    used_attribute = typename+"_color" + "," + typename +"_size"
                    super_attibute_value = line[name_i_dict.get("color_name")] + ":0:0|" + line[name_i_dict.get("size_name")] + ":0:0"
                elif line[name_i_dict.get("color_name")] != "":
                    super_attibute_value = line[name_i_dict.get("color_name")] + ":0:0"
                    used_attribute = typename + "_color"
                elif line[name_i_dict.get("size_name")] != "":
                    super_attibute_value = line[name_i_dict.get("size_name")] + ":0:0"
                    used_attribute = typename + "_size"
                else:
                    super_attibute_value = ""
                    used_attribute = ""
            elif name_i_dict.get("color_name")  and not name_i_dict.get("size_name"):
                if line[name_i_dict.get("color_name")] != "":
                    super_attibute_value = line[name_i_dict.get("color_name")] + ":0:0"
                    used_attribute = typename + "_color"
                else:
                    super_attibute_value = ""
                    used_attribute = ""
            elif not name_i_dict.get("color_name") and name_i_dict.get("size_name"):
                if line[name_i_dict.get("size_name")] != "":
                    super_attibute_value = line[name_i_dict.get("size_name")] + ":0:0"
                    used_attribute = typename + "_size"
                else:
                    super_attibute_value = ""
                    used_attribute = ""
            else:
                used_attribute = ""
                super_attibute_value = ""
            child_products_sku = ""
            description = line[name_i_dict.get("product_description")]
            weight = line[name_i_dict.get(u"毛重")]
            is_in_stock = "1"
            qty = "100"
            status = "Enabled"
            options_container = "Product Info Column"
            tax_class_id = "None"
            
            visibility = "Not Visible Individualy"
            try:
                man_color = line[name_i_dict.get("color_name")]
            except:
                man_color = ""
            try:
                man_size = line[name_i_dict.get("size_name")]
            except:
                man_size = ""
            write_lst = [store, websites, attribute_set, categories, type_txt, sku, name, price, used_attribute,
                         super_attibute_value, child_products_sku, description, weight, is_in_stock, qty, status,
                         options_container, tax_class_id, visibility, man_color, man_size ]    
            writer.writerow(write_lst)
        print "write configure product over ..."
        configure_filename_csv.close()
        return {"status": True}
        pass
        
    def write_images_csv(self, image_csv_name):
        if not self.tb_data.get("status"):
            return {"status": False, "message":self.tb_data.get("message")}
        need_index_name = ['sku','main_image_url', 'other_image_url8', 'parent_child']
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
        #print "name_i_dict: ", name_i_dict
        writer = csv.writer(img_file)
        image_csv_header = ['store', 'websites', 'sku', 'images' ]
        writer.writerow(image_csv_header)
        lastline = False
        current_product_parent = False
        images_all = ""
        current_n = 0
        sku_line  = {}
        for line in self.content:
            if line[name_i_dict.get("parent_child")].lower() == "parent":
                current_product_parent = True
                sku_line = self.content[self.content.index(line) + 1]
                if current_product_parent:
                    continue
                #print "parent ..."
                #line = self.content[self.content.index(line) + 1]
            #images = "|".join(filter(lambda x:x.endswith(".jpg") or x.endswith(".png"),
            #                         line[name_i_dict.get("main_image_url"): name_i_dict.get("other_image_url8")]))
            if not sku_line:
                continue
            for img in line[name_i_dict.get("main_image_url"): name_i_dict.get("other_image_url8")]:
                if img not in images_all.split("|"):
                    images_all += img + "|"
            if line == self.content[-1]:
                lastline = True
            current_n = self.content.index(line)
            sku = sku_line[name_i_dict.get("sku")] + "_main" 
            if lastline or self.content[current_n + 1][name_i_dict.get("parent_child")].lower() == "parent":
                current_product_parent = False
            if not current_product_parent or lastline:
                writer.writerow(['admin', 'base', sku, images_all[0:-1]])
                images_all = ""
        img_file.close()
        print "write image_csv over ..."
        return {"status":True}
        
                        
    def write_configure_product(self, configure_filename):
        if not self.tb_data.get("status"):
            return {"status": False, "message":self.tb_data.get("message")}
        need_index_name = ['parent_child','sku', 'item_name', u'单价', 'product_description', u'毛重','department_name', 'item_type']
        not_index_name = ['color_name', 'size_name']
        name_i_dict = {}
        #print self.header
        for name in need_index_name:
            try:
                name_i_dict[name] = self.header.index(name)
            except Exception, e:
                print "not found %s index in header ..." %(name)
                return {"status":False, "message": u"没有找到 %s 字段" % (name)}
        for name in not_index_name:
            try:
                name_i_dict[name] = self.header.index(name)
                #print name_i_dict[name]
            except Exception,e :
                print "not found %s index in header ..."%(name)
        try:
            configure_filename_csv = open(configure_filename, "wb")
        except Exception, e:
            print "open file Error, %s" % e
            return {"status":False, "message": "open file Error, %s" %e}
        writer = csv.writer(configure_filename_csv)
        if self.content[1][name_i_dict.get("department_name")] == "mens":
            typename = "men"
            configure_header = self.judge_header(self.content[1],typename, name_i_dict)
        elif self.content[1][name_i_dict.get("department_name")] == "womens":
            typename = "wom"
            configure_header = self.judge_header(self.content[1], typename, name_i_dict)
        else:
            typename = "jewels"
            configure_header = self.judge_header(self.content[1], typename, name_i_dict)
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
            #print line[name_i_dict.get("parent_child")], self.content.index(line)
            if line[name_i_dict.get("parent_child")].lower() == "parent":
                parent_line = line
                current_product_parent = True
                if current_product_parent:
                    continue

            if current_product_parent:
                tmp_child_products_sku += line[name_i_dict.get("sku")] + ","
                if line[name_i_dict.get("department_name")].lower() == "mens":
                    if name_i_dict.get("color_name") and  name_i_dict.get("color_name")!="None":
                        if "man_color" not in tmp_used_attribute:
                            tmp_used_attribute.append("man_color")
                    if name_i_dict.get("size_name") and  name_i_dict.get("size_name"):
                        if "man_size" not in tmp_used_attribute:
                            tmp_used_attribute.append("man_size")
                elif line[name_i_dict.get("department_name")].lower() == "womens":
                    if name_i_dict.get("color_name") and name_i_dict.get("color_name") != "None":
                        if "wom_color" not in tmp_used_attribute:
                            tmp_used_attribute.append("wom_color")
                    if name_i_dict.get("size_name") and   name_i_dict.get("size_name") != "None":
                        if "wom_size" not in tmp_used_attribute:
                            tmp_used_attribute.append("wom_size")
                else:
                    tmp_used_attribute = []
                
                #parent_price += float(line[name_i_dict.get(u"单价", 0)])
                parent_price = line[name_i_dict.get(u"单价", 0)] 
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
                #parent_line[name_i_dict.get("item_name")] = parent_line[name_i_dict.get("")]
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
        type_txt = "simple" if line[name_i_dict.get("parent_child")].lower() == "child" else "configurable"
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
        options_container = "Product Info Column"
        tax_class_id = "None"

        if line[name_i_dict.get("parent_child")].lower() == "child":
            visibility = "Not Visible Individually"
        else:
            visibility = "Catalog, Search"
        if line[name_i_dict.get("parent_child")].lower() == "child":
            try:
                man_color = line[name_i_dict.get("color_name")]
            except:
                man_color = ""
        else:
            man_color = ""
                
        if line[name_i_dict.get("parent_child")].lower() == "child":
            try:
                man_size = line[name_i_dict.get("size_name")]
            except:
                man_size = ""
        else:
            man_size = ""

        return [store, websites, attribute_set, categories, type_txt, sku, name, price,
                used_attribute, super_attibute_value, child_products_sku, description,
                weight, is_in_stock, qty, status, options_container, tax_class_id, visibility,
                man_color, man_size]
    def judge_header(self, line, typename, name_i_dict):
        if name_i_dict.get("color_name") and name_i_dict.get("size_name"):
            configure_header = ['store', 'websites', 'attribute_set', 'categories', 'type', 'sku', 'name', 'price',
                            'used_attribute','super_attibute_value', 'child_products_sku', 'description', 'weight',
                            'is_in_stock', 'qty', 'status', 'options_container', 'tax_class_id','visibility',
                            '%s_color'%typename, '%s_size'%typename]
        elif name_i_dict.get("color_name") and not name_i_dict.get("size_name"):
            configure_header = ['store', 'websites', 'attribute_set', 'categories', 'type', 'sku', 'name', 'price',
                            'used_attribute','super_attibute_value', 'child_products_sku', 'description', 'weight',
                            'is_in_stock', 'qty', 'status', 'options_container', 'tax_class_id','visibility',
                                '%s_color'%typename]
        elif not name_i_dict.get("color_name") and name_i_dict.get("size_name"):
            configure_header = ['store', 'websites', 'attribute_set', 'categories', 'type', 'sku', 'name', 'price',
                            'used_attribute','super_attibute_value', 'child_products_sku', 'description', 'weight',
                            'is_in_stock', 'qty', 'status', 'options_container', 'tax_class_id','visibility',
                                '%s_size'%typename]
        else:
            configure_header = ['store', 'websites', 'attribute_set', 'categories', 'type', 'sku', 'name', 'price',
                            'used_attribute','super_attibute_value', 'child_products_sku', 'description', 'weight',
                            'is_in_stock', 'qty', 'status', 'options_container', 'tax_class_id','visibility']
        return configure_header
    
    
def splitFile(filename, upload_path):
    file_start = filename.split(".")[0]
    image_csv_filename = file_start + "_images_csv_" + str(time.time()).replace(".","") + ".csv"
    #image_csv_filename = os.path.join(upload_path, image_csv_filename_start)
    print "image_csv_filename:",image_csv_filename
    configure_filename = file_start + "_configure_filename_" + str(time.time()).replace(".", "") + ".csv"
    #configure_filename = os.path.join(upload_path, configure_filename_start)
    print "configure_filename:", configure_filename
    myget = GetContent(filename)
    print "myjuedge: ", myget.myjudge()
    if not myget.myjudge():
        img_status =  myget.jewel_write_images_csv(image_csv_filename)
        image_csv_name = image_csv_filename.split("/")[-1] if img_status else ""
        configure_status = myget.jewel_write_configure_csv(configure_filename)
        configure_name = configure_filename.split("/")[-1] if configure_status else ""
    else:
        img_status =  myget.write_images_csv(image_csv_filename)
        image_csv_name = image_csv_filename.split("/")[-1] if img_status else ""
        configure_status = myget.write_configure_product(configure_filename)
        configure_name = configure_filename.split("/")[-1] if configure_status else ""
    print "img_status: ", img_status        
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
    
            

    
