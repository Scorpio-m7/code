<?php 
$servername = "localhost";
$username = "root";
$password = "123456";
$dbname = "teacher";
$db = mysqli_connect($servername, $username, $password, $dbname);
if (! $db) {
    die("连接失败" . mysqli_connect_error());
}
$sql="select *from qd";
$result=mysqli_query($db, $sql);
if(mysqli_num_rows($result)>0){
while($row=mysqli_fetch_array($result))
{
echo "姓名".$row['name']."签到时间".$row['qd']."</br>";
}}
else{
	echo "没有结果";
}	

