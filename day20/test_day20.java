import static org.junit.Assert.*;

import org.junit.Test;

public class test_day20 {

	@Test
	public void test() {
		assertEquals(10, Day20.calc_house(1));
	    assertEquals(30, Day20.calc_house(2));
	    assertEquals(40, Day20.calc_house(3));
	    assertEquals(70, Day20.calc_house(4));
	    assertEquals(60, Day20.calc_house(5));
	    assertEquals(120, Day20.calc_house(6));
	    assertEquals(80, Day20.calc_house(7));
	    assertEquals(150, Day20.calc_house(8));
	    assertEquals(130, Day20.calc_house(9));
	}

}
