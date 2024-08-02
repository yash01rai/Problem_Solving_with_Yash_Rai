class Solution:
    def countSeniors(self, details: List[str]) -> int:

        #Understanding
        # Given a list of passenger details, each consisting of string values of length 15.
        # In each string:
        # The first 10 characters are the phone number.
        # The 11th character is the gender.
        # The 12th and 13th characters represent the age.
        # The last 2 characters are the seat number.
        # Return the number of passengers who are strictly more than 60 years old.

        #Approach
        # 1. Declare a result variable to store the count of passengers above age 60.
        # 2. Iterate through the details list.
        # 3. For each passenger detail string, extract the age substring and convert it to an integer.
        # 4. Check if the age is above 60; if so, increase the result count by 1.
        # 5. Return the result.

        #Complexities
        # Time: O(n)
            # Iterating through each passenger detail string once.
        # Space: O(1)
            # Using a constant amount of extra space.


        result = 0

        for passenger in details:
            age = int(passenger[11:13])
            
            if age > 60:
                result += 1

        return result
        