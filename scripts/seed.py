from app.database import SessionLocal
from app.models import Department, Employee
from app.security import hash_password

DEMO_PASSWORD = "DemoPassword@123"  # For fictional/demo test data only


def seed_data() -> None:
    db = SessionLocal()
    try:
        # If the employee already exists, stop here to avoid duplicates.
        existing_employee = db.query(Employee).first()
        if existing_employee is not None:
            print("Already seeded")
            return

        password_hash = hash_password(DEMO_PASSWORD)

        # ১. Create Departments / Use Python Dictionary
        departments = {
            "Engineering": Department(name="Engineering"),
            "Operations": Department(name="Operations"),
            "People": Department(name="People"),
        }
        db.add_all(departments.values())
        db.flush()  # Flush to get department.id

        # 2. HR_ADMIN (top of the tree, manager_id is empty)
        hr_admin = Employee(
            full_name="Farhana Rahman",
            email="farhanarahman@gamil.com",
            password_hash=password_hash,
            role="HR_ADMIN",
            manager_id=None,
            department_id=departments["People"].id,
            is_active=True,
        )
        db.add(hr_admin)
        db.flush()  # Flush to get hr_admin.id

        # 3. MANAGER (2 people; for both, the manager is HR_ADMIN)
        manager_a = Employee(
            full_name="Tanvir Hasan",
            email="manager.a@gamil.com",
            password_hash=password_hash,
            role="MANAGER",
            manager_id=hr_admin.id,
            department_id=departments["Engineering"].id,
            is_active=True,
        )
        manager_b = Employee(
            full_name="Nadia Islam",
            email="manager.b@gmail.com",
            password_hash=password_hash,
            role="MANAGER",
            manager_id=hr_admin.id,
            department_id=departments["Operations"].id,
            is_active=True,
        )
        db.add_all([manager_a, manager_b])
        db.flush()  # Flush to obtain manager_a.id and manager_b.id

       # 4. EMPLOYEE (4 people: 2 under manager_a, 2 under manager_b)
        employees = [
            Employee(
                full_name="Sabbir Ahmed",
                email="sabbirahamed.a1@gmail.com",
                password_hash=password_hash,
                role="EMPLOYEE",
                manager_id=manager_a.id,
                department_id=departments["Engineering"].id,
                is_active=True,
            ),
            Employee(
                full_name="Mitu Akter",
                email="mituakter.a2@gamil.com",
                password_hash=password_hash,
                role="EMPLOYEE",
                manager_id=manager_a.id,
                department_id=departments["Engineering"].id,
                is_active=True,
            ),
            Employee(
                full_name="Rashed Mahmud",
                email="rashedmahmud.b1@gamil.com",
                password_hash=password_hash,
                role="EMPLOYEE",
                manager_id=manager_b.id,
                department_id=departments["Operations"].id,
                is_active=True,
            ),
            Employee(
                full_name="Sumaiya Karim",
                email="sumiya.b2@gmail.com",
                password_hash=password_hash,
                role="EMPLOYEE",
                manager_id=manager_b.id,
                department_id=departments["Operations"].id,
                is_active=True,
            ),
        ]
        db.add_all(employees)

        # All changes are permanently saved to the database
        db.commit()
        print("Seed completed successfully!")
        print(f"Demo password for seeded users: {DEMO_PASSWORD}")
        print("Managers: manager.a@gamil.com| manager.b@gmail.com")
    except Exception:
        db.rollback()
        raise
    finally:
        db.close() # Closes the database session


if __name__ == "__main__":
    seed_data()






"""
# Hit Terminal
python -m scripts.seed
"""