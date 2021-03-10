def admin():
    print('管理员登陆'.center(50,'*'))
    adminname1 = input('用户名：')
    adminpasswd1 = input('密码：')
    adminname = ['admin']
    adminpasswd = ['123']

    if adminname1 == adminname[0] and adminpasswd1 == adminpasswd[0]:
        while True:
            print("""
        1.管理员密码修改
        2.添加学生信息
        3.删除学生信息
        4.修改学生信息
        5.查询学生的信息（根据学号）
        6.查看所有学生的信息
        7.退出系统
            """)
            admin1 = int(input('请选择：'))
            if admin1 == 1:
                print('管理员密码修改'.center(50,'*'))
                newadminpasswd = input('请输入新密码：')
                if newadminpasswd not in adminpasswd:
                    del adminpasswd[0]
                    adminpasswd.append(newadminpasswd)
                else:
                    print('密码已存在')
            if admin1 == 2:
                print('添加学生信息'.center(50,'*'))
                addscore = input('添加学号：')
                if addscore not in addnamepasswd:
                    addname = input('添加学生姓名:')
                    addpasswd = input('添加密码：')
                    addsex = input('性别：')
                    addage = input('年龄：')
                    addnamepasswd[addscore]={'姓名':addname,
                                             '密码':addpasswd,
                                             '学号':addscore,
                                             '性别':addsex,
                                             '年龄':addage
                                        }
                    print(addnamepasswd)
                else:
                    print('该学生已存在')
            if admin1 == 3:
                print('删除学生信息'.center(50,'*'))
                print(addnamepasswd)
                delname = input('请输入学号：')
                if delname in addnamepasswd:
                    del addnamepasswd[delname]
                    print('%s已删除' %(delname))
                else:
                    print('该学生不存在')
            if admin1 == 4:
                print('修改学生信息'.center(50,'*'))
                changename = input('请输入学号：')
                if changename in addnamepasswd:
                    print(addnamepasswd)
                    changepasswd = input('请修改密码：')
                    changesname = input('请修改姓名：')
                    changesex = input('请修改性别')
                    changeage = input('请修改年龄：')
                    addnamepasswd[changename]={'姓名':changesname,
                                               '密码':changepasswd,
                                               '性别':changesex,
                                               '年龄':changeage
                                               }
            if admin1 == 5:
                print('查看学生信息'.center(50,'*'))
                print(addnamepasswd)
                look = input('输入学生学号：')
                if look in addnamepasswd:
                    print(addnamepasswd[look])
            if admin1 == 6:
                print('查看所有学生信息'.center(50,'*'))
                print(addnamepasswd)
            if admin1 == 7:
                print('logout')
                break

    else:
        print('用户名或密码错误请重新登陆')

def student():
    print('学生登陆系统'.center(50,'*'))
    studentname = input('请输入学号：')
    studentpasswd = input('请输入密码：')
    if studentname in addnamepasswd:
        if addnamepasswd[studentname]['密码'] == studentpasswd:
            print('登陆成功')
        while True:
            print('''
            1 查询个人信息;
            2 修改信息;
            3 退出
            ''')
            studentcx = input('请选择：')
            if studentcx == '1':
                print('查询个人信息'.center(50,'*'))
                print(addnamepasswd[studentname])
            if studentcx == '2':
                print('修改个人信息'.center(50,'*'))
                print('''
                 1.修改年龄
                 2.修改密码
                ''')
                studentxg = input('请选择：')
                if studentxg == '1':
                    studentage = input('修改年龄：')
                    addnamepasswd[studentname]['年龄'] = studentage
                    print('%s年龄修改成功' %(studentname))
                if studentxg == '2':
                    studentps = input('修改密码：')
                    addnamepasswd[studentname]['密码'] = studentps
                    print('%s密码修改成功' %(studentname))
            if studentcx == '3':
                print('logout')
                break

def main():
    while True:
        print('学生管理系统'.center(50,'*'))
        print("""
            1.管理员登陆
            2.学生登陆
            3.退出
            """)
        firstch = input('请选择：')

        if firstch == '1':
            admin()
        if firstch == '2':
            student()
        if firstch == '3':
            exit(0)


addnamepasswd = {}
main()