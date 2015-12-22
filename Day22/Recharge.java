package Day22;

public class Recharge implements Spell {

	private boolean _freshCast = true;
	private int _turns = 5;
	
	@Override
	public void castEffect(Player p, Boss b) {
		if(_freshCast) {
			_freshCast = false;
			return;
		}
		if(_turns > 0) {
			p.rejuvenate(101);
			_turns--;
		}
	}

	@Override
	public boolean usedUp() {
		return _turns <= 0;
	}

	@Override
	public int manaCost() {
		return 229;
	}

}
