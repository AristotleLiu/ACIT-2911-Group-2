from app import app, db

with app.app_context():
    """
    Create all database tables using the defined models.

    This code is executed within the application context, which ensures that
    the necessary application configurations and resources are available.

    Note:
        This code assumes that the necessary database models have been defined
        and imported into the 'app' module, and the SQLAlchemy instance 'db'
        has been initialized.
    """
    db.create_all()
    print("All tables should have been created now.")
