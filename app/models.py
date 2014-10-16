from sqlalchemy import Column, Integer, String, ForeignKey, Date, Table, Text
from sqlalchemy.orm import relationship, backref 
from flask.ext.appbuilder import Model
from flask.ext.appbuilder.models.mixins import AuditMixin, BaseMixin, FileColumn, ImageColumn
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

"""

You can use the extra Flask-AppBuilder fields and Mixin's

AuditMixin will add automatic timestamp of created and modified by who


"""

class schema(Model):
	__tablename__ = 'schema'
	id = Column(Integer, primary_key=True)
	name = Column(String(50), unique = True, nullable=False)

	def __repr__(self):
		return self.name   

class table(Model):
	__tablename__ = 'table'
	id = Column(Integer, primary_key=True)
	name = Column(String(70), nullable=False)
	type = Column(String(30), default = 'Imported Table') #Derived Table from RR, #View from ops_data, #One Time table
	schema_id = Column(Integer, ForeignKey('schema.id'))
	schema = relationship("schema")

	def __repr__(self):
		return self.name


field_feature_association = Table('field_feature_association',Model.metadata,
											Column('field_id', Integer, ForeignKey('field.id')),
											Column('feature_id',Integer, ForeignKey('feature.id')),
											schema="main"
										)

class field(Model):
	__tablename__ = 'field'
	id = Column(Integer, primary_key=True)
	name = Column(String(70), nullable=False)
	database_type = Column(String(70)) #varchar(255), text, int
	joinable_to = Column(Text()) # merchants.pk = transactions.merchant_fk 
	notes = Column(Text()) #don't use this for X 
	table_id = Column(Integer, ForeignKey('table.id'))
	table = relationship("table")
	features = relationship("feature",
    				secondary = field_feature_association,
    				backref = backref('fields'),
    				)

	def __repr__(self):
		return self.name

class feature(Model):
	__tablename__ = 'feature'
	id = Column(Integer, primary_key=True)
	name = Column(String(70), unique = True, nullable=False)
	field_id = Column(Integer, ForeignKey('field.id'))
	#field = relationship("field")

	def __repr__(self):
		return self.name




