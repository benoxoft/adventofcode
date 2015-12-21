
public class Day20 {

	public static void main(String[] args) {
		System.out.println("Starting...");
		for(int i=1;i<33100000;i++) {
			if (i % 10000 == 0)
				System.out.println(i);
			if(calc_house(i) >= 33100000) {
				System.out.println(i);
				System.exit(0);
			}
			
		};
	}

	
	public static int calc_house(int house_no) {
		int presents = 0;
		for(int i=1;i<house_no+1;i++) {
			if(house_no % i == 0 && i * 50 >= house_no) {				
				presents += i*11;
			}
		}
		return presents;
	}		
}
