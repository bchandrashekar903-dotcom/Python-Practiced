'''735. Asteroid Collision
We are given an array asteroids of integers representing asteroids in a row. The indices of the asteroid in the array represent their relative position in space.
For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.
Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.'''

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for ast in asteroids:
            while st and ast<0 and st[-1]>0:
                if st[-1] < -ast:
                    st.pop()
                    continue
                elif st[-1] == -ast:
                    st.pop()
                break
            else:
                st.append(ast)
        return st
s = Solution()
print(s.asteroidCollision([5,-4,4]))       


        