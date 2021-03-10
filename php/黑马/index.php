<html>
	<head><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /></head>
	<body>
		<?php
			#php教程：https://www.bilibili.com/video/BV18x411H7qD?p=96
			/*phpinfo();//php环境*/
			$var1;
			$var2=1;
			echo '<hr/>',$var2,'<br/>';
			unset($var2);//释放空间
			//echo $var2;//无法输出
			//*************************
			$中国='china';//变量可以是中文
			$a='b';
			$b='qwer';
			echo $$a,'<br>';//可变变量
			//*************************
			$q=10;
			$w=$q;//值传递
			$w=5;
			echo $q,'~',$w,'~';
			$w=&$q;//引用传递
			$w=5;
			echo $q,'~',$w,'<br>';
			//*************************
			define('pi', 3.14);//函数定义常量
			const pii=3;//const关键字定义常量
			define('-_-','smile');//常量不需要使用$,变量为$
			echo pi,'~',pii,'~',constant('-_-'),'<br>';//常量访问函数constant
			//*************************
			echo PHP_VERSION,'~',PHP_INT_SIZE,'~',PHP_INT_MAX,/*系统常量*/'~',__DIR__,'~',__FILE__,'~',__LINE__,/*魔术常量,跟着环境变化,用户无法改变*/'<br>';
			//**************************
			$a='abc1.1.1';//字母开头的字符串转换成数值为0
			$b='1.1.1abc';//以数字开头的字符串,取到字符串为止(不会包含两个小数点)
			echo $a+$b,/*自动转换算术+运算,先转换成数值类型(整形和浮点型)然后运算*/'~',(float)$a,'~',(float)$b,'<br/>';//强制转换//不会改变原本数据类型
			//***************************
			var_dump(is_int($a));//判断数据类型
			echo '~',gettype($a),'~',var_dump(settype($b, 'int'))/*这里返回bool(true)表示转换成功*/,'~',gettype($b),'<br/>';//settype函数会改变函数类型
			//***************************
			$a1=110;
			$a2=0b110;
			$a3=0110;
			$a4=0x110;
			echo $a1,'~',$a2,'~',$a3,'~',$a4,'~';
			var_dump(decbin(107));//十进制转换二进制//hexdec十六进制转十进制
			echo "<br>";
			//**************************
			$f1=1.23;//浮点数
			$f2=1.23e10;//1.23*10的10次方
			$f3=PHP_INT_MAX+1;//大于整形的值自动转换成浮点数
			$f4=0.7;
			$f5=2.1/3;//浮点数不精确
			var_dump($f1,'~',$f2,'~',$f3,'~',$f4==$f5);
			echo "<br>";
			//**************************
			$var1='123';
			$var2=123;
			var_dump($var1==$var2,'~',$var1===$var2);#全等于:===
			echo "<br>";
			//**************************
			$a='abc';
			$b='123';
			$c=($b>1)?(100):(0);//if($b>1) return 100 else return 0
			echo $a.$b,/*连接运算符,$a.=$b*/'~',@($a/0)/*错误抑制符@,报错不显示*/,'~',$c,'~',$a-=$b-1,/*$a=$a-($b-1)*/'<br>';
			//**************************
			$x=5;//原码=00000101=反码=补码
			$y=-5;//原码=10000101,反码=11111010,补码=11111011
			echo $x&/*位运算符*/$y,'~',~$y,'~',$y>>2,"<br>";
			/*位运算直接操作补码,运算结果还要转换成原码
			x=5= 00000101
			y=-5=11111011
			x&y= 00000001=1
			*************
			y=-5=11111011
			~y=4=00000100
			*************
			y=-5=11111011
			y>>2=11111110=补码=右移两位,左面补符号位
			反码=11111101=补码-1
			原码=10000010=反码取反=-2*/
			//**************************
			$day=1;
			switch ($day) {
				case '1':
					echo "1";
					//break;//$day匹配一次后,不会判断条件,执行下面的代码直到break
				case '2':
					echo '~',"2";
					break;
				default:
					echo "error";
					break;
			}
			//**************************
			echo "<br>";
			$i=1;
			do {//先循环再判断
				if ($i%2!=1) {
					echo $i,'~';
				}
				$i++;
			} while ($i<= 10);
			//***************************
			echo "<br>";
			$i=1;
			while ($i<= 100) {//先判断再循环
				if ($i%5!=0) {
					$i++;
					continue;//重新跳到循环开始处
				}
			echo $i++,'~';
			}
			//***************************
			echo '<br/>',print('hello~'),'~';//print结构会返回1,()可以变成''
			$a='hello~';
			print_r($a);//类似var_dump,但不会输出数据类型,只输出值
			echo date('Y 年 m 月 d 日 H:i:s'),'~',time(),'~',strtotime('tomorrow');#time()表示从1970年到现在多少秒
			//***************************
			echo "<br/>";
			$res=include './index1.php';//包含文件index1.php,遇到一次执行一次(可以多次执行),include不影响下面的代码执行,require如果找不到文件则不执行下面的代码
			include_once 'D:/php/PHPTutorial/WWW/index1.php';//如果已经包含则不会执行
			echo $a,'~',PI,'~',$res;
			//***************************
			echo "<br/>";
			$num0=10;
			echo add($num0,10);#先编译后执行,在内存中能找到对应函数,就可以执行
			function add($arg1=0,$arg2=0){#定义函数,实参个数可以多于形参
				return $arg1+$arg2;#如果没有return,则返回null
				echo $arg1;#return直接结束程序,后面内容不执行
			}
			//***************************
			echo "<br/>";
			function display($a,&$b){#引用传值,这里取的是$b的地址,所以函数会改变传入的值
				$a=$a*$a;
				$b=$b*$b;
				echo $a,'~',$b,'~';
			}
			$a=10;
			$b=5;
			display($a,$b);
			echo $a,'~',$b;#b的值会因为函数dispaly()改变
			//***************************
			echo "<br/>";
			$global = 'global area';//被系统纳入超全局变量中：$GLOBALS['global']=global area;
			function display1(){
				//echo $global;//函数内部不能访问全局变量
				echo $GLOBALS['global'],'~';//以数组方式访问超全局变量
				global $local;
				$local=1;
				static $count=1;//静态变量,在系统编译的时候就会对static这行进行初始化,调用时自动跳过这行
				echo $local++,'~',$count++,"~";
			}
			$func='display1';
			display1();
			display1();
			$func();#可变函数
			echo $local;
			//***************************
			echo "<br>";
			function sys_function($arg1,$arg2){
				$arg2=$arg2+10;
				return $arg1($arg2);#user_function(20)
			}
			function user_function($num){#这个函数叫回调函数
				return $num*$num*$num*$num;
			}
			echo sys_function('user_function',10);#将函数名传给sys_function函数,称为回调
			//***************************
			echo "<br>";
			function displaya(){#闭包函数
				$name=__FUNCTION__;//返回当前函数名
				$innerfunction=function() use($name){#定义匿名函数
					echo $name;#use将外部变量保留给内部使用
				};
				return $innerfunction;#返回内部匿名函数
			}
			$closure=displaya();#局部变量name在这里运行结束之后并没有被释放
			$closure();#name在外部调用内部匿名函数时可以被调用
			//***************************
			function test($a,$b){
				echo '<br>',func_get_arg(1),'~';//返回第二个传入的参数
				var_dump(func_get_args());//数组形式存储所有传入的参数
				echo '~',func_num_args();//传入参数的个数
			}
			function_exists('test') && test(1,'2',3,4);//test函数存在前部分为1,执行后面的函数赋值操作
			//***************************
			//错误类型
			//系统错误：E_PARSE:编译错误,代码不执行,E_ERROR:fatal error,致命错误,代码不能执行,E_WARNING:warning,警告错误,不影响代码执行,E_NOTICE:notice,通知错误不影响代码执行
			//用户错误:E_USER_ERROR,E_USER_WARNING,E_USER_NOTICE,用户使用自定义错误时用的代号
			//E_ALL：代表所有错误
			//排除notice错误:E_ALL&~E_NOTICE,警告和通知:E_WARNING|E_NOTICE
			header('Content-Type:text/html;charset=utf-8');//让浏览器按指定字符集解析
			$a=100;
			$b=0;
			if ($b==0) {
				trigger_error('除数不能为零');//默认notice错误,会继续执行代码
				#trigger_error('严重错误',E_USER_ERROR);//报error错误,后面代码不执行
				#echo $a/$b;
			}
			//***************************
			function my_error($errno,$errstr,$errfile,$errline){//自定义错误处理机制
				if (!(error_reporting()&$errno)) {//error_reporting没有参数代表获取当前错误信息
					return false;//排除系统就要排除的错误
				}
				switch ($errno) {
					case E_ERROR:
					case E_USER_ERROR:
						echo 'fatal error in file'.$errfile.'on line'.$errline.'error info:'.$errstr;
						break;
					case E_WARNING:
					case E_USER_WARNING:
						echo 'warning in file'.$errfile.'on line'.$errline.'error info:'.$errstr;
						break;
					case E_NOTICE:
					case E_USER_NOTICE:
						echo 'notice in file'.$errfile.'on line'.$errline.'error info:'.$errstr;
						break;
				}
				return true;
			}
			set_error_handler('my_error');
			echo $zxcvb;
			//***************************
			$a='hello你好';#中文占3字节
			$str1='abc\r\ndef\t\'\"\$fg';#转义符号,\r:回到当前行的首位置,\n:新一行,\t:四个空格,\$:输出$,\':输出',\":输出"
			$str2="abc\r\ndef\t\'\"\$fg";#单引号中只识别\',双引号中除了\'都识别
			$str3="abc$a fg";#双引号可以解析变量
			$str4="abc{$a}fg";#{}:变量标识符
			$str5=<<<EOD
				<script>
					alert('$a');
				</script>
