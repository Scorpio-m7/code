/*
当数据类型不一样时，将会发生数据类型转换。

自动类型转换（隐式）
	1. 特点：代码不需要进行特殊处理，自动完成。
	2. 规则：数据范围从小到大。

强制类型转换（显式）
	1. 特点：代码需要进行特殊的格式处理，不能自动完成。
	2. 格式：范围小的类型 范围小的变量名 = (范围小的类型) 原本范围大的数据;
	注意事项：
	1. 强制类型转换一般不推荐使用，因为有可能发生精度损失、数据溢出。
	2. byte/short/char这三种类型都可以发生数学运算，例如加法“+”.
	3. byte/short/char这三种类型在运算的时候，都会被首先提升成为int类型，然后再计算。
	4. boolean类型不能发生数据类型转换
*/
public class Demo01DataType {
	public static void main(String[] args) {
		float num = 30L;//long-->float，范围是float更大一些，发生了自动类型转换
		System.out.println(num);
		int num1 = (int) 100L;// long --> int，强制类型转换
		System.out.println(num1);
		int num2 = (int) 6000000000L;//long --> int，数据溢出
		System.out.println(num2); // 1705032704
		int num3 = (int) 3.99;//double --> int，精度损失
		System.out.println(num3); // 3
		char zifu1 = 'A'; // 字符型变量，ASCII码：65
		System.out.println(zifu1 + 1); // 66，将字符转换成ASCII码运算
		byte num4 = 40;
		byte num5=50;//byte/short/char这三种类型在运算的时候，都会被首先提升成为int类型，然后再计算。
		int result1 = num4 + num5;// byte + byte --> int + int --> int，使用int接收
		System.out.println(result1); // 90
		short num6 = 60;// byte + short --> (short)(int + int) --> short
		short result2 = (short) (num4 + num6);// int强制转换为short：注意必须保证逻辑上真实大小本来就没有超过short范围，否则会发生数据溢出
		System.out.println(result2); // 100
	}
}