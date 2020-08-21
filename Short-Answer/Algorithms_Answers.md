#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) - Steps = 1 + 4n + 1 + 4n^2. The notation is O(n^3) because the loop is going
through n and doing multiple calculations using n.

b) - Steps = 1 + n + 2 + n + 2. The notation is O(n^2) because there are 2 loops
going through n and two slots of memory being used.

c) - Steps = 2n. The notation is O(n) because this recursive function is
reccursively looping through the length of n, with very few other steps.

## Exercise II

        == == ==
        Since we don't know what f is yet, first we find it. Since we don't have to keep all of our eggs safe, we can drop an egg at a time until it breaks, which means we've hit f.

        for n in building:
            if egg != broken:
                drop_egg()
            else:
                n = f
                break

        O(n)

        We can make this better by moving by 2 floors each pass instead of 1, halving our number of dropped eggs.

        <!-- This solution is assuming we do not have to get to the end of building to find f, negating if the building length is even or odd -->

        while x < building.length():
            if egg != broken:
                drop_egg()
                x += 2
            else:
                n = f
                break

        O(log n)
        == == ==
