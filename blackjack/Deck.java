public class Deck {

    private Card[] cards;
    private int cardsDrawn;
	
    //any more instance variables you may want here

	
    public Deck(){
    // This constructor should instatiate 52 distinct Card
    // objects and place them in the cards array.
    // your code here
    
			
    }
	
    public Card draw(){
    // this method deals the top card of the deck
    // your code here

    }
	
    public void shuffle(){
    // this method shuffles the deck and resets cardsdrawn
        
    // your code here

    }
	
    public int getCardsDrawn(){
    // leave this method as is. 
    // This is for the graders to test your code.
	return cardsDrawn;
    }

    public String toString(){
    // This method should return a string consisting of 52 lines
    // each line should contain a description of the card in the
    // deck at the corresponding position top-to-bottom


    // your code here

    }

    // any more methods you may need here


}
