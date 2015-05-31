import java.util.Scanner;
import java.util.ArrayList;

public class Player {

  private ArrayList<Card> hand; // the player's cards
  private int handTotal; // The total value of the hand
  private Scanner input; 

  public Player(){
    this.handTotal = 0;
    this.hand = new ArrayList<Card>();
  }

  public void addCard(Card myCard){
    this.hand.add(myCard);
    if(myCard.getValue() == 1 && (this.handTotal + 11 <= 21))
      this.handTotal += 11;
    else
      this.handTotal += myCard.getValue();
  }

  public int getTotal(){
    return handTotal;
  }

  public String showCards(){
    String result = "";

    for(int x = 0; x <= this.hand.size() - 1; x++)
    {
      result += this.hand.get(x).toString() + "\n";
    }

    return result;
  }
}

