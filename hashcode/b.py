import sys
infp = open('f_a.txt', 'r')
sys.stdin = infp
outfp = open('ad_out/f_out.txt', 'w')
sys.stdout = outfp


from collections import defaultdict

class lib:
	def __init__(self, id, args, books):
		self.id = id
		self.nbooks = args[0]
		self.sign_dur = args[1]
		self.ship = args[2]
		self.books = books
		self.book_order = sorted(self.books, key = lambda i:scores[i], reverse = True)
		self.score = None
 
	
	def cal_score(self):
		sc = 0
		for i in self.books:
			sc+=(scores[i]/book_cnt[i])
		self.score = sc

		

	def __str__(self):
		return str(self.id)

B, L, D = [int(i) for i in input().split()]
scores = [int(i) for i in input().split()]
lib_arr = []
book_cnt = defaultdict(lambda : 0)

for i in range(L):
	new_lib = lib(i,[int(i) for i in input().split()], [int(i) for i in input().split()])
	lib_arr.append(new_lib)
	for i in new_lib.books:
		book_cnt[i]+=1
for i in lib_arr:
	i.cal_score()

lib_arr.sort(key = lambda i : i.score, reverse = True)



out = []
st = set()
d = 0


nlib = 0


for lib in lib_arr:
	ans = {}
	ans['id'] = lib.id
	d += lib.sign_dur
	if d>=D:
		break
	nlib += 1
	mx = (D-d)*lib.ship
	ans['arr'] = []
	
	
	for i in lib.book_order:
		if mx >= 1:
			if i not in st:
				mx-=1
				st.add(i)
				ans['arr'].append(i)

	out.append(ans)
	#print(ans)


print(nlib)


for i in range(len(out)):
	print(out[i]['id'], len(out[i]['arr']))
	print(*out[i]['arr'])




		


