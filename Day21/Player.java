package Day21;

public class Player extends Character {

	private final Armor _armor;
	private final Weapon _weapon;
	private final Ring _leftRing;
	private final Ring _rightRing;
	
	public Player(Armor armor, Weapon weapon, Ring lring, Ring rring) {
		super(100);
		_armor = armor;
		_weapon = weapon;
		_leftRing = lring;
		_rightRing = rring;
	}

	@Override
	public int getArmor() {
		int armor = 0;
		armor += _armor.getArmor();
		armor += _leftRing.getArmor();
		armor += _rightRing.getArmor();
		return armor;
	}

	@Override
	public int getDamage() {
		int damage = 0;
		damage += _weapon.getAttack();
		damage += _leftRing.getAttack();
		damage += _rightRing.getAttack();
		return damage;
	}
	
	public int getCost() {
		int cost = 0;
		cost += _weapon.getCost();
		cost += _armor.getCost();
		cost += _leftRing.getCost();
		cost += _rightRing.getCost();
		return cost;
	}
	
	public String toString() {
		return "Armor: " + _armor.getName() + " Weapon: " + _weapon.getName() + " Left Ring: " + _leftRing.getName() + " Right Ring: " + _rightRing.getName();
	}
	
}