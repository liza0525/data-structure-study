import java.util.ArrayList;

public class ListPractice {
    public static void main(String[] args) {
        // 자료구조 선언
        ArrayList<Integer> intList = new ArrayList<>();
        ArrayList<String> strList = new ArrayList<>();

        // 리스트 요소 추가
        intList.add(1);
        intList.add(2);
        intList.add(3);
        strList.add("one");
        strList.add("three");
        strList.add(1, "two"); // 해당 순서에 넣고 싶은 데이터를 삽입할 수 있다.

        // 리스트 요소 검색
        // 1. get : index 번호로 데이터 탐색
        System.out.println(intList.get(1));
        System.out.println(strList.get(2));

        // 2. contains : 해당 자료가 있는지 검색, return 값은 boolean type
        System.out.println(strList.contains("three")); // true
        System.out.println(strList.contains("four")); // false

        // 리스트 요소 삭제
        intList.remove(1);
    }
}