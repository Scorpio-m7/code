<?php 
$servername = "localhost";
$username = "root";
$password = "123456";
$dbname = "student";
$db = mysqli_connect($servername, $username, $password, $dbname);
$xm=$_POST['xm'];
$cj=$_POST['cj'];

if (! $db) {
    die("连接失败".mysqli_connect_errno());
}
$sql = "insert into student(name,cj)values('$xm','$cj')";


if (mysqli_query($db, $sql)) {
    echo "数据插入成功！";
} else {
    echo "数据插入失败";
}
mysqli_close($db);
