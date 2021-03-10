<body>
<form id="form1" name="form1" method="post" action="21.php">
<table align="center">
<tr>
<td>
<p>
<div >学生姓名：
<input type="text" name="xm" id="textfield" />
</div>
</p>
</td>
</tr>
<tr>
<td>
<p >
<label for="textfield2">签到时间：</label>
<input type="text" name="sj" id="textfield2" value="<?php echo date('Y-m-d h:i:s', time());?>"/>
 
</td>
</tr>
<tr>
<td>
<p align="center">
 <input type="submit" name="button" id="button" value="签到" />
 
</p>
</td>
</tr>
</table>
</form>
</body>