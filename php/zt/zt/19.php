<?php
    if ($_FILES["file"]["error"] > 0) {
        echo "����" . $_FILES["file"]["error"] . "<br/>";
    } else {
        echo "�ļ��ϴ�����:" . $_FILES["file"]["name"] . "<br/>";
        echo "�ļ��ϴ�����:" . $_FILES["file"]["type"] . "<br/>";
        echo "�ļ��ϴ���С:" . $_FILES["file"]["size"] . "<br/>";
        echo "�ļ��ϴ�λ��:" . $_FILES["file"]["tmp_name"] . "<br/>";
        if (file_exists("upload/" . $_FILES["file"]["name"])) {
            echo $_FILES["file"]["name"] . "�ļ��Ѿ�����";
        } else {
            
            move_uploaded_file($_FILES["file"]["tmp_name"], "upload/" . $_FILES["file"]["name"]);
            echo "�ļ��洢��" . "upload/" . $_FILES["file"]["name"];
        }
    }
?>
