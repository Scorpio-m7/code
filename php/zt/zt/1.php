<body bgcolor="#FFFFFF" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0">
<!-- Save for Web Slices (2.psd) -->
<table id="__01" width="1000" height="625" border="0" cellpadding="0" cellspacing="0">
	<tr>
		<td colspan="3">
			<img src="images/2_01.gif" width="1000" height="259" alt=""></td>
	</tr>
	<tr>
		<td rowspan="2">
			<img src="images/2_02.gif" width="275" height="366" alt=""></td>
		<td><table width="406" height="238" background="images/2_03.gif" border="0" cellspacing="0" cellpadding="0">
		  <tr>
		    <td> <script type="text/javascript">
     function chayan(form){
           if(form1.yhm.value==''){
              alert('用户名不能为空');
              form1.yhm.focus();

              return false;
           }
           if(form1.mm.value==''){
               alert('密码不能为空');
               form1.mm.focus();

               return false;
            }
</script>


<form name="form1"action="2.php" method="post">
<table align="center">
<tr><td>用户名</td><td><input type="text" name="yhm"></td></tr>
<tr><td>密码</td><td><input type="password" name="mm"></td></tr>
<tr><td>验证码</td><td><input type="text" name="yan"></td>

<td><font>
<?php

$yzm=rand(0,9).rand(0,9).rand(0,9).rand(0,9);
echo $yzm;
session_start();
$_SESSION['yzmnew']=$yzm;
?></font>
</td>
</tr>
</table>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
 &nbsp;&nbsp;&nbsp;
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
 <input type="submit" value="提交" onClick="return chayan(this);" />
</form></td>
	      </tr>
	    </table></td>
		<td rowspan="2">
			<img src="images/2_04.gif" width="319" height="366" alt=""></td>
	</tr>
	<tr>
		<td>
			<img src="images/2_05.gif" width="406" height="128" alt=""></td>
	</tr>
</table>
<!-- End Save for Web Slices -->
</body>