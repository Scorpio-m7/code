/*
程序运行期间固定不变的量叫常量:
1.字符串常量:"abc","123"
2.整数常量:100,0,-2
3.浮点数常量:5,-3.6,0.0
4.字符常量:'a','1','打'
5.布尔常量: ture,false
6.空常量:null
 */
public class Demo01Const{
	public static void main(String[] args) {
		System.out.println("字");/*字符串常量,可以为空*/
		System.out.println(-3.14);//整数&浮点数常量
		System.out.println('a');//字符常量有且仅有一个字符，不可为空
		System.out.println(true);//布尔常量
	}
}