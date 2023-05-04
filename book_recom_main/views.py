from urllib import response
from xxlimited import foo
import pandas as pd
from django.http import HttpResponse
from django.shortcuts import render
import numpy as np # linear algebra
import pandas as pd
from scipy.sparse.linalg import svds
from .models import user_data

from django.shortcuts import render
from .forms import InputForm
 
# Create your views here.
def home_view(request):
	form = InputForm(request.POST, request.POST)
	# print(request.POST)
	if form.is_valid():
		form.save()
		return render(request, "new.html")
	return render(request, "new.html", {"form":form})


def home(request):
	book = '/home/pela/Documents/SE project/book_recom_main/static/data files/Books.csv'
	book_df = pd.read_csv(book)
	
	# for recommendation 
	books = book_df['Book-Title'].tolist()

	
	if request.method =='GET'and'submit_book' in request.GET:	
		print("final info on the way")
		selected_book = request.GET.get('book_name')
		print("book selected is :", selected_book)
		# selected_book = 'Classical Mythology'	
		# print("selected book is ", ')myprofile
		select_book_title = book_df.loc[book_df['Book-Title'] == selected_book]['Book-Title'].item()
		select_book_ISBN = book_df.loc[book_df['Book-Title'] == selected_book]['ISBN'].item()

		select_book_author = book_df.loc[book_df['Book-Title'] == selected_book]['Book-Author'].item()
		select_book_img = book_df.loc[book_df['Book-Title'] == selected_book]['Image-URL-L'].item()
		return render(request, 'recom.html', {'output':True, 'select_book_title': select_book_title, 'select_book_author':select_book_author, 'select_book_img':select_book_img, 'select_book_ISBN':select_book_ISBN})


	return render(request, 'home.html', {'r':True, 'books': books})



def add_to_cart(request):
	print("Ah")
	if request.method=="POST":
		print("hi")

		book_id = request.POST.get('r_book_isbn')
		u_name = str(request.user.username)
		# print(request.POST['l_book'])
		book_name = request.POST.get('r_book')
		author= request.POST.get('book_author')
		user_data.objects.create(book_id = book_id, u_name=u_name, book_name=book_name, author = author)
		return render(request, 'home.html', {'r':True})
	else:
		return render(request, 'home.html', {'r':True})











# def recom():
# 	book = '/home/pela/Documents/SE project/book_recom_main/static/data files/Books.csv'
# 	book_df = pd.read_csv(book)
	
# 	# for recommendation 
# 	books = book_df['Book-Title'].tolist()
# 	ratings_df = pd.read_csv('/home/pela/Documents/SE project/book_recom_main/static/data files/Ratings.csv').sample(40000)
# 	user_df = pd.read_csv('/home/pela/Documents/SE project/book_recom_main/static/data files/Users.csv')
# 	user_rating_df = ratings_df.merge(user_df, left_on = 'User-ID', right_on = 'User-ID')
# 	book_user_rating = book_df.merge(user_rating_df, left_on = 'ISBN',right_on = 'ISBN')
# 	book_user_rating = book_user_rating[['ISBN', 'Book-Title', 'Book-Author', 'User-ID', 'Book-Rating']]
# 	book_user_rating.reset_index(drop=True, inplace = True)
# 	d ={}
# 	for i,j in enumerate(book_user_rating.ISBN.unique()):
# 		d[j] =i
# 	book_user_rating['unique_id_book'] = book_user_rating['ISBN'].map(d)

# 	users_books_pivot_matrix_df = book_user_rating.pivot(index='User-ID', 
# 															columns='unique_id_book', 
# 															values='Book-Rating').fillna(0)
# 	users_books_pivot_matrix_df.head()
# 	users_books_pivot_matrix_df = users_books_pivot_matrix_df.values
# 	users_books_pivot_matrix_df


# 	NUMBER_OF_FACTORS_MF = 15

# 	#Performs matrix factorization of the original user item matrix
# 	U, sigma, Vt = svds(users_books_pivot_matrix_df, k = NUMBER_OF_FACTORS_MF)


# 	sigma = np.diag(sigma)
# 	sigma.shape

# 	all_user_predicted_ratings = np.dot(np.dot(U, sigma), Vt) 
# 	all_user_predicted_ratings
# 	def top_cosine_similarity(data, book_id, top_n=10):
# 		index = book_id 
# 		book_row = data[index, :]
# 		magnitude = np.sqrt(np.einsum('ij, ij -> i', data, data))
# 		similarity = np.dot(book_row, data.T) / (magnitude[index] * magnitude)
# 		sort_indexes = np.argsort(-similarity)
# 		return sort_indexes[:top_n]

# 	def similar_books(book_user_rating, book_id, top_indexes):
# 		print('Recommendations for {0}: \n'.format(
# 		book_user_rating[book_user_rating.unique_id_book == book_id]['Book-Title'].values[0]))
# 		for id in top_indexes + 1:
# 			print(book_user_rating[book_user_rating.unique_id_book == id]['Book-Title'].values[0])

	
# 	if request.method =='GET'and'submit_book' in request.GET:	
# 		print("final info on the way")
# 		selected_book = request.GET.get('book_name')
# 		print("book selected is :", selected_book)
# 		# selected_book = 'Classical Mythology'	
# 		# print("selected book is ", ')
# 		select_book_title = book_df.loc[book_df['Book-Title'] == selected_book]['Book-Title'].item()
# 		select_book_ISBN = book_df.loc[book_df['Book-Title'] == selected_book]['Book-Title'].item()

# 		select_book_author = book_df.loc[book_df['Book-Title'] == selected_book]['Book-Author'].item()
# 		select_book_img = book_df.loc[book_df['Book-Title'] == selected_book]['Image-URL-L'].item()
# 		k = 50
# 		movie_id = select_book_ISBN
# 		top_n = 5
# 		sliced = Vt.T[:, :k] # representative data

# 		s_b = similar_books(book_user_rating, select_book_ISBN, top_cosine_similarity(sliced, movie_id, top_n))
# 		return render(request, 'home.html', {'output':True, 'select_book_title': select_book_title, 'select_book_author':select_book_author, 'select_book_img':select_book_img,'s_b': s_b})

# 	return render(request, 'home.html', {'r':True, 'books': books})

def myprofile(request):
	user = str(request.user.username)
	foo_instance =user_data.objects.all().values()
	print(foo_instance)
	li = []
	di= {}
	for i in foo_instance:
		if i['u_name'] == user:
			# di['transaction_id'] = i['transaction_id']
			di['book_id'] = i['book_id']
			di['book_name'] = i['book_name']
			di['author'] = i['author']
		li.append(di)
		di = {}
	return render(request, "myprofile.html", {'user':user, 'di': li})