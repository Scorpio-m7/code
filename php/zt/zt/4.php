<?php 
// $servername = "localhost";
// $username = "root";
// $password = "123456";
// $db = mysqli_connect($servername, $username, $password);
// mysql_select_db($db,'teacher');
// if (! $db) {
// 	die("����ʧ��" . mysqli_connect_error());
// }
// else {
// 	echo "���ݿⴴ��ʧ��";
//  }

// �������ݿ�
// $servername = "localhost";
// $username = "root";
// $password = "123456";
// $db = mysqli_connect($servername, $username, $password);
// if (! $db) {
// die("����ʧ��" . mysqli_connect_error());
// }
// $sql = "create database teacher";
// if (mysqli_query($db, $sql)) {
// echo "���ݿⴴ���ɹ���";
// } else {
// echo "���ݿⴴ��ʧ��";
// }
// ������

// $servername = "localhost";
// $username = "root";
// $password = "123456";
// $dbname = "teacher";
// $db = mysqli_connect($servername, $username, $password, $dbname);
// if (! $db) {
// die("����ʧ��" . mysqli_connect_error());
// }

// $sql = "create table xmmm
// (
// id int(11) auto_increment primary key,
// name varchar(25) not null,
// mima int(4) not null,
// )";
// if (mysqli_query($db, $sql)) {
// echo "�����ɹ���";
// } else {
// echo "����ʧ��";
// }

$servername = "localhost";
$username = "root";
$password = "123456";
$dbname = "teacher";
$db = mysqli_connect($servername, $username, $password, $dbname);
if (! $db) {
    die("����ʧ��" . mysqli_connect_error());
}
$sql="select *from teacher";
$result=mysqli_query($db, $sql);
if(mysqli_num_rows($result)>0){
while($row=mysqli_fetch_array($result))
{
echo "�û���".$row['name']."����".$row['mima']."</br>";
}}
else{
	echo "û�н��";
}	
