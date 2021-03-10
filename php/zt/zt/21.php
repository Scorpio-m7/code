<?php 
$servername = "localhost";
$username = "root";
$password = "123456";
$dbname = "teacher";
$db = mysqli_connect($servername, $username, $password, $dbname);
$xm=$_POST['xm'];
$qd=$_POST['sj'];


if (! $db) {
    die("连接失败".mysqli_connect_errno());
}
$sql = "insert into qd(name,qd)values('$xm','$qd')";


if (mysqli_query($db, $sql)) {
    echo "已签到！";
} else {
    echo "数据插入失败";
}
mysqli_close($db);
