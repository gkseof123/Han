

public class DataTypeEx2 { 
            public  static void main(String[] args ){ 
                boolean b1 = true, b2= false;
                boolean b3 = (boolean)0; //b3 =1
               /*논리 자료형과 정수형의 호환 불가, promotion, casting 안됨*/
             
              System.out.println(b1);
              System.out.println(b2);
}            
}