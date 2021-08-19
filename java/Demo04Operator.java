/*
运算符：进行特定操作的符号。例如：+
表达式：用运算符连起来的式子叫做表达式。例如：a + b

一旦运算当中有不同类型的数据，会发生数据类型转换。
*/
public class Demo04Operator {
	public static void main(String[] args) {
		int a = 3;
		int b = 10;
        System.out.println(b + 2.5);//12.5，int + double --> double + double --> double
		System.out.println(a - b); //-7，-首先计算得到表达式的结果，然后再打印输出这个结果。
		System.out.println(a * 10); //30
		System.out.println( b / a); //3，对于一个整数的表达式来说，除法用的是整除，结果只看商，不看余数。
		System.out.println(b % a); //1，只有对于整数的除法来说，取模运算符才有余数的意义。
		String str1="Hello";//3. 对于字符串String来说，加号代表字符串连接操作。任何数据类型和字符串进行连接的时候，结果都会变成字符串
		System.out.println(str1+"World"+20+(20+30));//通过添加()改变运算优先级
	}
}