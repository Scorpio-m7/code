#mysql数据库教程：https://www.bilibili.com/video/BV1Vx411g7uJ?p=57
#***************************************************数据库操作****************************************************
create database test charset gbk;#创建数据库
show databases;#显示所有数据库
#information_schema保存数据库结构信息
#mysql权限关系核心数据库
#performance_schema效率库
show databases like "t%";#查看以t开头的数据库
show databases like "ad_in";#查看中间一个字符不确定的数据库
show create database admin;#显示数据库创建语句
use test;#选择数据库
alter database test charset utf8;#修改数据库字符集
#drop database admin;#删除数据库
#***************************************************表操作****************************************************
create table test.class(id int primary key auto_increment,name varchar(10) comment '名字') charset utf8;#在指定数据库下创建数据表,id为主键自动增长(自增长一表一个),varchar最多存储21844个utf8字符,最大存储32766个gbk字符
#alter table class auto_increment=10;#修改自增长(不可以变小)
#alter table class modify id int;#删除自增长
show variables like 'auto_increment%';#查看自增长初始变量
#truncate class;#删除表中数据同时重置自增长
create table class1 like test.class;#复制数据表
show tables;#显示数据表
show tables like 'c%';#匹配数据表
show columns from my_class;--显示表结构
describe class;#显示表结构
desc class;#显示表结构
show create table class\G#横向显示数据表创建语句
rename table my_class to class;#重命名
alter table class add sf int first;#在数据表最前面加入字段
alter table class change sf id int;#修改字段名
alter table class modify name varchar(20);#修改字段类型
alter table class drop id;#删除字段
#drop table class;#删除表
#***************************************************数据操作****************************************************
insert into class (age,name) values(30,'jack'),(20,数据操作'anne'),(30,'lucy');#插入数据
insert into class values(2,25,'perter') on duplicate key update name='perter';#主键id冲突,只更新name
replace into class values(1,'mark',15);#替换所有数据
select distinct name as name1,name name2 from class where age and between 20 and 30;#查询age在20到30的name,去除完全重复的,as取别名查询`
select * from (select name,age from class) as my_class order by age desc limit 1,2;#动态查询一定要取别名,按照年龄age降序,limit 1,2->(偏移1个,返回2个)
select age,avg(id),group_concat(name) from class group by age with rollup;#使用聚合函数,统计各年龄id的平均值,拼接名字数据,回溯统计id平均值和名字
select name,sum(id) as sum_id from class group by age having sum_id>2;#按照年龄age分组,查询各组id和大于2的名字,id和别名为sum_id,where不能跟聚合函数
delete from class where age in (12,13);#删除age是12或13的
update class set age=45 where name='jack' and age is not null limit 1;#修改前1个name=jack,age不为空的age数据
#***************************************************字符集****************************************************
#set names gbk;#设置客户端,服务端返回的数据和连接层的字符集,这样才能插入中文数据
set character_set_client=gbk;#让服务器识别客户端传来的数据
set character_set_results=gbk;#让客户端识别服务器的字符
show variables like 'character_set%';#查看系统保存的处理字符集,默认utf-8
#***************************************************列类型****************************************************
create table my_int(int_1 tinyint,int_2 smallint,int_3 mediumint,int_4 int,int_5 bigint,int_6 tinyint unsigned)charset utf8;#分别为1,2,3,4,8个字节,最后一个无符号数
alter table my_int add int_7 tinyint(2) zerofill;#插入1字节字段,最短显示2个字符,左侧用零填充
insert into my_int values(1,1,1,1,1,1,1);#用来检验上面的
create table my_float(f1 float,f2 float(10,2),f3 decimal(10,2));#f2是浮点数10位整数2位小数,f3是定点数0位整数2位小数(最大65位整数30位小数)
insert into my_float values(3e3,12345678.90,99999999.99);#单精度浮点数精度大概存7位
create table my_date(d1 date,d2 time,d3 datetime,d4 timestamp,d5 year);
insert into my_date values('1900-01-01','512:12:12','1900-01-01 12:12:12','1999-01-01 12:12:12','69');#d5的year是2069以下或者1970以上
update my_date set d2 = '5 12:12:12' where d5=2069;#d2的time是5*24+12=132,d4时间戳自动更新
create table my_enum(gender enum('man','women','another'));#单选框,只能插入规定的数据项,枚举enum给每一个元素定义一个下标,下标1是'man'
insert into my_enum values('women');#下标2是'women'
select gender+0 from my_enum;#将字段按数值输出
insert into my_enum values(3);#插入数据'another'
create table my_set(hobby set('篮球','足球','乒乓球','网球'))charset utf8;#集合型字符串,多选框,每个位置对应0/1
insert into my_set values('网球,篮球,乒乓球');#自动排序,存储为二进制1011->翻转顺序1101->十进制13
insert into my_set values(12);#12->1100->0011->乒乓球,网球
select hobby+0 from my_set;
#***************************************************列属性****************************************************
create table my_score(student_no char(10),course_no char(10),score tinyint not null);#每个学生每门课一个成绩
alter table my_score add primary key(course_no,student_no);#添加主键,复合主键
#alter table my_score drop primary key(student_no);#删除主键
create table my_unique(id int primary key auto_increment,username varchar(10),unique key(username));#如果不为空的情况下,不容许重复
alter table my_unique drop index username;#允许多个唯一键
#***************************************************子查询****************************************************
create table my_char(name varchar(20) not null)charset=utf8;#蠕虫复制
insert into my_char(name) select name from class;#可以从其他表中复制数据
(select * from class order by id limit 4) union all (select age,name,id from class order by id desc limit 4);#联合查询不需要字段类型一致,使用order by必须使用括号和limit,不去重查询1.按照id降序2.age,name,id按照id升序
select * from class as a inner join my_char b using(name);#内连接查询,class和my_char表中的name相等时取别名拼接输出,使用using代替on
select * from class as a left join my_char b on a.name=b.name;#外连接查询,class表为主表,主表的内容一定显示
select * from class where name=(select * from my_char where name='perter');#标量子查询
select id from class where name =any(select name from my_char);#列子查询,查找class中名字在my_char表中的id
select * from class where (id,age)=(select max(age),max(id) from class);#行子查询,查找id,age最大的信息
select * from (select * from class order by id desc) as temp group by age;#表子查询,各年龄id最大的信息
select * from class as a where exists(select * from my_char as b where a.name=b.name);#exists子查询,返回布尔值,查询到值返回true
##***************************************************数据库备份****************************************************
mysqldump.exe -hlocalhost -P3306 -uroot -p123456 test > D:/php/PHPTutorial/MySQL/bin/test.sql#整库备份
mysqldump -uroot -p123456 test class my_char > D:/php/PHPTutorial/MySQL/bin/class_my_char.sql#多表备份
mysql -uroot -p123456 mytest < D:/php/PHPTutorial/MySQL/bin/test.sql#还原数据,在cmd中运行
source D:/php/PHPTutorial/MySQL/bin/class_my_char.sql;#先use 库
#***************************************************用户权限管理****************************************************
select * from mysql.user\G#查看mysql用户,host和user共同组成主键区分用户
create user 'user1'@'%' identified by '123456';#创建用户user1,所有IP都可访问,密码123456
#drop user user1@'%';#删除用户
set password for 'user1'@'%'=password('654321');#修改密码
grant select on test.class to 'user1'@'%';#给user1赋予查询test数据库中class表的权限
revoke all privileges on test.class from 'user1'@'%';#从user1收回test.class所有权限
flush privileges;#刷新权限
mysql.exe --skip-grant-tables//mysql.exe可以直接以root权限启动服务器
#***************************************************外键****************************************************
CREATE TABLE t4(nid int(11) AUTO_INCREMENT primary key)ENGINE=InnoDB DEFAULT CHARSET=utf8;#被连接的主表必须是主键
CREATE TABLE t5(pid int(11) primary key)ENGINE=InnoDB DEFAULT CHARSET=utf8;#相互连接的名称不能一样
create table t6(id1 int,id2 int,CONSTRAINT fk_t4_t6 foreign key (id1) REFERENCES t4(nid))engine=innodb default charset=utf8;#t6的id1外键连接t4的nid
alter table t6 drop foreign key `t5_t6_ibfk_1`;#删除外键
alter table t6 drop index `t5_t6_ibfk_1`;#删除自动添加的索引
insert into t4 values(1);#主表随意插入数据,必须向删除从表才能删除主表
insert into t6 values(2);#错误,从表不能插入外键主表没有的记录
alter table t6 add constraint `t5_t6_ibfk_1` foreign key(id2) references t5(pid) on update cascade on delete set null;#修改t6表,将id2设为外键,指定外键名字为t5_t6_ibfk_1,连接到t5的pid,更新级联,删除置空
insert into t5 values(2);#主表随意插入
insert into t6 values(1,2);#从表只能插入主表有的记录
update t5 set pid=3 where pid=2;#更改t5中的pid也会使t6中的id2更改,更新级联
delete from t5 where pid=3;#删除t5中的pid会使t6中的id2设为为null,删除置空
#***************************************************视图****************************************************
create view class_v as select * from class;#创建视图,视图是虚拟表
alter view class_v as select * from my_char;#修改视图
drop view class_v;#删除视图
#***************************************************事务安全****************************************************
show variables like 'autocommit%';==select @@autocommit;#查看自动事务开关
set autocommit=on;#开启自动更新事物,本次会话有效
start transaction;#开启事物
savepoint sp1;#设置回滚点sp1=虚拟机快照
rollback to sp1;#回到快照sp1
commit;#提交,在自动事务关闭后同步数据表
rollback;#回滚,取消操作
#***************************************************变量****************************************************
set global auto_increment_increment=1;==set @@global.auto_increment_increment=1;#设置全局自增长步长,重启客户端生效
set @name='HelloWorld';==set @name :='HelloWorld';#定义用户变量,可跨库可在函数中使用,:=为赋值符号,=为比较符号
select @name :=name,@age:=age from class limit 1;#通过查询数据为变量赋值,将class表中第一行的name和age赋给用户变量@name,@age
select name,age from class order by id desc limit 1 into @name,@age;#将class表按id从大到小排序后，取第一行name,age赋给用户变量@name,@age
#****************************************************if分支******************************************************
select *,if(age>20,'old','young') as judge from class;#年龄大于20为old
##***************************************************内置函数****************************************************
select char_length('长度'),length('长度'),concat('拼','接'),instr('存在','在'),lcase('LOWERcAsE'),left('左侧开始到指定位置',5),ltrim('   ab  c ');#字符数,字节数,拼接,不存在返回0,全部小写,左侧开始截取,消除左侧空格
select mid('从指定位置开始到结束',6),now(),curdate(),curtime(),datediff('2021-10-1','2018-2-25'),date_add('2021-3-15',interval 1314 minute),unix_timestamp();#从指定位置截取,日期 时间,日期,时间,日期差,时间增加,时间戳
select from_unixtime(123456789),abs(-1),ceiling(1.1),floor(1.1),pow(2,4),rand(),round(1.5),md5('a'),version(),database();#时间戳变日期,绝对值,向上取整,向下取整,指数,0-1随机数,四舍五入,md5加密,版本号,数据库
#****************************************************自定义函数*******************************************************
delimiter $$#修改语句结束符
create function my_sum(last int) returns int#创建函数要确定形参类型和返回类型
begin
	declare result int default 0;#declare声明局部变量要在其他语句前
	declare i int default 1;
	mywhile:while i<=last do#循环
		if i%5=0 then#去掉5的倍数
			set i=i+1;#mysql中没有++
			iterate mywhile;
		end if;
		set result=result+i;#修改变量
		set i=i+1;
	end while mywhile;
	return result;#函数内部select语句只能赋值
