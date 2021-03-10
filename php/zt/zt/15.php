<?php 
$servername = "localhost";
$username = "root";
$password = "123456";
$dbname = "student";
$xm=$_POST['xm'];
$db = mysqli_connect($servername, $username, $password, $dbname);
if (! $db) {
    die("连接失败" . mysqli_connect_error());
}
$sql="select *from student";
$result=mysqli_query($db, $sql);
if(mysqli_num_rows($result)>0){
while($row=mysqli_fetch_array($result))
{
    $xs=$row["name"];
    if($xm==$xs){
        echo "姓名".$row['name']."成绩".$row['cj']."</br>";
    }

}
mysqli_free_result($result);
mysqli_close($db);
}

else{
	echo "没有结果";
}	
