

public class DataTypeEx5 { 
            public  static void main(String[] args ){ 
              //long Ÿ���� ����Ÿ��, 8byte�Ҵ�, -2147483648~2147483641������ �Ѵ� //������ �ݵ�� L �Ǵ� l �� �Բ� �������� �����ؾ��մϴ�.
            long num = 1 ; //num = 1L;
          //  num = 2147483648; error
              num = 2147483648L;
              System.out.println(num);
            //  int num2 = 0.5;
              //  num = 0.5;
          //flaotŸ���� �Ǽ�Ÿ��, 4byte�Ҵ�, �����ο� �����η� �ε��Ҽ��� ������ �����
         //   float f = 0.5;  //0.5�� JVM�� 8byte�ε��Ҽ����������� ����
              float f = 0.5F;  //f=0.5f;
      //doubleŸ���� �Ǽ�Ÿ��, 8byte�Ҵ�, �����ο� �����η� �ε��Ҽ��� ������ �����
             double d = 0.5;
              System.out.println(f);          
              System.out.println(d);    
             d = 1.5D; // d= 1.5d;
              System.out.println(d);       
         //2147483648 ���� IEEEǥ������ 2.124783648E9
               d =  2.124783648E9;
             double  d2 =  2124783648L;
              System.out.println(d);
              System.out.println((long)d==(long)d2);
              
}           
}