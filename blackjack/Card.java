public class Card {

  private String suit;
  private int value;
	
  public Card(int aValue, String aSuit){
    value=aValue;
    suit=aSuit;
  }

  public String toString(){
    String myCard;
  
    if(value==1)
        myCard="Ace of ";
    else if(value==11)//Jack
        myCard="Jack of ";
    else if(value==12)//Queen
        myCard="Queen of ";
    else if(value==13)//King
        myCard="King of ";
    else 
      myCard=value +" of ";
      myCard+=suit;
    return myCard;
  }

  public int getValue(){
    return value;
  }
}
