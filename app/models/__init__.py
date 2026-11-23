from app.models.department import Department
from app.models.employee import Employee

__all__ = ["Department", "Employee"]

"""
# Check command
python -c "from app.database import Base; import app.models; print(sorted(Base.metadata.tables.keys()))"
"""