import java.util.Scanner;

public class Game {

	private Deck deck;
	private Player player;
	private Dealer dealer;
	private Scanner input;

  public void play(){
    String in;
    this.input = new Scanner(System.in);
    this.deck = new Deck();
    boolean keepPlaying = true;

    while(keepPlaying){
      this.player = new Player();
      this.dealer = new Dealer();

      this.deck.shuffle();

      this.player.addCard(this.deck.draw());
      this.player.addCard(this.deck.draw());
      this.dealer.addCard(this.deck.draw());
      this.dealer.addCard(this.deck.draw());

      System.out.println("New game!");
      System.out.print("Dealer card: \n" + this.dealer.showOne());
      System.out.print("Your cards: \n" + this.player.showCards()); 

      System.out.println("Hit or Stay? [h/s]");
      in = this.input.nextLine();

      while(this.player.getTotal() <= 21 && in != "s"){
        this.player.addCard(this.deck.draw());
        System.out.print("Your cards: \n" + this.player.showCards()); 
        if(this.player.getTotal() <= 21){
          System.out.println("Hit or Stay? [h/s]");
          in = this.input.nextLine();
        }
      }

      while(this.dealer.getTotal() <= 16){
        this.dealer.addCard(this.deck.draw());
      }

      System.out.print("Dealer card: \n" + this.dealer.showCards());
      System.out.print("Your cards: \n" + this.player.showCards()); 

      int d = this.dealer.getTotal();
      int p = this.player.getTotal();

      System.out.println("Dealer total: " + d);
      System.out.println("Player total: " + p);
      
      System.out.println("Play again? [y/n]");
      in = this.input.nextLine();

      if(in == "n")
        keepPlaying = false;
    }
  }
}