end
$$
delimiter ;#改回语句结束符
show function status\G#查看所有函数
show create function my_sum;#查看函数创建语句
select my_sum(10);#调用函数,只能调用对应数据库下的函数
drop function my_sum;#在对应数据库下删除自定义函数
#****************************************************存储过程*******************************************************
set @n1=1,@n2=2,@n3=3;#创建会话变量
delimiter $$--修改语句结束符
create procedure my_pro1(in int_1 int,out int_2 int,inout int_3 int)--过程没有返回值，但可以传入形参
begin#如果过程体中只有一条指令,可以省略begin和end
	declare i int default 1;
	#declare sum int default 0;#局部变量
	set @sum=0;#会话变量
	while i<=100 do#求1-100之间的和
		set @sum=@sum+i;
		set i=i+1;
	end while;
	select @sum;#显示结果
	select int_1,int_2,int_3;#首先设置out类型的变量为null
	set int_1='91',int_2='92',int_3='93';#修改会话变量
end
$$
delimiter ;#改回语句结束符
show procedure status\G#查看所有存储过程
show create procedure my_pro1\G#查看过程创建语句
call my_pro1(@n1,@n2,@n3);#传入形参,没有返回值,select不能调用
select @n1,@n2,@n3;#out和inout类型的值会被修改
drop procedure my_pro1;#在对应数据库下删除存储过程
