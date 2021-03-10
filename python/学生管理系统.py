# 学生管理系统, 分为管理员登陆和学生登陆；
# 管理员登陆， 可以操作：
    # 管理员密码修改;
    # 添加学生的信息;
    # 删除学生的信息;
    # 修改学生的信息;
    # 查询学生的信息(根据学号);
    # 查看所有学生的信息;
    # 退出系统;
# 学生登录:
    # 查询个人改信息；
#         # 修改年龄；
#         # 修改密码;信息;
    # 修
# 学生信息包括:
    # 学号， 姓名， 性别， 班级， 出生年月， 用户名， 密码
    # 学生用户名和学号保持一致;
# 管理员信息包括:
#     用户名, 密码

rootname = ['root']
rootpasswd = ['123456']
stumessage = {'学号':[],'姓名':[],'性别':[],'班级':[],'出生年月日':[],'用户名':[],'密码':[]}

while True:
    print("欢迎登录学生管理系统".center(40,"*"))
    info1= """
        1.管理元登录
        2.学生登陆
        3、退出
    """
    print(info1)
    choice1 = input('请输入你的选择：')
    if choice1 == '1':
        print('欢迎进入管理员登录页面'.center(30,'*'))
        inrootname = input("请输入管理员用户名：")
        inrootpasswd = input('请输入管理员密码：')
        while True:
            if inrootname == rootname[0] and inrootpasswd == rootpasswd[0]:
                print("欢迎进入管理员操作页面".center(30,'*'))
                info2 = """
                     1.管理员密码修改;
                     2.添加学生的信息;
                     3.删除学生的信息;
                     4.修改学生的信息;
                     5.查询学生的信息(根据学号);
                     6.查看所有学生的信息;
                     7.退出系统;                
                """
                print(info2)
                choice2 = input("请输入你的操作编号：")
                if choice2 == '1':
                    print("欢迎进入管理员密码修改页面".center(30,"*"))
                    newrootpaswd = input("请输入管理新密码:")
                    rootpasswd.pop()
                    rootpasswd.append(newrootpaswd)
                    print("密码修改成功")
                elif  choice2 == '2':
                    print("欢迎进入学生信息添加页面".center(30, '*'))
                    newstudentname = input('请输入学生姓名：')
                    if newstudentname in stumessage['姓名']:
                        print("此学生已存在")
                    else:
                        newstudentxuehao = input("输入学号：")
                        newstudentsex = input("输入性别：")
                        newstudentclass = input("输入班级名称：")
                        newstudentbri = input("输入出生年月日：")
                        newstudentusername = input("输入用户名：")
                        newstudentpasswd = input("输入密码：")
                        stumessage['姓名'].append(newstudentname)
                        stumessage['学号'].append(newstudentxuehao)
                        stumessage['性别'].append(newstudentsex)
                        stumessage['班级'].append(newstudentclass)
                        stumessage['出生年月日'].append(newstudentbri)
                        stumessage['用户名'].append(newstudentusername)
                        stumessage['密码'].append(newstudentpasswd)
                        print("%s同学信息添加成功" %newstudentname)
                elif choice2 == '3':
                    print("欢迎进入学生信息删除页面".center(30, '*'))
                    delstudentname = input("输入要删除的学生姓名：")
                    if delstudentname not in stumessage['姓名']:
                        print("无此学生信息")
                    else:
                         i = stumessage['姓名'].index(delstudentname)
                         for t in stumessage:
                             stumessage[t].pop(i)
                             print("删除该学生信息已成功")
                elif choice2 == '4':
                    print("欢迎进入学生信息修改页面".center(30, '*'))
                    changename = input('输入要修改的学生姓名：')
                    if changename in stumessage:
                        info3 = """
                            修改选项：姓名，学号，性别，班级，出生年月日，用户名，密码
                        """
                        print(info3)
                        change = input('输入需要修改的名称：')
                        if change in stumessage:
                            changepoint = input('输入新的%s' % change)
                            i = stumessage['姓名'].index(changename)
                            stumessage[change].pop(i)
                            stumessage[change].insert(i,changepoint)
                        else:
                            print('无此修改选项')
                    else:
                        print('无此学生')
                elif choice2 == '5':
                    print("欢迎进入学生个人信息查询页面".center(30, '*'))
                    seachxuehao = input('输入要查找的学生学号')
                    if seachxuehao in stumessage['学号']:
                        i = stumessage['学号'.index(seachxuehao)]
                        for t in stumessage:
                            print(stumessage[t],stumessage[t][i])
                    else:
                        print('无此学号')
                elif choice2 == '6':
                    print("欢迎进入所有学生的查询页面".center(30, '*'))
                    for i in stumessage:
                        print(i)
                        for  t in stumessage[i]:
                            print(t)
                elif choice2 == '7':
                    print('退出系统')
                    break
                else:
                    print('选择输入有误，重新输入')
            else:
                print('登录失败')
                break
    elif choice1 == '2':
        print('欢迎进入学生登陆页面'.center(30,'*'))
        studentusername = input('输入登录学生系统用户名：')
        studentpasswd = input("输入登录学生系统密码：")
        while True:
            if studentusername in stumessage['用户名']:
                i = stumessage['用户名'].index(studentusername)
                if stumessage['密码'][i] == studentpasswd:
                    info4 = """
                         1.查询隔热膜信息
                         2.修改个人信息
                         3.退出
                    """
                    print(info4)
                    choice3 = input('请输入你的选择编号：')
                    if choice3 == '1':
                        print("欢迎进入学生个人信息查询页面".center(30,'*'))
                        i = stumessage['用户名'].index(studentusername)
                        for t in stumessage:
                            print(stumessage[t],stumessage[t][i])
                    elif choice3 == '2':
                        print("欢迎进入学生个人信息修改页面".center(30, '*'))
                        info5 = """
                             1.修改年龄
                             2.修改密码
                             3.退出
                        """
                        choice4 = input('输入你的操作编号：')
                        if choice4 == '1':
                            i = stumessage['用户名'].index(studentusername)
                            changeyage = input("输入修改后的年龄")
                            stumessage['年龄'].pop(i)
                            stumessage['年龄'].insert(i,changeyage)
                            print('年龄修改成功')
                        elif choice4=='2':
                        	i=stumessage['用户名'].index(studentusername)
                        	changestupasswd=input("输入新密码")
                        	stumessage['密码'].pop(i)
                        	stumessage['密码'].insert(i,changestupasswd)
                        	print("密码修改成功")
                        else:
                        	print("返回上一级")
                        	break
                    else:
                    	print("返回上一级")
                else:
                    print("学生用户名密码错误")
                    break
            else:
                print("没有这个账户")
                break
    elif choice1=='3':
    	print("退出系统")
    	break
    else:
   		print("输入错误")