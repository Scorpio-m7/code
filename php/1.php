<html>
<head>
<title>1</title>
<style type="text/css">
#apDiv1 {
	position: absolute;
	left: 492px;
	top: 282px;
	width: 547px;
	height: 555px;
	z-index: 1;
	}</style>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
</head>
<body bgcolor="#FFFFFF" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0">
<!-- Save for Web Slices (未标题-1) -->
<table id="__01" width="800" height="1000" border="0" cellpadding="0" cellspacing="0" align="center" >
	<tr>
		<td colspan="2">
			<img src="images/未标题-1_01.png" alt="" width="800" height="198" usemap="#Map2" border="0"></td>
	</tr>
	<tr>
		<td colspan="2">
		  <img src="images/未标题-1_02.png" alt="" width="800" height="51" usemap="#Map" border="0"></td>
	</tr>
	<tr>
		<td><table background="images/未标题-1_03.png" width="210" height="500" alt="">
			<tr><td width="43" height="93"></td><td width="127"></td><td width="24"></td></tr>
			<tr><td height="322"></td><td><?php 
						session_start();
						echo "当前用户：",$_SESSION['user'],"<br>","系统时间:",date("y年m月d日h:i:sa"),"<br>";
						if (!@$fp=fopen("counter.txt", r)) {
							echo "counter.txt创建成功";	
						}
						@$sum=fgets($fp,12);
						if ($sum == ""){
							$sum = 0;
						}
						$sum =$sum+1;
						@fclose($fp);
						$fp=fopen("counter","w");
						fwrite($fp, $sum);
						fclose($fp);
						echo "您是第".$sum."浏览者";
					?></td><td width="24"></td></tr>
			<tr><td height="330"></td><td><iframe scr="userdl.php" width="80%" height="65%" frameborder="0" name="frame2"></iframe></td><td width="24"></td></tr>
			</table>
	  </td>
		<td><table background="images/未标题-1_04.png" width="590" height="750" alt="">
		  <tr><td width="43" height="149"></td><td width="478"></td><td width="53"></td></tr>
			<tr><td height="413"></td>
			  <td><iframe scr="userdl.php" width="100%" height="100%" frameborder="0" name="frame1"></iframe></td><td width="53"></td></tr>
			<tr><td height="112"></td><td></td><td width="53"></td></tr>
			</table>
	</td>
	</tr>
</table>
<p><!-- End Save for Web Slices --></p>
<map name="Map">
  <area shape="rect" coords="13,8,59,37" href="1.php" target="_self" >
  <area shape="rect" coords="68,9,189,37" href="sql.php" target="frame1">
  <?php if ($_SESSION['user']=='teacher') {?>
  <area shape="rect" coords="202,10,324,36" href="teachercourse.php" target="frame1">
  <?php }elseif ($_SESSION['user']=='student') {?>
  <area shape="rect" coords="202,10,324,36" href="studentcourse.php" target="frame1">
  <?php } ?>
  <?php if ($_SESSION['user']=='teacher') {?>
  <area shape="rect" coords="336,11,456,35" href="sql.php" target="frame1">
  <?php }elseif ($_SESSION['user']=='student') {?>
  <area shape="rect" coords="336,11,456,35" href="sqlstudent.php" target="frame1">
  <?php } ?>
  <area shape="rect" coords="467,12,550,34" href="uploadimage.php" target="frame1">
  <area shape="rect" coords="563,11,601,36" href="#">
  <area shape="rect" coords="615,9,679,37" href="#">
</map>

<map name="Map2">
  <?php if ($_SESSION['user']=='admin') {?>
  <area shape="rect" coords="683,8,731,36" href="adminsql.php" target="frame1" >
  <?php } ?>
  <area shape="rect" coords="739,10,783,34" href="userdl.php" target="frame1">
</map>
</body>
</html>