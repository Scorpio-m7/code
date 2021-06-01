/*
当数据类型不一样时，将会发生数据类型转换。

自动类型转换（隐式）
	1. 特点：代码不需要进行特殊处理，自动完成。
	2. 规则：数据范围从小到大。

强制类型转换（显式）
	1. 特点：代码需要进行特殊的格式处理，不能自动完成。
	2. 格式：范围小的类型 范围小的变量名 = (范围小的类型) 原本范围大的数据;

*/
public class Demo01DataType {
	public static void main(String[] args) {
		float num3 = 30L;
		System.out.println(num3);//long-->float,范围是float更大一些,发生了自动类型转换
		int num = (int) 100L;// long强制转换成为int类型
		System.out.println(num);
	}
}
