import java.util.Random;

public class Arr {
    public int[] CreateArr(int a) {
        Random ran = new Random();
        int arr[] = new int[a];
        for (int i = 0; i < arr.length; i++) {
            arr[i] = ran.nextInt(100);
            System.out.println(arr[i]);
        }
        return arr;
    }

    public void SoftArr(int arr[]) {


        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr.length - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    int t = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = t;
                }
            }
        }

        System.out.println("after sort array");
        for (int i = 0; i < arr.length; i++) {
            System.out.println(arr[i]);
        }
    }
}



//        int min = 0;
//        int imin=0;
//
//        for (int i = 0; i < arr.length; i++) {
//            min = arr[i];
//            imin = i;
//            for (int j = i + 1; j < arr.length; j++) {
//                if (arr[j] < min) {
//                    min = arr[j];
//                    imin = j;
//                }
//            }
//            if (i != imin) {
//                int temp = arr[i];
//                arr[i] = arr[imin];
//                arr[imin] = temp;
//            }
//
//
//        }
//        System.out.println("~~~~~~~~~~~~~");
//        System.out.println(min);
//        System.out.println(imin);
//    }
