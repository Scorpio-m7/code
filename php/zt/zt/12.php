<?php 
$servername = "localhost";
$username = "root";
$password = "123456";
$dbname = "teacher2";
$db = mysqli_connect($servername, $username, $password, $dbname);
if (! $db) {
    die("����ʧ��" . mysqli_connect_error());
}
$sql="select *from teacher2";
$result=mysqli_query($db, $sql);
if(mysqli_num_rows($result)>0){
while($row=mysqli_fetch_array($result))
{
echo "����".$row['name']."�γ�".$row['kc']."</br>";
}}
else{
	echo "û�н��";
}	
