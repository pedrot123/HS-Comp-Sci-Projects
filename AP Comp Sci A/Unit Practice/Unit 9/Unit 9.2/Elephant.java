package Unit92;

public class Elephant extends Herbivore{
    private double tuskLength;
    public Elephant(String n, Double t) {
        super("elephant", n);
        tuskLength = t;
    }

    public String toString() {
        return super.toString() + " with tusks " + tuskLength + " meters long";
    }
}
