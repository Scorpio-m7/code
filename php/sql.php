<html>
<marquee><h3>录入信息</h3></marquee>
<!DOCTYPE html>
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<title></title>
	<script type="text/javascript">
		function yz(form){
			if (form1.name.value=='') {
				alert('学生姓名不能为空');
				form1.name.focus();
				return false;
			}
			if (form1.age.value=='') {
				alert('学生出生日期不能为空');
				form1.age.focus();
				return false;
			}
			if (form1.salary.value=='') {
				alert('学生成绩不能为空');
				form1.salary.focus();
				return false;
			}
			
		}
	</script>
</head>
<body>
	<div align="center">
	<h1>添加学生信息</h1>
	<hr>
	<form name="form1" action="sql2.php" method="post">
		<table align="content">
			<tr>
				<td>学生姓名：</td>
				<td><input type="text" name="name"></td>
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
				<td>学生成绩：</td>
				<td><input type="text" name="salary"></td>
			</tr>
			<tr>
				<td><input type="submit" name="button" id="button" value="添加" onclick="return yz(this);" /></td>
				<td><input name="查看学生信息" type="button" value="查看学生信息"  onclick="location.href='sql2.php'" /></td>
			</tr>
	</form>
	</div>
</body>
</html>