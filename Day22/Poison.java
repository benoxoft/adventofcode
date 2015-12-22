package Day22;

public class Poison implements Spell {

	private boolean _freshCast = true;
	private int _turns = 6;
	
	@Override
	public void castEffect(Player p, Boss b) {
		if(_freshCast) {
			_freshCast = false;
			return;
		}
		if (_turns > 0) { 
			b.receiveDamage(3);
			_turns--;
		}
	}

	@Override
	public boolean usedUp() {
		return _turns <= 0;
	}

	@Override
	public int manaCost() {
		return 173;
	}

}
