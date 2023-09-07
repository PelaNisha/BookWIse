from distutils.file_util import move_file
from pickle import LONG_BINGET
from urllib import response
from xxlimited import foo
import pandas as pd
from django.http import HttpResponse
from django.shortcuts import render, redirect
import numpy as np # linear algebra
import pandas as pd
from scipy.sparse.linalg import svds
from .models import user_data
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from .forms import InputForm
from django.contrib.auth.decorators import login_required

import logging
import shutil
# from pyrsistent import T
logger = logging.getLogger(__name__)
from datetime import datetime
import pandas as pd
import numpy as np
from scipy.sparse.linalg import svds

# # Load data once during application startup
book_df = pd.read_csv('/home/pela/Documents/SE project/book_recom_main/static/data files/Books.csv')
ratings_df = pd.read_csv('/home/pela/Documents/SE project/book_recom_main/static/data files/Ratings.csv').sample(40000)
user_df = pd.read_csv('/home/pela/Documents/SE project/book_recom_main/static/data files/Users.csv')

# Merge dataframes
user_rating_df = ratings_df.merge(user_df, left_on='User-ID', right_on='User-ID')
book_user_rating = book_df.merge(user_rating_df, left_on='ISBN', right_on='ISBN')
book_user_rating = book_user_rating[['ISBN', 'Book-Title', 'Book-Author', 'User-ID', 'Book-Rating']]
book_user_rating.reset_index(drop=True, inplace=True)

# Create a mapping for ISBN to unique_id_book
d = {}
for i, j in enumerate(book_user_rating['ISBN'].unique()):
	d[j] = i
book_user_rating['unique_id_book'] = book_user_rating['ISBN'].map(d)

# Pivot and fill NaN with 0
users_books_pivot_matrix_df = book_user_rating.pivot(index='User-ID', columns='unique_id_book', values='Book-Rating').fillna(0)

NUMBER_OF_FACTORS_MF = 15

# Performs matrix factorization of the original user-item matrix
U, sigma, Vt = svds(users_books_pivot_matrix_df.values, k=NUMBER_OF_FACTORS_MF)

sigma = np.diag(sigma)

all_user_predicted_ratings = np.dot(np.dot(U, sigma), Vt)



def login_page(request):
	if(request.user.is_authenticated):
		return redirect('home')
	else:
		if request.method =='POST':
			username = request.POST.get("user")
			password = request.POST.get("pass")
			user = authenticate(username=username, password=password)      

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				return render(request, "login.html", {"error":True})
		return render(request, "login.html")

# Create your views here.

def home_view(request):
	form = InputForm(request.POST, request.POST)
	# print(request.POST)
	if form.is_valid():
		form.save()
		return render(request, "new.html")
	return render(request, "new.html", {"form":form})


def home(request):	
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

	return render(request, 'home.html', { 'books': books})

@login_required(login_url='/login/') 
def read_now(request):
	return render(request, 'read_now.html')

@login_required(login_url='/login/') 
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
		return render(request, 'recom.html', {'r':True})
	else:
		return render(request, 'recom.html')


def custom_logout(request):
	logout(request)
	return redirect('home')


def top_cosine_similarity(data, book_id, top_n=10):
		if book_id >= (len(data)):
			raise ValueError("book_id is out of bounds for the data array.")
		print(len(data))
		# Calculate cosine similarities
		book_row = data[1, :]
		magnitude = np.sqrt(np.einsum('ij, ij -> i', data, data))
		similarity = np.dot(book_row, data.T) / (magnitude[book_id] * magnitude)
		
		# Sort the indexes by similarity in descending order
		sort_indexes = np.argsort(-similarity)
		
		# Return the top_n most similar book indexes
		return sort_indexes[:top_n]
	
def similar_books(book_user_rating, book_id, top_indexes):
	recommendations = []
	book_title = book_user_rating.loc[book_user_rating.unique_id_book == book_id]['Book-Title'].values[0]
	print(f'Recommendations for {book_title}:')
	for id in (top_indexes + 1):
		recommended_title = book_user_rating.loc[book_user_rating.unique_id_book == id]['Book-Title'].values[0]
		recommendations.append(recommended_title)
		print(recommended_title)
	return recommendations

def home__x(request):	
	books = book_df['Book-Title'].tolist()
	if request.method == 'GET' and 'submit_book' in request.GET:
		selected_book = request.GET.get('book_name')
		print("Book selected is:", selected_book)

		selected_book_data = book_df.loc[book_df['Book-Title'] == selected_book].iloc[0]  # Get the first match
		select_book_title = selected_book_data['Book-Title']
		select_book_ISBN = selected_book_data['ISBN']
		select_book_author = selected_book_data['Book-Author']
		select_book_img = selected_book_data['Image-URL-L']

		k = 50
		# movie_id = select_book_ISBN
		movie_id = 5001
		top_n = 5
		sliced = Vt.T[:, :k]  # Representative data
		# print("sliced ", sliced)
		s_b = similar_books(book_user_rating, movie_id, top_cosine_similarity(sliced, movie_id, top_n))
		print(type(s_b))
		return render(request, 'recom.html', {'output': True, 'select_book_title': select_book_title, 'select_book_author': select_book_author, 'select_book_img': select_book_img, 's_b': s_b})

	return render(request, 'home.html', {'r': True, 'books': books})


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