EOD;
//heredoc结构,类似双引号
			$str6=<<<'EOD'
				APPLE
					banana
EOD;
//nowdoc结构,类似单引号
			echo '<br>',$str1,'~',$str2,'~',$str3,'~',$str4,/*$str5,*/'~',$str6,'~',strlen($a)/*按ASCII码统计*/,'~',mb_strlen($a,'utf-8')/*按utf-8统计字数*/;
			//***************************
			echo "<br>";
			$str='bacDE aF g  ';
			echo trim($str)/*除去两边空格*/,'~',substr($str,2,3)/*从2位置开始截取3个字符*/,'~',strstr($str,'c')/*从c字符开始到最后*/,'~',strtoupper($str)/*全部大写*/,'~',ucfirst($str)/*首字母大写*/,'~',strpos($str,'a')/*首次出现a的位置*/,'~',strrpos($str,'a')/*最后一次出现a的位置*/,'~',str_replace('a','x',$str)/*把str中的a替换成x*/,'~',sprintf("%d, and ,%s",$num0,$a)/*格式化输出*/,'~',str_repeat($a,3)/*重复输出3次$a*/,'~',str_shuffle($str)/*随机打乱*/,'<br>';
			//***************************
			$arr1=array(array('zh',0),array('ok',4));#函数定义数组
			$i=0;
			foreach ($arr1 as $key => $value) {#foreach循环
				foreach ($arr1[$i] as $k => $v) {#$k可以省略
					echo $k,'->',$v,'~';#输出二维数组
				}
				echo $key,'->',var_dump($value),'~';#输出一维数组
				$i=$i+1;
			}
			$arr3[] = 1;#$arr3[0]=1
			$arr3[true] = true;#特殊下标转换:$arr3[1]=ture
			$arr3['key'] = 'key';#字符也可以作为数组下标
			//***************************
			echo "<br>";
			$arr2 = array(1,'name' =>'TOM' ,3,'age' =>30);
			while (list($key,$value)=each($arr2)) {#list从数组中取得元素值(批量为变量赋值:值来源于数组),$key=$arr2[0],$value=$arr2[1]
				/*each函数能从数组中获取下标和值,然后下移数组指针
				0下标->元素下标
				1下标->元素的值
				key下标->元素下标
				value下标->元素的值*/
				echo $key.'->'.$value,'~';
			}
			//***************************
			echo "<br>";
			$arr4 = array(3,1,5,2,10);
			sort($arr4);#顺序排序,下标重排
			#asort($arr4);#顺序排序,下标保留
			#krsort($arr4);#逆序排序,按照键名
			#shuffle($arr4);#打乱数组元素,下标重排
			print_r($arr4);#都是更改原数组
			echo '~',next($arr4)/*指针下移,取得下一个元素的值*/,'~',current($arr4)/*获取当前指针的值*/,'~',key($arr4)/*获取当前指针的下标*/,'~',prev($arr4)/*指针上移,取得上一个元素的值*/,'~',end($arr4)/*重置指针,将数组指针回到末尾*/,'~',reset($arr4),'~';#重置指针,将数组指针回到首位
			array_pop($arr4);#从数组尾取出元素
			array_push($arr4,9);#从数组尾加入元素
			array_unshift($arr4,8);#从数组头加入元素
			array_reverse($arr4);#数组元素反转
			in_array(8,$arr4);#判断元素是否在数组中
			array_keys($arr4);#获取所有下标,返回数组
			array_values($arr4);#获取所有值,返回数组
			print_r($arr4);
			//***************************
			function my_recursive($des){#斐波那契数列
				if ($des==1||$des==2) {#递推思想
					return 1;
				}
				$f[1]=$f[2]=1;
				for ($i=3; $i<=$des ; $i++) { 
					$f[$i]=$f[$i-1]+$f[$i-2];
				}
				return $f[$des];
			}
			function recursion($n){#递归思想
				if ($n==1||$n==2) {#递归出口
					return 1;
				}
				return recursion($n-1)+recursion($n-2);#递归点
			}
			echo '<br>',my_recursive(15),'~',recursion(14);
			//***************************
			for ($i=0; $i<count($arr4); $i++) { #冒泡排序 
			 	for ($j=0; $j <count($arr4)-1-$i ; $j++) { 
			 		if ($arr4[$j]>$arr4[$j+1]) {
			 			$temp=$arr4[$j];
			 			$arr4[$j]=$arr4[$j+1];
			 			$arr4[$j+1]=$temp;
			 		}
			 	}
			 }
			 echo "<br>";
			 print_r($arr4);
			//***************************
			$arr5 = array(5,9,8,4,2,6,1);
			for ($i=0,$len=count($arr5); $i <$len ; $i++) { #选择排序
				$min=$i;
				for ($j=$i+1; $j <$len ; $j++) { 
					if ($arr5[$j]<$arr5[$min]) {
						$min=$j;
					}
				}
				if ($min!=$i) {
					$temp=$arr5[$i];
					$arr5[$i]=$arr5[$min];
					$arr5[$min]=$temp;
				}
			}
			echo "<br>";
			print_r($arr5);
			//***************************
			$arr6 = array(5,7,8,4,2,6,1);
			for ($i=1,$len=count($arr6);$i<$len ; $i++) {#插入排序 
				$temp=$arr6[$i];#取出当前要插入的元素的值
				$change=false;
				for ($j=$i-1; $j >=0 ; $j--) { 
					if ($arr6[$j]>$temp) {
						$arr6[$j+1]=$arr6[$j];
						$change=true;
					}else{
						break;
					}
				}
				if ($change) {
					$arr6[$j+1]=$temp;#数据移动
				}
			}
			echo "<br>";
			print_r($arr6);
			//***************************
			$arr7 = array(5,11,8,4,2,6,1);
			function quick_sort($arr7){#快速排序
				$len=count($arr7);
				if($len<=1) return $arr7;#递归出口
				$left=$right = array();#取出一个元素,将剩余数组分散到两个不同的数组中
				for ($i=1; $i <$len ; $i++) { 
					if ($arr7[$i]<$arr7[0]) {
						$left[]=$arr7[$i];#小的放入left

					}else{
						$right[]=$arr7[$i]; #大的放入right
					}
				}
				$left=quick_sort($left);
				$right=quick_sort($right);#递归点
				return array_merge($left,(array)$arr7[0],$right);#合并数组
			}
			echo "<br>";
			print_r(quick_sort($arr7));
			//***************************
			$arr8 = array(5,9,8,4,5,3,12);
			function merge_sort($arr8){#归并排序
				$len=count($arr8);
				if ($len<=1) {#递归出口
					return $arr8;
				}
				$middle=floor($len/2);#拆分
				$left= array_slice($arr8,0,$middle);#拆分函数
				$right=array_slice($arr8,$middle);
				$left=merge_sort($left);#递归点
				$right=merge_sort($right);
				$m = array();#二路归并
				while (count($left) && count($right)) {#left或right还有元素则循环
					$m[]=$left[0]<$right[0] ? array_shift($left) : array_shift($right);#如果左数组小就放入左数组的值，如果右数组小就放入有数组的值
				}
				return array_merge($m,$left,$right);#合并数组
			}
			echo "<br>";
			print_r(merge_sort($arr8));
			//***************************
			$res=12;
			function check_break($arr,$res){#二分查找算法
				$right=count($arr);#数组边界
				$left=0;
				while ( $left<= $right) {#循环匹配
					$middle=floor(($right+$left)/2);#中间位置
					if ($arr[$middle]==$res) {#匹配数据
						return $middle+1;
					}
					if ($arr[$middle]<$res) {#值在右边
						$left=$middle+1;
					}else {#值在左边
						$right=$middle-1;
					}
				}
				return false;
			}
			echo "<br>",$res."在".check_break($arr8,$res);
			//***************************
		?>
		<!-- ***********************************日期选择器 -->
		<form name="f1" id="f1" action="" method="post">
			<select name="s1" id="s1">
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
			</select>日
		</form>
		<!-- ***********************************输出学生信息 -->
		<table border=1>
			<?php $arr=[
				['1' => "学号",'2'=>"姓名",'3'=>"性别",'4'=>"年龄",'5'=>"出生日期" ,'6'=>"联系方式",'7'=>"家庭住址"],
				['1' => 2019001, '2'=>"赵构",'3'=>"男",'4'=>20,'5'=>"1984.10.2",'6'=>1561646546,'7'=>"呼和浩特"],
				['1' => 2019002,'2'=>"赵娜",'3'=>"女",'4'=>21,'5'=>"1985.10.2",'6'=>1561588546,'7'=>"呼和浩特"],
				['1' => 2019004,'2'=>"大白菜",'3'=>"男",'4'=>23,'5'=>"1987.10.2",'6'=>1786178546,'7'=>"呼和浩特"],
				['1' => 2019005,'2'=>"小白菜",'3'=>"女",'4'=>24,'5'=>"1988.10.2",'6'=>1567888546,'7'=>"呼和浩特"]
				];?>
				<?php  foreach($arr as $key=>$value): ?>
				<tr>
					<td><?=$value['1']?></td>
					<td><?=$value['2']?></td>
					<td><?=$value['3']?></td>
					<td><?=$value['4']?></td>
					<td><?=$value['5']?></td>
					<td><?=$value['6']?></td>
					<td><?=$value['7']?></td>
				</tr>
				<?php endforeach;?>
		</table>
	</body>
</html>
