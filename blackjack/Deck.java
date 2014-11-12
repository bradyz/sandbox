import java.util.Random;

public class Deck {

  private Card[] cards;
  private int cardsDrawn;
  private int top;

  public Deck(){
    int n = 0;
    int[] val = {1,2,3,4,5,6,7,8,9,10,11,12,13};
    String[] face = {"Heart", "Spade", "Diamond", "Clubs"};

    cards = new Card[52];
    this.top = 0;

    for(int x = 0; x <= 12; x++)
    {
      for(int y = 0; x <= 3; y++)
      {
        this.cards[n] = new Card(val[x], face[y]);
        n++;
      }
    }
  }

  public Card draw(){
    Card myCard = this.cards[this.top];

    this.top += 1;
    this.cardsDrawn += 1;

    return myCard;
  }

  public void shuffle(){
    Random r = new Random();
    Card temp;
    
    for(int x = 51; x > 0; x--)
    {
      int i = r.nextInt(x + 1);
      temp = this.cards[i];
      this.cards[i] = this.cards[x];
      this.cards[x] = temp;
    }

    this.top = 0;
    this.cardsDrawn = 0;
  }

  public int getCardsDrawn(){
    return cardsDrawn;
  }

  public String toString(){
    String result = "";

    for(int x = 0; x < 52; x++)
    {
      result += this.cards[x].toString() + "\n";
    }

    return result;
  }
}
