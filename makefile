runserver:
	uvicorn quoteGenerator.main:app --reload
r:
	uvicorn books:app --reload