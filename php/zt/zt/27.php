<?php 
$servername = "localhost";
$username = "root";
$password = "123456";
$dbname = "teacher";
$db = mysqli_connect($servername, $username, $password, $dbname);
$xm=$_POST['xm'];
$mm=$_POST['mm'];

if (! $db) {
    die("����ʧ��".mysqli_connect_errno());
}
$name=$_POST['xm'];
$sql = "delete from teacher where name = '$name'";


if (mysqli_query($db, $sql)) {
    echo "����ɾ���ɹ���";
} else {
    echo "����ɾ��ʧ��";
}
mysqli_close($db);

