<?php 
$servername = "localhost";
$username = "root";
$password = "123456";
$dbname = "student";
$db = mysqli_connect($servername, $username, $password, $dbname);
$xm=$_POST['xm'];

if (! $db) {
    die("连接失败".mysqli_connect_errno());
}

$sql = "delete from student where name = '$xm'";

if (mysqli_query($db, $sql)) {
    echo "数据删除成功！";
} else {
    echo "数据删除失败";
}
mysqli_close($db);