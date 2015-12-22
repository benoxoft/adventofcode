package Day22;

public class Drain implements Spell {

	@Override
	public void castEffect(Player p, Boss b) {
		b.receiveDamage(2);
		p.heal(2);
		// TODO Auto-generated method stub

	}

	@Override
	public boolean usedUp() {
		return true;
	}

	@Override
	public int manaCost() {
		return 73;
	}

}
