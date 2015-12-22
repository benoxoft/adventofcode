package Day22;

import java.util.List;
import java.util.Vector;

public class Spellbook {

	private List<Spell> _activeSpells = new Vector<Spell>();
	
	public void clearSpells() {
		_activeSpells = new Vector<Spell>();
	}
	
	public void activateSpells(Player p, Boss b) {
		List<Spell> used = new Vector<Spell>();
		for(Spell s : _activeSpells) {
			s.castEffect(p, b);
			if(s.usedUp()) {
				used.add(s);
			}
		}
		for(Spell s : used) {
			_activeSpells.remove(s);
		}
	}
	
	private boolean addActiveSpell(Spell ns) {
		for(Spell s : _activeSpells) {
			if(s.getClass() == ns.getClass()) {
				return false;
			}
		}
		_activeSpells.add(ns);
		return true;
	}
	
	public boolean castSpell(int page, Player p, Boss b) {
		Spell s = null;
		switch(page) {
		case 0:
			s = new MagicMissile();
			break;
		case 1:
			s = new Drain();
			break;
		case 2:
			s = new Shield();
			break;
		case 3:
			s =  new Poison();
			break;
		case 4:
			s = new Recharge();
			break;
		}
		
		if(p.castSpell(s)) {
			s.castEffect(p, b);
			if(!s.usedUp()) {
				return addActiveSpell(s);
			}
			return true;
		}
		return false;
	}
	
}