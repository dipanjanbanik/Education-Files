class Account 
{
	 String accId, accName;
	private int accBalance;
	
	static int totalNumberofTransaction;
	int[] Transactionamount = new int[10];
	String[][] Transactiondetails = new String[10][10];
	
	public Account()
	{
		System.out.println("from super class its empty");
	} 
	public Account(String accId, String accName, int accBalance)
	{
		this.accId = accId;
		this.accName = accName;
		this.accBalance = accBalance;
		System.out.println("accId: " +this.accId);
		System.out.println("accName: "+this.accName);
		System.out.println("accBalance: "+this.accBalance);
	}
	
	
	void deposite (int x)
	{
		accBalance = accBalance + x;
		//addtranc(,,,,);
		System.out.println("/n" +accBalance+ "\nDeposite to: " +accName+ "\nno of ID "+accId);
	}
	
	
	void withdraw ( int x )
	{
		accBalance = accBalance + x;
		System.out.println("/n" +accBalance+ "\nWithdraw to: " +accName+ "\nno of ID "+accId);
	}
	
	void showInfo()
	{
		//System.out.println("accId: " +this.accId);
		System.out.println("hhhhhhhhhhhhhhhhhhhhhh ");
	}
	
	void addTransaction(String sender, String receiver, int amount)
	{
		
	}
}

class Transaction extends Account
{
	String Accountsender, Accountreceiver, additionalInfo;
	int amount;
	
	public Transaction()
	{
		System.out.println("empty");
		System.out.println("empty" +super.accId);
	}
	
	public Transaction(String Accountsender, String Accountreceiver, int amount, String additionalInfo)
	{
		super("14-xxxxx-1", "Fouzia", 5000);
		
		this.Accountsender = Accountsender;
		this.Accountreceiver = Accountreceiver;
		this.amount = amount;
		this.additionalInfo=additionalInfo;
		System.out.println("came from: " +this.Accountsender);
		System.out.println("received: "+this.Accountreceiver);
		System.out.println("amount: " +this.amount);
		System.out.println("additionalInfo"+this.additionalInfo);
		
	}
	void showInfo()
	{
	super.showInfo();
		System.out.println("amount: " +this.amount);
		
	} 
	
	public static void main (String [] args)
	{
		/*Account ob1 = new Account();
		Account ob2 = new Account("12345778" , "fsahgaf","100");
		ob2.showInfo();
		ob2.deposite(100);
		ob2.withdraw(50);*/
		
		System.out.println("hello");
		Transaction o1 = new Transaction();
		Transaction o2 = new Transaction("abc", "def", 5000, "ghi");
		o2.showInfo();
		
		
		
	}
} 








