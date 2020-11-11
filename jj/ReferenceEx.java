

public class ReferenceEx { 
            public  static void main(String[] args ){ 
    //ReferenceType은 클래스, 배열, 인터페이스,enum 타입,
   //ReferenceType은 객체
   //객체는 속성(멤버필드)과 기능(메서드)을 가짐
  String s = new String("java");  //객체생성
  System.out.println(s.length());
  Integer integer1 = new Integer("100");
  System.out.println(Integer.toBinaryString(integer1));
  System.out.println(integer1.MAX_VALUE);
}           
}