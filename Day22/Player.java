package Day22;

import java.util.Arrays;

public class Player {
	
	private int _hp = 50;
	private int _mana = 500;
	private int _manaUsed = 0;
	private boolean _shield = false;
	
	private int[] _spellChain;
	
	public Player(int[] spellChain) {
		_spellChain = new int[spellChain.length];
		System.arraycopy(spellChain, 0, _spellChain, 0, spellChain.length);
	}
	
	public int getHP() {
		return _hp;
	}
	
	public int getMana() {
		return _mana;
	}
	
	public void heal(int hp) {
		_hp += hp;
	}
	
	public void rejuvenate(int mana) {
		_mana += mana;
	}
	
	public void shield(boolean up) {
		_shield = up;
	}
	
	public void receiveDamage(int damage) {
		if(_shield) {
			damage -= 7;
			if(damage < 1) {
				damage = 1;
			}
		}
		_hp -= damage;
	}
	
	public int getManaUsed() {
		return _manaUsed;
	}
	
	public boolean castSpell(Spell s) {
		int cost = s.manaCost();
		if(cost > _mana) {
			return false;
		}
		_manaUsed += cost;
		_mana -= cost;
		return true;
	}
	
	public String toString() {
		return Arrays.toString(_spellChain);
	}
}