package Unit7;

import java.util.ArrayList;

public class Unit7 {
    public static void main(String[] args) {
        int[][] arr = {{1, 2, 3},

                {4, 5, 6},

                {7, 8, 9},

                {3, 2, 1}};

        for (int j = 0; j < arr.length; j++)

        {

            for (int k = j; k < arr[0].length; k++)

            {

                System.out.print(arr[j][k] + " ");

            }

            System.out.println();

        }
    }
}