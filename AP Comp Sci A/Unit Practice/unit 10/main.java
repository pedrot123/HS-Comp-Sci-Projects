package unit10;

import java.util.ArrayList;

public class main {
    public static int surprise(int b)
    {
        if ((b % 2) == 0)
        {
            if (b < 10)
                return b;
            else
                return ((b % 10) + surprise(b / 10));
        }
        else
        {
            if (b < 10)
                return 0;
            else
                return surprise(b / 10);
        }
    }

    public static void main(String[] args) {
        System.out.println(surprise(146781) == 0);
        System.out.println(surprise(7754) == 4);
        System.out.println(surprise(58216) == 16);



    }
}