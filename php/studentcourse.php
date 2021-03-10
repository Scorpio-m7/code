<marquee>
  <h3>欢迎进入学生课程信息管理系统</h3>
</marquee>
<!DOCTYPE html>
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<title></title>
</head>
<body>
	<form name="from1" action="studentcoursesql.php" method="post" align="center">
		<table align="center">
			<tr>
				<td>学号：</td>
				<td><input type="text" name="id"></td>
			</tr>
			<tr>
				<td>姓名：</td>
				<td><input type="text" name="name"></td>
			</tr>
			<tr>
				<td>性别：</td>
				<td><input type="radio" name="sex" value="男" >男<input type="radio" name="sex" value="女">女</td>
			</tr>		
			<tr>
				<td>课程：</td>
				<td>
				    <input type="checkbox" name="c" value="c" id="CheckboxGroup1_0">
				    c</label>
				    <input type="checkbox" name="python" value="python" id="CheckboxGroup1_1">
				    python</label>
				    <input type="checkbox" name="C++" value="c++" id="CheckboxGroup1_2">
				    c++</label>
				    <input type="checkbox" name="php" value="php" id="CheckboxGroup1_3">
				    php</label>
				</td>
			</tr>	
		<tr>
		<td><input type="submit" name="button" id="button" value="提交">	</td>
		</tr>
		</table>
	</form>
</body>
</html>