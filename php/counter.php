<!DOCTYPE html>
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<title>访客计数器</title>
</head>
<body>
<?php 
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
	echo "第".$sum."浏览者";
?>
</body>
</html>