#http://www.dev102.com/2008/07/21/a-programming-job-interview-challenge-13-brackets/

#~ Your input is a string which is composed from bracket characters. 
#~ The allowed characters are:’(', ‘)’, ‘['. ']‘, ‘{’, ‘}’, ‘<’ and ‘>’. 
#~ Your mission is to determine whether the brackets structure is legal or not.
#~ Example of a legal expression: “([](<{}>))”.
#~ Example of an illegal expression: “({<)>}”.
#~ Example of a legal expression: “([](<{}>))”.
#~ Example of an illegal expression: “({<)>}”.
Library = {'(' => ')', 
         '[' => ']',
         '{' => '}',
         '<' => '>'}

test_case_1 = "([](<{}>))"
test_case_2 = "({<)>}"

def checkLegality(input_string)
  stack = []
  
  #Sanity check if string has odd# length, can't possible close brackets, Finished
  return false unless input_string.length % 2 == 0 
  
  input_string.split("").each do |char| # For each character in input_string
    if Library.has_key? char # if character is opening bracket
      stack << char # Add character to end of stack
    elsif Library.has_value? char # else if character is closing bracket
      if Library[stack[-1]] == char #and if it closes last bracket in stack
        stack.pop # Remove the bracket pair
      else # If wrong type of closing bracket
        return false # Otherwise not legal, finished
      end
    else # If it's not in library at all
      return false #Not legal bracket, finished
    end
  end # Gone through entire list
  if stack == []
    return true #Everything worked and all brackets closed
  else
    return false #Brackets closed properly, but not all brackets closed
  end
end


puts checkLegality(test_case_1)
puts checkLegality(test_case_2)