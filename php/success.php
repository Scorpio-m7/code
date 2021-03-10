<!DOCTYPE html>
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<title></title>
</head>
<body>
	<form name="form1" action="1.php" method="post">
		<?php
			@$name=$_POST['user'];
			@$passwd=$_POST['passwd'];
			$servername="localhost";
			$username="root";
			$passwd="123456";
			$dbname="employee";
			$db=mysqli_connect($servername,$username,$passwd,$dbname);
			if (!$db) {
				die("mysql连接失败".mysql_connect_error());
			}
			$sql3="select * from user";
			$result=mysqli_query($db,$sql3);
			$i=1;
			if (mysqli_num_rows($result)>0) {
				while ($row=mysqli_fetch_assoc($result)) {
					$usernamed[$i]=$row["username"];
					$userpasswd[$i]=$row["passwd"];
					$i=$i+1;
				}
			}else{
				echo "没结果";
				}
			session_start();
			if (isset($_POST['user'])) {
				$user=$_POST['user'];
			}
			if (isset($_POST['passwd'])) {
				$passwd=$_POST['passwd'];
			}
			if (isset($_POST['passwd2'])) {
				$passwd2=$_POST['passwd2'];
			}
			if (!(($user==$usernamed[1] & $passwd==$userpasswd[1])||($user==$usernamed[2] & $passwd==$userpasswd[2])||($user==$usernamed[3] & $passwd==$userpasswd[3])|| @($user==$usernamed[4] & $passwd==$userpasswd[4])|| @($user==$usernamed[5] & $passwd==$userpasswd[5]))){
				echo "<script>alert('用户名密码错误');</script>";
			}elseif ($passwd2!= $_SESSION['passwd2']) {
				echo "<script>alert('验证码错误');</script>";
			}else{
				echo "<script>alert('登陆成功');</script>";
				$_SESSION['user']=$user;
			}
			mysqli_free_result($result);
			mysqli_close($db);
		?>
	</form>
	<div align="center">
	</div>
</body>
</html>	