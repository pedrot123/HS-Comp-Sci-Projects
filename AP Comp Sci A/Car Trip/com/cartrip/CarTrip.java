/*
Car Trip
Description: This program returns a few qualities for a car
Author: Pedro Torres
 */
package com.cartrip;
public class CarTrip {

        //Instance Variables
        private double myStartOdometer;
        private double myEndOdometer;
        private double myTime;
        private double myGallonsUsed;

        //Constructor
        public CarTrip(double sOdo, double eOdo, double time, double gallons) {
                myStartOdometer = sOdo;
                myEndOdometer = eOdo;
                myTime = time;
                myGallonsUsed = gallons;
        }

        //Getter Methods
        double getMyStartOdometer() {
                return myStartOdometer;
        }

        double getMyEndOdometer() {
                return myEndOdometer;
        }

        double getMyTime() {
                return myTime;
        }

        double getMyGallonsUsed() {
                return myGallonsUsed;
        }

        //Setter Methods
        void setMyStartOdometer(double newStart) {
                myStartOdometer = newStart;
        }

        void setMyEndOdometer(double newEnd) {
                myEndOdometer = newEnd;
        }

        void setMyTime(double newTime) {
                myTime = newTime;
        }

        void setMyGallonsUsed(double newGal) {
                myGallonsUsed = newGal;
        }

        //Calculation Methods
        double getTripDistance() {
                double tripDistance = myEndOdometer - myStartOdometer;
                return tripDistance;
        }

        double getAverageSpeed() {
                double averageSpeed = getTripDistance() / myTime;
                return averageSpeed;

        }

        double getGasMileage() {
                double gasMileage = getTripDistance() / myGallonsUsed;
                return gasMileage;
        }

        double getTotalGasPrice(double pricePerGallon) {
                double totalGasPrice = pricePerGallon * myGallonsUsed;
                return totalGasPrice;
        }
}