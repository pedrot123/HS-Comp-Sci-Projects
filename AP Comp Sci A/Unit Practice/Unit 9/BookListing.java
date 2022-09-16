package Unit9;

import java.util.ArrayList;

public class BookListing {
    private double price;
    Book bookInfo;

    public BookListing(Book b, double p) {
        bookInfo = b;
        price = p;
    }

    public void printDescription() {
        bookInfo.printBookInfo();
        System.out.println(", $" + price);
    }
}
