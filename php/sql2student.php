<!DOCTYPE html>
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<title></title>
</head>
<body>
	<?php
		@$name=$_POST['name'];
		$servername="localhost";
		$username="root";
		$passwd="123456";
		$dbname="employee";
		$db=mysqli_connect($servername,$username,$passwd,$dbname);
		if (!$db) {
			die("mysql连接失败".mysql_connect_error());
		}
		if (isset($_POST['name'])) {
		$sql3="select * from employee where name='$name' ";
		$result=mysqli_query($db,$sql3);
		if (mysqli_num_rows($result)>0) {
			while ($row=mysqli_fetch_assoc($result)) {
				echo "编号".$row["id"].",姓名".$row["name"].",出生日期".$row["age"].",成绩".$row["salary"]."<br>";
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