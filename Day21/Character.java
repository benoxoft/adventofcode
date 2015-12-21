package Day21;

public abstract class Character {
	
	private int _hp;
	
	public Character(int hp) {
		_hp = hp;
	}
	
	public void receiveDamage(Character c) {
		int actualDamage = c.getDamage() - getArmor();
		if(actualDamage < 0) {
			return;
		}
		_hp -= actualDamage;
	}
	
	public abstract int getArmor();
	
	public abstract int getDamage();
	
	public int getHP() {
		return _hp;
	}
	
}