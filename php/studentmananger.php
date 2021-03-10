<marquee>
  <h3>欢迎进入学生信息管理系统</h3>
</marquee><!DOCTYPE html>
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<title></title>
</head>
<body>
	<form name="from1" action="studentmananger.php" method="post">
		<table align="content">
			<tr>
				<td>学号：</td>
				<td><input type="text" name="xh"></td>
			</tr>
			<tr>
				<td>姓名：</td>
				<td><input type="text" name="name"></td>
			</tr>
			<tr>
				<td>性别：</td>
				<td><input type="radio" name="sex" value="男" >男<input type="radio" name="sex" value="女">女</td>
			</tr>
			<tr>
				<td>出生日期：</td>
				<td><select name="s1" id="s1">
				<?php for ($i=1980; $i<=2019 ; $i++):?>
					<option value='<?php echo $i?>'><?php echo $i?></option>
				<?php endfor ?>
			</select>年
			<select name="s2" id="s2">
				<?php for ($j=1; $j<=12 ; $j++){?>
					<option value='<?php echo $j?>'><?php echo $j?></option>
				<?php } ?>
			</select>月
			<select name="s3" id="s3">
				<?php for ($k=1; $k<=31 ; $k++){?>
					<option value='<?php echo $k?>'><?php echo $k?></option>
				<?php } ?>
			</select>日</td>
			</tr>
		
			<tr>
				<td>专业特长：</td>
				<td>
				    <input type="checkbox" name="c" value="c" id="CheckboxGroup1_0">
				    c</label>
				    <input type="checkbox" name="python" value="python" id="CheckboxGroup1_1">
				    python</label>
				    <input type="checkbox" name="C++" value="c++" id="CheckboxGroup1_2">
				    c++</label>
				    <input type="checkbox" name="php" value="php" id="CheckboxGroup1_3">
				    php</label>
				</td>
			</tr>
			<tr><td>家庭住址:</td><td><textarea rows="5" cols="30"></textarea></td></tr>
		</table>		
		<br>
		<input type="submit" name="button" id="button" value="提交">	
		<input type="reset">
	</form>
	<?php
		@$xh=$_POST['xh'];
		@$name=$_POST['name'];
		@$sex=$_POST['sex'];
		echo $xh,$name,$sex;
	?>
</body>
</html>