/*
数据类型 变量名称; // 创建变量
变量名称 = 数据值; // 将右边的数据值赋值给左边的变量

数据类型 变量名称 = 数据值; // 在创建变量的同时,立刻放入指定的数据值

1. 对于float和long类型来说，字母后缀F和L不要丢掉。
2. 如果使用byte或者short类型的变量，那么右侧的数据值不能超过左侧类型的范围。
3. 变量使用不能超过作用域的范围。
【作用域】：从定义变量的一行开始，一直到直接所属的大括号结束为止。
*/
public class Demo02Variable {
	public static void main(String[] args) {
		int num1;//定义整型变量
		num1 = 10;//向变量存入数据
		System.out.println(num1); //显示变量的内容
		num1 = 20;// 改变变量当中本来的数字
		System.out.println(num1); // 20
		int num2 = 25;// 一步到位的格式定义变量
		System.out.println(num2); // 25
		byte num3 = 30; //定义字节型变量,右侧数值的范围不能超过左侧数据类型的取值范围
		System.out.println(num3); // byte num4 = 400; 右侧超出了byte数据范围
		short num5 = 50;//定义短整型变量
		System.out.println(num5); // 50
		long num6 = 3000000000L;//定义长整型变量
		System.out.println(num6); // 3000000000
		float num7 = 2.5F;//定义单精度浮点型变量
		System.out.println(num7); // 2.5
		{
			double num8 = 1.2;//定义双精度浮点型变量
			System.out.println(num8); // 1.2
		}
		// System.out.println(num8); // 超出作用域，变量不能再使用
		char zifu1 = '中';//定义字符型变量
		System.out.println(zifu1); // 中
		boolean var1=true,var2=var1;//定义两个布尔型变量，并且各自赋值，将右侧变量var1里面的true值,向左交给var2变量进行存储
		System.out.println(var1); 
		System.out.println(var2); // true
	}
}