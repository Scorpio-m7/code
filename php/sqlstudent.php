<html>
<marquee><h3>查询信息</h3></marquee>
<!DOCTYPE html>
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<title></title>
	<script type="text/javascript">
		function yz(form){
			if (form1.name.value=='') {
				alert('学生姓名不能为空');
				form1.name.focus();
				return false;
			}			
		}
	</script>
</head>
<body>
	<div align="center">
	<h1>查询成绩信息</h1>
	<hr>
	<form name="form1" action="sql2student.php" method="post">
		<table align="content">
			<tr>
				<td>学生姓名：</td>
				<td><input type="text" name="name"></td>
			</tr>
			<tr>
				<td><input name="查看学生信息" type="submit" value="查看学生信息"  onclick="location.href='sql2student.php'" /></td>
			</tr>
	</form>
	</div>
</body>
</html>