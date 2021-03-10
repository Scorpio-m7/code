<marquee>
  <h3>欢迎登陆</h3>
</marquee><!DOCTYPE html>
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<title></title>
	<script type="text/javascript">
		function yz(form){
			if (form1.user.value=='') {
				alert('用户名不能为空');
				form1.user.focus();
				return false;
			}
			if (form1.passwd.value=='') {
				alert('密码不能为空');
				form1.passwd.focus();
				return false;
			}
			if (form1.passwd2.value=='') {
				alert('验证码不能为空');
				form1.passwd2 .focus();
				return false;
			}
			
		}
	</script>
</head>
<body>
	<div align="center">
	<h1>用户登陆</h1>
	<hr>
	<form name="form1" action="success.php" method="post">
		<table align="content">
			<tr>
				<td>用户名：</td>
				<td><input type="text" name="user"></td>
			</tr>
			<tr>
				<td>密码：</td>
				<td><input type="text" name="passwd"></td>
			</tr>
			<tr>
				<td>验证码：</td>
				<td><input type="text" name="passwd2">
					<?php 
						session_start();
						$_SESSION['passwd2']=rand(1000,9999);
						echo $_SESSION['passwd2'];
					?>
				</td>
			</tr>
			<tr>
				<td><input type="submit" name="button" id="button" value="登陆" onclick="return yz(this);" /></td>
				<td><input type="reset"></td>
			</tr>
	</form>
	</div>
</body>
</html>	
