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
    reviews_id = db.relationship(
        "Reviews", backref="user", cascade="all, delete", lazy=True)


    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return f"#{self.id} - Username:{self.username} | Reviewed {self.song_name}"


class Reviews(db.Model):
    """
    Schema for reviews model
    """
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(
        "user.id", ondelete="CASCADE"), nullable=False)
    song_name = db.Column(db.String, nullable=False)
    artist = db.Column(db.String, nullable=False)
    release_year = db.Column(db.String, nullable=False)
    album = db.Column(db.String, nullable=False)
    producer = db.Column(db.String, nullable=False)
    studio = db.Column(db.String, nullable=False)
    monthly_listeners = db.Column(db.String, nullable=False)
    video = db.Column(db.String, nullable=False)
    review_id = db.relationship(
        "User", backref="user", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self
