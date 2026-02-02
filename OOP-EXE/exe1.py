class BankAccount:
    # Class variable - shared by all instances
    bank_name = "Python Bank"
    
    def __init__(self, account_number, account_holder, initial_balance):
        # Validate initial balance
        if initial_balance < 0:
            raise ValueError("Initial balance must be positive")
        
        # Instance variables - unique to each object
        self.account_number = account_number
        self.account_holder = account_holder
        self._balance = initial_balance  # Private by convention (_)
        
        # You can call additional setup here
        self._setup_account()
    
    def _setup_account(self):
        """Private method for additional setup"""
        self.transaction_count = 0
    
    def deposit(self, amount):
        """Add money to account"""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        
        self._balance += amount
        self.transaction_count += 1
        return self._balance
    
    def withdraw(self, amount):
        """Remove money from account"""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        
        self._balance -= amount
        self.transaction_count += 1
        return self._balance
    
    def get_balance(self):
        """Public getter for balance"""
        return self._balance
    
    def __str__(self):
        """String representation for printing"""
        return f"BankAccount({self.account_holder}, Balance: ${self._balance:.2f})"
    
    # Bonus: __repr__ for debugging
    def __repr__(self):
        return f"BankAccount(account_number='{self.account_number}', holder='{self.account_holder}')"
    

    # Test cases
try:
    # Create account
    acc1 = BankAccount("ACC123", "John Doe", 1000)
    print(acc1)  # Uses __str__
    
    # Deposit
    acc1.deposit(500)
    print(f"After deposit: ${acc1.get_balance()}")
    
    # Withdraw
    acc1.withdraw(300)
    print(f"After withdrawal: ${acc1.get_balance()}")
    
    # Try invalid operations
    # acc1.withdraw(2000)  # Should raise ValueError
    # acc1.deposit(-100)   # Should raise ValueError
    
    # Access class variable
    print(f"Bank: {BankAccount.bank_name}")
    acc1.withdraw(2000)
except ValueError as e:
    print(f"Error: {e}")