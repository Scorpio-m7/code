<!DOCTYPE html>
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<title></title>
</head>
<body>
	<?php
		@$name=$_POST['name'];
		@$passwd=$_POST['passwd'];
		@$sta=$_POST['sta'];
		$servername="localhost";
		$username="root";
		$passwd="123456";
		$dbname="employee";
		$db=mysqli_connect($servername,$username,$passwd,$dbname);
		if (!$db) {
			die("mysql连接失败".mysql_connect_error());
		}
		if (isset($_POST['name'])) {
			$sql2="insert into user(username,passwd,sta)values('$name','$passwd','$sta');";
			if (mysqli_query($db,$sql2)) {
				echo "<script>alert('数据插入成功');</script>";
			}else{
				echo "<script>alert('数据插入失败');</script>";
			}
		}else{
		$sql3="select * from user ";
		$result=mysqli_query($db,$sql3);
		if (mysqli_num_rows($result)>0) {
			while ($row=mysqli_fetch_assoc($result)) {
				echo "编号".$row["Id"].",用户名".$row["username"].",密码".$row["passwd"].",职位".$row["sta"]."<br>";
			}
		}else{
			echo "没结果";
			}
		mysqli_free_result($result);
		}
		mysqli_close($db);
	?>
	<div align="center">
	</div>
</body>
</html>	