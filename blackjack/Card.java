public class Card {

  private String suit;
  private int value;
	
  public Card(int aValue, String aSuit){
    value = aValue;
    suit = aSuit;
  }

  public String toString(){
    String myCard;
  
    if(this.value == 1)
        myCard="Ace of ";
    else if(this.value == 11)
        myCard="Jack of ";
    else if(this.value == 12)
        myCard="Queen of ";
    else if(this.value == 13)
        myCard="King of ";
    else 
      myCard = this.value +" of ";
      myCard += this.suit;
    return myCard;
  }

  public int getValue(){
    return value;
  }
}
