<?php 
$servername = "localhost";
$username = "root";
$password = "123456";
$dbname = "teacher2";
$db = mysqli_connect($servername, $username, $password, $dbname);
if (! $db) {
    die("连接失败" . mysqli_connect_error());
}
$sql="select *from teacher2";
$result=mysqli_query($db, $sql);
if(mysqli_num_rows($result)>0){
while($row=mysqli_fetch_array($result))
{
echo "姓名".$row['name']."课程".$row['kc']."</br>";
}}
else{
	echo "没有结果";
}	
