public class ArrayPractice {
    public static void main(String[] args) {
        // 자료구조 선언
        int[] intArray = {1, 2, 3, 4, 5};
        String[] strArray = {"one", "two", "three"};

        // 배열 요소 검색
        System.out.println(intArray[0]);
        System.out.println(strArray[1]);

        // 배열은 값을 초기화 하거나 변경만 가능(인덱스로 접근하면 된다.)
        // 요소의 추가나 삭제는 불가(길이가 불변)
    }
}