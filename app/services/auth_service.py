from sqlalchemy.orm import Session

from app.models import Employee
from app.security import verify_password


def authenticate_user(db: Session, email: str, password: str) -> Employee | None:
    normalized_email = email.strip().lower() # Clean up and lowercase the email address


    employee= db.query(Employee).filter(Employee.email == normalized_email).first() # It searches the database for an employee with that email and retrieves the first match (or `None` if no match is found).
    if employee is None:
        return None

    if not employee.is_active: # If an employee's account is inactive, it will not allow login and will return 'None'.
        return None

    if not verify_password(password, employee.password_hash):
        return None
    
    return employee



