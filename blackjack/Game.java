import java.util.Scanner;

public class Game {

	private Deck deck;
	private Player player;
	private Dealer dealer;
	private Scanner input;

  public void play(){
    this.deck = new Deck();
    this.input = new Scanner(System.in);

    while(true){
      this.player = new Player();
      this.dealer = new Dealer();

      this.deck.shuffle();

      this.player.addCard(this.deck.draw());
      this.player.addCard(this.deck.draw());
      this.dealer.addCard(this.deck.draw());
      this.dealer.addCard(this.deck.draw());
      System.out.println("New game!\n");
      System.out.println("Dealer card: " + this.dealer.showOne());
      System.out.println("Your cards: " + this.player.showCards()); 

      while(this.player.getTotal() <= 21 && input.nextLine() != "S"){
        this.player.addCard(this.deck.draw());
      }

      while(this.dealer.getTotal() <= 16){
        this.dealer.addCard(this.deck.draw());
      }

      System.out.println("Dealer card: " + this.dealer.showCards());
      System.out.println("Your cards: " + this.player.showCards()); 

      int d = this.dealer.getTotal();
      int p = this.player.getTotal();

      System.out.println("Dealer total: " + d + "\n");
      System.out.println("Player total: " + p + "\n");
      
      System.out.println("Play again? [y/n]\n");

      if(this.input.nextLine() == "n")
        break;
    }
  }
}
