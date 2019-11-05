"""Ilya is a frontman of the most famous rock band on Earth. Band decided to
make the most awesome music video ever for their new single. In that music
video Ilya will go through Manhattan standing on the top of a huge truck and
playing amazing guitar solos. And during this show residents of the island
will join in singing and shaking their heads. However, there is a problem.
People on some streets hate rock.
Recall that Manhattan consists of n vertical and m horizontal streets which
form the grid of (n − 1)×(m − 1) squares. Band’s producer conducted a
research and realized two things. First, band’s popularity is constant on
each street. Second, a popularity can be denoted as an integer from 1 to
10^9. For example, if rockers go along the street with popularity equal to
10^9 then people will greet them with a hail of applause, fireworks,
laser show and boxes with... let it be an orange juice. On the other hand,
if rockers go along the street with popularity equal to 1 then people will
throw rotten tomatoes and eggs to the musicians. And this will not help to
make the most awesome music video!
So, a route goes from the upper left corner to the bottom right corner. Let
us define the route coolness as the minimal popularity over all streets in
which rockers passed non-zero distance. As you have probably guessed,
the musicians want to find the route with the maximal coolness. If you help
them then Ilya will even give you his autograph!
Input
In the first line there are integers n and m (2 ≤ n, m ≤ 10^5), separated by
space. These are the numbers of vertical and horizontal streets, respectively.
In the following n lines there are popularity values (one value on each
line) on vertical streets in the order from left to right.
In the following m lines there are popularity values (one value on each
line) on horizontal streets in the order from top to bottom.
It is guaranteed that all popularity values are integers from 1 to 10^9.
Output
Output a single integer which is a maximal possible route coolness."""
num_vs, num_hs = [int(x) for x in input().split()]
vrt_str = [int(input()) for x in range(num_vs)]
hrz_str = [int(input()) for x in range(num_hs)]
coolness = max(min(hrz_str[0], vrt_str[num_vs - 1]),
               min(vrt_str[0], hrz_str[num_hs - 1]),
               min(hrz_str[0], max(vrt_str[1:-1], default=0),
                   hrz_str[num_hs - 1]),
               min(vrt_str[0], max(hrz_str[1:-1], default=0),
                   vrt_str[num_vs - 1]))
print(coolness)
