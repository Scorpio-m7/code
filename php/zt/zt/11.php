<?php 
$servername = "localhost";
$username = "root";
$password = "123456";
$dbname = "teacher2";
$db = mysqli_connect($servername, $username, $password, $dbname);
$xm=$_POST['xm'];
$kc=$_POST['kc'];

if (! $db) {
    die("����ʧ��".mysqli_connect_errno());
}
$sql = "insert into teacher2(name,kc)values('$xm','$kc')";


if (mysqli_query($db, $sql)) {
    echo "���ݲ���ɹ���";
} else {
    echo "���ݲ���ʧ��";
}
mysqli_close($db);
