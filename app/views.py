from flask.ext.appbuilder.models.datamodel import SQLAModel
from flask.ext.appbuilder import ModelView, AppBuilder, expose, BaseView, has_access
from app import appbuilder, db
from .models import schema, table, field, feature

'''
class MyView(BaseView):

    default_view = 'method1'

    @expose('/method1/')
    @has_access
    def method1(self):
        # do something with param1
        # and return to previous page or index
        return 'Hello'

    @expose('/method2/<string:param1>')
    @has_access
    def method2(self, param1):
        # do something with param1
        # and render template with param
        param1 = 'Goodbye %s' % (param1)
        return param1

	@expose('/method3/<string:param1>')
	@has_access
	def method3(self, param1):
	    # do something with param1
	    # and render template with param
	    param1 = 'Goodbye %s' % (param1)
	    self.update_redirect()
	    return render_template('method3.html',
	                           param1 = param1,
	                           appbuilder=self.appbuilder)
'''

class featureModelView(ModelView):
	datamodel = SQLAModel(feature)

class fieldModelView(ModelView):
	datamodel = SQLAModel(field)
	related_views = [featureModelView]

class tableModelView(ModelView):
	datamodel = SQLAModel(table)
	related_views = [fieldModelView]
	label_columns = {'schema':'Schema'}
	list_columns = ['name','type']

class schemaModelView(ModelView):
	datamodel = SQLAModel(schema)
	related_views = [tableModelView]

db.create_all()	

#appbuilder.add_view(MyView, "Method1", category='My View')
#appbuilder.add_link("Method2", href='/myview/method2/jonh', category='My View')
#appbuilder.add_link("Method3", href='/myview/method3/jonh', category='My View')

appbuilder.add_view(schemaModelView, "List Schemas",icon = "fa-database",category = "Database",
                category_icon = "fa-database")
appbuilder.add_view(tableModelView, "List Tables",icon = "fa-table",category = "Database")
appbuilder.add_view(fieldModelView, "List Fields",icon = "fa-bars", category="Database")
appbuilder.add_view(featureModelView,"List Features",icon = "fa-code",category="Database")



