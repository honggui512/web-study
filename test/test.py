from tornado import web,ioloop,httpserver
import os
import pymysql
class MainPageHandler(web.RequestHandler):
    def get(self,*args,**kwargs):
        # self.write("hello world too")
        self.render('index.html')


class WishHandler(web.RequestHandler):
    #返回
    def get(self,*args,**kwargs):   #对应的是http get 请求
        self.render('wish.html')


settings ={
    'template_path':r'/test/templates',    #设置 模板文件的路径
    'static_path':r'/statics' #设置 静态文件路径

}

#路由系统 分机
application = web.Application([
    (r"/",MainPageHandler),
    (r"/wish",WishHandler),
    ])
if __name__=='__main__':
    #socket 服务 前台
    http_server = httpserver.HTTPServer(application)
    http_server.listen(8081)
    ioloop.IOLoop.current().start()