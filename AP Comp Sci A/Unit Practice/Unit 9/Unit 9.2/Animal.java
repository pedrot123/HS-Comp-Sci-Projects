package Unit92;

public class Animal {
    private String animalType;
    private String species;
    private String name;

    public Animal(String a, String s, String n) {
        animalType = a;
        species = s;
        name = n;
    }

    public String toString() {
        return name + " the " + species + " is a " + animalType;
    }

}
