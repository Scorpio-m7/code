import java.io.*;

public class JavaSerializeExample{
    public static void main(String[] args) throws Exception{
        //定义myObj对象
        MyObject myobj = new MyObject();
        myobj.name="test";
        //创建一个包含对象进行序列化信息的object.ser数据文件
        ObjectOutputStream os = new ObjectOutputStream(new FileOutputStream("name:" + "object.ser"));
        //writeObject()方法将myObject对象写入object.ser文件
        os.writeObject(myobj);
        os.close();
        //从object.ser文件中反序列化对象
        ObjectInputStream ois = new ObjectInputStream(new FileInputStream("name:" + "object.ser"));
        //通过readObject()方法读取对象
        MyObject objectFromDisk=(MyObject)ois.readObject();
        System.out.println(objectFromDisk.name);
        ois.close();
    }
}
class MyObject implements Serializable{
    public String name;
    //重写readObject()方法
    private void readObject(ObjectInputStream in) throws IOException, ClassNotFoundException {
        in.defaultReadObject();
        Runtime.getRuntime().exec("calc.exe");
    }
}