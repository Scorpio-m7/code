<?php 
$servername = "localhost";
$username = "root";
$password = "123456";
$dbname = "student";
$db = mysqli_connect($servername, $username, $password, $dbname);
if (! $db) {
    die("����ʧ��" . mysqli_connect_error());
}
$sql="select *from student";
$result=mysqli_query($db, $sql);
if(mysqli_num_rows($result)>0){
while($row=mysqli_fetch_array($result))
{
echo "����".$row['name']."�ɼ�".$row['cj']."</br>";
}}
else{
	echo "û�н��";
}	

