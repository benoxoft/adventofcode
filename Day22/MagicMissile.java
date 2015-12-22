package Day22;

public class MagicMissile implements Spell {

	@Override
	public void castEffect(Player p, Boss b) {
		b.receiveDamage(4);
	}

	@Override
	public boolean usedUp() {
		return true;
	}

	@Override
	public int manaCost() {
		return 53;
	}

}
