package Day22;

public interface Spell {
	public void castEffect(Player p, Boss b);
	public boolean usedUp();
	public int manaCost();
}