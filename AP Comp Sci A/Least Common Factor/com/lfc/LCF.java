package com.lfc;
/*
LCF
Description: This program finds the least common factor
Author: Pedro Torres
 */
import java.util.InputMismatchException;
import java.util.Scanner;

public class LCF {
    public static void main(String args[]) {
        boolean termBool = true;
        int term1 = 0;
        int term2 = 0;
        while (termBool) {
            Scanner input = new Scanner(System.in);
            try {
                System.out.print("Enter your first term (number greater than 0): ");
                term1 = input.nextInt();
                termBool = term1 <= 1;
            }
            catch (InputMismatchException lcf){
                System.out.println("Invalid Input");
            }
        }
        System.out.println();

        termBool = true;

        while (termBool) {
            Scanner input = new Scanner(System.in);
            try {
                System.out.print("Enter your second term (number greater than 0): ");
                term2 = input.nextInt();
                termBool = term2 <= 1;
            } catch (InputMismatchException lcf) {
                System.out.println("Invalid Input");
            }
        }
        System.out.println();

        int lcf = 0;
        for (int i = 2;i <= term1; i++)
        {
            if((term1 % i == 0) && (term2 % i == 0))
                lcf = i;
                break;
        }
        if (lcf == 0) {

        }

        boolean prime1 = true;
        for (int i = 2; i <= term1 / 2; ++i) {
            if (term1 % i == 0) {
                prime1 = false;
                break;
            }
        }

        boolean prime2 = true;
        for (int i = 2; i <= term2 / 2; ++i) {
            if (term2 % i == 0) {
                prime2 = false;
                break;
            }
        }

        if (prime1 && prime2) {
            System.out.print("For " + term1 + " and " + term2 + " LCF = " + lcf + ". Both terms are prime.");
        } else if (prime1) {
            System.out.print("For " + term1 + " and " + term2 + " LCF = " + lcf + ". " + term1 + " is prime.");
        } else if (prime2) {
            System.out.print("For " + term1 + " and " + term2 + " LCF = " + lcf + ". " + term2 + " is prime.");
        } else {
            System.out.print("For " + term1 + " and " + term2 + " LCF = " + lcf);
        }

    }
}
