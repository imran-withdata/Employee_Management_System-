from sqlalchemy import Column, Integer, String,Boolean, DateTime, ForeignKey, func
from app.database import Base



class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key= True,index=True)
    full_name = Column(String(50), nullable= False )
    email = Column(String(60), unique= True,index=True, nullable= False)
    password_hash = Column(String(255), nullable=False)
    role = Column(String(50),nullable=False) # HR_ADMIN, MANAGER, EMPLOYEE
    
    manager_id = Column(Integer, ForeignKey("employees.id"), nullable= True)
    department_id = Column(Integer, ForeignKey("departments.id"), nullable=True )
    
    is_active = Column(Boolean, default=True, nullable= False )

    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate= func.now(),
        nullable= False
    )


    """
    # Show tables name
    python -c "from sqlalchemy import inspect; from app.database import engine; insp = inspect(engine); print(insp.get_table_names())"
    
    """