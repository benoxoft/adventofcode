package Day22;

import java.util.List;
import java.util.Vector;

public class Day22 {
	
	public static void main(String args[]) {
		System.out.println(new Day22().solve());
	}
	
	private int solve() {
		List<Player> survivors = new Vector<Player>();
		
		for(int i=0;i<Math.pow(5, _spellChain.length);i++) {
			_sb.clearSpells();
			if(i % 100000 == 0) {
				System.out.println(i);
			}
			Player p = new Player(_spellChain);
			Boss b = new Boss();
			if(performBattle(p, b)) {
				survivors.add(p);
			}
			incrementSpellChain();
		}
		int minMana = Integer.MAX_VALUE;
		for(Player p : survivors) {
			if(p.getManaUsed() < minMana) {
				minMana = p.getManaUsed();
				System.out.println(p);
			}
		}
		return minMana;
	}
	
	private boolean performBattle(Player p, Boss b) {
		for(int i=0;i<_spellChain.length;i++) {
			p.receiveDamage(1);
			if(p.getHP() <= 0) {
				return false;
			}			
			p.shield(false);
			_sb.activateSpells(p, b);
			if(b.getHP() <= 0) {
				return true;
			}
			if(!_sb.castSpell(_spellChain[i], p, b)) {
				return false;
			}
			p.shield(false);
			_sb.activateSpells(p, b);
			if(b.getHP() <= 0) {
				return true;
			}
			p.receiveDamage(b.getDamage());
			if(p.getHP() <= 0) {
				return false;
			}
		}
		return false;
	}
	
	private Spellbook _sb = new Spellbook();
	private int[] _spellChain = new int[] {0,0,0,0,0,0,0,0,0};

	private void incrementSpellChain() {
		incrementSpellChain(0);
	}
	
	private void incrementSpellChain(int cursor) {
		if(cursor >= _spellChain.length) {
			return;
		}
		
		_spellChain[cursor]++;
		if(_spellChain[cursor] == 5) {
			_spellChain[cursor] = 0;
			incrementSpellChain(cursor+1);
		}
	}
}
