public class HelloGoodbye {
    public static void main(String[] args) {

        if (args.length != 2) {
            System.out.println("Please provide exactly two names as command line arguments.");
            return;
        }

        String firstPerson = args[0];
        String secondPerson = args[1];

        System.out.println("Hello " + firstPerson + " and " + secondPerson + ".");
        System.out.println("Goodbye " + secondPerson + " and " + firstPerson + ".");
    }
}
