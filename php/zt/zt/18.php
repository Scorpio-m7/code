<body>
<form id="form1" name="form1" method="post" action="17.php">
<table align="center">
<tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr>
<tr><td>ѧ��������<input type="text" name="xm"></td></tr>
  <tr><td>
<div align="center">ѡ��Ŀ�Ŀ��
  <select name="select" id="select">


<?php
 $servername = "localhost";
$username = "root";
$password = "123456";
$dbname = "teacher2";
$db = mysqli_connect($servername, $username, $password, $dbname);
if (! $db) {
    die("����ʧ��" . mysqli_connect_error());
}
$sql="select*from teacher2";
$result=mysqli_query($db,$sql);
if(mysqli_num_rows($result)>0){
  while($row=mysqli_fetch_assoc($result)){
   $kc=$row["kc"];?>
   <option><?php echo $kc?></option>
  <?php }
  mysqli_free_result($result);
  mysqli_close($db);
}?>
</select>
</div>
</td>
</tr>
<tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr>
<tr>

<td><p align="center">
  <input type="submit" name="button" id="button" value="���" />
</p ></td>
</tr>


</table>
</form>

</body>
</html>
