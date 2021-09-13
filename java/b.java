import java.security.MessageDigest; 
import java.util.*;
public class b {
    public b() {
        super();
    }
    public static void main(String[] args){
        String varV2 = "Stra1234";
        String varV1B = a(varV2);
        String varKey = varV2 + varV1B + "yaphetshan";
        System.out.print("KEY = ");
        System.out.print(b(varKey).substring(0,7));
    }
    public static final String a(String arg9) {
        String v0_2;
        int v0 = 0;
        char[] v2 = new char[]{'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'};
        try {
            byte[] v1 = arg9.getBytes();
            MessageDigest v3 = MessageDigest.getInstance("MD5");
            v3.update(v1);
            byte[] v3_1 = v3.digest();
            int v4 = v3_1.length;
            char[] v5 = new char[v4 * 2];
            int v1_1 = 0;
            while(v0 < v4) {
                int v6 = v3_1[v0];
                int v7 = v1_1 + 1;
                v5[v1_1] = v2[v6 >>> 4 & 15];
                v1_1 = v7 + 1;
                v5[v7] = v2[v6 & 15];
                ++v0;
            }
            v0_2 = new String(v5);
        }
        catch(Exception v0_1) {
            v0_2 = null;
        }
        return v0_2;
    }
    public static final String b(String arg9) {
        String v0_2;
        int v0 = 0;
        char[] v2 = new char[]{'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'};
        try {
            byte[] v1 = arg9.getBytes();
            MessageDigest v3 = MessageDigest.getInstance("SHA-1");
            v3.update(v1);
            byte[] v3_1 = v3.digest();
            int v4 = v3_1.length;
            char[] v5 = new char[v4 * 2];
            int v1_1 = 0;
            while(v0 < v4) {
                int v6 = v3_1[v0];
                int v7 = v1_1 + 1;
                v5[v1_1] = v2[v6 >>> 4 & 15];
                v1_1 = v7 + 1;
                v5[v7] = v2[v6 & 15];
                ++v0;
            }
            v0_2 = new String(v5);
        }
        catch(Exception v0_1) {
            v0_2 = null;
        }
        return v0_2;
    }
}