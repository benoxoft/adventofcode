import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class Day20Thread extends Thread {

	public static void main(String[] args) {
		System.out.println("Starting...");
		ExecutorService s = Executors.newFixedThreadPool(10);
		for(int i=500000;i<928440;i++) {
			if (i % 10000 == 0)
				System.out.println(i);
			s.execute(new Day20Thread(i));
			try {
				Thread.sleep(0);
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		};
	}

	private final int house_no;
	
	public Day20Thread(int house_no) {
		this.house_no = house_no;
	}
	
	public void run() {
		if (calc_house() >= 33100000) {
			System.out.println(this.house_no);
			System.exit(0);
		}
	}
	
	public int calc_house() {
		int presents = 0;
		for(int i=1;i<house_no+1;i++) {
			if(house_no % i == 0 && i * 50 >= house_no) {				
				presents += i*11;
			}
		}
		return presents;
	}		
}
