package Day21;

public abstract class Wearable {
	
	private final int _cost;
	private final int _armor;
	private final int _attack;
	private final String _name;
	
	public Wearable(int cost, int damage, int armor, String name) {
		_cost = cost;
		_armor = armor;
		_attack = damage;
		_name = name;
	}
	
	public int getCost() {
		return _cost;
	}
	public int getArmor() {
		return _armor;
	}
	public int getAttack() {
		return _attack;
	}
	public String getName() {
		return _name;
	}
}