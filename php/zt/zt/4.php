<?php 
// $servername = "localhost";
// $username = "root";
// $password = "123456";
// $db = mysqli_connect($servername, $username, $password);
// mysql_select_db($db,'teacher');
// if (! $db) {
// 	die("连接失败" . mysqli_connect_error());
// }
// else {
// 	echo "数据库创建失败";
//  }

// 创建数据库
// $servername = "localhost";
// $username = "root";
// $password = "123456";
// $db = mysqli_connect($servername, $username, $password);
// if (! $db) {
// die("连接失败" . mysqli_connect_error());
// }
// $sql = "create database teacher";
// if (mysqli_query($db, $sql)) {
// echo "数据库创建成功！";
// } else {
// echo "数据库创建失败";
// }
// 创建表

// $servername = "localhost";
// $username = "root";
// $password = "123456";
// $dbname = "teacher";
// $db = mysqli_connect($servername, $username, $password, $dbname);
// if (! $db) {
// die("连接失败" . mysqli_connect_error());
// }

// $sql = "create table xmmm
// (
// id int(11) auto_increment primary key,
// name varchar(25) not null,
// mima int(4) not null,
// )";
// if (mysqli_query($db, $sql)) {
// echo "表创建成功！";
// } else {
// echo "创建失败";
// }

$servername = "localhost";
$username = "root";
$password = "123456";
$dbname = "teacher";
$db = mysqli_connect($servername, $username, $password, $dbname);
if (! $db) {
    die("连接失败" . mysqli_connect_error());
}
$sql="select *from teacher";
$result=mysqli_query($db, $sql);
if(mysqli_num_rows($result)>0){
while($row=mysqli_fetch_array($result))
{
echo "用户名".$row['name']."密码".$row['mima']."</br>";
}}
else{
	echo "没有结果";
}	
