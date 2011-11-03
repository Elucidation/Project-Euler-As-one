def Englify(n)
  singles = ["zero","one","two",
                "three","four","five",
                "six","seven","eight",
                "nine"]
  teens = ["ten","eleven","twelve","thirteen",
               "fourteen","fifteen","sixteen",
               "seventeen","eighteen","nineteen"]
  tens = ["twenty","thirty","forty","fifty",
             "sixty","seventy","eighty","ninety"]
  return "#{Englify(n/1000)} thousand" if n % 1000 == 0
  return "#{Englify(n/1000)} thousand #{Englify(n%1000)}" if n / 1000 > 0
  return "#{singles[n/100]} hundred" if n / 100 > 0 and n % 100 == 0
  return "#{singles[n/100]} hundred and #{Englify(n%100)}"  if n / 100 > 0
  return tens[n/10-2] if n/10 > 1 and n%10 == 0
  return "#{tens[n/10-2]} #{Englify(n%10)}" if n/10 > 1
  return teens[ n%10] if n/10 == 1
  return singles[n]
end

a = (1..1000).inject("") {|x,n| x + Englify(n)}.delete(" ")
puts a.delete(" ").length
# Answer: 21124