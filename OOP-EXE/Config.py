class Config:
    app_name = "MyApp"
    
    def __init__(self, **kwargs):
        for key , value in kwargs.items():
            setattr(self, key , value)

            
    def to_dict(self):
        result = {}
        for key in dir(self):
            if not key.startswith("_"):
                result[key] = getattr(self , key)
        return result
    
    def update(self, **kwargs):
        for key , value in kwargs.items():
            if value is not None:
                setattr(self, key, value)
    
    def get(self, key , default = None):
        if hasattr(self, key):
            return getattr(self, key)
        return default
    
    def __str__(self):
    # Count settings (use your to_dict() method!)
        count = len(self.to_dict())
        return f"Config(settings: {count}, app: {self.app_name})"
            
    def __contains__(self, key):
        return hasattr(self, key)
   
   
