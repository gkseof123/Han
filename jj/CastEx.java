

public class CastEx { 
            public  static void main(String[] args ){ 
          int num = 4 ; 
         double d = num; //promotion
        // int num2 = d;
//ūŸ���� ����Ÿ�Կ� �Ҵ��Ҷ� �ڵ� ����ȯ�� �Ͼ�� �ʵǹǷ� , ������� //����ȯcasting�� �ؾ��մϴ�.
       int num2 = (int) d;
          byte b1 = 65;
          char ch = (char)b1;
          num2 = 0;
          boolean b2 = (boolean)num2;
}           
}