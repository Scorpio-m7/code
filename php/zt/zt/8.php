<?php 
$servername = "localhost";
$username = "root";
$password = "123456";
$dbname = "student";
$db = mysqli_connect($servername, $username, $password, $dbname);
$xm=$_POST['xm'];
$cj=$_POST['cj'];

if (! $db) {
    die("����ʧ��".mysqli_connect_errno());
}
$sql = "insert into student(name,cj)values('$xm','$cj')";


if (mysqli_query($db, $sql)) {
    echo "���ݲ���ɹ���";
} else {
    echo "���ݲ���ʧ��";
}
mysqli_close($db);
