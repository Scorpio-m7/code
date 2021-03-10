<!DOCTYPE html>
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<title></title>
</head>
<body>
	<?php
		@$id=$_POST['id'];
		@$name=$_POST['name'];
		@$sex=$_POST['sex'];
		@$course=$_POST['c'].' '.$_POST['python'].' '.$_POST['c++'].' '.$_POST['php'];
		$servername="localhost";
		$username="root";
		$passwd="123456";
		$dbname="employee";
		$db=mysqli_connect($servername,$username,$passwd,$dbname);
		if (!$db) {
			die("mysql连接失败".mysql_connect_error());
		}
		if (isset($_POST['id'])) {
			$sql2="insert into course(Id,name,sex,course)values('$id','$name','$sex','$course');";
			if (mysqli_query($db,$sql2)) {
				echo "<script>alert('数据插入成功');</script>";
			}else{
				echo "<script>alert('数据插入失败');</script>";
			}
		}else{
		$sql3="select * from course ";
		$result=mysqli_query($db,$sql3);
		if (mysqli_num_rows($result)>0) {
			while ($row=mysqli_fetch_assoc($result)) {
				echo "学号:".$row["Id"].",姓名:".$row["name"].",性别:".$row["sex"].",课程:".$row["course"]."<br>";
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