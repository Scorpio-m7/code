<!DOCTYPE html>
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
</head>
<body>
	<?php 
		$allowed = array("gif","jpeg","jpg","png");
		for ($i=0; $i < 3; $i++) {
			$temp = explode(".", $_FILES["file"]["name"][$i]);
			echo $_FILES["file"]["name"][$i];
			$extension=end($temp);
			if ((($_FILES["file"]["type"][$i] == "image/gif") || ($_FILES["file"]["type"][$i] == "image/jpeg") || ($_FILES["file"]["type"][$i] == "image/jpg") || ($_FILES["file"]["type"][$i] == "image/pjpeg") || ($_FILES["file"]["type"][$i] == "image/x-png") || ($_FILES["file"]["type"][$i] == "image/png")) && ($_FILES["file"]["size"][$i] < 204800) && in_array($extension, $allowed)) 
			{
				 
		    	if ($_FILES["file"]["error"][$i] > 0) {
		    		switch ($_FILES["file"]["error"][$i]) {
		                case 1: // UPLOAD_ERR_INI_SIZE
		                    $mes = "超过配置文件中上传文件的大小";
		                    break;
		                case 2: // UPLOAD_ERR_FORM_SIZE
		                    $mes = "超过表单中配置文件的大小";
		                    break;
		                case 3: // UPLOAD_ERR_PARTIAL
		                    $mes = "文件被部分上传";
		                    break;
		                case 4: // UPLOAD_ERR_NO_FILE
		                    $mes = "没有文件被上传";
		                    break;
		                case 6: // UPLOAD_ERR_NO_TMP_DIR
		                    $mes = "没有找到临事文件目录";
		                    break;
		                case 7: // UPLOAD_ERR_CANT_WRITE
		                    $mes = "文件不可写";
		                    break;
		                case 8: // UPLOAD_ERR_EXTENSION
		                    $mes = "php扩展程序中断了上传程序";
		                    break;
		            }
		        	echo $mes."<br/>";
		    	} else {
		        echo "文件上传名称:" . $_FILES["file"]["name"][$i] . "<br/>";
		        echo "文件上传类型:" . $_FILES["file"]["type"][$i] . "<br/>";
		        echo "文件上传大小:" . $_FILES["file"]["size"][$i] . "<br/>";
		        echo "文件上传位置:" . $_FILES["file"]["tmp_name"][$i] . "<br/>";
		        if (file_exists("upload/" . $_FILES["file"]["name"][$i])) {
		            echo $_FILES["file"]["name"][$i] . "文件已经存在";
		        } else {
		            
		            move_uploaded_file($_FILES["file"]["tmp_name"][$i], "upload/" . $_FILES["file"]["name"][$i]);
		            echo "文件存储在" . "upload/" . $_FILES["file"]["name"][$i];
		        }
		    }
			} else {
			    echo "文件为非法格式 ";
			}
	}
?>
</body>
</html>	