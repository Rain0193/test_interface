# -*- coding:utf-8 -*-
'''
Created on 2017年6月28日

@author: lt
'''
#根据
from Common import ReadExcel
read=ReadExcel.Excel('E:\\project\\test_interface\\case.xls')
f=open('E:\\project\\test_interface\\case\\test_case.py','w')
def edit(num):
    global read,f
    for i in range(1,num):
        f.write("    #%s\n"%read.get_del(i).encode('utf-8'))
        f.write("    def %s(self):\n"%read.get_test_mode(i))
        f.write("        write=WriteExcel.Excel(Common.Path.case_Path())\n")
        f.write("        print '-----------------%s------------'%self.case_desc\n")
        f.write("        print '接口地址:%s' %self.url.encode('utf-8')\n")
        f.write("        print '传递参数:%s' %self.data.encode('utf-8')\n")
        if read.get_file(i)=='true':
            f.write("        files = {'cover': open(Common.Path.photo_Path(), 'rb')}\n")
            f.write("        response,state = self.http.%s(self.url, self.data, self.host, files)\n"%read.get_http(i))
        else:
            f.write("        response,state = self.http.%s(self.url, self.data, self.host)\n"%read.get_http(i))
        f.write("        if {} == response:\n")
        f.write("            self.result = 'Error'\n")
        f.write("            print '返回的http状态:%s' %state\n")
        f.write("            try:\n")
        f.write("                if state ==200:\n")
        f.write("                    write.write_fail(self.case_id, self.result,'Null',state)\n")
        f.write("                    raise Custom_exception.NO_json\n")
        f.write("                elif state==400 and state==self.expect_http:\n")
        f.write("                    write.write_fail(self.case_id, 'Pass','Null',state)\n")
        f.write("                else:\n")
        f.write("                    write.write_fail(self.case_id, self.result,'Null',state)\n")
        f.write("                    raise Custom_exception.Request_fail\n")
        f.write("            except Exception as e:\n")
        f.write("                print('%s' % e)\n")
        f.write("                raise\n")
        f.write("            return\n")
        f.write("        try:\n")
        f.write("            # 断言\n")
        f.write("            self.assertEqual(response['code'], self.code, msg='返回的code不是%s\\ncode=%s\\nmsg=%s' %(self.code,response['code'].encode('utf-8'),response['msg'].encode('utf-8')))\n")
        if read.get_expect_data(i):           
            dictionary=eval(read.get_expect_data(i))
            list=[key for key in dictionary if not key.startswith('__')]
            list_num=len(list)
            for j in range(0,list_num):
                c='%s'
                d='%s' %list[j]
                e='%response'
                k="[\'%s\']" %list[j] 
                h="\'%s\'" %dictionary[list[j]]
                f.write("            self.assertEqual(response[\'%s\'].encode(\'utf-8\'), %s, msg=\'返回的%s错误\\n%s=%s\' %s%s.encode(\'utf-8\')) \n" %(d,h,d,d,c,e,k))
        if read.get_expect_msg(i):
            l='%s'
            m='%response'
            n="\'%s\'" %read.get_expect_msg(i).encode('utf-8')
            f.write("            self.assertEqual(response[\'msg\'].encode(\'utf-8\'), %s, msg=\'返回的msg错误\\n返回的msg=%s\' %s[\'msg\'].encode(\'utf-8\'))\n" %(n,l,m))
        f.write("            self.result = 'Pass'\n")
        f.write("            self.reason = 'Null'\n")
        f.write("        except AssertionError as e:\n")
        f.write("            self.result = 'Fail'\n")
        f.write("            self.reason = '%s' %e\n")
        f.write("            print self.reason\n")
        f.write("            try:\n")
        f.write("                write.write_fail(self.case_id, self.result, self.reason.decode('utf-8'),state)\n")
        f.write("            except Exception as e:\n")
        f.write("                print('%s' % e)\n")
        f.write("                raise\n")
        f.write("            raise\n")
        f.write("            # 更新结果表中的用例运行结果\n")
        f.write("        try:\n")
        f.write("            write.write(self.case_id, self.result,state)\n")
        f.write("        except Exception as e:\n")
        f.write("            print('%s' % e)\n")
        f.write("            raise\n")
        if read.get_del_add(i):
            a='%s'
            b="%response['data']['id']"
            f.write("        try:\n")
            f.write("            db=getdb.mongodb()\n")
            f.write("            db.db_drop(\"%s\", {\"_id\":ObjectId(\"%s\" %s)})\n" %(read.get_del_add(i),a,b))
            f.write("        except Exception as e:\n")
            f.write("            print '%s' %e\n")
            f.write("            pass\n")
def edit_case():
    global read,f
    f.write("# -*- coding:utf-8 -*-\n")
    f.write("'''\n")
    f.write("Created on 2017年5月5日\n")
    f.write("@author: lt\n" )
    f.write("'''\n")
    f.write("import  unittest\n")
    f.write("from Common import WriteExcel\n")
    f.write("import Common.Path\n")
    f.write('from Exception import Custom_exception\n')
    f.write("from Common import getdb\n")
    f.write("from bson.objectid import ObjectId\n")
    f.write("# 测试用例(组)类\n")
    f.write("class ParametrizedTestCase(unittest.TestCase):\n")
    f.write("    \"\"\" TestCase classes that want to be parametrized should\n")
    f.write("        inherit from this class.\n")
    f.write("    \"\"\"\n")
    f.write("    def __init__(self, methodName='runTest', url=None, http=None, data=None, host=None,case_id=None,code=None,case_desc=None,expect_http=None):\n")
    f.write("        super(ParametrizedTestCase, self).__init__(methodName)\n")
    f.write("        self.url = url\n")
    f.write("        self.http = http\n")
    f.write("        self.data = data\n")
    f.write("        self.host = host\n")
    f.write("        self.case_id=case_id\n")
    f.write("        self.code=code\n")
    f.write("        self.case_desc=case_desc\n")
    f.write("        self.expect_http=expect_http\n")
    f.write("class TestInterfaceCase(ParametrizedTestCase):\n")
    f.write("    def setUp(self):\n")
    f.write("        pass\n")
    read.excel_table_byname(u'前端接口')
    edit(read.get_nrows())
    read.excel_table_byname(u'后台接口')
    edit(read.get_nrows())
    f.close()
