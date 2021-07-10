import os
import sys
import docx
import re
from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from tkinter import *
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
back1=[]
back2=[]
back3=[]
result1=[]
back4=[]
excel_VBA=[]
back5=[]
back6=[]
back7=[]
back8=[]
back9=[]
python_r_matlab_spss_sass=[]
back10=[]
back11=[]
back12=[]
back13=[]
bl_sn_sf_sap=[]
back14=[]
back15=[]
back16=[]
back17=[]
c_plus_java=[]
back18=[]
back19=[]
microsoft=[]
table=[]



#读取pdf文件到字符串
def getContet(file_name, pages=None):
    if (file_name is None):
        return
    print(file_name)
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)
    output = StringIO()
    # 创建一个PDF资源管理器存储共享资源
    manager = PDFResourceManager()
    # 创建一个PDF设备对象
    converter = TextConverter(manager, output, laparams=LAParams())
    # 创建一个PDF解释器对象
    interpreter = PDFPageInterpreter(manager, converter)
    infile = open(file_name, 'rb')#以二进制读取文件
    #对pdf的每一页进行分析
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    #得到每一页的txt文档
    content = output.getvalue()
    lower_content=content.casefold()#全部小写
    #print(lower_content)
    #print(content[0:6])

    def find(skill1):
        if skill1 in lower_content:
            res1=int((lower_content.index(skill1))/30)
            return res1


    #第一项SQL
    a=find('sql')
    if a is None:#没有写此项技能
        back1.append(0)
        back1.append(-10)
        result1.append(back1)
        #print(back1)
    else:
        back1.append(a)

        forward=a+15
        bakcward=a-40
        extract_str = content[bakcward:a]
        extract_str_split=extract_str.split()
        str1 = extract_str_split
        alist = []
        for x in str1:
            alist.append(x)
        if 'advanced' in alist[0:6] or 'proficiency' in alist[0:6]:
            print('value is:', 6)
            back1.append(6)
            result1.append(back1)
            #print(back1)
        else:
            def hasNumbers(inputString):
                return any(char.isdigit() for char in inputString)
            check=hasNumbers(content[a:forward])
            if check is True:#后面写了使用时长
                number = filter(str.isdigit, content[a:forward])
                num = list(number)
                extract = int(num[0])  # 把使用时间取出来
                if extract < 2:
                    value = 3
                if extract >= 2:
                    value = 6
                back1.append(value)
                result1.append(back1)
                #print(back1)
            if check is False:#没有写使用年份的情况
                back1.append(3)
                result1.append(back1)
                #print(back1)
                return

    # 第二项part1:excel
    b = find('excel')
    if b is None:  # 没有写此项技能
        back2.append(0)
        back2.append(-10)

    else:
        back2.append(b)

        forward = b + 15
        bakcward = b - 40
        extract_str = content[bakcward:b]
        extract_str_split = extract_str.split()
        str1 = extract_str_split
        alist = []
        for x in str1:
            alist.append(x)
        if 'advanced' in alist[0:6] or 'proficiency' in alist[0:6]:

            back2.append(6)

        else:
            def hasNumbers(inputString):
                return any(char.isdigit() for char in inputString)

            check = hasNumbers(content[a:forward])
            if check is True:  # 后面写了使用时长
                number = filter(str.isdigit, content[a:forward])
                num = list(number)
                extract = int(num[0])  # 把使用时间取出来
                if extract < 2:
                    value = 3
                if extract >= 2:
                    value = 6
                back2.append(value)

            if check is False:  # 没有写使用年份的情况
                back2.append(3)

                return

    # 第二项part2:vba
    c = find('vba')
    if c is None:  # 没有写此项技能
        back3.append(0)
        back3.append(-10)
        #print(back3)
        excel_VBA.append(back2)
        excel_VBA.append(back3)
        result1.append(excel_VBA)
        #print(excel_VBA)
    else:
        back3.append(c)
        forward = c + 15
        bakcward = c - 40
        extract_str = content[bakcward:c]
        extract_str_split = extract_str.split()
        str1 = extract_str_split
        alist = []
        for x in str1:
            alist.append(x)
        if 'advanced' in alist[0:6] or 'proficiency' in alist[0:6]:

            back3.append(6)
            excel_VBA.append(back2)
            excel_VBA.append(back3)
            result1.append(excel_VBA)
            #print(excel_VBA)

        else:
            def hasNumbers(inputString):
                return any(char.isdigit() for char in inputString)

            check = hasNumbers(content[c:forward])
            if check is True:  # 后面写了使用时长
                number = filter(str.isdigit, content[a:forward])
                num = list(number)
                extract = int(num[0])  # 把使用时间取出来
                if extract < 2:
                    value = 3

                if extract >= 2:
                    value = 6
                back3.append(value)
                excel_VBA.append(back2)
                excel_VBA.append(back3)
                result1.append(excel_VBA)
                #print(excel_VBA)

            else:  # 没有写使用年份的情况
                back3.append(3)
                excel_VBA.append(back2)
                excel_VBA.append(back3)
                result1.append(excel_VBA)
    # 第三项tablu（4）
    d = find('tableau')
    if d is None:  # 没有写此项技能
        back4.append(0)
        back4.append(-6)
        result1.append(back4)
        #print(back4)
    else:
        back4.append(d)
        forward = d + 15
        bakcward = d - 40
        extract_str = content[bakcward:d]
        extract_str_split = extract_str.split()
        str1 = extract_str_split
        alist = []
        for x in str1:
            alist.append(x)
        if 'advanced' in alist[0:6] or 'proficiency' in alist[0:6]:

            back4.append(6)
            result1.append(back4)
            #print(back4)
        else:
            def hasNumbers(inputString):
                return any(char.isdigit() for char in inputString)

            check = hasNumbers(content[a:forward])
            if check is True:  # 后面写了使用时长
                number = filter(str.isdigit, content[a:forward])
                num = list(number)
                extract = int(num[0])  # 把使用时间取出来
                if extract < 2:
                    value = 3
                if extract >= 2:
                    value = 6
                back4.append(value)
                result1.append(back4)
                #print(back4)
            if check is False:  # 没有写使用年份的情况
                back4.append(3)
                result1.append(back4)
                #print(back4)
                return

    # 第四项python（5）
    e = find('python')
    if e is None:  # 没有写此项技能
        back5.append(0)
        back5.append(-4)
        # print(back5)
    else:
        back5.append(e)
        forward = e + 15
        bakcward = e - 40
        extract_str = content[bakcward:e]
        extract_str_split = extract_str.split()
        str1 = extract_str_split
        alist = []
        for x in str1:
            alist.append(x)
        if 'advanced' in alist[0:6] or 'proficiency' in alist[0:6]:

            back5.append(5)
            # print(back5)
        else:
            def hasNumbers(inputString):
                return any(char.isdigit() for char in inputString)

            check = hasNumbers(content[a:forward])
            if check is True:  # 后面写了使用时长
                number = filter(str.isdigit, content[a:forward])
                num = list(number)
                extract = int(num[0])  # 把使用时间取出来
                if extract < 2:
                    value = 2
                if extract >= 2:
                    value = 5
                back5.append(value)
                # print(back5)
            if check is False:  # 没有写使用年份的情况
                back5.append(2)
                return


    # 第四项r（6）
    f = find(' r ')
    if f is None:  # 没有写此项技能
        back6.append(0)
        back6.append(-4)
        # print(back6)
    else:
        back6.append(f)
        forward = f + 15
        bakcward = f - 40
        extract_str = content[bakcward:f]
        extract_str_split = extract_str.split()
        str1 = extract_str_split
        alist = []
        for x in str1:
            alist.append(x)
        if 'advanced' in alist[0:6] or 'proficiency' in alist[0:6]:
            # print('value is:', 6)
            back6.append(5)
            # print(back6)
        else:
            def hasNumbers(inputString):
                return any(char.isdigit() for char in inputString)

            check = hasNumbers(content[a:forward])
            if check is True:  # 后面写了使用时长
                number = filter(str.isdigit, content[a:forward])
                num = list(number)
                extract = int(num[0])  # 把使用时间取出来
                if extract < 2:
                    value = 2
                if extract >= 2:
                    value = 5
                back6.append(value)
                # print(back6)
            if check is False:  # 没有写使用年份的情况
                back6.append(2)
                # print(back6)
                return

    # 第四项matlab（7）
    e = find('matlab')
    if e is None:  # 没有写此项技能
        back7.append(0)
        back7.append(-4)
        # print(back7)
    else:
        back7.append(e)
        forward = e + 15
        bakcward = e - 40
        extract_str = content[bakcward:e]
        extract_str_split = extract_str.split()
        str1 = extract_str_split
        alist = []
        for x in str1:
            alist.append(x)
        if 'advanced' in alist[0:6] or 'proficiency' in alist[0:6]:
            # print('value is:', 6)
            back7.append(5)
            # print(back7)
        else:
            def hasNumbers(inputString):
                return any(char.isdigit() for char in inputString)

            check = hasNumbers(content[a:forward])
            if check is True:  # 后面写了使用时长
                number = filter(str.isdigit, content[a:forward])
                num = list(number)
                extract = int(num[0])  # 把使用时间取出来
                if extract < 2:
                    value = 2
                if extract >= 2:
                    value = 5
                back7.append(value)
                # print(back7)
            if check is False:  # 没有写使用年份的情况
                back7.append(2)
                # print(back7)
                return

    # 第四项spss（8）
    f = find('spss')
    if f is None:  # 没有写此项技能
        back8.append(0)
        back8.append(-4)
        # print(back8)
    else:
        back8.append(f)
        forward = f + 15
        bakcward = f - 40
        extract_str = content[bakcward:f]
        extract_str_split = extract_str.split()
        str1 = extract_str_split
        alist = []
        for x in str1:
            alist.append(x)
        if 'advanced' in alist[0:6] or 'proficiency' in alist[0:6]:
            # print('value is:', 6)
            back8.append(5)
            # print(back8)
        else:
            def hasNumbers(inputString):
                return any(char.isdigit() for char in inputString)

            check = hasNumbers(content[a:forward])
            if check is True:  # 后面写了使用时长
                number = filter(str.isdigit, content[a:forward])
                num = list(number)
                extract = int(num[0])  # 把使用时间取出来
                if extract < 2:
                    value = 2
                if extract >= 2:
                    value = 5
                back8.append(value)
                # print(back8)
            if check is False:  # 没有写使用年份的情况
                back8.append(2)
                # print(back8)
                return

    # 第四项sas（7）
    g = find('sas')
    if g is None:  # 没有写此项技能
        back9.append(0)
        back9.append(-4)
        python_r_matlab_spss_sass.append(back5)
        python_r_matlab_spss_sass.append(back6)
        python_r_matlab_spss_sass.append(back7)
        python_r_matlab_spss_sass.append(back8)
        python_r_matlab_spss_sass.append(back9)
        result1.append(python_r_matlab_spss_sass)
        #print(python_r_matlab_spss_sass)
        # print(back9)
    else:
        back9.append(g)
        forward = g + 15
        bakcward = g - 40
        extract_str = content[bakcward:g]
        extract_str_split = extract_str.split()
        str1 = extract_str_split
        alist = []
        for x in str1:
            alist.append(x)
        if 'advanced' in alist[0:6] or 'proficiency' in alist[0:6]:

            back9.append(5)
            python_r_matlab_spss_sass.append(back5)
            python_r_matlab_spss_sass.append(back6)
            python_r_matlab_spss_sass.append(back7)
            python_r_matlab_spss_sass.append(back8)
            python_r_matlab_spss_sass.append(back9)
            result1.append(python_r_matlab_spss_sass)
            #print(python_r_matlab_spss_sass)
            # print(back9)
        else:
            def hasNumbers(inputString):
                return any(char.isdigit() for char in inputString)

            check = hasNumbers(content[a:forward])
            if check is True:  # 后面写了使用时长
                number = filter(str.isdigit, content[a:forward])
                num = list(number)
                extract = int(num[0])  # 把使用时间取出来
                if extract < 2:
                    value = 2
                if extract >= 2:
                    value = 5
                back9.append(value)
                python_r_matlab_spss_sass.append(back5)
                python_r_matlab_spss_sass.append(back6)
                python_r_matlab_spss_sass.append(back7)
                python_r_matlab_spss_sass.append(back8)
                python_r_matlab_spss_sass.append(back9)
                result1.append(python_r_matlab_spss_sass)
                #print(python_r_matlab_spss_sass)
                # print(back9)
            if check is False:  # 没有写使用年份的情况
                back9.append(2)
                python_r_matlab_spss_sass.append(back5)
                python_r_matlab_spss_sass.append(back6)
                python_r_matlab_spss_sass.append(back7)
                python_r_matlab_spss_sass.append(back8)
                python_r_matlab_spss_sass.append(back9)
                result1.append(python_r_matlab_spss_sass)
                #print(python_r_matlab_spss_sass)
                # print(back9)
                return
    # 第五项bloombera（8）
    f = find('spss')
    if f is None:  # 没有写此项技能
        back8.append(0)
        back8.append(-4)
        # print(back8)
    else:
        back8.append(f)
        forward = f + 15
        bakcward = f - 40
        extract_str = content[bakcward:f]
        extract_str_split = extract_str.split()
        str1 = extract_str_split
        alist = []
        for x in str1:
            alist.append(x)
        if 'advanced' in alist[0:6] or 'proficiency' in alist[0:6]:
            # print('value is:', 6)
            back8.append(5)
            # print(back8)
        else:
            def hasNumbers(inputString):
                return any(char.isdigit() for char in inputString)

            check = hasNumbers(content[a:forward])
            if check is True:  # 后面写了使用时长
                number = filter(str.isdigit, content[a:forward])
                num = list(number)
                extract = int(num[0])  # 把使用时间取出来
                if extract < 2:
                    value = 2
                if extract >= 2:
                    value = 5
                back8.append(value)
                # print(back8)
            if check is False:  # 没有写使用年份的情况
                back8.append(2)
                # print(back8)
                return

    # 第四项sas（7）
    g = find('sas')
    if g is None:  # 没有写此项技能
        back9.append(0)
        back9.append(-4)
        python_r_matlab_spss_sass.append(back5)
        python_r_matlab_spss_sass.append(back6)
        python_r_matlab_spss_sass.append(back7)
        python_r_matlab_spss_sass.append(back8)
        python_r_matlab_spss_sass.append(back9)
        result1.append(python_r_matlab_spss_sass)
        #print(python_r_matlab_spss_sass)
        # print(back9)
    else:
        back9.append(g)
        forward = g + 15
        bakcward = g - 40
        extract_str = content[bakcward:g]
        extract_str_split = extract_str.split()
        str1 = extract_str_split
        alist = []
        for x in str1:
            alist.append(x)
        if 'advanced' in alist[0:6] or 'proficiency' in alist[0:6]:

            back9.append(5)
            python_r_matlab_spss_sass.append(back5)
            python_r_matlab_spss_sass.append(back6)
            python_r_matlab_spss_sass.append(back7)
            python_r_matlab_spss_sass.append(back8)
            python_r_matlab_spss_sass.append(back9)
            result1.append(python_r_matlab_spss_sass)
            #print(python_r_matlab_spss_sass)
            # print(back9)
        else:
            def hasNumbers(inputString):
                return any(char.isdigit() for char in inputString)

            check = hasNumbers(content[a:forward])
            if check is True:  # 后面写了使用时长
                number = filter(str.isdigit, content[a:forward])
                num = list(number)
                extract = int(num[0])  # 把使用时间取出来
                if extract < 2:
                    value = 2
                if extract >= 2:
                    value = 5
                back9.append(value)
                python_r_matlab_spss_sass.append(back5)
                python_r_matlab_spss_sass.append(back6)
                python_r_matlab_spss_sass.append(back7)
                python_r_matlab_spss_sass.append(back8)
                python_r_matlab_spss_sass.append(back9)
                result1.append(python_r_matlab_spss_sass)
                #print(python_r_matlab_spss_sass)
                # print(back9)
            if check is False:  # 没有写使用年份的情况
                back9.append(2)
                python_r_matlab_spss_sass.append(back5)
                python_r_matlab_spss_sass.append(back6)
                python_r_matlab_spss_sass.append(back7)
                python_r_matlab_spss_sass.append(back8)
                python_r_matlab_spss_sass.append(back9)
                result1.append(python_r_matlab_spss_sass)
                #print(python_r_matlab_spss_sass)
                # print(back9)
                return
    # 第五项bloombera（8）
    h = find('bloombera')
    if h is None:  # 没有写此项技能
        back10.append(0)
        back10.append(0)
        # print(back10)
    else:
        back10.append(h)
        forward = h + 15
        bakcward = h - 40
        extract_str = content[bakcward:h]
        extract_str_split = extract_str.split()
        str1 = extract_str_split
        alist = []
        for x in str1:
            alist.append(x)
        if 'advanced' in alist[0:6] or 'proficiency' in alist[0:6]:
            # print('value is:', 6)
            back10.append(1)
            # print(back10)

        else:
            def hasNumbers(inputString):
                return any(char.isdigit() for char in inputString)

            check = hasNumbers(content[a:forward])
            if check is True:  # 后面写了使用时长
                number = filter(str.isdigit, content[a:forward])
                num = list(number)
                extract = int(num[0])  # 把使用时间取出来
                if extract < 2:
                    value = 0
                if extract >= 2:
                    value = 6
                back10.append(value)
                # print(back10)
            if check is False:  # 没有写使用年份的情况
                back10.append(0)
                # print(back10)
                return

    # 第五项serviecenow（8）
    i = find('serviecenow')
    if i is None:  # 没有写此项技能
        back11.append(0)
        back11.append(0)
        # print(back11)
    else:
        back11.append(i)
        forward = i + 15
        bakcward = i - 40
        extract_str = content[bakcward:i]
        extract_str_split = extract_str.split()
        str1 = extract_str_split
        alist = []
        for x in str1:
            alist.append(x)
        if 'advanced' in alist[0:6] or 'proficiency' in alist[0:6]:
            # print('value is:', 6)
            back11.append(1)
            # print(back11)
        else:
            def hasNumbers(inputString):
                return any(char.isdigit() for char in inputString)

            check = hasNumbers(content[a:forward])
            if check is True:  # 后面写了使用时长
                number = filter(str.isdigit, content[a:forward])
                num = list(number)
                extract = int(num[0])  # 把使用时间取出来
                if extract < 2:
                    value = 0
                if extract >= 2:
                    value = 1
                back11.append(value)
                # print(back11)
            if check is False:  # 没有写使用年份的情况
                back11.append(0)
                # print(back11)
                return

    # 第五项salesforce（8）
    j = find('salesforce')
    if j is None:  # 没有写此项技能
        back12.append(0)
        back12.append(0)
        # print(back12)
    else:
        back12.append(j)
        forward = j + 15
        bakcward = j - 40
        extract_str = content[bakcward:j]
        extract_str_split = extract_str.split()
        str1 = extract_str_split
        alist = []
        for x in str1:
            alist.append(x)
        if 'advanced' in alist[0:6] or 'proficiency' in alist[0:6]:
            # print('value is:', 6)
            back12.append(1)
            # print(back12)
        else:
            def hasNumbers(inputString):
                return any(char.isdigit() for char in inputString)

            check = hasNumbers(content[a:forward])
            if check is True:  # 后面写了使用时长
                number = filter(str.isdigit, content[a:forward])
                num = list(number)
                extract = int(num[0])  # 把使用时间取出来
                if extract < 2:
                    value = 0
                if extract >= 2:
                    value = 1
                back12.append(value)
                # print(back12)
            if check is False:  # 没有写使用年份的情况
                back12.append(0)
                # print(back12)
                return

    # 第五项sap（8）
    l = find('sap')
    if l is None:  # 没有写此项技能
        back13.append(0)
        back13.append(0)

        bl_sn_sf_sap.append(back10)
        bl_sn_sf_sap.append(back11)
        bl_sn_sf_sap.append(back12)
        bl_sn_sf_sap.append(back13)
        result1.append(bl_sn_sf_sap)
        #print(bl_sn_sf_sap)

        # print(back13)
    else:
        back13.append(l)
        forward = l + 15
        bakcward = l - 40
        extract_str = content[bakcward:l]
        extract_str_split = extract_str.split()
        str1 = extract_str_split
        alist = []
        for x in str1:
            alist.append(x)
        if 'advanced' in alist[0:6] or 'proficiency' in alist[0:6]:
            # print('value is:', 6)
            back13.append(1)
            bl_sn_sf_sap.append(back10)
            bl_sn_sf_sap.append(back11)
            bl_sn_sf_sap.append(back12)
            bl_sn_sf_sap.append(back13)
            result1.append(bl_sn_sf_sap)
            #print(bl_sn_sf_sap)
            # print(back13)
        else:
            def hasNumbers(inputString):
                return any(char.isdigit() for char in inputString)

            check = hasNumbers(content[a:forward])
            if check is True:  # 后面写了使用时长
                number = filter(str.isdigit, content[a:forward])
                num = list(number)
                extract = int(num[0])  # 把使用时间取出来
                if extract < 2:
                    value = 0
                if extract >= 2:
                    value = 1
                back13.append(value)
                bl_sn_sf_sap.append(back10)
                bl_sn_sf_sap.append(back11)
                bl_sn_sf_sap.append(back12)
                bl_sn_sf_sap.append(back13)
                result1.append(bl_sn_sf_sap)
                #print(bl_sn_sf_sap)
                # print(back13)
            if check is False:  # 没有写使用年份的情况
                back13.append(0)
                bl_sn_sf_sap.append(back10)
                bl_sn_sf_sap.append(back11)
                bl_sn_sf_sap.append(back12)
                bl_sn_sf_sap.append(back13)
                result1.append(bl_sn_sf_sap)
                #print(bl_sn_sf_sap)
                # print(back13)
                return

    m=find('database')
    if m is None:#没有写此项技能

        back14.append(0)
        back14.append(0)
        result1.append(back14)
        #print(back14)
    else:
        back14.append(m)
        forward=m+15
        bakcward=m-40
        extract_str = content[bakcward:m]
        extract_str_split=extract_str.split()
        str1 = extract_str_split
        alist = []
        for x in str1:
            alist.append(x)
        if 'advanced' in alist[0:6] or 'proficiency' in alist[0:6]:

            back14.append(2)
            result1.append(back14)
            #print(back14)
        else:
            def hasNumbers(inputString):
                return any(char.isdigit() for char in inputString)
            check=hasNumbers(content[a:forward])
            if check is True:#后面写了使用时长
                number = filter(str.isdigit, content[a:forward])
                num = list(number)
                extract = int(num[0])  # 把使用时间取出来
                if extract < 2:
                    value = 1
                if extract >= 2:
                    value = 2
                back14.append(value)
                result1.append(back14)
                #print(back14)
            if check is False:#没有写使用年份的情况
                back14.append(1)
                result1.append(back14)
                #print(back14)
                return




    n=find(' c ')
    if n is None:#没有写此项技能
        back15.append(0)
        back15.append(0)

    else:
        back15.append(n)
        forward=n+15
        bakcward=n-40
        extract_str = content[bakcward:n]
        extract_str_split=extract_str.split()
        str1 = extract_str_split
        alist = []
        for x in str1:
            alist.append(x)
        if 'advanced' in alist[0:6] or 'proficiency' in alist[0:6]:

            back15.append(2)

        else:
            def hasNumbers(inputString):
                return any(char.isdigit() for char in inputString)
            check=hasNumbers(content[a:forward])
            if check is True:#后面写了使用时长
                number = filter(str.isdigit, content[a:forward])
                num = list(number)
                extract = int(num[0])  # 把使用时间取出来
                if extract < 2:
                    value = 1
                if extract >= 2:
                    value = 2
                back15.append(value)

            if check is False:#没有写使用年份的情况
                back15.append(1)

                return


    o=find('c++')
    if o is None:#没有写此项技能
        back16.append(0)

        c_plus_java.append(back17)
        result1.append(c_plus_java)
        #print(c_plus_java)


    else:
        back17.append(p)
        forward=p+15
        bakcward=p-40
        extract_str = content[bakcward:p]
        extract_str_split=extract_str.split()
        str1 = extract_str_split
        alist = []
        for x in str1:
            alist.append(x)
        if 'advanced' in alist[0:6] or 'proficiency' in alist[0:6]:

            back17.append(2)
            c_plus_java.append(back15)
            c_plus_java.append(back16)
            c_plus_java.append(back17)
            result1.append(c_plus_java)
            #print(c_plus_java)
        else:
            def hasNumbers(inputString):
                return any(char.isdigit() for char in inputString)
            check=hasNumbers(content[a:forward])
            if check is True:#后面写了使用时长
                number = filter(str.isdigit, content[a:forward])
                num = list(number)
                extract = int(num[0])  # 把使用时间取出来
                if extract < 2:
                    value = 1
                if extract >= 2:
                    value = 2
                back17.append(value)
                c_plus_java.append(back15)
                c_plus_java.append(back16)
                c_plus_java.append(back17)
                result1.append(c_plus_java)
                #print(c_plus_java)
            if check is False:#没有写使用年份的情况
                back17.append(1)
                c_plus_java.append(back15)
                c_plus_java.append(back16)
                c_plus_java.append(back17)
                result1.append(c_plus_java)
                #print(c_plus_java)
                return




    q = find('ms office')
    if q is None:  # 没有写此项技能
        back18.append(0)
        back18.append(0)

    else:
        back18.append(q)
        forward = q + 15
        bakcward = q - 40
        extract_str = content[bakcward:q]
        extract_str_split = extract_str.split()
        str1 = extract_str_split
        alist = []
        for x in str1:
            alist.append(x)
        if 'advanced' in alist[0:6] or 'proficiency' in alist[0:6]:

            back18.append(1)

        else:
            def hasNumbers(inputString):
                return any(char.isdigit() for char in inputString)

            check = hasNumbers(content[a:forward])
            if check is True:  # 后面写了使用时长
                number = filter(str.isdigit, content[a:forward])
                num = list(number)
                extract = int(num[0])  # 把使用时间取出来
                if extract < 2:
                    value = 0
                if extract >= 2:
                    value = 1

                back18.append(value)

            if check is False:  # 没有写使用年份的情况
                back18.append(0)

                return

    r = find('microsoft office')
    if r is None:  # 没有写此项技能
        back19.append(0)
        back19.append(0)

        microsoft.append(back18)
        microsoft.append(back19)
        result1.append(microsoft)
        #print(microsoft)


    else:
        back19.append(r)
        forward = r + 15
        bakcward = r - 40
        extract_str = content[bakcward:r]
        extract_str_split = extract_str.split()
        str1 = extract_str_split
        alist = []
        for x in str1:
            alist.append(x)
        if 'advanced' in alist[0:6] or 'proficiency' in alist[0:6]:

            back19.append(1)
            microsoft.append(back18)
            microsoft.append(back19)
            result1.append(microsoft)
            #print(microsoft)
        else:
            def hasNumbers(inputString):
                return any(char.isdigit() for char in inputString)

            check = hasNumbers(content[a:forward])
            if check is True:  # 后面写了使用时长
                number = filter(str.isdigit, content[a:forward])
                num = list(number)
                extract = int(num[0])  # 把使用时间取出来
                if extract < 2:
                    value = 0
                if extract >= 2:
                    value = 1
                back19.append(value)
                microsoft.append(back18)
                microsoft.append(back19)
                result1.append(microsoft)
                #print(microsoft)
            if check is False:  # 没有写使用年份的情况
                back19.append(0)
                microsoft.append(back18)
                microsoft.append(back19)
                result1.append(microsoft)
                #print(microsoft)
                return
    print('finaltable:', result1)