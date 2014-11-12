import java.util.ArrayList;

public class Dealer {

  private ArrayList<Card> hand; 
  private int handTotal;

  public Dealer(){
    this.hand = new ArrayList<Card>();
    this.handTotal = 0;
  }

  public void addCard(Card myCard){
    this.hand.add(myCard);
    if(myCard.getValue() == 1 && (this.handTotal + 11 <= 21))
      this.handTotal += 11;
    else
      this.handTotal += myCard.getValue();
  }

  public int getTotal(){
    return this.handTotal;
  }

  public String showOne(){
    return this.hand.get(0).toString() + "\n";
  }

  public String showCards(){
    String result = "";

    for(int x = 0; x < this.hand.size() - 1; x++)
    {
      result += this.hand.get(x).toString() + "\n";
    }

    return result;
  }
}
