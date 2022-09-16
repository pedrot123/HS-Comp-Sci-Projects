package Unit9;

import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {


        ArrayList<Book> myLibrary = new ArrayList<Book>();
        Book book1 = new Book("Frankenstein", "Mary Shelley");
        Book book2 = new PictureBook("The Wonderful Wizard of Oz", "L. Frank Baum", "W.W. Denslow");
        myLibrary.add(book1);
        myLibrary.add(book2);
        BookListing listing2 = new BookListing(book2, 12.99);
        listing2.printDescription();

        BookListing listing1 = new BookListing(book1, 10.99);
        listing1.printDescription();
    }
}