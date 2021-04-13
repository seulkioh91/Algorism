import java.util.Scanner;                   //Scanner기능 import

public class Main0408 {
    public static void main(String[] args){
        System.out.print("검색할 데이터를 입력하세요:"); //
        Scanner sc = new Scanner(System.in);
        int search = sc.nextInt();          //정수 integer 받기
        int[] arr = {11,13,17,19,23,29,31};    //int형식의 arr 선언 (어디가서 찾을지)

        Bsearch(arr, search); //Bsearch라는 메소드에 arr, search 던지기 (그걸 구현할 메소드)
    }

    public static void Bsearch(int[] arr, int search){
        int head = 0;
        int tail = arr.length - 1; // (arr의 끝까지)
        int center;

        while (head <= tail){
            center = (head+tail)/2;
            if (search == arr[center]) {
                System.out.println(center+"번째의 요소가 일치");
                break;
            }
            
            if (arr[center] < search) {
                head = center + 1;
            }else{ 
                tail = center -1;
            }
            
        }if (head > tail) {        
            System.out.println("못찾았습니다.");
    }
}
}


