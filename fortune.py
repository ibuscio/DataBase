from data import Base
import sqlalchemy as sqa

class Fortune(Base):
    __tablename__= 'fortune500'

    rank = sqa.Column(sqa.Integer, primary_key = True)
    title = sqa.Column(sqa.String)
    website = sqa.Column(sqa.String)
    employees = sqa.Column(sqa.Integer)
    sector = sqa.Column(sqa.String)
    industry = sqa.Column(sqa.String)

    def __init__(self, rank, title, website, employees, sector, industry):
        self.rank = rank
        self.title = title
        self.website = website
        self.employees = employees
        self.sector = sector
        self.industry = industry
