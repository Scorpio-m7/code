<?php
    if ($_FILES["file"]["error"] > 0) {
        echo "错误：" . $_FILES["file"]["error"] . "<br/>";
    } else {
        echo "文件上传名称:" . $_FILES["file"]["name"] . "<br/>";
        echo "文件上传类型:" . $_FILES["file"]["type"] . "<br/>";
        echo "文件上传大小:" . $_FILES["file"]["size"] . "<br/>";
        echo "文件上传位置:" . $_FILES["file"]["tmp_name"] . "<br/>";
        if (file_exists("upload/" . $_FILES["file"]["name"])) {
            echo $_FILES["file"]["name"] . "文件已经存在";
        } else {
            
            move_uploaded_file($_FILES["file"]["tmp_name"], "upload/" . $_FILES["file"]["name"]);
            echo "文件存储在" . "upload/" . $_FILES["file"]["name"];
        }
    }
?>
