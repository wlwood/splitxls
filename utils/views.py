#!/usr/bin/env python
# encoding:utf-8

import os
import json
import tornado.web
import time 
import urllib
from splitxls import splitFile

import sys
reload(sys)
sys.setdefaultencoding("utf-8")






class BaseHandler(tornado.web.RequestHandler):
    def __init__(self, *args, **kwargs):
        tornado.web.RequestHandler.__init__(self, *args, **kwargs)

class ErrorHandler(BaseHandler):
    def get(self):
        self.write_error(404)
    def write_error(self,status_code, **kwargs):
        self.write('error:'+str(status_code))

class IndexHandler(BaseHandler):
    def get(self):
        self.render("index.html")
        

class UpFileHandler(BaseHandler):
    def get(self):
        self.redirect("/")
    def post(self):
        try:
            upload_file_dict = self.request.files.get("file_data")[0]
        except Exception ,e:
            print "upload file error, %s" %e 
        filename = str(upload_file_dict.get("filename",""))
        if filename.endswith(".xls") or  filename.endswith(".xlsx"):
            pass
        else:
            result_dict = {"status":"False"}
            return self.write(json.dumps(result_dict))
            return self.finish()
        print "upload file: %s" % str(filename)
        filestr = upload_file_dict.get("body")
        upload_file_path = try_upload_path()
        if not os.path.exists(upload_file_path):
            os.mkdir(upload_file_path)
        #filename = urllib.quote(filename)
        rfilename = os.path.join(upload_file_path, filename)
        with open(rfilename, "wb") as upf:
            upf.write(filestr)
        result_dict = splitFile( rfilename, upload_file_path) 
        if result_dict.get("status") != False:
            result_dict["configure_filename"] = urllib.quote(str(result_dict.get("configure_filename")))
            result_dict["image_csv_filename"] = urllib.quote(str(result_dict.get("image_csv_filename")))
            result_dict.update({"status":"True"})
        else:
            result_dict.update({"status":"False",
                                "message":result_dict.get("message",u"转换失败"),
                                "filename": filename,
                            })
        self.write(json.dumps(result_dict))
        self.finish()

    
class DownloadHandler(BaseHandler):
    def get(self):
        buf_size = 1024
        file_path = str(self.get_argument("file_path", ""))
        
        filename = str(file_path).split("/")[-1]
        self.set_header ('Content-Type', 'application/octet-stream')
        self.set_header ('Content-Disposition', 'attachment; filename='+filename)
        if os.path.exists(file_path):
            try:
                with open(file_path, "rb") as f:
                    while True:
                        data = f.read(buf_size)
                        if not data:break
                        self.write(data)
            except Exception, e:
                print "open image csv file Error, %s" % e
                return self.finish()
        else:
            print "not found file:%s" % filename
            self.write("没有找到文件")
        self.finish()

def try_upload_path():
    upload_file_path = "upload"
    if not os.path.exists(upload_file_path):
        os.mkdir(upload_file_path)
    timenow = time.strftime("%Y-%m-%d",time.localtime())
    upload_file_path = os.path.join(upload_file_path,timenow)
    if not upload_file_path:
        os.mkdir(upload_file_path)
    return upload_file_path
