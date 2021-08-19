<?php
	header('Content-Type:text/html;charset=utf-8');//声明服务器返回的内容是text/html,使用utf-8字符集解析
	$a=1;
	echo $a;
	echo "<pre>";
    var_dump($_GET);//PHP超全局（没有范围限制）预定义数组
    echo "<hr>";
    print_r($_POST);
    echo "<hr>";
    var_dump($_REQUEST);//如果GET和POST中有同名数组元素（下标），POST会覆盖GET，这个可以在php.ini中进行配置