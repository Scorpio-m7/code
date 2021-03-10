<?php 
$servername = "localhost";
$username = "root";
$password = "123456";
$dbname = "teacher2";
$db = mysqli_connect($servername, $username, $password, $dbname);
$xm=$_POST['xm'];
$kc=$_POST['kc'];

if (! $db) {
    die("连接失败".mysqli_connect_errno());
}
$sql = "insert into teacher2(name,kc)values('$xm','$kc')";


if (mysqli_query($db, $sql)) {
    echo "数据插入成功！";
} else {
    echo "数据插入失败";
}
mysqli_close($db);
