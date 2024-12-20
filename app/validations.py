import re
from fastapi import HTTPException, status

def validate_password(password: str):
    if (len(password) < 8 or 
        not re.search(r'[A-Z]', password) or 
        not re.search(r'[a-z]', password) or 
        not re.search(r'[0-9]', password) or 
        not re.search(r'[@$!%*?&#]', password)):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Password must be at least 8 characters long, contain one uppercase, one lowercase, one digit, and one special character."
        )
