package Day21;

public class Boss extends Character {

	public Boss() {
		super(109);
	}

	@Override
	public int getArmor() {
		return 2;
	}

	@Override
	public int getDamage() {
		return 8;
	}
	
}