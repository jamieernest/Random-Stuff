import java.util.Date;
import java.util.Calendar;
import java.util.GregorianCalendar;
import java.text.SimpleDateFormat;
import java.text.DateFormat;
import java.text.ParseException;
import java.util.TimeZone;
import java.util.Locale;
import java.util.Scanner;
import java.time.ZoneId;
import java.time.LocalDate;

class preRelease{
    public static void main(String[] args) {
        System.out.println("What is your first name?");
        String firstName = System.console().readLine();
        System.out.println("What is your last name?");
        String lastName = System.console().readLine();
        System.out.println("Would you like to volunteer? [Y/n]");
        String volunteer = System.console().readLine();
        if(volunteer.startsWith("y")){
            System.out.println("Where would you like to volunteer? [(p)ier entrance gate, (g)ift shop, painting and (d)ecorating, (c)ancel]");
            String volunteerLocation = System.console().readLine();
            while(!volunteerLocation.startsWith("p") && !volunteerLocation.startsWith("g") && !volunteerLocation.startsWith("d") && !volunteerLocation.startsWith("c")){
                System.out.println("Please enter a valid location. Where would you like to volunteer? [(p)ier entrance gate, (g)ift shop, painting and (d)ecorating]");
                volunteerLocation = System.console().readLine();
            }
            if(volunteerLocation.equals("c")){
                System.out.println("Cancelled.");
            }
        }
        System.out.println("When did you join? [YYYY-MM-DD]");
        String joinDate = System.console().readLine();
        Date date = new Date();
        LocalDate localDate = date.toInstant().atZone(ZoneId.systemDefault()).toLocalDate();
        joinDate = joinDate.replaceAll("[^0-9]", "");
        while(joinDate.length() != 10 || Integer.parseInt(joinDate.substring(0,4)) > localDate.getYear() || Integer.parseInt(joinDate.substring(5,7)) > localDate.getMonthValue() || (Integer.parseInt(joinDate.substring(5,7)) == localDate.getMonthValue() && Integer.parseInt(joinDate.substring(8,10)) > localDate.getDayOfMonth())){
            System.out.println("Please enter a valid date. When did you join? [YYYY-MM-DD]");
            joinDate = System.console().readLine();
        }
    }
}