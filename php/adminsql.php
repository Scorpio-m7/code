<html>
<marquee><h3>录入信息</h3></marquee>
<!DOCTYPE html>
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<title></title>
	<script type="text/javascript">
		function yz(form){
			if (form1.name.value=='') {
				alert('用户名不能为空');
				form1.name.focus();
				return false;
			}
			if (form1.age.value=='') {
				alert('密码不能为空');
				form1.age.focus();
				return false;
			}
		}
	</script>
</head>
<body>
	<div align="center">
	<h1>添加用户</h1>
	<hr>
	<form name="form1" action="adminsql2.php" method="post">
		<table align="content">
			<tr>
				<td>用户名：</td>
				<td><input type="text" name="name"></td>
			</tr>
			<tr>
				<td>密码：</td>
				<td><input type="text" name="passwd"></td>
			</tr>
			<tr>
				<td>职称：</td>
				<td><input type="text" name="sta"></td>
			</tr>
			<tr>
				<td><input type="submit" name="button" id="button" value="添加" onclick="return yz(this);" /></td>
				<td><input name="查看所有用户信息" type="button" value="查看所有用户信息"  onclick="location.href='adminsql2.php'" /></td>
			</tr>
	</form>
	</div>
</body>
</html>