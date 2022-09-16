/*
Car Trip
Description: This program returns a few qualities for a car
Author: Pedro Torres
 */
package com.cartrip;

public class CarTripTester {
    public static void main(String args[]) {
        // Creates object car1, an instance of CarTrip
        CarTrip car1 = new CarTrip(20.0, 40.0, 40.0, 0.5);

        //prints all attributes of the car1 object
        System.out.println("Start Odometer: " + car1.getMyStartOdometer());
        System.out.println("End Odometer: " + car1.getMyEndOdometer());
        System.out.println("Time: " + car1.getMyTime());
        System.out.println("Gallons Used: " + car1.getMyGallonsUsed());
        //prints the final output sentence
        System.out.println("Car 1 drove " + car1.getTripDistance() + " miles. Its speed average was " +
                car1.getAverageSpeed() + ", its gas mileage was " + car1.getGasMileage() +
                ". The total amount spent on gas was " + car1.getTotalGasPrice(2.5));

    }
}
