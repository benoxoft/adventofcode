package Day22;

public class Shield implements Spell {

	private boolean _freshCast = true;
	private int _turns = 6;
	
	@Override
	public void castEffect(Player p, Boss b) {
		if(_freshCast) {
			_freshCast = false;
			return;
		}
		p.shield(true);	
		_turns--;
	}

	@Override
	public boolean usedUp() {
		return _turns <= 0;
	}

	@Override
	public int manaCost() {
		return 113;
	}

}
