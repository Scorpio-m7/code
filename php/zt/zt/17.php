<?php 
$servername = "localhost";
$username = "root";
$password = "123456";
$dbname = "student";
$db = mysqli_connect($servername, $username, $password, $dbname);
$kc=$_POST['select'];
$xm=$_POST['xm'];
if (! $db) {
    die("����ʧ��".mysqli_connect_errno());
}
$sql = "update student set kc='$kc' where name='$xm'";
if (mysqli_query($db, $sql)) {
    echo "���ݲ���ɹ���";
} else {
    echo "���ݲ���ʧ��";
}
mysqli_close($db); 
