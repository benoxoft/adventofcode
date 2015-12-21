package Day21;

import java.util.List;
import java.util.Vector;

public class Day21 {

	public static void main(String[] args) {
		Day21 d = new Day21();
		System.out.println(d.solve());
	}
	
	private final Shop _shop = new Shop();
	private final List<Player> _players = new Vector<Player>();
	
	public Day21() {}
	
	private int solve() {
		for(Weapon w : _shop.getWeapons()) {
			for(Armor a : _shop.getArmors()) {
				for(Ring lr : _shop.getRings()) {
					for(Ring rr : _shop.getRings()) {
						if(lr == rr) {
							continue;
						}
						Player p = new Player(a, w, lr, rr);
						if(performBattle(p)) {
							_players.add(p);
						}
					}
				}
			}
		}
		int cost = 0; //Integer.MAX_VALUE;
		for(Player p : _players) {
			if(cost < p.getCost()) {
				cost = p.getCost();
			}
		}
		return cost;
	}
	
	private boolean performBattle(Player p) {
		System.out.println(p);
		Boss b = new Boss();
		while(b.getHP() > 0 && p.getHP() > 0) {
			b.receiveDamage(p);
			if(b.getHP() > 0) {
				p.receiveDamage(b);
			}
		}
		return p.getHP() <= 0; 
	}
}
