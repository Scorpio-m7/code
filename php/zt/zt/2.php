<?php
$name=$_POST['yhm'];
$mm1=$_POST['mm'];
$yzm1=$_POST['yan'];
session_start();
$_SESSION["name1"]=$name;
$yzm2=$_SESSION['yzmnew'];
echo "用户注册信息";
echo "<hr>";
if($yzm1 != $yzm2){
    echo "验证码输入不正确，请重新输入！！";
}

else{
 $servername = "localhost";
 $username = "root";
 $password = "123456";
 $dbname = "teacher";   
 $db = mysqli_connect($servername, $username, $password, $dbname);
 if (! $db) {
  die("连接失败" . mysqli_connect_error());
 }
 $sql="select*from teacher";
 $sql2="select*from student";
 $result=mysqli_query($db,$sql);
 $result2=mysqli_query($db,$sql2);
 if(mysqli_num_rows($result)>0){
  while($row=mysqli_fetch_assoc($result)){
   $jiaoshi=$row["name"];
   $jiaoshimm=$row["mima"];
   if($name==$jiaoshi){
    if($mm1 !=$jiaoshimm){
    echo '< a href="1.php">返回上一页</ a>';
    }
    else {header("location:7.php");}
   }
   
  }
  mysqli_free_result($result);
  mysqli_close($db);
 }
 if (mysqli_num_rows($result2)>0){
  while($row=mysqli_fetch_assoc($result2)){
   $xs=$row["name"];
   $xsmm=$row["cj"];
   if($name==$xs){
    if($mm1 !=$xsmm){
    echo '< a href="1.php">返回上一页</ a>';
    }
    else {header("location:14.php");}
   }
  }
  mysqli_free_result($result2);
  mysqli_close($db);
 }
 if ($name=='admin'){
  if($mm1!="123456")
  {echo '< a href="1.php">返回上一页</ a>';}
  header("location:3.php");
 }
}
?>