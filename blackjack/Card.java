public class Card {

  private String suit;
  private int value;
	
  public Card(int aValue, String aSuit){
    this.value = aValue;
    this.suit = aSuit;
  }

  public String toString(){
    String myCard;
  
    switch(this.value) {
      case 1:
        myCard="Ace of ";
        break;
      case 11:
        myCard="Jack of ";
        break;
      case 12:
        myCard="Queen of ";
        break;
      case 13:
        myCard="King of ";
        break;
      default:
        myCard = this.value +" of ";
        myCard += this.suit;
        break;
    }

    return myCard;
  }

  public int getValue(){
    return this.value;
  }
}
