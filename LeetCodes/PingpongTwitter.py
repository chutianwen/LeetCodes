# Enter your code here. Read input from STDIN. Print output to STDOUT
print("Hello World~")
#AABBAABB
#win
# A Serve: P(A)  1 - P(B)
# B serve: P(B)  1 - P(A)

(1 - P(A)) ^

#AABBAABBAAB
P(A) ^ 6 * (1 - P(B)) ^ 5

#AABBAABBAABB: A failed first match
(1 - P(A)) * P(A) ^ 5 * (1 - P(B)) ^ 6

1 - P(A lost)

recusive to Sum P(A)

P(A win 10 games) P(A), P(B)
P(A win 11 games) = P(A win 10 games) * P(A) or P(A win 10 games) * (1 - P(B))

P(A win first match) = P(A)

# [a, b]
# (a + b) % 2 => who serve,
P(a, b) = Comb(a+b, a) * P(A) a
a = a_A + a_B
a_A: A wins when A serve
a_B: A wins when B serve


p(a, b) := probability that score is [a, b]
p(a, b) = P(a-1,b) * P(A) + P(a, b - 1) * P(B)

p(a = 0, b = 1)
p(a = 1, b = 0)

sum( p(a = 11, b = i) for i in range(10))

first game served by A:

item(row, col) => P(row, col)
def win_rate(game_limit, pa, pb):

	# 11 * 10
	cache = [[0 for _ in range(game_limit)] for _ in range(game_limit - 1)]
	# P(a = 0, b = 1)
	cache[0][1] = (1 - pa)
	# a wins 1st game
	cache[1][0] = pa
	cache[0][0] = 1

	# p(a = 0, b = i)
	for b in range(1, game_limit - 1):
		cache[0][b] = cache[0][b-1] * poss_b_win(b, pa, pb)

	# p(a = i, b = 0)
	for a in range(1, game_limit):
		cache[a][0] = cache[a-1][0] * poss_a_win(a, pa, pb)

	for a in range(1, game_limit):
		for b in range(1, game_limit - 1):
			# p(a, b) = P(a-1,b) * P(A) + P(a, b - 1) * P(B)
			cache[a][b] = cache[a-1][b] * poss_a_win(a + b, pa, pb) + cache[a][b-1] * poss_b_win(a + b, pa, pb)

	# sum the last row: sum(P(a=11, b=i))
	return sum(cache[-1])

# 0, 1, 2, 3, 4
# A, A, B, B, A

def who_serve(id_game):
	is_player_b = id_game // 2 % 2 == 1
	return is_player_b

def poss_b_win(id_game, pa, pb):
	return pb if who_serve(id_game) else 1 - pa

def poss_a_win(id_game, pa, pb):
	return 1 - pb if who_serve(id_game) else pa


