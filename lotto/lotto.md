There is a logic error in the comparison between the input and the random lotto number.
It is checked with a nested for loop, so there will be 36 iterations rather than 6 since it is iterating for every character in the input for every character in the lotto number.
Since the lotto number is modulus 45, the range of numbers in the lotto number is restricted to 1~45.
The possible values for our input are further restricted since we know that the input is mistakenly stored as an unsigned char array, so that limits us to only printable characters (i.e. 33~45).

Now our chances are extremely high. Just enter any 6 characters from the range 33~45 such as '!!!!!!' and it is very likely that we will get enough points to print the flag.
