from rhythmreview import db


class User(db.Model):
    """
    Schema for user model
    """
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String, nullable=False)
    lname = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, unique=True, nullable=False)
    is_admin = db.Column(db.Boolean, default=False, nullable=False)
    reviews = db.relationship(
        "Review", backref="user", cascade="all, delete", lazy=True)


    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return f"#{self.id} - Username:{self.username} | Admin: {self.is_admin}"


class Admin(db.Model):
    '''
    schema for Admin model
    '''
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(
        "user.id", ondelete="CASCADE"), nullable=False)
    admin_name = db.Column(db.String, nullable=False)
    reviews = db.relationship(
        "Review", backref="admin", cascade="all, delete", lazy=True)

    def __repr__(self):
        # represents itself in the form of a string
        return self.admin_name


class Review(db.Model):
    """
    Schema for review model
    """
    id = db.Column(db.Integer, primary_key=True)
    admin_id = db.Column(db.Integer, db.ForeignKey(
            "admin.id", ondelete="CASCADE"), nullable=False)
    song_name = db.Column(db.String(100), nullable=False)
    artist = db.Column(db.String(100), unique=True, nullable=False)
    release_year = db.Column(db.Integer, nullable=False)
    album = db.Column(db.String(100), unique=True, nullable=False)
    producer = db.Column(db.String(100), unique=True, nullable=False)
    studio = db.Column(db.String(100), unique=True, nullable=False)
    monthly_listeners = db.Column(db.Integer, unique=True, nullable=False)
    video = db.Column(db.String(100), unique=True, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.review_title

class Comments(db.Model):
    # schema for the comments model
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(
    "user.id", ondelete="CASCADE"), nullable=False)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return f"{self.id} - {self.title}"