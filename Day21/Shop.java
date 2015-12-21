package Day21;

import java.util.List;
import java.util.Vector;

public class Shop {
	
	private final List<Weapon> _weapons = new Vector<Weapon>();
	private final List<Armor> _armors = new Vector<Armor>();
	private final List<Ring> _rings = new Vector<Ring>();
	
	public Shop() {
		_weapons.add(new Weapon(8, 4, 0, "Dagger"));
		_weapons.add(new Weapon(10, 5, 0, "Shortsword"));
		_weapons.add(new Weapon(25, 6, 0, "Warhammer"));
		_weapons.add(new Weapon(40, 7, 0, "Longsword"));
		_weapons.add(new Weapon(74, 8, 0, "Greataxe"));
		
		_armors.add(new Armor(13, 0, 1, "Leather"));
		_armors.add(new Armor(31, 0, 2, "Chainmail"));
		_armors.add(new Armor(53, 0, 3, "Splintmail"));
		_armors.add(new Armor(75, 0, 4, "Bandedmail"));
		_armors.add(new Armor(102, 0, 5, "Platemail"));
		_armors.add(new Armor(0, 0, 0, "Empty"));
		
		_rings.add(new Ring(25, 1, 0, "Damage +1"));
		_rings.add(new Ring(50, 2, 0, "Damage +2"));
		_rings.add(new Ring(100, 3, 0, "Damage +3"));
		_rings.add(new Ring(20, 0, 1, "Defense +1"));
		_rings.add(new Ring(40, 0, 2, "Defense +2"));
		_rings.add(new Ring(80, 0, 3, "Defense +3"));
		_rings.add(new Ring(0, 0, 0, "Empty 1"));
		_rings.add(new Ring(0, 0, 0, "Empty 2"));
		
	}
	
	public List<Weapon> getWeapons() {
		return _weapons;
	}
	
	public List<Armor> getArmors() {
		return _armors;
	}
	
	public List<Ring> getRings() {
		return _rings;
	}
}