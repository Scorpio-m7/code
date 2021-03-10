<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
</head><?php 
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
$sql = "insert into teacher(name,mima)values('$xm','$mm')";


if (mysqli_query($db, $sql)) {
    echo "数据插入成功！";
} else {
    echo "数据插入失败";
}
mysqli_close($db);
</html>
</head>