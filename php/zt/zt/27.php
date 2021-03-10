<?php 
$servername = "localhost";
$username = "root";
$password = "123456";
$dbname = "teacher";
$db = mysqli_connect($servername, $username, $password, $dbname);
$xm=$_POST['xm'];
$mm=$_POST['mm'];

if (! $db) {
    die("连接失败".mysqli_connect_errno());
}
$name=$_POST['xm'];
$sql = "delete from teacher where name = '$name'";


if (mysqli_query($db, $sql)) {
    echo "数据删除成功！";
} else {
    echo "数据删除失败";
}
mysqli_close($db);

