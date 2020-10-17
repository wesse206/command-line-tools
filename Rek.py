class category:
	vastebates = False
	bedryfsbates = False
	
	inkomstes = False
	uitgawes = False

class bates:
	def __init__(self):
		self.T = 'plmn'
		self.category = [category.vastebates, category.bedryfsbates]
		self.status = False
		
class ekwiteit:
	def __init__(self):
		self.T = 'mnpl'
		self.category = [category.inkomstes, category.uigawes]
		self.status = False
class laste:
	pass

class maincategory:
	B = bates()
	E = ekwiteit()
	L = laste()


class balansstaat:
	def __init__(self):
		maincategory.B = False
		maincategory.E = False
		maincategory.L = False
	
class nominale_rekening:
	def __init__(self):
		category.inkomstes = False
		category.uitgawes = False
		if category.inkomstes or category.uitgawes == True:
			maincategory.E.status = True
			
