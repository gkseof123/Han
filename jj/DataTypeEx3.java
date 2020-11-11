

public class DataTypeEx3 { 
            public  static void main(String[] args ){ 
             //1byte 할당 = 8bit 중 왼쪽 비트는 sign 비트 , -2^7~+2^7-1, -128~127
               byte b1 = 127 ;
               //b1 = 128 ;
              //   b1 = (byte)128; //casting, 명시적 형변환 
              System.out.println(b1);
             //2byte 할당, -2^15~2^15-1, -32768~32767
              short s1 = 32767;
            //  s1 = 32768;
                s1 = (short)32768;
              System.out.println(s1);
             //2byte할당, uniconde 지원 (ascii포함)
               char ch1 = 65, ch2 = 97, ch3 = 48 ;
              System.out.println(ch1);
              System.out.println(ch2);
              System.out.println(ch3);
              ch1 = 'B' ;
              ch2 = '\u0043';
              ch3 = '가' ;
              System.out.println(ch1);
              System.out.println(ch2);
              System.out.println(ch3);
}           
}