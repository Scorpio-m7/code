<?php 
$servername = "localhost";
$username = "root";
$password = "123456";
$dbname = "student";
$db = mysqli_connect($servername, $username, $password, $dbname);
$xm=$_POST['xm'];

if (! $db) {
    die("����ʧ��".mysqli_connect_errno());
}

$sql = "delete from student where name = '$xm'";

if (mysqli_query($db, $sql)) {
    echo "����ɾ���ɹ���";
} else {
    echo "����ɾ��ʧ��";
}
mysqli_close($db);