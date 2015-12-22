package Day22;

public class Boss  {

	private int _hp = 51;
	
	public Boss() {	}

	public int getHP() {
		return _hp;
	}
	
	public int getDamage() {
		return 9;
	}
	
	public void receiveDamage(int damage) {
		_hp -= damage;
	}
	
}