class transaction
{
	public String account_sender, account_receiver, additional_info;
	public int amount;
	
	public transaction()
	{
		System.out.println("Empty constructor from transaction\n");
	}
	
	public transaction(String as, String ar, int am, String additional_info)
	{
		account_sender 		= as;
		account_receiver 	= ar;
		amount 				= am;
		additional_info 	= ai;
	}
	
	public void showinfo()
	{
		System.out.println("Sender name: "		+account_sender);
		System.out.println("Receiver name: "	+account_receiver);
		System.out.println("Amount: "			+amount);
		System.out.println("Additional Info: "	+additional_info);
	}
}





class account extends transaction
{
	private String accID, accName;
	private int accBalance;
	
	static int totalNumberofTransaction=0;
	int[] transactionamount = new int[10];
	String[][] transactiondetails = new String[10][10];
	
	account()
	{
	
		System.out.println("Empty Constructor from account");
		totalNumberofTransaction++;
	}
	
	account(String accID, String accName, int accBalance)
	{
		this.accID = accID;
		this.accName = accName;
		this.accBalance = accBalance;
		
		totalNumberofTransaction++;
	}
	
	void addTransaction(String as, String ar, int am)
	{
		this.account_sender=as;
		this.account_receiver=ar;
		this.amount=am;
	}
	
	void showAllTransaction()
	{
		System.out.println("Account ID: "				+accID);
		System.out.println("Account Name: "				+accName);
		System.out.println("Account Balance: "			+accBalance);
		System.out.println("Sender Name: "				+super.account_sender);
		System.out.println("Receiver Name: "			+super.account_receiver);
		System.out.println("Amount: "					+super.amount);
		System.out.println("Number of Transaction: "	+totalNumberofTransaction);
	}
	
	
	
	public static void main(String args[])
	{
		account o1 = new account();
		account o2 = new account("14-xxxxx-1", "Fouzia", 5000);
		o2.addTransaction("Fouzia", "Banik", 3000);
		o2.showAllTransaction();
	}
	
}